import time
from Fibgen import Fibgen


def test_fib():
    start = time.clock()
    counter = 0
    for n in Fibgen.fib():
        #print n
        counter += 1
        if counter == 30:
            break
    no_memo_time = time.clock() - start
    print "\n%s iterations took %s seconds without memoization" % (counter, no_memo_time)

    new_start = time.clock()
    counter = 0
    for n in Fibgen.fib(1):
        counter += 1
        if time.clock() - new_start > no_memo_time:
            break

    print "\nwith the same time, memoization passed %s iterations" % counter

test_fib()