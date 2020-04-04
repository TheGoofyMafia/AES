from Crypto.Cipher import AES
from init import *
import struct
from Padding import pad
sz = 2048
fsz = os.path.getsize('/Users/goofy/Desktop/test.txt')
with open('test.txt') as fin:
    while True:
        data = fin.read(sz)
        n = len(data)
        if n == 0:
            break
        # elif n % 16 != 0:
            # data += ' ' * (16 - n % 16)  # <- padded with spaces
        aes = AES.new(key, AES.MODE_CBC, iv)
        with open('encfile.txt', 'wb') as fout:
            # fout.write(iv)
            encd = aes.encrypt(pad(data, 16))
            fout.write(encd)
            # fout.write(struct.pack('<Q', fsz))

# with open('/Users/goofy/Desktop/encfile', 'wb') as fout:
#     fout.write(struct.pack('<Q', fsz))
#     fout.write(iv)

# if data == decd:
#     print("Working with success")
# else:
#     print("Try again")