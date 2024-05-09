import socket
import hashlib
import random


def MD5_Hash(data: str):

    return hashlib.md5(data.encode()).hexdigest()  # returns 32 byte str


port = 12000
host = socket.gethostname()
ip = socket.gethostbyname(host)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))
clientSocket.send(b'Auth')
msg = clientSocket.recv(10).decode()
while msg != 'Hash Found':
    print(msg)
    ranInt = random.randint(0, 31)
    data = str(ip)+str(ranInt)
    clientHash = MD5_Hash(data)
    clientSocket.send(clientHash.encode())
    msg = clientSocket.recv(10).decode()

clientSocket.close()
