import xmlrpc.client

def main():
    server_url = 'http://localhost:9000'
    proxy = xmlrpc.client.ServerProxy(server_url)
    print('Connected to RPC server at', server_url)
    print('1. Compute factorial of a single number')
    print('2. Compute factorials of a list of numbers (batch)')
    choice = input('Choose an option (1 or 2): ')
    if choice == '1':
        try:
            n = int(input('Enter a non-negative integer: '))
        except ValueError:
            print('Invalid input. Please enter an integer.')
            return
        try:
            result = proxy.factorial(n)
            print(f'Factorial of {n} is: {result}')
        except Exception as e:
            print('Error communicating with server:', e)
    elif choice == '2':
        nums_str = input('Enter non-negative integers separated by spaces: ')
        try:
            numbers = [int(x) for x in nums_str.strip().split()]
        except ValueError:
            print('Invalid input. Please enter only integers.')
            return
        try:
            results = proxy.batch_factorial(numbers)
            for n, res in zip(numbers, results):
                print(f'Factorial of {n} is: {res}')
        except Exception as e:
            print('Error communicating with server:', e)
    else:
        print('Invalid choice.')

if __name__ == '__main__':
    main()
