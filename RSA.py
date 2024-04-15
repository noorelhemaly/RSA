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



