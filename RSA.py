# Import necessary libraries
import random  
import math  
import time  

#function to generate a prime number of specified bits
def generate_prime(bits):
    while True:
        p = random.randint 
        if prime(p):
            return p
        
#function to check if a number is prime
def prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#function to calculate the modular inverse
def modular_inverse(a,m):
    g, x, y = extended_gcd (a,m)
    if g !=1:
        raise ValueError("Modular inverse doesn't exist")
    return x % m

#function to calculate the extended greatest common divisor 
def extended_gcd (a,b):
    if b = 0:
        return a,1,0
    g, x, y = extended_gcd(b, a%b)
    return g, 

#funtion to generate RSA keys (private,public)
def keys (bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q -1)

    while True:
        e = random.randint 2, phi - 1)
        if math.gcd(e, phi) == 1:
            break
    d = modular_inverse(e, phi)
    return (e, n), (d, n)

#function to encrypt a text
def encrypt(text, public_key):
    e, n = public_key
    encryptedtext = [pow(ord(char), e, n) for char in text]
    return encryptedtext

#function to decrypt the encrypted text
def decrypt (encryptedtext, private_key)
    d, n = private_key
    text = [chr(pow(char, d,n)for char in encryptedtext)]
    return text

#function for factorization approach to calculate private exponent
def factorization_approach(public_key):
    start_time = time.perf_counter()
    e, n = public_key
    p, q = factorize(n)
    phi = (p - 1) * (q - 1)
    d = modular_inverse(e, phi)
    end_time = time.perf_counter()
    return d, end_time - start_time

#function to factorize a number
def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        # Check if i is prime
            if prime(i):
                if prime(n // i):
                    return i, n // i
    return None

#function for bruteforce approach to calculate private exponent
def bruteforce_approach(public_key, factorization_d):
    start_time = time.perf_counter()
    e, n = public_key
    p, q = factorize(n)
    phi = (p - 1) * (q - 1)
    d = factorization_d + 1 # Start searching for d from factorization_d + 1
    while True:
        if (e * d) % n == 1:
            break
        d += 1
    end_time = time.perf_counter()
    return d, end_time - start_time
