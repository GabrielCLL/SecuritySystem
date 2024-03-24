from socket import *
from feistelcipher import FeistelCipher

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

#Conecta ao servidor
clientSocket.connect((serverName,serverPort))

#Recebe mensagem do usuario e envia ao servidor
message = input('Digite uma frase: ')

#Chave gerada usando função generate_secure_key em feistelcipher
key = '1000100000100011110101001111100010010001011010101100001110100010'
cipher = FeistelCipher(key)
encriptedMessage = cipher.encrypt(message)

clientSocket.send(encriptedMessage.encode('UTF-8'))

#Aguarda mensagem de retorno e a imprime
modifiedMessage, addr = clientSocket.recvfrom(2048)
modifiedMessageDecripted = cipher.decrypt(modifiedMessage.decode())

print("Retorno do Servidor:",modifiedMessageDecripted)

clientSocket.close()