import Crypto.Cipher.AES
import Crypto.Random
import base64
import binascii

class Cipher_AES:
    pad_pkcs5 = lambda x, y: x + (y - len(x) % y) * chr(y - len(x) % y).encode("utf-8")
    unpad_pkcs5 = lambda x: x[:-ord(x[-1])]

    def __init__(self, key, iv):
        self.__key = key
        self.__iv = iv

    def text_verify(self, text, method):
        while len(text) > len(self.__key):
            text_slice = text[:len(self.__key)]
            text = text[len(self.__key):]
            yield text_slice
        else:
            if len(text) == len(self.__key):
                yield text
            else:
                yield self.pad_method(text, method)


    def pad_method(self, text, method):
        if method == "":
            return Cipher_AES.pad_default(text, 16)
        elif method == "PKCS5Padding":
            return Cipher_AES.pad_pkcs5(text, 16)
        else:
            return Cipher_AES.pad_user_defined(text, 16, method)

    def Cipher_MODE_CBC(self):
        self.__x = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), Crypto.Cipher.AES.MODE_CBC, self.__iv.encode("utf-8"))
        print(self.__x)


    def encrypt(self, text, cipher_method, pad_method="", code_method=""):
        if cipher_method.upper() == "MODE_CBC":
            self.Cipher_MODE_CBC()
        cipher_text = b"".join([self.__x.encrypt(i) for i in self.text_verify(text.encode("utf-8"), pad_method)])
        if code_method.lower() == "base64":
            return base64.encodebytes(cipher_text).decode("utf-8").rstrip()
        elif code_method.lower() == "hex":
            return binascii.b2a_hex(cipher_text).decode("utf-8").rstrip()
        else:
            return cipher_text.decode("utf-8").rstrip()