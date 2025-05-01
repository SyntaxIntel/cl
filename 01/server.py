from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return 'Error: Input must be a non-negative integer.'
    result = 1
    for i in range(2, n + 1):
        result *= i
    return str(result)

def batch_factorial(numbers):
    """Compute factorials for a list of integers."""
    if not isinstance(numbers, list):
        return 'Error: Input must be a list of non-negative integers.'
    results = []
    for n in numbers:
        results.append(factorial(n))
    return results

def main():
    server = SimpleXMLRPCServer(('localhost', 9000), requestHandler=RequestHandler, allow_none=True)
    server.register_function(factorial, 'factorial')
    server.register_function(batch_factorial, 'batch_factorial')
    print('RPC Server running on port 9000...')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')

if __name__ == '__main__':
    main()
