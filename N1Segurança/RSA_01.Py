import random

def gcd(a, b):
    """Algoritmo de Euclides para encontrar o MDC (máximo divisor comum)."""
    while b != 0:
        a, b = b, a % b
    return a

def find_mod_inverse(a, m):
    """Encontra o inverso multiplicativo de 'a' modulo 'm' usando o algoritmo estendido de Euclides."""
    if gcd(a, m) != 1:
        return None  # Nenhum inverso se a e m não forem coprimos

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def select_e(phi):
    """Seleciona um valor 'e' tal que e seja coprimo com 'phi'."""
    e = 2
    while gcd(e, phi) != 1:
        e += 1
        if e >= phi:  # Caso improvável, mas para garantir que não entremos em um loop infinito
            return None
    return e

def rsa_key_generation(p, q):
    """Gera as chaves pública e privada a partir de dois números primos 'p' e 'q'."""
    n = p * q
    phi = (p - 1) * (q - 1)

    e = select_e(phi)
    d = find_mod_inverse(e, phi)

    # Chave pública (e, n) e chave privada (d, n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Criptografa uma mensagem com a chave pública."""
    e, n = public_key
    # Converte a mensagem em um número usando codificação simples (por exemplo, convertendo cada caractere em seu valor ASCII)
    message_as_int = sum([ord(char) << (8 * i) for i, char in enumerate(message)])
    # Aplica a criptografia RSA
    ciphertext = pow(message_as_int, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    """Descriptografa uma mensagem cifrada com a chave privada."""
    d, n = private_key
    # Aplica a descriptografia RSA
    message_as_int = pow(ciphertext, d, n)
    # Converte o número de volta para uma string (mensagem original)
    message = "".join([chr((message_as_int >> (8 * i)) & 0xFF) for i in range(len(str(message_as_int)) // 2)])
    return message

# Exemplo de uso
p = 61
q = 53
public_key, private_key = rsa_key_generation(p, q)

original_message = "Hello RSA!"
print("Original Message:", original_message)

ciphertext = encrypt(original_message, public_key)
print("Ciphertext:", ciphertext)

decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted Message:", decrypted_message)
