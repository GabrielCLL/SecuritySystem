from socket import *
from feistelcipher import FeistelCipher

serverPort = 12000
#Cria o Socket TCP (SOCK_STREAM) para rede IPv4 (AF_INET)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
#Socket fica ouvindo conexoes. O valor 1 indica que uma conexao pode ficar na fila
serverSocket.listen(1)

print("Servidor pronto para receber mensagens. Digite Ctrl+C para terminar.")

#Chave gerada usando função generate_secure_key em feistelcipher
key = '1000100000100011110101001111100010010001011010101100001110100010'
cipher = FeistelCipher(key)

while 1:
       #Cria um socket para tratar a conexao do cliente
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024)
     decodedSentence = sentence.decode('UTF-8')
     decriptedSentence = cipher.decrypt(decodedSentence)
     capitalizedSentence = decriptedSentence.upper()
     capitalizedSentenceEncripted = cipher.encrypt(capitalizedSentence)
     connectionSocket.send(capitalizedSentenceEncripted.encode('UTF-8'))
     connectionSocket.close()