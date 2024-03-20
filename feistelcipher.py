import random
import math

def stringToASCII(s):
    return [ord(c) for c in s]

def formatToBinary(c):
    return f'{c:08b}'

def splitInHalf(c):
    N = len(c)
    return {'l' : c[0:N//2] , 'r': c[N//2:]}

def generateKeys():
    maxVal = math.pow(2,8)
    k1 = random.randint(0,maxVal)
    k2 = random.randint(0,maxVal)
    return [formatToBinary(k1),formatToBinary(k2)]

def XOR(a,b):
    c = ''
    for j in range(len(a)):
        if a[j] == '0':
            if b[j] == '0':
                c += '0'
            elif b[j] == '1':
                c += '1'
        elif a[j] == '1':
            if b[j] == '0':
                c += '1'
            elif b[j] == '1':
                c += '0'
    return c

s = 'Hell0'
k1,k2 = generateKeys()
asciiCodes = stringToASCII(s)
print(f'Key1: {k1} Key2: {k2}')
print(f'Original String: {s}')
print(f'ASCII Codes: {asciiCodes}')
for code in asciiCodes:
    print(f'Char: {chr(code)}')
    codeFormatted = formatToBinary(code)
    halves = splitInHalf(codeFormatted)
    print(f'Original Bin-Encoding: {bin(code)}  Formatted: {codeFormatted}')
    print(f'Left Half: {halves["l"]} Right Half: {halves["r"]}')