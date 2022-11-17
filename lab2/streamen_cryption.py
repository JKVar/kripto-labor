def stream_encryption(message, key, key_generator: function):
    # i need to expand the key with the key_generator algorithm
    # then xor the message with the expanded key
    print(message)