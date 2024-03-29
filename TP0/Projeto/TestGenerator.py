import GeradorPseudoAleatorio

''' 
Parâmetro que guarda o número de palavras 
de 64 bits geradas o prng
'''
N = 2


def main():
    pwd = input("Inserir password: ")
    gpa = GeradorPseudoAleatorio.GeradorPseudoAleatorio(pwd.encode("utf-8"), N)
    # print(str(gpa.getNumWords()) + ' Words found')

    plaintext = b"Esta mensagem e secreta.......:)"  # Esta mensagem contém exatamente 32 bytes
    print(b"Mensagem a cifrar: " + plaintext)
    ciphertext = gpa.cifrar(plaintext)
    print(b"Ciphertext gerado: " + ciphertext)
    decipheredtext = gpa.decifrar(ciphertext)
    print(b"DecipheredText: " + decipheredtext)


if __name__ == "__main__":
    main()
