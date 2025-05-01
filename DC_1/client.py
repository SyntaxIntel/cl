import xmlrpc.client


def main():
    server = xmlrpc.client.ServerProxy("http://localhost:8000/")
    try:
        n = int(input("Enter a non-negative integer: "))
        result = server.factorial(n)
        print(f"Factorial of {n} is: {result}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
