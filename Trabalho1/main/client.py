from socket import *
import json
serverName = 'localhost'
serverPort = 3000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def sendToServer(msg):
    clientSocket.send(msg.encode())


def getQuestions():
    total = 0
    data = json.loads(clientSocket.recv(1024).decode())
    for item in data:
        print(item['question'])
        print('a:', item['a'])
        print('b:', item['b'])
        print('c:', item['c'])
        print('d:', item['d'], '\n')

        answer = item['answer']
        op = input("Qual é a resposta?\n")
        if op == answer:
            total += 1

    print(f"Sua porcentagem de acerto foi de {(total/4)*100}%")


def closeClient():
    clientSocket.close()


sendToServer("Aloha")
getQuestions()