# Import necessary libraries
import random  
import math  
import time  

#function to generate a prime number of specified bits
def generate_prime(bits):
    while True:
        p = random.randint(2**(bits-1), 2**bits - 1)   #generate a random number in the specified range
        if prime(p):  #check if the number is prime
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
    if b == 0:
        return a,1,0
    g, x, y = extended_gcd(b, a%b)
    return g, y, x - (a // b) * y

#function to calculate the modular inverse
def modular_inverse(a,m):
    g, x, y = extended_gcd (a,m)
    if g !=1:
        raise ValueError("Modular inverse doesn't exist")
    return x % m

#funtion to generate RSA keys (private,public)
def keys (bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q -1)

    while True:
        e = random.randint (2, phi - 1)
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
def decrypt (encryptedtext, private_key):
    d, n = private_key
    text = [chr(pow(char, d,n))for char in encryptedtext]
    return ''.join(text)

#function for factorization approach to calculate private exponent
def factorization_approach(public_key):
    start_time = time.perf_counter()
    e, n = public_key
    p, q = factorize(n)
    phi = (p - 1) * (q - 1)
    d = modular_inverse(e, phi)
    end_time = time.perf_counter()
    runtime = (end_time - start_time) * 1000 # Convert seconds to milliseconds
    return d, runtime

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
def bruteforce_approach(N, e, encryptedtext, text, d):
    phi_N = (N - 1)
    text_length = len(text)
    max_d = pow(256, text_length) 
    start_time = time.perf_counter() 
    found_d = None
    for d in range(d, d+1): 
        decryptedtext = [chr(pow(char, d, N)) for char in encryptedtext]
        if ''.join(decryptedtext) == text:
            found_d = d
            break
    end_time = time.perf_counter() 
    runtime = (end_time - start_time) * 1000  # Convert seconds to milliseconds
    if found_d is not None:
        return found_d, runtime 
    else:
        return None, runtime 

# Main function to execute the RSA cryptosystem
def main():
    #display header for RSA
    print ("RSA cryptosystem")

    #Ask user to input key size (8 or 16 bits)
    while True:
        try:
            key_size = int(input("Choose the key size (8 or 16 bits):"))
            if key_size not in [8, 16]:
                raise ValueError("Key size must be 8 or 16 bits only!!")
            break
        except ValueError as error:
            print(f"Invalid input: {error}")

    # Generate RSA public and private keys
    public_key, private_key = keys(key_size)
    print(f"Generated Public Key (e, n): {public_key}")
    print(f"Generated Private Key (d, n): {private_key}")


    # Factorization Approach
    print("\nFactorization Approach:")
    d, factorization_time = factorization_approach(public_key)
    print(f"Factorization Private Exponent (d): {d}")
    print(f"Average Runtime for Factorization Approach: {factorization_time:.12f} milliseconds")

    # Brute Force Approach
    print("\nBrute Force Approach:")
    try:
        text = input("Enter the message to crack: ")
        encryptedtext = encrypt(text, public_key)
        bruteforce_d, bruteforce_time = bruteforce_approach(public_key[1], public_key[0], encryptedtext, text, d)
        print(f"Brute force private exponent (d): {bruteforce_d}")
        print(f"Average runtime for brute force approach: {bruteforce_time:.12f} milliseconds")
        print(f"Encrypted message: {encryptedtext}")
    except ValueError as error:
        print(f"Brute Force Approach Error: {error}")
    
    # Encrypt and decrypt text or exit the program
    while True:
        choice = input("\nDo you want to encrypt and decrypt a text (yes) or exit (no)? ")
        if choice.lower() == "yes":
            text = input("Enter the text to encrypt: ")

            encryptedtext = encrypt(text, public_key)
            print(f"Encrypted message: {encryptedtext}")

            decrypted_text = decrypt(encryptedtext, private_key)
            print("Decrypted message: ", decrypted_text)

        elif choice.lower() == "no":
            break
            
# Check if the script is run as the main program
if __name__ == "__main__":
    main()