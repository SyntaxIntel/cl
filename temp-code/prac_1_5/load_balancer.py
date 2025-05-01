from abc import ABC, abstractmethod
import random
from typing import List
from server import Server


class LoadBalancingStrategy(ABC):
    @abstractmethod
    def select_server(self, servers: List[Server]) -> Server:
        pass


class RoundRobin(LoadBalancingStrategy):
    def __init__(self):
        self.current_index = -1

    def select_server(self, servers: List[Server]) -> Server:
        self.current_index = (self.current_index + 1) % len(servers)
        return servers[self.current_index]


class LeastConnections(LoadBalancingStrategy):
    def select_server(self, servers: List[Server]) -> Server:
        return min(servers, key=lambda s: s.current_connections)


class RandomSelection(LoadBalancingStrategy):
    def select_server(self, servers: List[Server]) -> Server:
        return random.choice(servers)


class LoadBalancer:
    def __init__(self, strategy: LoadBalancingStrategy):
        self.servers: List[Server] = []
        self.strategy = strategy

    def add_server(self, server: Server):
        self.servers.append(server)

    def remove_server(self, server: Server):
        self.servers.remove(server)

    def handle_request(self, request_id: int) -> float:
        if not self.servers:
            raise Exception("No servers available")

        selected_server = self.strategy.select_server(self.servers)
        return selected_server.handle_request(request_id)

    def get_stats(self):
        return [server.get_stats() for server in self.servers]
