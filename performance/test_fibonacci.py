# -*- coding: utf-8 -*-
import sys 
import functools


@functools.lru_cache()
def fibonacci_cached(n):
    if n < 2:
        return n
    else:
        return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
        

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        

if __name__ == '__main__':
    n = 30
    if sys.argv[-1] == 'cache':
        fibonacci_cached(n)
    else:
        fibonacci(n)
     
# no_cache version
# python3 -m cProfile -s calls test_fibonacci.py no_cache
     
# cache version
# python3 -m cProfile -s calls test_fibonacci.py cache
     
'''        
Ncalls: The number of calls that were made to the function
Tottime: The total time spent in seconds within this function with all sub-
    functions excluded
    Percall, tottime / ncalls
Cumtime: The total time spent within this function, including sub-functions
    Percall, cumtime / ncalls
'''
