Simple implementation of AES encryption standard using python, created using Pycrypto.

IV - initialization vector and it is is generated with every encryption, and its purpose is to produce different encrypted data so that an attacker cannot use cryptanalysis to infer key data or message data.

key is the standard encryption 16, 24 or 32 byte key.

The text accordingly also has to be in the said size i.e 16,24 or 32 byte. So we need to add a buffer if the size of the text is not in the said format.

You can test the String Encryption using main.py.




# ~~CREATE PAD BUFFER~~ - DONE
# IMPLEMENT KEY SIZE(16,24,32) ACCORDING TO THE TEXT INPUT FOR ENCRYPTION
# CREATE AN ENGINE FOR KEY GENERATION
