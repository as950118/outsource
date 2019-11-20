from socket import *
import time
serverName = 'localhost'
serverPort = 6789

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Input filenames(a /test.txt) : ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print ('From Server:', modifiedSentence.decode())

clientSocket.close()