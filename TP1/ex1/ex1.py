import io, os
import multiprocessing as mp
import NGenerator as ng

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import padding

from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric.padding import PSS, MGF1, PKCS1v15

from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Size of dsa keys
DSA_KEY_SIZE = 2048 #bits

PKCS7_BIT_LEN = 128 # bits
AES_BLOCK_LEN = 16 # bytes
HMAC_KEY_LEN = 32 # bytes

# Header do ciphertext que guarda o tamanho do ciphertext propriamente dito (sem o digest)
CIPHERTEXT_HEADER_LEN = 4 # bytes

# Chaves pública de sender e receiver
sender_public_key = None
receiver_public_key = None

# RFC 3526's parameters. Easier to hardcode...
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 2
params_numbers = dh.DHParameterNumbers(p,g)
parameters = params_numbers.parameters()

''' 
Função que permite gerar uma chave privada e 
que irá ser usada por ambas as entidades, sender e 
emitter para poder realizar a troca de chaves
'''
def generatePrivateKeys() :

    sender_private_key = dsa.generate_private_key(
        key_size=DSA_KEY_SIZE,
    )
    receiver_private_key = dsa.generate_private_key(
        key_size=DSA_KEY_SIZE,
    )
    return sender_private_key,receiver_private_key

'''
Função que recebe o par de chaves privadas geradas 
e gera cada uma das correspondentes chaves públicas
'''
def generatePublicKeys(private_pair) :

    global sender_public_key, receiver_public_key
    sender_public_key = private_pair[0].public_key()
    receiver_public_key = private_pair[1].public_key()

'''
Função responsável pelo handshake a ser 
realizado por parte do sender. Retorna a chave a 
ser usada para a comunicação entre ambas as entidades.
'''
def sender_handshake(conn, private_key, ng) :

    # Generate and Send the client's generated key: g^x
    dh_g_x = parameters.generate_private_key()
    dh_g_x_as_bytes = dh_g_x.private_bytes(Encoding.PEM,PrivateFormat.PKCS8,NoEncryption())
    conn.send(dh_g_x_as_bytes)

    # Recebemos a primeira mensagem do receiver
    data = conn.recv()
    args = data.split(sep=b'\r\n\r\n')
    dh_g_y_as_bytes = args[0]
    dh_g_y = load_pem_private_key(dh_g_y_as_bytes,password=None)
    signature = args[1]
    # Verificamos a assinatura do receiver -> FIXME WITH TRY... CATCH
    verify(receiver_public_key,dh_g_y_as_bytes + b'\r\n\r\n' + dh_g_x_as_bytes, signature)

    # Generate the shared key between server<->client communication
    shared_key = dh_g_x.exchange(dh_g_y.public_key())
    # Perform key derivation.
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(shared_key)

    # Envia a respetiva assinatura para ser verificada pelo receiver
    conn.send(sign(private_key, dh_g_x_as_bytes + b'\r\n\r\n' + dh_g_y_as_bytes))

    # No final é recebida, pelo sender (emitter) uma mensagem de termino da fase de handshake
    assert decrypt(derived_key,conn.recv(),ng).decode('utf-8') == 'END HANDSHAKE'

    print('[SENDER] Handshake phase successfully done!')

    return derived_key


'''
Função responsável pelo handshake a ser 
realizado por parte do receiver. Retorna a chave a 
ser usada para a comunicação entre ambas as entidades.
'''
def receiver_handshake(conn, private_key, ng) :

    # Recebemos a chave gerada pelo sender
    dh_g_x_as_bytes = conn.recv()
    dh_g_x = load_pem_private_key(dh_g_x_as_bytes,password=None)

    # Generate and Send the server's generated key: g^y
    dh_g_y = parameters.generate_private_key()
    dh_g_y_as_bytes = dh_g_y.private_bytes(Encoding.PEM,PrivateFormat.PKCS8,NoEncryption())

    # Generate the shared key between server<->client communication
    shared_key = dh_g_y.exchange(dh_g_x.public_key())

    # Perform key derivation.
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
    ).derive(shared_key)

    # Enviamos para o sender a chave gerada e a respetiva assinatura
    conn.send(dh_g_y_as_bytes + b'\r\n\r\n' + sign(private_key, dh_g_y_as_bytes + b'\r\n\r\n' + dh_g_x_as_bytes))

    # Recebemos a assinatura e verificamos se é autentica -> FIXME WITH TRY... CATCH
    data = conn.recv()
    verify(sender_public_key, dh_g_x_as_bytes + b'\r\n\r\n' + dh_g_y_as_bytes, data)

    # No final é enviada uma mensagem de termino da fase de handshake
    conn.send(encrypt(derived_key,'END HANDSHAKE'.encode('utf-8'),ng))

    print('[RECEIVER] Handshake phase successfully done!')

    return derived_key

'''
Função que permite assinar uma determinada mensagem 
com uma determinada chave privada
'''
def sign(private_key, data) :

    signature = private_key.sign(
        data,
        hashes.SHA256()
    )
    return signature

'''
Função que permite verificar uma determinada assinatura.
'''
def verify(public_key, data, signature) :

    public_key.verify(
        signature,
        data,
        hashes.SHA256()
    )

