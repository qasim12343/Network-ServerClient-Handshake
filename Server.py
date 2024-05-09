import socket
import random
import hashlib


def MD5_Hash(data: str):
    return hashlib.md5(data.encode()).hexdigest()  # returns 32 byte str


serverPort = 12000
host = socket.gethostname()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(1)

connectionSocket = ''
IP_addr = ''
print('The server is ready to recieve')

while True:
    connectionSocket, IP_addr = serverSocket.accept()
    msg = connectionSocket.recv(4).decode()
    if msg == 'Auth':
        ip = IP_addr[0]
        ranInt = random.randint(0, 31)
        data = str(ip)+str(ranInt)
        ServerHash = MD5_Hash(data)
        recvHash = ''
        while ServerHash != recvHash:
            connectionSocket.send(b'Send Hash!')
            recvHash = connectionSocket.recv(32).decode()
            print(ServerHash)
            print(recvHash)

        connectionSocket.send(b'Hash found')
connectionSocket.close()
