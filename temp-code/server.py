#!/usr/bin/env python3
from xmlrpc.server import SimpleXMLRPCServer
import logging
from decimal import Decimal, getcontext

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set precision for Decimal calculations
getcontext().prec = 1000


def factorial(n):
    """
    Calculate factorial of number n using Decimal for arbitrary precision
    """
    if n < 0:
        return "Error: Cannot calculate factorial of negative number"
    elif n == 0 or n == 1:
        return str(1)
    else:
        try:
            result = Decimal(1)
            for i in range(2, n + 1):
                result *= Decimal(i)
            # Convert to string to avoid XML-RPC integer limits
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"


# Create server
server = SimpleXMLRPCServer(("localhost", 8000), logRequests=True)
server.register_function(factorial)

# Run the server's main loop
if __name__ == "__main__":
    try:
        print("Factorial RPC Server is running on port 8000...")
        print("Use Ctrl+C to stop.")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server is shutting down...")