# Receives and returns bytes.
def encrypt(k, m, iv_gen):

    padder = padding.PKCS7(PKCS7_BIT_LEN).padder()
    padded_data = padder.update(m) + padder.finalize()
    iv = iv_gen.get()
    cipher = Cipher(algorithms.AES(k), modes.CBC(iv))
    encryptor = cipher.encryptor()

    ct = encryptor.update(padded_data) + encryptor.finalize()
    ct = iv+ct
    len_ct = len(ct)
    len_ct_bytes = len_ct.to_bytes(CIPHERTEXT_HEADER_LEN,'little')

    h = hmac.HMAC(k, hashes.SHA256())
    h.update(ct)
    digest = h.finalize()
    return len_ct_bytes+ct+digest

# Receives and returns bytes.
def decrypt(k, c, iv_gen):

    len_ct_bytes = c[:CIPHERTEXT_HEADER_LEN]
    len_ct = int.from_bytes(len_ct_bytes,'little',signed=True)
    ct, digest = c[CIPHERTEXT_HEADER_LEN:(len_ct+CIPHERTEXT_HEADER_LEN)], c[(len_ct+CIPHERTEXT_HEADER_LEN):]
    iv, ct = ct[:AES_BLOCK_LEN], ct[AES_BLOCK_LEN:]
    
    iv_gen.addToHistoric(iv)

    # Verificamos, logo, a assinatura
    h = hmac.HMAC(k, hashes.SHA256())
    h.update(iv+ct)
    h.verify(digest)

    cipher = Cipher(algorithms.AES(k), modes.CBC(iv))
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(PKCS7_BIT_LEN).unpadder()
    pt = unpadder.update(pt) + unpadder.finalize()
    return pt

''' 
Função que representa a execução da entidade sender
'''
def sender(conn,private_key,stdin):

    iv_generator = ng.NGenerator(AES_BLOCK_LEN)
    #hmac_key_generator = ng.NGenerator(HMAC_KEY_LEN) -> Esperar pela resposta do stor
    # Iniciamos a fase de handshake com o receiver...
    shared_key = sender_handshake(conn,private_key,iv_generator)
    stdin.send('ready')

    message = stdin.recv()

    while message != 'exit' and len(message) > 0 :
        conn.send(encrypt(shared_key,message.encode('utf-8'),iv_generator))
        assert 'ok' == decrypt(shared_key,conn.recv(),iv_generator).decode('utf-8')     # para garantir o sincronismo
        ''' Pedimos à thread principal a 
        próxima mensagem lida a partir do stdin'''
        stdin.send('next')
        message = stdin.recv()

    # Para terminar a conexão
    conn.send(encrypt(shared_key,'exit'.encode('utf-8'),iv_generator))
    conn.close()
    print('[Emitter] SHUTDOWN')

''' 
Função que representa a execução da entidade receiver 
'''
def receiver(conn,private_key):

    iv_generator = ng.NGenerator(AES_BLOCK_LEN)
    #hmac_key_generator = ng.NGenerator(HMAC_KEY_LEN) -> Esperar pela resposta do stor
    # Iniciamos a fase de handshake com o sender
    shared_key = receiver_handshake(conn,private_key,iv_generator)

    try:
        message = decrypt(shared_key,bytes(conn.recv()),iv_generator).decode('utf-8')
        while message != 'exit':
            # Imprimimos o conteudo da mensagem recebida
            print('[Receiver] RECEIVED: ' + message)
            conn.send(encrypt(shared_key,'ok'.encode('utf-8'),iv_generator))        # para garantir o sincronismo
            message = decrypt(shared_key,bytes(conn.recv()),iv_generator).decode('utf-8')
    except EOFError:
        print('[Receiver] SHUTDOWN')

    print('[Receiver] SHUTDOWN')
    conn.close()


''' 
Função responsável por arrancar a 
execução de ambas as entidades, o emitter 
e o receiver. Para além disto é responsável por 
mediar a comunicação entre o stdin e o sender
'''
def main() :
    try:
        mp.set_start_method('fork')
    except:
        print("O start_method já foi inicializado anteriormente ")

    # Geramos a chave privada para cada uma das entidades e, de seguida, as chaves públicas
    sender_private_key, receiver_private_key = generatePrivateKeys()
    generatePublicKeys((sender_private_key, receiver_private_key))

    receiver_conn, sender_conn = mp.Pipe()
    receiver_stdin, main_stdin = mp.Pipe()
    s = mp.Process(target=sender, args=(sender_conn,sender_private_key,receiver_stdin))
    r = mp.Process(target=receiver, args=(receiver_conn,receiver_private_key))
    s.start()
    r.start()

    # Esperamos que o emitter esteja a postos para receber mensagens para serem enviadas
    assert 'ready' == main_stdin.recv()

    message = input('[Emitter] > Mensagem a ser enviada: \n')
    while len(message) != 0 and message != 'exit':
        main_stdin.send(message)
        ''' Esperamos a confirmação do sender para 
        receber nova mensagem do stdin'''
        assert 'next' == main_stdin.recv()
        message = input('[Emitter] > Mensagem a ser enviada: \n')
    # Para terminar a ligação
    main_stdin.send('')


if __name__ == "__main__":
    main()
