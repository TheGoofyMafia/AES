import random
import string
with open('big_test.txt', 'w') as testfile:
    sz = int(input('Size of test file in bytes: '))
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(sz)])
    testfile.write(random)

# This is a test generator for text files ONLY...