import threading
import os
import time

def HandleThread(target, args):
    t = threading.Thread(target = target, args = args)
    t.daemon = True
    return t

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
        connectionSocket.send("HTTP/1.1 200 OK\nCOUNT = {0}\nADDR = {1}\r\n\r\n".format(count,addr).encode())

        # Send the content of the requested file to the connection socket
        connectionSocket.sendall(outputdata)

        connectionSocket.send("\r\n".encode())

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

    # For counting number of thread
    time.sleep(10)
    # Close the client connection socket
    connectionSocket.close()