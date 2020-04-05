from Crypto.Cipher import AES
from init import *
import struct
from Padding import unpad
sz = 2048


with open('encfile.txt', 'rb') as fin:

    # iv = fin.read(16)

    aes = AES.new(key, AES.MODE_CBC, iv)

    with open('verfile.txt', 'wb') as fout:
        while True:
            data = fin.read(sz)
            n = len(data)
            print(n)
            if n == 0:
                break
            # decd = unpad(aes.decrypt(data),16)
            decd = aes.decrypt(data)
            #decd = decd.decode("utf-8")
            #fsz = struct.unpack('<Q', fin.read(struct.calcsize('<Q')))[0]
            # if fsz > n:
            #     fout.write(decd)
            # else:
            #     fout.write(decd[:fsz])  # <- remove padding on last block
            # fsz -= n
            fout.write(decd)