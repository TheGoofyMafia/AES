from Crypto.Cipher import AES
from init import key,iv
from Padding import unpad
sz = 4893*4
from F_Encryption import data # There is no sense in adding this, however whenever this statement is removed, we face an error 'Padding is incorrent'. Just import anything from F_Encryption We'll Look into it
with open('encfile.txt', 'rb') as fin:
    # iv = fin.read(16)



    with open('verfile', 'w') as fout:
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
