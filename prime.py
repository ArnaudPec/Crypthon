# My tiny implementation of asymetric ciphers

from math import gcd, log2
from numpy import random

#Implement a good primality test

# Femat's primality test
def fermat_prime_test(n):
    if n <= 1 :
        return False
    else :
        a = random.random_integers(1,n)
        if a**(n-1) % n == 1:
            return True
        else :
            return False

# Miller rabin primality test
def miller_rab_prime_test(arg):
    if n <= 1 :
        return False
    else :

    return True


'''

    Input: integer n > 1.

    Find the smallest r such that Or(n) > (log2 n)2.
    If 1 < gcd(a,n) < n for some a ≤ r, output composite.
    If n ≤ r, output prime.
    For a = 1 to \scriptstyle\lfloor \scriptstyle{\sqrt{\varphi(r)}\log_2(n)} \scriptstyle\rfloor do

        if (X+a)n≠ Xn+a (mod Xr − 1,n), output composite;

    Output prime.

'''
# Aks primality test
# def aks_prime_test(n):
#     if n <= 1 :
#         return False
#     else :
#
#     #  If n = a^b for integers a > 1 and b > 1, output False.
#
#         b = 2
#         while b<log2(n):
#             a = n ** (1/b)
#             b+=1
#             if a.is_integer() :
#                 return False
