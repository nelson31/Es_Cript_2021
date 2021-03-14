import GeradorPseudoAleatorio
import os
import timeit

from Emitter.emitter import cifraGCM
from Emitter.emitter import decifraGCM
from Emitter.emitter import derivationKey

''' 
Parâmetro N usado para especificar o numero de 
palavras a serem geradas pelo prng
'''
N = 10  # Vamos ter sequencias de 1024 bytes


def homeMadeCipher():
    pwd = "miguel"
    plaintext = os.urandom(2 ** N)
    gpa = GeradorPseudoAleatorio.GeradorPseudoAleatorio(pwd.encode("utf-8"), N)
    ciphertext = gpa.cifrar(plaintext)
    print(ciphertext)
    print(plaintext == gpa.decifrar(ciphertext))


def aesgcmCipher():
    pwd = "nelson"
    key = derivationKey(pwd.encode("utf-8"))
    nonce = os.urandom(12)
    plaintext = os.urandom(2 ** N)
    ciphertext = cifraGCM(key, plaintext, nonce)
    print(ciphertext)
    print(plaintext == decifraGCM(key, ciphertext, nonce))


HM = '''
homeMadeCipher()
'''

AESGCMM = '''
aesgcmCipher()
'''

setup = '''
from __main__ import homeMadeCipher
from __main__ import aesgcmCipher
'''


def main():
    print('> Iniciado processo de cifragem usando a nossa cifra...')
    timeHM = timeit.timeit(stmt=HM, number=100, setup=setup)
    print("Done.")

    print('> Iniciado processo de cifragem usando a cifra AESGCM...')
    timeAESGCM = timeit.timeit(stmt=AESGCMM, number=100, setup=setup)
    print("Done.")

    print("\n[TIMES]")
    print("Home made: " + str(timeHM))
    print("AESGCM: " + str(timeAESGCM))


if __name__ == "__main__":
    main()
