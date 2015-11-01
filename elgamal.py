#ElGamal
#This fle contains a really basic implementation of ElGamal,
# and functions to encrypt and decrypt a short text message

import prime

# Generate ElGamal's secret key a
def generate_a(p):
    a = prime.random.randrange(p-1)
    return a

# Calculate beta
def calculate_beta(alpha, a, p):
    return pow(alpha,a,p)

# Encrypt a message
def encrypt(alpha,beta,k,m):
    return (pow(alpha,k),pow(beta,k)*m)

# Decrypt the message, input c the ciphertext, a the secret key
def decrypt(c0, c1,a):
    return pow(c0,-a)*c1
