# Import socket module
from socket import *
import sys  # In order to terminate the program
import os
import time
import ThreadGen

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 5 connection at a time
serverSocket.listen(5)

while True:
    # Server should be up and running and listening to the incoming connections

    print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed

    # Check Thread
    names = ThreadGen.threading.enumerate()
    print("Name of Threads :", names)
    count = ThreadGen.threading.active_count()
    print("Number of Threads :", count)

    # Start Threading
    Thread = ThreadGen.HandleThread(target=ThreadGen.HandleClient, args=(connectionSocket, addr, count))
    Thread.start()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
