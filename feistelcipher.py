import random

class FeistelCipher():
    def __init__(self,message):
        self.message = message

    def toBinary(self,c):
        return f'{c:08b}'
    
    def splitInHalf(self,c):  
        N = len(c)
        return  c[0:N//2] , c[N//2:]
    
    def encodeBitsWithKey(self,key,bitSeq):
        bitSeqEncoded = ''
        originalBitSeq = [b for b in bitSeq]
        for k in key:
            bitSeqEncoded += originalBitSeq[k]
        return bitSeqEncoded
    
    def XOR(self,a,b):
        return f'{int(a,2) ^ int(b,2):04b}'
    
    def encode(self, numSteps = 14,keys = None):
        newMsg = ''
        # key with size of each half (4 bits)
        key = random.sample([i for i in range(4)],4) 
        for j in range(len(self.message)):
            currentChar = self.message[j]
            currentCharASCII = ord(currentChar)
            currentCharBin = self.toBinary(currentCharASCII)
            l0,r0 = self.splitInHalf(currentCharBin)
            r0_encoded = self.encodeBitsWithKey(key,r0)
            l1,r1 = r0, self.XOR(l0,r0_encoded)
            newCharBin = f'{l1}{r1}'
            newChar = chr(int(newCharBin,2))
            newMsg += newChar
        return newMsg

msg = 'H'
#Currently returning non printable characters such as '/x85'
print(FeistelCipher(msg).encode())