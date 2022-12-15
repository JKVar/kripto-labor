import random
import utils

# returns the generated superincreasing sequence and the total sum of it
def generate_superincreasing_sequence(n):
    sequence = [random.randint(2,10)]
    total = sequence[0]

    for i in range(1,n):
        rand_num = random.randint(total+1, 2*total)
        sequence.append(rand_num)
        total += rand_num

    return sequence, total

# return the coprime of a and b
def coprime(a, b):
    while b:
        a, b = b, a % b

    if a == 1:
        return True

    return False

# generates the public and private key with Merkle-Hellman algorithm
def keygen_merkle_hellman(n = 8):
    w, total = generate_superincreasing_sequence(n)
    q = random.randint(total+1, 2*total)

    r = random.randint(2, q-1)
    while not coprime(r, q):
        r = random.randint(2, q-1)

    beta = tuple(map(lambda b: (r*b)%q, w))
    w = tuple(w)

    return beta, (w,q,r)

# encrypts the message with Merkle-Hellman
def encrypt_merkle_hellman(plain_text, key: tuple):
    cipher_text = ''
    for char in plain_text:
        binary_list = utils.byte_to_bits(ord(char))
        ci = sum(map(lambda x: x[0]*x[1], zip(binary_list, key)))
        cipher_text += chr(ci)

    return cipher_text

# solves the superincreasing subset sum 
def solve_supinc_ss(w, cc):
    indexes = []
    key_length = len(w)
    subset_sum = 0

    for index, wi in enumerate(w[::-1]):
        if wi <= cc:
            subset_sum += wi
            cc = cc - wi
            indexes.append(key_length - index)

    return indexes

# decrypts the message with Merkle-Hellman
def decrypt_merkle_hellman(cipher_text, key: tuple):
    w, q, r = key
    key_length = len(w)
    s = utils.modinv(r,q) # modular inverse
    decrypted_text = ''

    for char in cipher_text:
        cc = (ord(char)*s) % q
        indexes = solve_supinc_ss(w, cc)
        decrypted_text += chr(sum(map(lambda i: 2**(key_length-i), indexes)))

    return decrypted_text

def main():
    public_key, private_key = keygen_merkle_hellman()
    message =  input(' [] Enter the message here:\n >> ')

    secret_msg = encrypt_merkle_hellman(message, public_key)
    decrypted_msg = decrypt_merkle_hellman(secret_msg, private_key)

    print('\n [] Encrypted message:\n >>', secret_msg)
    print(' [] Decrypted message:\n >>', decrypted_msg)

if __name__ == '__main__':
    main()
