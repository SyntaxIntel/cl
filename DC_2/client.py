import Pyro4


def main():
    # Read the server URI from the file
    with open("server_uri.txt", "r") as f:
        uri = f.read().strip()
    # Get a proxy for the remote object
    string_concatenator = Pyro4.Proxy(uri)
    # Input two strings from the user
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    # Call the remote method
    result = string_concatenator.concat(str1, str2)
    print(f"[CLIENT] Concatenated result: {result}")


if __name__ == "__main__":
    main()
