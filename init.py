import random
from Crypto.Cipher import AES
# from Crypto.Cipher import adec
import binascii
import os
# key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
key = os.urandom(16)
print(key)
# print('key', [x for x in key])
# prints
# key ['+', 'Y', '\xd1', '\x9d', '\xa0', '\xb5', '\x02', '\xbf', ';', '\x15', '\xef', '\xd5', '}', '\t', ']', '9']
# iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
iv = os.urandom(16)
# print('iv', [x for x in iv])

# ENCRYPTION
aes = AES.new(key, AES.MODE_CBC, iv)
data = 'hello world 1234'  # <- 16 bytes OR add buffer to make it 16 bytes
encd = aes.encrypt(data)
print(encd)

# DECRYPTION

aes = AES.new(key, AES.MODE_CBC, iv)
decd = aes.decrypt(encd)
print(decd)
