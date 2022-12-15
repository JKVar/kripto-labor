import random
import utils

def generate_superincreasing_sequence(n):
    sequence = [random.randint(2,10)]
    total = sequence[0]

    for i in range(1,n):
        rand_num = random.randint(total+1, 2*total)
        sequence.append(rand_num)
        total += rand_num

    return sequence, total

def coprime(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c

    if a == 1:
        return True
    return False

def keygen_merkle_hellmann(n = 8):
    w, total = generate_superincreasing_sequence(n)
    q = random.randint(total+1, 2*total)

    r = random.randint(2, q-1)
    while coprime(r, q):
        r = random.randint(2, q-1)

    beta = tuple(map(lambda b: (r*b)%q, w))
    w = tuple(w)

    return beta, (w,q,r)

def char_to_binary_list(char):
    num = ord(char)
    return list(map(lambda k: int(k), bin(num)[2:]))

def encrypt_merkle_hellmann(plain_text, key: tuple):
    cipher_text = ''
    for char in plain_text:
        binary_list = utils.byte_to_bits(ord(char))
        # binary_list = char_to_binary_list(char)
        ci = sum(map(lambda x: x[0]*x[1], zip(binary_list, key)))
        cipher_text += chr(ci)

    return cipher_text

def decrypt_merkle_hellmann(cipher_text, key: tuple):
    raise NotImplementedError

def main():
    public_key, private_key = keygen_merkle_hellmann()
    print(public_key)
    message = 'Hello'
    print('-------------------')
    secret_msg = encrypt_merkle_hellmann(message, public_key)
    print('-------------------')

    print(secret_msg)

if __name__ == '__main__':
    main()
