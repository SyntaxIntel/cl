# Distributed String Concatenation using Python (Simulated RMI)

## Problem Statement
Design a distributed application using RMI for remote computation where client submits two strings to the server and server returns the concatenation of the given strings using Python.

## How it works
- The server (`server.py`) listens for client connections and exposes a remote method (via socket) to concatenate two strings.
- The client (`client.py`) connects to the server, sends two strings, and receives the concatenated result.

## How to Run
1. Open two terminals.
2. In the first terminal, start the server:
   ```bash
   python3 server.py
   ```
3. In the second terminal, run the client:
   ```bash
   python3 client.py
   ```
4. Enter two strings when prompted. The client will display the concatenated result received from the server.

## Explanation
- This example uses Python's socket library to simulate RMI (Remote Method Invocation) behavior.
- The server acts as the remote object, and the client invokes the remote method by sending data over the network.
- The code is simple and well-commented for easy understanding and explanation during your practical exam.
