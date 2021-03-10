import GeradorPseudoAleatorio
import os
import timeit

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

''' 
Parâmetro N usado para especificar o numero de 
palavras a serem geradas pelo prng
'''
N = 10

HM = '''
def homeMadeCipher():
    pwd = miguel
    plaintext = os.urandom(2 ** N)
    gpa = GeradorPseudoAleatorio.GeradorPseudoAleatorio(pwd.encode("utf-8"), N)
    ciphertext = gpa.cifrar(plaintext)
    decipheredtext = gpa.decifrar(ciphertext)
    print('cu')
'''

AESGCMM = '''
def aesgcmCipher():
    key = os.urandom(32)
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    plaintext = os.urandom(2 ** N)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode("utf-8"))
'''

setup = '''
import GeradorPseudoAleatorio
import os
import timeit

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
'''


def main():
    print('> Iniciado processo de cifragem usando a nossa cifra...')
    timeHM = timeit.timeit(stmt=HM, number=10, setup=setup)
    print("Done.")

    print('> Iniciado processo de cifragem usando a cifra AESGCM...')
    timeAESGCM = timeit.timeit(stmt=AESGCMM, number=10, setup=setup)
    print("Done.")

    print("Home made: " + str(timeHM) + "\n")
    print("AESGCM: " + str(timeAESGCM) + "\n")


if __name__ == "__main__":
    main()
