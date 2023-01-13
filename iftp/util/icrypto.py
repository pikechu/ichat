import base64
from random import randint
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.Cipher import DES3


class iBaseCrypto(object):
    def __init__(self) -> None:
        self.char_enum = [chr(x) for x in range(32, 126) if (x >= ord('0') and x <= ord('9')) or (x >= ord('a') and x <= ord('z')) or (x >= ord('A') and x <= ord('Z'))]

    def get_random_key(self, dig: int) -> str:
        return ''.join([self.char_enum[randint(0, len(self.char_enum) - 1)] for x in range(dig)])




class iEncrypto(iBaseCrypto):
    def __init__(self, public_key_path=None) -> None:
        self.public_key = None
        if public_key_path:
            self.configure(public_key_path)

    def configure(self, public_key_path: str):
        with open(public_key_path) as f:
            self.public_key = RSA.importKey(f.read())

    def rsa_encrypt(self, data: str):
        if not self.public_key:
            raise Exception('no self.public_key, please init first')
        cipher = PKCS1_cipher.new(self.public_key)
        return base64.b64encode(cipher.encrypt(data.encode())).decode()

    def aes_encrypt(self, key: str, data: str):
        raise Exception('todo')

    

class iDecrypto(iBaseCrypto):
    def __init__(self, private_key_path=None) -> None:
        self.private_key = None
        if private_key_path:
            self.configure(private_key_path)

    def configure(self, private_key_path: str):
        with open(private_key_path) as f:
            self.private_key = RSA.importKey(f.read())

    def rsa_decrypt(self, data: str):
        if not self.private_key:
            raise Exception('no self.private_key, please init first')
        cipher = PKCS1_cipher.new(self.private_key)
        return cipher.decrypt(base64.b64decode(data), 0).decode()

# test
if __name__ == '__main__':
    msg = 'hello world!'
    import os
    en = iEncrypto(os.getcwd()+'/../rsa_public_key.pem')
    de = iDecrypto(os.getcwd()+'/../rsa_private_key.pem')
    en_t = en.rsa_encrypt(msg)
    print(en_t)
    de_t = de.rsa_decrypt(en_t)
    print(de_t)