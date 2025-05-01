# python3 main.py --algorithm all
import time
import random
from typing import Callable


class Client:
    def __init__(self, client_id: int, request_rate: float):
        """
        Initialize a client with an ID and request rate (requests per second)
        """
        self.client_id = client_id
        self.request_rate = request_rate
        self.total_requests = 0
        self.total_response_time = 0

    def generate_requests(self, handler: Callable[[int], float], duration: float):
        """
        Generate requests for a specified duration
        handler: function that processes the request and returns response time
        duration: how long to generate requests for (in seconds)
        """
        start_time = time.time()
        next_request_time = start_time

        while time.time() - start_time < duration:
            current_time = time.time()

            if current_time >= next_request_time:
                request_id = f"{self.client_id}-{self.total_requests}"
                try:
                    response_time = handler(request_id)
                    self.total_response_time += response_time
                    self.total_requests += 1
                except Exception as e:
                    print(f"Request {request_id} failed: {str(e)}")

                # Calculate next request time based on request rate with some randomness
                next_request_time = current_time + (
                    1.0 / self.request_rate
                ) * random.uniform(0.8, 1.2)

            # Small sleep to prevent busy waiting
            time.sleep(0.01)

    def get_stats(self):
        """
        Return client statistics
        """
        avg_response_time = (
            self.total_response_time / self.total_requests
            if self.total_requests > 0
            else 0
        )
        return {
            "client_id": self.client_id,
            "total_requests": self.total_requests,
            "average_response_time": avg_response_time,
            "request_rate": self.request_rate,
        }
