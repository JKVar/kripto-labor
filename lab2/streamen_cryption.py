import solitaire as keygen

def xor(barr1, barr2):
    new_barr = bytearray(b'')
    for a, b in zip(barr1, barr2):
        new_barr.append(a^b)

    return new_barr

def stream_encryption(message, key, key_generator):
    array_len = len(message)

    key = key_generator(key, array_len)
    encoded_message = xor(message, key)

    return encoded_message

solitaire_key = [255, 94, 198, 60, 217, 87, 176, 42, 107, 233, 148, 117, 122, 39, 132, 196, 55, 215, 96, 46, 33, 45, 235, 242, 44, 101, 167, 240, 50, 232, 200, 92, 4, 3, 81, 139, 228, 156, 14, 31, 64, 145, 85, 181, 72, 77, 248, 131, 191, 166, 32, 125, 41, 152, 182, 134, 237, 24, 246, 110, 207, 105, 5, 120, 133, 84, 243, 180, 40, 54, 244, 119, 128, 147, 25, 56, 234, 164, 239, 143, 172, 61, 230, 62, 227, 210, 83, 206, 70, 11, 113, 190, 118, 43, 168, 130, 201, 170, 57, 149, 177, 124, 155, 27, 171, 75, 99, 68, 63, 98, 48, 103, 58, 97, 121, 82, 8, 245, 199, 104, 34, 26, 163, 88, 249, 2, 220, 204, 151, 19, 169, 16, 229, 108, 1, 157, 89, 112, 144, 69, 106, 80, 231, 9, 38, 253, 126, 91, 136, 205, 218, 224, 78, 86, 194, 49, 158, 17, 53, 251, 73, 160, 20, 254, 209, 138, 186, 189, 137, 36, 123, 141, 12, 21, 59, 90, 175, 79, 15, 185, 236, 250, 187, 127, 116, 51, 193, 10, 247, 202, 71, -255, 52, 114, 129, 178, 165, 197, 93, 6, 13, 115, 142, 18, 109, 35, 192, 100, 203, 95, 102, 37, 184, 146, 67, 241, 23, 211, 66, 173, 188, 153, 150, 183, 179, 65, 213, 22, 216, 76, 74, 30, 7, 225, 226, 140, 29, 221, 219, 111, 195, 238, 135, 174, 159, 47, 161, 208, 212, 214, 154, 222, 162, 28, 223, 252]
bbs_key = 1988

### Blum-Blum-Shub
print('Blum-blum-shub')
print('=== Szoveg kodolasa ===')
st = input('Kodolni kivant szoveg: ')
st_bin = bytearray(st, 'ascii')
encoded_message = stream_encryption(st_bin, bbs_key, keygen.blum_blum_shub)
decoded_message = stream_encryption(encoded_message, bbs_key, keygen.blum_blum_shub)

print(st_bin)
print(encoded_message)
print(decoded_message)

# file-ra teszt
print('\n=== File kodolasa ===')
fname = 'message.jpg'
try:
    fin = open(fname, 'rb')
    barr = fin.read()
    encoded_message = stream_encryption(barr, bbs_key, keygen.blum_blum_shub)
    with open('encoded_bbs.jpg', 'wb') as fenc:
        fenc.write(encoded_message)

    decoded_message = stream_encryption(encoded_message, bbs_key, keygen.blum_blum_shub)
    with open('decoded_bbs.jpg', 'wb') as fdec:
        fdec.write(decoded_message)

    fin.close()
except FileNotFoundError:
    print('nem sikerult ', fname, '-t megnyitni')


### solitaire
print('\n-------------------------------------\n')
print('Solitaire algoritmus')
# szoveg kodolasa
print('=== Szoveg kodolasa ===')
st = input('Kodolni kivant szoveg: ')
st_bin = bytearray(st, 'ascii')
encoded_message = stream_encryption(st_bin, solitaire_key, keygen.solitaire)
decoded_message = stream_encryption(encoded_message, solitaire_key, keygen.solitaire)

print(st_bin)
print(encoded_message)
print(decoded_message)

# file-ra teszt
print('\n=== File kodolasa ===')
fname = 'message.jpg'
try:
    fin = open(fname, 'rb')
    barr = fin.read()

    encoded_message = stream_encryption(barr, solitaire_key, keygen.solitaire)
    with open('encoded_solitaire.jpg', 'wb') as fenc:
        fenc.write(encoded_message)

    decoded_message = stream_encryption(encoded_message, solitaire_key, keygen.solitaire)
    with open('decoded_solitaire.jpg', 'wb') as fdec:
        fdec.write(decoded_message)

    fin.close()
except FileNotFoundError:
    print('nem sikerult ', fname, '-t megnyitni')
