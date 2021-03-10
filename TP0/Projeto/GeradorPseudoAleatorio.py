import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Tamanho do bloco em bytes(64 bits)
SIZE_BLOCK = 8
# Parametro n para a decisão de quantas palavras se deve gerar (2^n)
PARAM_N = 3

''' 
Funcao usada para derivar uma chave
'''


def derivationKey(password):
    info = None
    # Geracao do salt para a derivacao da chave
    salt = os.urandom(16)
    hkdf = HKDF(
        hashes.SHA256(),
        32,
        salt,
        info,
    )
    return hkdf.derive(password)


def gerador(seed):
    # A sequencia de palavras tem de ter tamanho suficiente para as 2^n palavras
    digest = hashes.Hash(hashes.SHAKE256(SIZE_BLOCK*(2**PARAM_N)))
    digest.update(seed)
    return digest.finalize()


def main():

    # O utilizador deve introduzir uma password
    pw = input("Introduza uma password: ")
    # Gerar uma chave/seed para o gerador de números aleatórios
    seed = derivationKey(bytes(pw.encode("utf-8")))
    # Sequencia aleatoria gerada pelo gerador
    s = gerador(seed)
    # Criar as palavras como long integers
    blocos = []
    for i in range(2**PARAM_N):
        blocos.append(s[i*SIZE_BLOCK:i*SIZE_BLOCK + SIZE_BLOCK])
        print(blocos[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
