from socket import *
import connection
import json

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    msg = connectionSocket.recv(1024)

    data = connection.connectionDB()

    connectionSocket.send(data.encode())
    connectionSocket.close()