import time
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Server:
    id: int
    capacity: int  # Maximum number of concurrent connections
    current_connections: int = 0
    total_requests_handled: int = 0
    average_response_time: float = 0.0
    _response_times: list = field(default_factory=list)

    def handle_request(self, request_id: int) -> float:
        """
        Simulate handling a request and return the response time
        """
        if self.current_connections >= self.capacity:
            raise Exception(f"Server {self.id} is at capacity")

        self.current_connections += 1

        # Simulate processing time (between 0.1 and 0.5 seconds based on current load)
        processing_time = 0.1 + (self.current_connections / self.capacity) * 0.4
        time.sleep(processing_time)

        self.current_connections -= 1
        self.total_requests_handled += 1
        self._response_times.append(processing_time)
        self.average_response_time = sum(self._response_times) / len(
            self._response_times
        )

        return processing_time

    def get_load(self) -> float:
        """
        Return the current load as a percentage of capacity
        """
        return self.current_connections / self.capacity

    def get_stats(self) -> Dict:
        """
        Return server statistics
        """
        return {
            "id": self.id,
            "capacity": self.capacity,
            "current_connections": self.current_connections,
            "total_requests": self.total_requests_handled,
            "average_response_time": self.average_response_time,
            "load_percentage": self.get_load() * 100,
        }
