import random
from Crypto.Cipher import AES
import binascii
from Padding import pad, unpad
import os
from init import key,iv
from Encrypt import encd


def decrypt(encd):
    aes = AES.new(key, AES.MODE_CBC, iv)
    global decd
    decd = (unpad(aes.decrypt(encd), 16))
    decd = decd.decode("utf-8")
    return decd
decd = decrypt(encd)