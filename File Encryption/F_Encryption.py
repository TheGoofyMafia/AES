from Crypto.Cipher import AES
import time
from init import key,iv
import os
from Padding import pad
abc = 0.1
with open('Testing/big_test.txt') as finput:
    while True:
        time1 = time.perf_counter()
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
        print('The time taken to execute this program is: ', time.perf_counter() - time1)

