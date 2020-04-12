from Crypto.Cipher import AES

from Encrypt import encd
from Padding import unpad
from init import key, iv



def decrypt(encd):
    #iv = encd[:AES.block_size]
    aes = AES.new(key, AES.MODE_CBC, iv) # encryption Cipher
    print(encd[-1])
    global decd
    decd = (unpad(aes.decrypt(encd), 16))
    decd = decd.decode("utf-8")
    return decd
decd = decrypt(encd)
print(decd)