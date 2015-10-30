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

# generate a nb bit modulus
# def generate_npq(nb) :
    # a = random.randrange(3,10)

# Return the encryption key d
def calculate_d(totient,e):
    return extended_gcd(totient,e) % totient

# Extended euclidian Algorithm
def extended_gcd(a, b):
    (s, old_s) =( 0,1)
    (t, old_t) =( 1,0)
    (r, old_r) =( b, a)

    while r != 0 :
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return old_t

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
