import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Tamanho do bloco em bytes(64 bits)
SIZE_BLOCK = 8
# Parametro n para a decisão de quantas palavras se deve gerar (2^n)
PARAM_N = 1

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


''' 
Método que gera a sequêncide caracteres 
a ser utilizada para cifrar os dados 
'''


def gerador(seed):
    # A sequencia de palavras tem de ter tamanho suficiente para as 2^n palavras
    digest = hashes.Hash(hashes.SHAKE256(SIZE_BLOCK * (2 ** PARAM_N)))
    digest.update(seed)
    return digest.finalize()


''' 
Método que permite gerar as 2**N words de 64 bits
'''


def generateRandomWords(key):
    # Sequencia aleatoria gerada pelo gerador
    s = gerador(key)
    # Criar as palavras como long integers
    blocos = []
    for i in range(2 ** PARAM_N):
        blocos.append(s[i * SIZE_BLOCK:i * SIZE_BLOCK + SIZE_BLOCK])
    return blocos


''' Método usado para realizar o xor entre duas strings '''


def xor_str(str1, str2):
    return bytes([_a ^ _b for _a, _b in zip(str1, str2)])


class GeradorPseudoAleatorio:
    """
    Construtor para objeto da classe GeradorPseudoAleatorio
    """

    def __init__(self, password):
        self.key = derivationKey(password)
        self.words = generateRandomWords(self.key)

    ''' 
    Método que permite cifrar uma mensagem 
    '''

    def cifrar(self, message):
        i = 0
        ciphertext = b''
        for word in self.words:
            # print(b"Bloco: " + message[i * SIZE_BLOCK:(i + 1) * SIZE_BLOCK] + b"; word: " + word)
            ciphertext += xor_str(message[i * SIZE_BLOCK:(i + 1) * SIZE_BLOCK], word)
            i += 1
        return ciphertext

    ''' 
    Metodo que permite decifrar uma mensagem 
    '''

    def decifrar(self, ciphertext):
        i = 0
        plaintext = b''
        for word in self.words:
            # print(b"Bloco: " + ciphertext[i * SIZE_BLOCK:(i + 1) * SIZE_BLOCK] + b"; word: " + word)
            plaintext += xor_str(ciphertext[i * SIZE_BLOCK:(i + 1) * SIZE_BLOCK], word)
            i += 1
        return plaintext

    def getNumWords(self):
        return len(self.words)


def main():
    s1 = b"mesnahsj"
    s2 = b"\x1d}\xec\xf0;\xf3\xdf|"
    ct = b'p\x18\x9f\x9eZ\x9b\xac\x16'
    print(xor_str(ct, s2))


if __name__ == "__main__":
    main()
