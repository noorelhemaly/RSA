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


