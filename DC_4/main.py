import random

class LoadBalancer:
    def __init__(self, servers):
        """
        Initialize the load balancer with a list of server names.
        """
        self.servers = servers
        self.server_index_rr = 0  # For round robin tracking

    def round_robin(self):
        """
        Select a server using round robin strategy.
        """
        server = self.servers[self.server_index_rr]
        self.server_index_rr = (self.server_index_rr + 1) % len(self.servers)
        return server

    def random_selection(self):
        """
        Select a server randomly from the list.
        """
        return random.choice(self.servers)


def simulate_client_requests(load_balancer, num_requests):
    print("Simulating client requests and load balancing:\n")
    for i in range(num_requests):
        print(f"Request {i + 1}:")
        # Round Robin
        server_rr = load_balancer.round_robin()
        print(f"  Round Robin  -> {server_rr}")
        # Random Selection
        server_random = load_balancer.random_selection()
        print(f"  Random       -> {server_random}\n")


if __name__ == "__main__":
    # List of available servers
    servers = ["Server A", "Server B", "Server C"]
    # Create LoadBalancer instance
    load_balancer = LoadBalancer(servers)
    # Simulate 10 client requests
    simulate_client_requests(load_balancer, 10)
