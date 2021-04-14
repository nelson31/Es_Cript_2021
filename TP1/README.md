# Trabalho Prático 1

## Enunciado

### Use Criptography 

1. Use *Cryprography* para construir uma sessão síncrona de comunicação segura entre dois agentes (o Emitter e o Receiver), combinando os seguintes elementos constituintes:
    1. um **gerador de nounces**: um nounce, que nunca foi usado antes, deve ser criado aleatoriamente em cada instância da comunicação.
    2. a cifra simétrica **AES** usando autenticação de cada criptograma com **HMAC** e um modo seguro contra ataques aos vectores de iniciação (iv's).
    3. o protocolo de acordo de chaves **Diffie-Hellman** com verificação da chave, e  autenticação dos agentes através do esquema de assinaturas DSA.
    4. Usando **Curvas Elípticas**, criar uma versão do esquema anterior substituindo, no protocolo de acordo de chaves, o DH pelo ECDH e o DSA pelo ECDSA.


### Use o SageMath para

1. Construir uma classe *Python* que implemente um **KEM-RSA**. A classe deve
    1. Inicializar cada instância recebendo  o parâmetro de segurança (tamanho em bits do módulo RSA) e gere as chaves pública e privada.
    2. Conter funções para encapsulamento e revelação da chave gerada.
2. Construir,  a partir deste KEM e usando a **transformação de Fujisaki-Okamoto**, um PKE que seja IND-CCA seguro.
3. Construir uma classe Python que implemente o **DSA**. A implementação deve, na iniciação,  receber como parâmetros o tamanho  dos primos $p$ e $q$; deve conter funções para assinar digitalmente e verificar a assinatura.
4. Construir uma classe Python que implemente o **ECDSA** usando uma das curvas elípticas primas definidas no FIPS186-4  (escolhida  na iniciação da classe).

