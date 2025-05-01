#!/usr/bin/env python3
import xmlrpc.client
import sys


def main():
    # Connect to the server
    print("Connecting to the factorial RPC server...")
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    try:
        while True:
            # Get input from user
            try:
                n = int(
                    input(
                        "Enter an integer to calculate factorial (or Ctrl+C to exit): "
                    )
                )
                if n < 0:
                    print("Error: Please enter a non-negative integer.")
                    continue

                # Send request to server and get response
                result = proxy.factorial(n)

                # Check if result is an error message
                if isinstance(result, str) and result.startswith("Error"):
                    print(f"Server error: {result}")
                else:
                    # Format large numbers with commas for readability
                    formatted_result = format(int(result), ",")
                    print(f"Server response: Factorial of {n} is {formatted_result}")
                print()

            except ValueError:
                print("Error: Please enter a valid integer.")
            except xmlrpc.client.Fault as e:
                print(f"RPC Error: {str(e)}")
            except ConnectionError:
                print("Error: Could not connect to the server.")
            except Exception as e:
                print(f"Unexpected error: {str(e)}")

    except KeyboardInterrupt:
        print("\nExiting client...")


if __name__ == "__main__":
    main()
