from Crypto.Cipher import AES
from init import key,iv
import os
from Padding import pad
abc = 0.1
fsz = os.path.getsize('/Users/goofy/Desktop/test.txt')
with open('big_test.txt') as finput:
    while True:
        global data
        data = finput.read()
        n = len(data)
        if n == 0:
            break
        elif n % 16 != 0:
            data += ' ' * (16 - n % 16)  # <- padded with spaces
        aes = AES.new(key, AES.MODE_CBC, iv)
        with open('encfile.txt', 'wb') as fout:
            # fout.write(iv)
            global encd
            encd = aes.encrypt(pad(data, 16))
            fout.write(encd)

