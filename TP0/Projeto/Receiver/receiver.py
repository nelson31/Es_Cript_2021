import os
import socket
import asyncio
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, hmac

ASSOCIATED_DATA = b"Exemplo de Associated Data para o TP0 de EC"
UDP_IP = "127.0.0.1"
UDP_PORT = 8888
SOCKET_READ_BLOCK_LEN = 4096  # bytes

''' 
Funcao usada para derivar uma chave
'''


def derivationKey(password, salt):
    info = None
    hkdf = HKDF(
        hashes.SHA256(),
        32,
        salt,
        info,
    )
    return hkdf.derive(password)


''' 
Funcao que serve para verificar a chave que foi recebida pelo receiver 
'''


def verifyKey(key1, key):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(key)
    h.verify(key1)


# Serve para autenticar a chave
def authData(key2):
    h = hmac.HMAC(key2, hashes.SHA256())
    h.update(key2)
    return h.finalize()


# Funcao que serve para validar a chave entre o Emitter e o Receiver
def validateKey(sock):
    # Acordar uma chave a ser usada na comunicação
    pw = input("Introduza a password: ")
    if len(pw) > 0:
        # Esperar pelo salt
        data, addr = sock.recvfrom(SOCKET_READ_BLOCK_LEN)
        salt = data[0:16]
        key1A = data[16:len(data)]
        # Gerar a chave
        key = derivationKey(pw.encode("utf-8"), salt)
        # Verificar se o Mac enviado pelo emitter corresponde ao mac da chave gerada
        try:
            verifyKey(key1A, key)
        except InvalidSignature as e:
            print("The key sent by the emitter does not match: %s" % e)
            sock.sendto(b"Invalido", (addr[0], addr[1]))
            sys.exit(0)
        # Autenticar a chave com a propria chave
        key2A = authData(key)
        # Enviar o mac da chave que foi gerada
        sock.sendto(key2A, (addr[0], addr[1]))
    else:
        sock.close()
        sys.exit(0)

    return key


'''
Funcao usada para cifrar e autenticar a mensagem
'''


def cifraGCM(key, mensagem, nonce):
    aesgcm = AESGCM(key)

    ct = aesgcm.encrypt(nonce, mensagem, ASSOCIATED_DATA)

    return ct


'''
Funcao usada para decifrar e autenticar a mensagem
'''


def decifraGCM(key, criptograma, nonce):
    aesgcm = AESGCM(key)

    msg = aesgcm.decrypt(nonce, criptograma, ASSOCIATED_DATA)

    return msg


# Funcao que serve para dar inicio à comunicação entre o Emitter<->Receiver
def communicate():
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.bind((UDP_IP, UDP_PORT))

    # Validar as chaves que foram geradas tanto pelo Emitter como o Receiver
    key = validateKey(sock)

    # Receber a mensagem
    data, addr = sock.recvfrom(SOCKET_READ_BLOCK_LEN)
    # Caso a mensagem enviada seja a dizer que o emmiter nao verificou as chaves
    if data == b"Invalido":
        sock.close()
        print("The emitter does not verify the keys!!")
        sys.exit(0)
    nonce = data[0:12]
    crypto = data[12:len(data)]
    print("Recebida do Emitter com endereço ", str(addr[0]), " a mensagem: ",
          (decifraGCM(key, crypto, nonce)).decode("utf-8"))

    # Nonce usado para cifrar a mensagem
    nonce = os.urandom(12)
    # Enviar resposta
    sock.sendto(nonce + cifraGCM(key, b"Mensagem recebida", nonce), (addr[0], addr[1]))

    sock.close()


def main():
    communicate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
