with open('verfile') as decrypted:
    with open('big_test.txt') as original:
        text = original.read()
        final = decrypted.read()
        if text ==  final:
            print("It is working. File encryption decryption works.")
        else:
            print("Please try again. There is an error.")
            print("The original file contained:", text)
            print("The decrypted file contains:", final)