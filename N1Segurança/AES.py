from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def cifrar_AES(texto, chave):
    if len(chave) != 16:
        raise ValueError("A chave deve ter 16 bytes (128 bits).")
    
    cipher = AES.new(chave, AES.MODE_CBC)
    
    texto_padded = pad(texto.encode(), AES.block_size)
    
    texto_cifrado = cipher.encrypt(texto_padded)
    
    return cipher.iv, texto_cifrado

def decifrar_AES(iv, texto_cifrado, chave):
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    
    texto_decifrado_padded = cipher.decrypt(texto_cifrado)
    
    texto_decifrado = unpad(texto_decifrado_padded, AES.block_size)
    
    return texto_decifrado.decode()

chave = get_random_bytes(16)

texto = "salve"

iv, texto_cifrado = cifrar_AES(texto, chave)
print(f"Texto Cifrado (em bytes): {texto_cifrado}")

texto_decifrado = decifrar_AES(iv, texto_cifrado, chave)
print(f"Texto Decifrado: {texto_decifrado}")
