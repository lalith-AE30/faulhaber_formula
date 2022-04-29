import math

def binomial(n,k):
    """n choose k"""
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

from functools import lru_cache
from fractions import Fraction as Fr
@lru_cache(maxsize=None)
def bernoulli(n:int):
    """nth Bernoulli number"""
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
    return A[0]

def faulhaber(n:int,p:int) -> int:
    """Sum of first n natural numbers to the power of p"""
    return 1/(p+1)*sum([(-1)**j*binomial(p+1,j)*bernoulli(j)*n**(p+1-j) for j in range(0,p+1)])
