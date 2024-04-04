import struct

def my_simple_sha(input_text):
    message = add_padding(input_text)
    blocks = divide_in_blocks(message, 64)

    hash_values = initialize_hash()

    for block in blocks:
        expanded_block = expand_block(block)
        hash_values = compress_hash(hash_values, expanded_block)

    final_hash = concatenate_hash(hash_values)
    return final_hash

def add_padding(input_text):
    length = len(input_text) * 8
    padding = b'\x80' + b'\x00' * (63 - (length // 8 % 64)) + struct.pack('>Q', length)
    return input_text.encode() + padding

def divide_in_blocks(message, block_size):
    return [message[i:i+block_size] for i in range(0, len(message), block_size)]

def initialize_hash():
    return [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

def expand_block(block):
    return block

def compress_hash(hash_values, block):
    for i in range(len(block)):
        hash_values[i % 4] = (hash_values[i % 4] + block[i]) % 0x100000000
    return hash_values

def concatenate_hash(hash_values):
    return ''.join(format(value, '08x') for value in hash_values)

input_text = "salve"
hash_result = my_simple_sha(input_text)
print(f"O hash simplificado de '{input_text}' é: {hash_result}")
