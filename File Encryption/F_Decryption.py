from Crypto.Cipher import AES
from init import key,iv
import time # For Testing Purposes
from Padding import unpad
import F_Encryption # There is no sense in adding this, however whenever this statement is removed, we face an error 'Padding is incorrent'. Just import anything from F_Encryption We'll Look into it
with open('encfile.txt', 'rb') as fin:
    # iv = fin.read(16)



    with open('Testing/verfile', 'w') as fout:
        time1 = time.perf_counter()
        while True:
            encd1 = fin.read()
            n = len(encd1)
            if n == 0:
                break
            aes = AES.new(key, AES.MODE_CBC, iv)
            decd = (unpad(aes.decrypt(encd1), 16))
            decd = decd.decode("utf-8")
            fout.write(decd)
            break

print('The time taken to execute this program is: ', time.perf_counter() - time1)