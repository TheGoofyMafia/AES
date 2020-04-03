import random
from Crypto.Cipher import AES
#from Crypto.Cipher import adec
import binascii
from Padding import pad, unpad

import os
#key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
#print('key', [x for x in key])
# prints
#iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
#print('iv', [x for x in iv])
key = os.urandom(16)
iv = os.urandom(16)
BS =16
# def pad:
#     pad = lambda d: d + (BS - len(d) % BS) * chr(BS - len(d) % BS)
# ENCRYPTION
def encrypt():
    aes = AES.new(key, AES.MODE_CBC, iv)
    print('#####################'
          '                     '
          'PLEASE INPUT ONLY 16 BYTES STRING'
          '                     '
          '#####################')
    global data
    data = input() #<- 16 bytes OR add buffer to make it 16 bytes
    encd = aes.encrypt(pad(data, 16))
    return encd

# DECRYPTION
def decrypt(encd):
    aes = AES.new(key, AES.MODE_CBC, iv)
    global decd
    decd = (unpad(aes.decrypt(encd), 16))
    decd = decd.decode("utf-8")


encd = encrypt()
decrypt(encd)

# Check for verification

if data == decd:
    print("Working with success")
else:
    print("Try again")