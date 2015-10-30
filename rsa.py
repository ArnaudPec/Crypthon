#RSA

import random
import prime

p = 24564797371
q = 145647973
e= 2 ** 16 +1

# Return totient of n
def calculate_totient_n(p,q):
    return (p-1)*(q-1)

# Return n
def calculate_n(p,q):
    return p*n

# Return primes q,p and modulus n = pq
# Modulus length as a parameters
# To avoid Fermat's little theorem factorization, p and q must be choosen of
# slightly different size
def generate_pqn(l):
    if l %2 != 0:
        l+=1
    k = random.randrange(2,9) # ensure that p and q are of different size
    p = prime.rand_prime(l//2 + k)
    q = prime.rand_prime(l//2 - k)

    return p,q,p*q

# Return the encryption key d
def calculate_d(totient,e):
    return extended_gcd(totient,e) % totient

# Extended euclidian Algorithm
def extended_gcd(a, b):
    (s, o_s) =( 0,1)
    (t, o_t) =( 1,0)
    (r, o_r) =( b, a)

    while r != 0 :
        quotient = o_r // r
        (o_r, r) = (r, o_r - quotient * r)
        (o_s, s) = (s, o_s - quotient * s)
        (o_t, t) = (t, o_t - quotient * t)
    return o_t

#Encryption
def encrypt(n,m,e):
    return pow(m,e,n)

#Decryption
def decrypt(n,c,d):
    return pow (c,d,n)

# String to number conversion
def conv_to_number(message):
    l=''
    for i in message.upper() :
        l+= str(ord(i))
    return int(l)

# Number to string
def conv_to_ascii(number):
    l = list(str(number))
    s=''
    for i in range(0,len(l),2):
        s+= chr(int("".join([l[i],l[i+1]])))
    return s
