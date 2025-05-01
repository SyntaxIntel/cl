# Distributed Factorial Computation using RPC (Python)

## Files
- `server.py`: RPC server that computes factorial.
- `client.py`: RPC client that sends integer and receives result.

## How it works
1. Start `server.py` (runs on localhost:8000).
2. Run `client.py`, enter an integer when prompted.
3. Client sends the integer to server, server computes factorial, returns result.

## Usage
Open two terminals:

**Terminal 1:**
```
python3 server.py
```

**Terminal 2:**
```
python3 client.py
```

Follow the prompts in the client.

## Explanation
- Uses Python's built-in `xmlrpc` for simple RPC communication.
- Code is well-commented for clarity.
- Handles negative input with an error message.
