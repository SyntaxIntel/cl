from xmlrpc.server import SimpleXMLRPCServer


def factorial(n):
    if n < 0:
        return "Error: Negative input not allowed."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("[SERVER] Listening on port 8000...")
    server.register_function(factorial, "factorial")
    server.serve_forever()
