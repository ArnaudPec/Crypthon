# My tiny implementation of asymmetric ciphers

from math import gcd, log2
import random

## Implement a good primality test

# Femat's primality test
def fermat_prime_test(n):
    if n <= 1 :
        return False
    else :
        a = random.randrange(1,n)
        # if a**(n-1) % n == 1: TO SLOW
        if pow(a,n-1,n) == 1 :
            return True
        else :
            return False

# Miller rabin primality test
# Probabilistic test
# Inputs
# n : tested number
# r : number of round, recommended value around 45
def miller_rab_prime_test(n,r):
    if n <= 1 :
        return False
    else :
        k,m = decompose(n-1)

        for _ in range(r):
            a = random.randrange(2,n-1)
            x = pow(a, m, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(k - 1):
                #x = x* x % n
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

def decompose(n):
    b=0
    while n % 2 == 0 :
      n //= 2
      b += 1
    return b, n

# Really basic prime generator

def prime_gen(n,max):
    for x in range(n, max +1 ) :
        isPrime = True
        for y in range(2, int(x ** 0.5) +1):
            if x % y == 0 :
                isPrime = False
                break
        if isPrime :
            print(x)

# Find a primitive root
# p is prime
def primitive_r(p):
    a = 2
    t = p -1
    while a < pow(p,1/2) :
        b = pow(a,t//a,p)
        if b != 1:
            return a
        a = nextPrime(a)
    else :
        return False

def nextPrime(a):
    while True :
        a += 1
        if fermat_prime_test(a):
            return a


# Random prime generator
# returns a prime between 2^n and 2^+1 (for n>32)
def gen_rand_prime(n):
    if n<32:
        n=32
    k = random.randrange(1,n-1)
    for i in range(pow(2,n)+pow(2,k)+1,pow(2,n+1),2):
        if miller_rab_prime_test(i,40):
            return i
    else :
        return 0


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
