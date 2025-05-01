import threading
from server import Server
from load_balancer import LoadBalancer, RoundRobin, LeastConnections, RandomSelection
from client import Client
import time


def run_simulation(
    strategy_name: str,
    strategy_class,
    num_servers: int = 3,
    num_clients: int = 5,
    duration: int = 30,
):
    print(f"\nStarting simulation with {strategy_name} strategy")
    print("-" * 50)

    # Initialize load balancer with the specified strategy
    load_balancer = LoadBalancer(strategy_class())

    # Create and add servers
    for i in range(num_servers):
        # Each server can handle 10 concurrent connections
        server = Server(id=i, capacity=10)
        load_balancer.add_server(server)

    # Create clients with different request rates
    clients = [
        Client(client_id=i, request_rate=random.uniform(1, 5))
        for i in range(num_clients)
    ]

    # Create threads for each client
    client_threads = []
    for client in clients:
        thread = threading.Thread(
            target=client.generate_requests,
            args=(load_balancer.handle_request, duration),
        )
        client_threads.append(thread)

    # Start all client threads
    start_time = time.time()
    for thread in client_threads:
        thread.start()

    # Wait for all threads to complete
    for thread in client_threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time

    # Print results
    print(f"\nSimulation completed in {total_time:.2f} seconds")
    print("\nServer Statistics:")
    for server_stats in load_balancer.get_stats():
        print(f"\nServer {server_stats['id']}:")
        print(f"  Total Requests Handled: {server_stats['total_requests']}")
        print(f"  Average Response Time: {server_stats['average_response_time']:.3f}s")
        print(f"  Final Load: {server_stats['load_percentage']:.1f}%")

    print("\nClient Statistics:")
    for client in clients:
        stats = client.get_stats()
        print(f"\nClient {stats['client_id']}:")
        print(f"  Total Requests: {stats['total_requests']}")
        print(f"  Average Response Time: {stats['average_response_time']:.3f}s")
        print(f"  Request Rate: {stats['request_rate']:.1f} req/s")


if __name__ == "__main__":
    import random

    random.seed(42)  # For reproducible results

    print("Load Balancing Simulation")
    print("=" * 50)

    # Test each strategy
    strategies = [
        ("Round Robin", RoundRobin),
        ("Least Connections", LeastConnections),
        ("Random Selection", RandomSelection),
    ]

    for strategy_name, strategy_class in strategies:
        run_simulation(strategy_name, strategy_class)
        print("\n" + "=" * 50)
