
# https://wiki.python.org/moin/Generators

import time

# Build and return a list (the usual way to do this type of thing)
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))

# Using the generator pattern (an iterable)
class FirstN(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(FirstN(1000000))


# a generator that yields items instead of returning a list
def firstn_shortcut(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn_shortcut(1000000))


def sum_range(n):
    sum(range(n))

def sum_xrange(n):
    sum(xrange(n))

def __black_box__timed_execute(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end-start

number = 10**8

# Note: Python 2.x only
# using a non-generator

no_generator_time = __black_box__timed_execute(sum_range, number)

# using a generator
generator_time = __black_box__timed_execute(sum_xrange, number)


print('with generator {} vs no generator {}'.format(generator_time, no_generator_time))


