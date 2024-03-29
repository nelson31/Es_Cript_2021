import asyncio
import os
import socket
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

UDP_IP = "127.0.0.1"
UDP_PORT = 8888
SOCKET_READ_BLOCK_LEN = 4096  # bytes
ASSOCIATED_DATA = b"Exemplo de Associated Data para o TP0 de EC"

# Geracao do salt para a derivacao da chave
salt = os.urandom(16)

''' 
Funcao usada para derivar uma chave
'''


def derivationKey(password):
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


def verifyKey(key2, key):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(key)
    h.verify(key2)


# Serve para autenticar a chave
def authData(key2):
    h = hmac.HMAC(key2, hashes.SHA256())
    h.update(key2)
    return h.finalize()


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


# Funcao que serve para validar a chave entre o Emitter e o Receiver
def validateKey(sock):
    # Acordar uma chave a ser usada na comunicação
    pw = input("Introduza a password: ")
    if len(pw) > 0:
        # Derivar a chave
        key = derivationKey(pw.encode("utf-8"))
        # Autenticar a chave com a propria chave
        keyA = authData(key)
        # Enviar o salt e o MAC(key) ao receiver
        sock.sendto(salt + keyA, (UDP_IP, UDP_PORT))
        # Esperar a resposta
        response, addr = sock.recvfrom(SOCKET_READ_BLOCK_LEN)
        # Se o Receiver nao ter verificado que as chaves são iguais
        if response == b"Invalido":
            sock.close()
            print("The receiver does not confirm the key!!")
            sys.exit(0)
        # Comparar se a resposta é mesmo igual à chave
        try:
            verifyKey(response, key)
        except InvalidSignature as e:
            print("The key sent by the receiver does not match: %s" % e)
            sock.sendto(b"Invalido", (UDP_IP, UDP_PORT))
            sys.exit(0)
    else:
        sock.close()
        sys.exit(0)

    return key


# Funcao que serve para dar inicio à comunicação entre o Emitter<->Receiver
def communicate():
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    # Validar as chaves que foram geradas tanto pelo Emitter como o Receiver
    key = validateKey(sock)

    # Efetuar a comunicacao entre as partes
    pt = input("Emitter message: ")
    if len(pt) > 0:
        # Nonce usado para cifrar a mensagem
        nonce = os.urandom(12)
        # Enviar a mensagem
        sock.sendto(nonce + cifraGCM(key, pt.encode("utf-8"), nonce), (UDP_IP, UDP_PORT))
        # Receber a resposta do receiver
        data, addr = sock.recvfrom(SOCKET_READ_BLOCK_LEN)
        nonce = data[0:12]
        crypto = data[12:len(data)]
        print("Resposta do Receiver: " + (decifraGCM(key, crypto, nonce)).decode("utf-8"))
    else:
        sock.close()


def main():
    communicate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
