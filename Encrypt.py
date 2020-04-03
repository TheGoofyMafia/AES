import random
from Crypto.Cipher import AES
import binascii
from Padding import pad, unpad
import os
from init import key,iv

def Encrypt():
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
encd = Encrypt()