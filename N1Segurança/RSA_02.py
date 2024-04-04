from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Função para gerar as chaves RSA
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Função para criptografar usando RSA
def encrypt_rsa(public_key, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Função para descriptografar usando RSA
def decrypt_rsa(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# Exemplo de uso
private_key, public_key = generate_rsa_keys()
print("Chave privada:", private_key)
print("Chave pública:", public_key)

texto_original = "salve"
ciphertext = encrypt_rsa(public_key, texto_original)
print("Texto criptografado:", ciphertext)

texto_decifrado = decrypt_rsa(private_key, ciphertext)
print("Texto decifrado:", texto_decifrado)