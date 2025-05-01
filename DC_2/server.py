import Pyro4


@Pyro4.expose
class StringConcatenator(object):
    def concat(self, str1, str2):
        print(f"[SERVER] Concatenating '{str1}' + '{str2}'")
        return str1 + str2


def main():
    daemon = Pyro4.Daemon()  # Make a Pyro daemon
    uri = daemon.register(StringConcatenator)  # Register the object as a Pyro object
    print(f"[SERVER] Ready. Object uri = {uri}")
    with open("server_uri.txt", "w") as f:
        f.write(str(uri))
    daemon.requestLoop()  # Start the event loop of the server to wait for calls


if __name__ == "__main__":
    main()
