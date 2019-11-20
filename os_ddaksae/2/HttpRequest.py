# Import socket module
from socket import *
import sys  # In order to terminate the program
import os
import ThreadGen

def StartServer():
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
    return serverSocket

def StartReceive(serverSocket):
    # Server should be up and running and listening to the incoming connections

    print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    return connectionSocket, addr

def HandleClient(connectionSocket, addr, count):
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode()
        if not message:
            return
        print(message)

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        print(filename)

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:], 'rb')

        # Store the entire contenet of the requested file in a temporary buffer
        outputdata_size = os.path.getsize(filename[1:])
        outputdata = f.read(outputdata_size)
        f.close()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("COUNT = {0}\nADDR = {1}\nHTTP/1.1 200 OK\r\n\r\n".format(count,addr).encode())

        # Send the content of the requested file to the connection socket
        connectionSocket.sendall(outputdata)

        connectionSocket.send("\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()
    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

    # Close the client connection socket
    connectionSocket.close()

def EndServer(serverSocket):
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    serverSocket = StartServer()
    thread_set = set()
    while True:
        count = len(thread_set)
        connectionSocket, addr = StartReceive(serverSocket)
        Thread = ThreadGen.HandleThread(target = HandleClient, args=(connectionSocket, addr, count))
        Thread.start()
        thread_set.add(Threadgetthreading.get_ident())
    EndServer(serverSocket)