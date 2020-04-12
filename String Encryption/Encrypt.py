from Crypto.Cipher import AES
from init import key, iv
from Padding import pad


def Encrypt():
    aes = AES.new(key, AES.MODE_CBC, iv)  # This is the encryption cipher
    print('#####################'
          '                     '
          'PLEASE INPUT ONLY 16 BYTES STRING'
          '                     '
          '#####################')
    global data
    data = input()  # <- 16 bytes OR add buffer to make it 16 bytes
    encd = aes.encrypt(pad(data, 16))
    return encd


encd = Encrypt()
print(encd)
