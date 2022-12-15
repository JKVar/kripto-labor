import random

def generate_superincreasing_sequence(n):
    sequence = [random.randint(2,11)]
    total = sequence[0]

    for i in range(1,n):
        rand_num = random.randint(total+1, 2*total)
        sequence.append(rand_num)
        total += rand_num

    return sequence

def keygen_merkle_hellmann(n = 8):
    raise NotImplementedError

def encrypt_merkle_hellmann():
    raise NotImplementedError

def decrypt_merkle_hellmann():
    raise NotImplementedError

def main():
    print('main function')

if __name__ == '__main__':
    main()
