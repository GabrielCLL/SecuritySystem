import secrets


class FeistelCipher:
    def __init__(self, key, rounds):
        self.block_size = 8 #64bits 
        self.key_size = len(key)
        self.rounds = rounds
        self.key = key
        self.subkeys = self.generate_sub_keys()
    
    def generate_sub_keys(self):
        """
        A method for generating subkeys, one per round, the technique for that is cyclic rotation.
        The number of subkeys its tha same of rounds.
        """
        return [self.key[i % self.key_size:] + self.key[:i % self.key_size] for i in range(self.rounds)]

    def split_in_half(self, text):
        """
        A method for slip the text in the middle.
        """
        return text[:self.block_size // 2], text[self.block_size // 2:]
    
    def set_message_blocks(self, msg):
        """
        A method for configuring the message. 
        If the size of the message is bigger than the block size, split the message into blocks with the permitted block size.
        """
        # divide the message in blocks with the block_size
        blocks = [msg[i: i + self.block_size] for i in range(0, len(msg), self.block_size)]

        # check if the last block is the correct size, otherwise fill it with blank
        last_block = blocks[-1]
        last_block_size = len(last_block)

        if (last_block_size < self.block_size):
            last_block += " " * (self.block_size - last_block_size)
            # if you want to fill with random things
            # random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=self.block_size - last_block_size))
            # last_block += random_chars

        blocks[-1] = last_block

        return blocks

    def encrypt(self, msg):
        """
        A method for encrypting the message using the Feistel cipher.
        """
        blocks = self.set_message_blocks(msg)

        ciphertext = ''

        for block in blocks:
            # create the vectors
            L = [""]*(self.rounds +1)
            R = [""]*(self.rounds +1)

            # initialiazer the first ones
            L[0], R[0] = self.split_in_half(block)

            # rounds to encode
            for index in range(1, self.rounds + 1):
                L[index] = R[index-1]
                R[index] = self.xor(L[index - 1], self.feistel_function(R[index - 1], self.subkeys[index - 1]))

            ciphertext += (L[self.rounds] + R[self.rounds])

        return ciphertext

    def decrypt(self, ciphertext):
        """
        A method for decrypting the message using the Feistel cipher.
        """
                
        blocks = self.set_message_blocks(ciphertext)

        msg = ''

        for block in blocks:
            # create the vectors
            L = [""]*(self.rounds +1)
            R = [""]*(self.rounds +1)

            # initialiazer the lastones
            L[self.rounds], R[self.rounds] = self.split_in_half(block)

            # rounds to decode
            for index in range(self.rounds, 0, -1):
                    
                R[index-1] = L[index]
                L[index-1] = self.xor(R[index], self.feistel_function(L[index], self.subkeys[index-1]))
        
            msg += (L[0] + R[0])

        return msg

    def feistel_function(self, text_block, key):
        """
        A method describing the technique used, similar to the f() function in the Feistel cipher.
        The technique involves permuting the positions of the text content based on the provided key.
        """
        bit_seq = ''.join(format(ord(c), '08b') for c in text_block)
        bit_seq_encoded = ''.join(bit_seq[int(k)] for k in key)

        return self.xor(bit_seq_encoded, text_block)
    
    def xor(self, text1, text2):
        """
        A simple XOR.
        """
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(text1, text2))


# Example
def generate_secure_key(bits):
    return ''.join(str(secrets.randbits(1)) for _ in range(bits))

plaintext = 'Hello this is a Random Text'
rounds = 4

key = generate_secure_key(64)

feistel = FeistelCipher(key, rounds)

encrypt_text = feistel.encrypt(plaintext)
print(f"Encrypted text: {encrypt_text}")

decrypt_text = feistel.decrypt(encrypt_text)
print(f"Decrypted text: {decrypt_text}")