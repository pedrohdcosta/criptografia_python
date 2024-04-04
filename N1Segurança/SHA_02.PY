import hashlib

def hash_with_sha256(input_text):
    sha_signature = hashlib.sha256(input_text.encode()).hexdigest()
    return sha_signature

input_text = "Salve"
print(f"O hash SHA-256 de '{input_text}' é: {hash_with_sha256(input_text)}")
