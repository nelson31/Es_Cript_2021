import GeradorPseudoAleatorio
import os

''' 
Parâmetro N usado para especificar o numero de 
palavras a serem geradas pelo prng
'''
N = 5


def main():
    print('Welcome to our cipher test!! (All rights reserved)')

    pwd = input('Introduza a password usada para a derivação da chave da cifra: ')
    gpa = GeradorPseudoAleatorio.GeradorPseudoAleatorio(pwd.encode("utf-8"), N)
    # print(str(gpa.getNumWords()) + ' Words found')

    plaintext = os.urandom(2 ** N)  # Esta mensagem contém exatamente 32 bytes
    print(b"Mensagem a cifrar: " + plaintext)

    print('> Iniciado processo de cifragem usando a nossa cifra...')
    ciphertext = gpa.cifrar(plaintext)
    print(b"Ciphertext gerado: " + ciphertext)
    decipheredtext = gpa.decifrar(ciphertext)
    print(b"DecipheredText: " + decipheredtext)


if __name__ == "__main__":
    main()
