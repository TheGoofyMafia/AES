from Crypto.Cipher import AES
from init import key,iv
import struct
from Padding import unpad
sz = 4096
from F_Encryption import encd

with open('encfile.txt', 'rb') as fin:
    # iv = fin.read(16)



    with open('verfile', 'w') as fout:
        while True:
            encd1 = fin.read(sz)
            n = len(encd)
            # print (encd)
            # print(n)
            if n == 0:
                break
            # print(encd[-1])
            aes = AES.new(key, AES.MODE_CBC, iv)
            decd = (unpad(aes.decrypt(encd1), 16))
            decd = decd.decode("utf-8")
            # ct = b64decode(b64['decd'])
            print(decd)
            # fsz = struct.unpack('<Q', fin.read(struct.calcsize('<Q')))[0]
            # if fsz > n:
            #      fout.write(decd)
            # else:
            #     fout.write(decd[:fsz])  # <- remove padding on last block
            # fsz -= n
            fout.write(decd)
            break
if encd == encd1:
    print("Okay this is right")