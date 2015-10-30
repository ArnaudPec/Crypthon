#RSA
#This fle contains a really basic implementation of RSA,
# and functions to encrypt and decrypt a short text message

import prime

e= 2 ** 16 +1

# Return totient of n
# Calculated by computing (p-1)(q-1)

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
    k = prime.random.randrange(2,9) # ensure that p and q are of different size
    p = prime.gen_rand_prime(l//2 + k)
    q = prime.gen_rand_prime(l//2 - k)

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

# Setting up and testing the Algorithm
def test():
    l = int(input("Enter a key length :"))
    e = pow(2,16)+1
    p,q,n = generate_pqn(l)
    totient = calculate_totient_n(p,q)
    d = calculate_d(totient,e)

    print("Public key :",(e,n))
    print("Secrete key :",(d,n))

    m= input('Enter a text message (154 char max) :')
    while len(m)>154:
        m= input('Enter a text message (154 char max) :')

    cipherText = encrypt(n,conv_to_number(m),e)

    print("cipherText :\n",cipherText)

    message = decrypt(n, cipherText, d)
    mc = conv_to_ascii(message)
    print("message : \n", mc )
