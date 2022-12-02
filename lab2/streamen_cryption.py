import solitaire as keygen

def xor(barr1, barr2):
    new_barr = bytearray(b'')
    for a, b in zip(barr1, barr2):
        new_barr.append(a^b)

    return new_barr

def stream_encryption(message, key, key_generator):
    array_len = len(message)

    key = key_generator(key, array_len)
    # print(key)
    encoded_message = xor(message, key)
    # print(encoded_message)

    return encoded_message

st = 'Hello World!'
st_bin = bytearray(st, 'ascii')
key = 1988
# print(st_bin)
encoded_message = stream_encryption(st_bin, key, keygen.blum_blum_shub)
decoded_message = stream_encryption(encoded_message, key, keygen.blum_blum_shub)

print(st_bin)
print(encoded_message)
print(decoded_message)
