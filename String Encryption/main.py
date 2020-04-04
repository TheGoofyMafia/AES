from Decrypt import *
from Encrypt import *
import init
# import os
# import struct
# sz = 2048
# fsz = os.path.getsize('/Users/goofy/Desktop/test.txt')
# with open('/Users/goofy/Desktop/test.txt') as fin:
#     while True:
#         data = fin.read(sz)
#         n = len(data)
#         if n == 0:
#             break
#         elif n % 16 != 0:
#             data += ' ' * (16 - n % 16)  # <- padded with spaces
#         aes = AES.new(key, AES.MODE_CBC, iv)
#         encd = aes.encrypt(data)
#         with open('/Users/goofy/Desktop/encfile', 'wb') as fout:
#             fout.write(struct.pack('<Q', fsz))
#             fout.write(iv)
#             fout.write(encd)

# with open('/Users/goofy/Desktop/encfile', 'wb') as fout:
#     fout.write(struct.pack('<Q', fsz))
#     fout.write(iv)

if data == decd:
    print('Your data is ' + decd)
    print("Working with success")
else:
    print("Try again")