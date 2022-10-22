#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
from distutils import text_file
from lib2to3.pgen2.token import CIRCUMFLEX
import utils

# Caesar Cipher

def encrypt_caesar(plaintext):
    """Encrypt plaintext using a Caesar cipher.

    Add more implementation details here.
    """
    encrypted_text = ''
    for ch in plaintext:
        encrypted_text += chr((ord(ch)-ord('A')+3) % 26 + ord('A'))
        
    return encrypted_text


def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.

    Add more implementation details here.
    """
    decrypted_text = ''
    for ch in ciphertext:
        decrypted_text += chr((ord(ch)-ord('A')-3) % 26 + ord('A'))

    return decrypted_text


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    """Encrypt plaintext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """
    keyword_length = len(keyword)
    encrypted_text = ''
    for i,ch in enumerate(plaintext):
        encrypted_text += chr((ord(ch) + ord(keyword[i%keyword_length]) - 2*ord('A')) % 26 + ord('A'))

    return encrypted_text

def decrypt_vigenere(ciphertext, keyword):
    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """
    keyword_length = len(keyword)
    decrypted_text = ''
    for i,ch in enumerate(ciphertext):
        decrypted_text += chr((ord(ch) - ord(keyword[i%keyword_length]) - 2*ord('A')) % 26 + ord('A'))

    return decrypted_text

# Scytale Cipher

def encrypt_scytale(plaintext, circumference):
    encrypted_text = ''
    text_length = len(plaintext)

    for i in range(circumference):
        j = 0
        while i+j*circumference < text_length:
            encrypted_text += plaintext[i+j*circumference]
            j += 1

    return encrypted_text

def decrypt_scytale(ciphertext, circumference):
    decrypted_text = ''
    text_length = len(ciphertext)
    length_div_circumference = text_length//circumference

    for i in range(length_div_circumference):
        j = 0
        while i + j*(length_div_circumference) < text_length:
            decrypted_text += ciphertext[i + j*length_div_circumference]
            j += 1
        
    return decrypted_text

# Railfence Cipher

def encrypt_railfence(plaintext, num_rails):
    encrypted_text = ''
    text_len = len(plaintext)
    faktor1 = num_rails*2
    faktor2 = -2
    i = 0

    while faktor1 >= 2:
        faktor1 -= 2
        faktor2 += 2
        j = i

        while j < text_len:
            if faktor1 > 0:
                encrypted_text += plaintext[j]
                j += faktor1
            if j>= text_len:
                break
            else:
                if faktor2 > 0:
                    encrypted_text += plaintext[j]
                    j += faktor2
        
        i += 1
    
    return encrypted_text

def decrypt_railfence(ciphertext, num_rails):
    decrypted_text = ''
    nn = len(ciphertext)
    fence_matrix = [['' for j in range(nn)] for i in range(num_rails)]

    # building railfence matrix
    k = 0
    faktor1 = num_rails*2
    faktor2 = -2
    for i in range(num_rails):
        faktor1 -= 2
        faktor2 += 2
        j = i
        while j < nn:
            if faktor1 > 0:
                fence_matrix[i][j] = ciphertext[k]
                j += faktor1
                k += 1
            if j >= nn:
                break
            else:
                if faktor2 > 0:
                    fence_matrix[i][j] = ciphertext[k]
                    j += faktor2
                    k += 1
    
    # read railfence matrix
    direction = 1 # 1 - down; -1 - up
    j = 0
    for i in range(nn):
        decrypted_text += fence_matrix[j][i]
        if j + direction >= num_rails or j + direction < 0:
            direction = -direction
        j += direction

    return decrypted_text

# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here

