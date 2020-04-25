import time
from multiprocessing.dummy import Pool as ThreadPool
import random
import string
#num_cores = multiprocessing.cpu_count()
sz = int(input('Size of test file in bytes: '))
open('big_test.txt', 'w').close()
pool = ThreadPool(4)
def test(sz):
    with open('big_test.txt', 'a+') as testfile:
        global time1
        time1 = time.perf_counter()
        random1 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(sz)])
        testfile.write(random1)

test(sz)
print('The time taken to execute this program is: ', time.perf_counter() - time1)
# This is a test generator for text files ONLY...