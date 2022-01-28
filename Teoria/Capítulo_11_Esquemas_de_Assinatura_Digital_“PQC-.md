# Capítulo  11: Esquemas de Assinatura Digital “PQC-Low-Algebra”.

# Introdução

Recentemente tem sido posto em causa o paradigma de segurança que deriva na crença da existência de um  “problema difícil”$$\;\mathcal{L}\in \mathsf{NP}\;$$e na confiança em provas de segurança que agem por redução de  $$\;\mathcal{L}\;$$ a um  hipotético “ataque” $$\;\mathcal{A}\in\mathsf{P}$$ . 

Vamos aqui classificar este paradigma por **“high algebra”** porque ambos os problemas  $$\,\mathcal{L},\mathcal{A}\;$$ formalizam-se em  estruturas algébricas complexas.

A principal crítica a esta abordagem deriva precisamente desta complexidade algébrica e da crença  que, quanto maior for a complexidade algébrica de $$\;\mathcal{L}\;$$, maior é a possibilidade de  conter  “hidden trapdoors”: isto é, reduções “ocultas” a  problemas que, em determinado modelos de computação, pertençam à classe $$\;\mathsf{P}\;$$.

O exemplo paradigmático é o algoritmo de Schor. Para o problema da factorização de inteiros este algoritmo pode ser visto como uma “hidden trapdoor” de complexidade polinomial no modelo de computação quântica.

Um paradigma alternativo, que em oposição ao anterior se pode designar por **“low algebra”**, baseia-se na crença de que, se uma estrutura criptográfica usa exclusivamente circuitos com formas bem testadas (e.g. funções de “hash” ou cifras simétricas) e se esses circuitos contêm apenas operadores simples (e.g   **xo**r’s , **and**’s   ou $$+,\times$$ em pequenos inteiros ) , então a possibilidade de existirem “hidden trapdoors” é muito pequena. Se as funções de “hash” e as cifras simétricas forem boas aproximações de um ”hash” aleatório ou de uma permutação aleatória, então a segurança das técnicas criptográficas desenvolvidas nesta estrutura é  elevada.

Esta paradigma de segurança  vai ser ilustrado aqui com duas das candidaturas a esquema de assinatura digital  no concurso NIST PQC: o esquema **SPHINCS+** , baseado em funções de “hash”, e o esquema **PICNIC**  baseado em computação partilhada em circuitos.


# Esquemas “Hash Based Signature” (HBS)

[O esquema SPHINCS+](https://sphincs.org) é a último de uma cadeia de propostas de esquemas HBS (“hash based signatures”); isto é,  esquemas de assinatura digital que apenas usam funções de “hash” .
O benefício imediato de um tal esquema está no facto de a sua segurança depender de um conjunto limitado de assunções; essencialmente a segurança do esquema de assinaturas depende apenas da segurança das funções de “hash” usadas.

A característica dos HBS’s, e que os torna radicalmente distintos dos restantes esquemas de assinatura digital, é a existência de um limite superior ao número de mensagens que uma chave privada pode assinar; se esse limite for ultrapassado a chave é revelada. Por isso estes esquemas têm, normalmente, um *estado* (um contador) que regista o número de mensagens em que a chave já foi utilizada.
O  XMSS (“Extended Merkle Signature Scheme”) é um exemplo de um esquema nesta categoria que está em vias de ser adoptado como standard NIST.
O SPHINCS, apresentado em 2015, e o SPHINCS+ , apresentado em 2017, são variantes do XMSS que não usam estado e por isso são diretamente comparáveis com os restantes esquemas de assinaturas apresentados ao concurso NIST.

Outra diferença essencial é a forma como são gerados os pares de chaves privada e pública. Nos esquemas de chave pública usuais existe um algoritmo **KeyGen** que em cada invocação produz um destes pares. Nos HBS’s, este algoritmo produz um número muito grande de pares de chaves; em princípio em número suficiente para todo o tempo de vida de uma instância do esquema.

Mas daqui resulta que essas chaves precisam de ser armazenadas e geridas. Nos esquemas tradicionais esse é o papel dos mecanismos de certificação das chaves, mecanismos esses que são independentes do esquema de assinaturas. Nos HBS’s o armazenamento  das chaves é feito através de estruturas de dados conhecidas como **Árvores de Merkle** que não gerem as chaves com integram o mecanismo de certificação.



## Estrutura geral de um esquema HBS

Um esquema HBS genérico da família XMSS/SPHINCS pode ser decomposto em dois níveis:

- *OTS & FTS*
    No 1º nível estão esquemas de assinaturas “one-time” e “few-time” em que cada par de chaves pública e privada é usado para criar uma única assinatura (nos OTS’s) ou um pequeno número de assinaturas (nos FTS’s). Estes esquemas usam-se para assinar diretamente as mensagens “plaintext” ou então para autenticar os pares de chaves usados para assinar mensagens.
- *MTS*
    No 2º nível estão os esquemas MTS (“many-time signatures”): esquemas  que permitem, com uma única chave pública, autenticar um número muito grande de assinaturas. 
    Estes esquemas baseiam-se em um *algoritmo de autenticação* que permite usar uma só chave pública  para autenticar um número elevado de pares de chaves OTS ou FTS.
    Adicionalmente, a este nível, está o *algoritmo de seleção* que, dada uma mensagem específica, permite escolher a chave privada OTS ou FTS que deve ser usada para a assinar.

Um esquema MTS em que o algoritmo de seleção assegura que uma chave privada OTS (ou FTS) é estritamente usada um única vez, exige sempre um *estado* que registe a sequência de chaves  privadas conforme são usadas. A existência desse estado faz com que um tal esquema MTS não possa ser descrito como uma instância de um DSS genérico; nomeadamente a sua segurança não pode ser formalizada como um simples EUF-CMA (ou semelhante). 
Por isso pretende-se (quase sempre) um MTS sem estado. Nesse caso, para cada mensagem, o algoritmo de seleção não pode depender de outras assinaturas previamente calculadas; só pode depender da mensagem que ser assinar e de informação aleatoriamente gerada (“salt”).


## Algoritmos OTS & FTS

Os algoritmos OTS usados na família XMSS/SPHINCS são, respetivamente, os esquemas WOTS e WOTS+  que já foram descritos e analisados no Capítulo 6.  

Nesta secção vamos descrever apenas dois esquemas FTS: o esquema HORST, usado no Sphincs de 2015, e o esquema FORS, usado na candidatura PQC NIST. 
Ambos são generalizações do esquema OTS original de Lamport que vamos aqui recordar:


| **Esquema OTS de Lamport**<br><br><br>    - Uma mensagem é uma palavra  **$$\,M\,\equiv\;(m_0,\cdots,m_{k-1})\,$$ com  $$\,k\,$$ *símbolos.*  Cada símbolo $$\,m_i\in \{0,1\}\,$$ tem um de dois *valores* possíveis.<br>    - A chave privada $$\,\mathsf{sk}\,$$ associa a cada posição da mensagem $$\,i<k\,$$ e a cada  um dos dois valores possíveis $$\,j\in\{0,1\}$$, uma palavra de $$\,n\,$$  bits. Isto é<br>                                           $$\,\mathsf{sk}\,\equiv\;\{\,\mathsf{sk}_{i,j}\,\}_{i<k\,,\,j< 2}\;\quad\;\text{com}\quad \mathsf{sk}_{i,j}\in\mathcal{B}_n$$<br>    - A chave pública $$\,\mathsf{pk}\,$$ associa, a cada a cada posição  $$\,i<k\,$$ e a cada valor $$\,j< 2\,$$ , o “hash”  de $$\,\mathsf{sk}_{i,j}\,$$.<br>                                    $$\,\mathsf{pk}\,\equiv\;\{\,\mathsf{pk}_{i,j}\,\}_{i<k\,,\,j<2}\;$$    com  $$\,\mathsf{pk}_{i,j}\,\equiv\,\mathsf{hash}(\mathsf{sk}_{i,j})$$  <br>    - A assinatura $$\,\sigma\;\equiv\;(\sigma_0,\cdots,\sigma_{k-1})\,$$ da mensagem $$\,M\,$$ é um vetor de $$\,k\,$$ palavras de $$\,n\,$$bits  com <br>                                                            $$\sigma_i\;\equiv\;\mathsf{sk}_{i,m_i}$$<br>    - A verificação do par  $$\,(\sigma,M)\,$$ testa, para cada posição  $$\,i < k\,$$,  a igualdade<br>                                                   $$\,\mathsf{pk}_{i,m_i}\;\stackrel{\small ?}{=}\;\sigma_i$$ |

No esquema de Lamport, a chave privada $$\,\mathsf{sk}\,$$ é uma “string” com $$\,2\cdot k\,$$  palavras de $$\,n\,$$ bits . O tamanho de $$\,\mathsf{sk}\,$$ é elevado mas pode  ser gerado  por um XOF a partir de uma *seed ;* assim **a complexidade descritiva da chave é só o tamanho da *seed.*

A chave pública $$\,\mathsf{pk}\,$$é também uma “string”  $$\,2\cdot k\,$$ palavras de $$\,n\,$$ bits. Porém, ao contrário da chave privada, não pode ser comprimida para uma *seed*  e um XOF . Isto porque cada $$\,\mathsf{pk}_{i,j}\,$$ coincide e só pode ser determinada como o “hash” de informação secreta $$\,\mathsf{sk}_{i,j}\,$$; por isso, a menos algum $$\,\mathsf{sk}_{i,j}\,$$ deixe de ser secreto, a chave pública  não pode ser comprimida.


----------

O esquema de Lamport é ainda um esquema OTS (ou quase) porque é possível  consultar duas vezes o oráculo de assinaturas e reconstruir completamente a chave privada; basta consultar o oráculo com as mensagens $$\,\mathsf{0}^k\,$$ e $$\,\mathsf{1}^k\,$$.

O esquema FTS básico designa-se por HORS (“Hash to Obtain a Random Subset”) e é a construção que está na origem do esquema HORST, usado no Sphincs, e FORS usado no esquema Sphincs+.


| **Esquema HORS**<br><br><br>    - *Parâmetros* :  <br>        - inteiros positivos $$\,n,t,k,\,$$ em que  $$\,t \gg k \,$$ e $$\,t=2^\tau\,$$, para algum $$\,\tau\,$$.<br>                                          *valores típicos*:  $$n=256\;,\;t=2^{16}\;,\;k=32$$ <br>        - uma função de “hash”  $$\;H\,\colon\, \mathbb{N} \to (\mathbb{Z}_t)^k\;$$<br>        - uma função de unidirecional  $$\,f\colon\mathcal{B}_n \to\mathcal{B}_n\,$$ e  uma “extended output function”   $$\,\mathcal{S}\,\colon\,\mathcal{B}_n\times\mathbb{Z}_t\,\to\, \mathcal{B}_n$$<br>                                                  <br>    - *KeyGen:*  $$\,n\,$$ é o parâmetro de segurança.<br>        - A chave privada é uma “seed”  $$\,\mathit{seed}\gets \mathcal{B}_n\,$$;  <br>        - A chave pública $$\,\mathsf{pk} \,=\,\{\mathsf{pk}_j\}_{0\leq j < t}\;$$  com $$\,\mathsf{pk}_j \gets f(\mathcal{S}(\mathit{seed},j))\,$$  para todo   $$\,0\leq j < t$$.<br>        <br>    - *Sign* : dada a mensagem $$\,m\in\mathbb{N}\,$$ e a chave privada $$\,\mathit{seed}\,\in\,\mathcal{B}_n\,$$<br>        - Calcula-se $$\,{x}\gets H(m)\,$$;  tem-se $$\,x = \{x_i\}_{0\leq i<k}$$  ,   com $$0\leq x_i < t\,$$<br>        - A assinatura é $$\,\sigma = \{\sigma_i\}_{0\leq i<k}\;$$ com $$\,\sigma_i \gets \mathcal{S}(\mathit{seed},x_i)\,$$   para todo $$\,0 \leq i <k\,$$.<br>        <br>    - *Verify:* dada a assinatura $$\,\sigma\in (\mathcal{B}_n)^k\,$$,  a mensagem $$\,m\in\mathbb{N}\,$$ e a chave pública $$\,\mathsf{pk}\,\in\,(\mathcal{B}_n)^t\,$$<br>        - Calcula-se $$\,{x}\gets H(m)\,$$;  tem-se $$\,x = \{x_i\}_{0\leq i<k}$$  ,   com $$0\leq x_i < t\,$$<br>        - A assinatura é aceite se e só se, para todo $$\,0 \leq i <k\,$$, se verifica  $$\,\mathsf{pk}_{x_i}\mathbin{\stackrel{\small ?}{=}}f(\sigma_i)\,$$. |


Porque $$\,t \gg k\,$$, para todo $$\,m\in \mathbb{N}\,$$ e com elevada probabilidade, as $$\,k\,$$ componentes do  vetor $$\,H(m)\,$$ são todas distintas; por isso, formam um sub-conjunto de $$\,\mathbb{Z}_t\,$$ com $$\,k\,$$ elementos.  
Daí resulta a designação “Hash to Obtain a Random Subset” (HORS)
Note-se que o número total de subconjuntos de $$\,\mathbb{Z}_t\,$$ que têm exatamente $$\,k\,$$ elementos é  $$\binom{t}k$$. 

----------

O tamanho da chave pública é o principal problema tanto do esquema de Lamport como do esquema HORS. Por exemplo, com os valores típicos indicados, o tamanho da chave pública HORS é $$\,\simeq 2\,\text{MBytes}\,$$.

O objetivo  do HORST , que aparece no Sphincs de 2015, ou do FORS, que faz parte da candidatura NIST, é precisamente comprimir a chave pública HORS para uma só palavra de $$\,n\,$$ bits (32 bytes). Como veremos esta compressão obtém-se à custa de mais processamento e de assinaturas ligeiramente maiores.

A técnica aí usada baseia-se nas **àrvores de Merkle** ou, genericamente, nas **árvores de “hash”**. 
Veremos na secção seguinte o que são árvores de hash e, nos casos particulares dos esquemas HORST e FORS, veremos como são usadas para comprimir a chave pública a uma única palavra de $$\,n\,$$bits e, no processo,  optimizando o algoritmo de verificação das assinaturas.


## Árvores de Hash

Uma árvore de “hash”  é uma árvore binária completa em que cada nodo é o “output”  de um “hash”. As dimensões da árvore são determinadas pela sua altura $$\,h\,$$ (“height”) e pelo tamanho $$\,n\,$$ dos seus nodos. 

Designamos por $$\,A_{i,j}\,$$ o nodo no nível  $$\,i\,$$ e posição $$\,j\,$$ nesse nível.  
Os níveis da árvore são  $$\,h+1\,$$,   enumerados desde  $$\,i=h\,$$, o nível da raíz, decrescendo até $$\,i=0\,$$, o nível das folhas.
Como a árvore é completa, o nível $$\,i\,$$  tem  $$\,2^{h-i}\,$$   nodos . Estes nodos são enumerados, da esquerda para a direita, desde $$\,j=0\,$$ até  $$\,j=2^{h-i}- 1$$ .

Algumas relações entre posições de nodos relativas ao nodo genérico $$\,A_{i,j}\,$$.


1. Se $$\,i>0\,$$ o nodo $$\,A_{i,j}\,$$  tem, como *descendente*s,  os nodos  $$\,A_{i-1\,,\,2j}\;$$e $$\,A_{i-1\,,\,2j+1}\;$$.
    *Por simplicidade  vamos representar estes nodos por* $$\,E_{i,j}\,$$ *e* $$\,D_{i,j}\,$$ *respetivamente.*
    
2. Se $$\,i< h\,$$ o nodo *ascendente* de $$\,A_{i,j}\,$$ é o nodo $$\,A_{i+1\,,\,j/2}\,$$, quando $$\,j\,$$ é par, ou o nodo $$\,A_{i+1\,,\, (j-1)/2}\;$$ quando $$\,j\,$$ é ímpar.
    *Por simplicidade de notação representamos por* $$\,U_{i,j}\,$$ *o ascendente de* $$\,A_{i,j}\,$$
    
3. Para todo $$\,i < h\,$$, o *irmão* (“sibling”) de $$\,A_{i,j}\,$$, representado por $$\,\bar{A}_{i,j}\,$$,  é o nodo distinto de $$\,A_{i,j}\,$$  que tem o mesmo nodo ascendente.  
    Tem-se  $$\,\bar{A}_{i,j}\,=\,$$ $$\,A_{i,j-1}\,$$, quando $$\,j\,$$é ímpar , e  $$\,\bar{A}_{i,j}\,=\,A_{i,j+1}\,$$, quando $$\,j\,$$é par.

A relação fundamental entre os valores dos nodos é determinada por uma família de $$\,h\,$$ funções de compressão  $$\;\{\,f_i\,\colon \,\mathcal{B}_{2n}\,\to\,\mathcal{B}_n\,\}_{0\leq i< h}\;$$ através de duas relações equivalentes

    - *(top-down)*
                                     $$A_{i,j}\;=\;f_{i-1}(E_{i,j}\,\|\,D_{i,j})$$        para $$0 < i \leq h$$
    - *(bottom-up)*
                          $$U_{i,j}\;=\; \left\{\begin{array}{ll} f_{i}(A_{i,j}\,\|\,\bar{A}_{i,j}) & \text{se}\;j\;\text{é par} \\ f_{i}(\bar{A}_{i,j}\,\|\,{A}_{i,j})& \text{se}\;j\;\text{é ímpar}\end{array}\right.$$     para   $$\, 0 \leq i < h$$

O  **caminho de autenticação** do nodo $$\,A_{i,j}\,$$ , representada por $$\,\mathsf{Auth}(A_{i,j})\,$$, é uma sequência de nodos que é nula, quando $$\,i=h$$ ,  e é calculada recursivamente como

                                    $$\mathsf{Auth}(A_{i,j}) \;\equiv\; \bar{A}_{i,j}\,\|\,\mathsf{Auth}(U_{i,j})$$

em caso contrário. É simples verificar que esta sequência tem comprimento $$\,(h-i)\,$$.


----------

**Algoritmo de Verificação**
Note-se que, se for conhecido o nodo $$\,A_{i,j}\,$$ e o respetivo caminho de autenticação $$\,\mathsf{Auth}(A_{i,j})\,$$ é  simples calcular a sequência de todos os nodos ascendentes de $$A_{i,j}\,$$.


    - Se $$\,i=h\,$$ não existem ascendentes de $$\,A_{i,j}$$; a sequência  é vazia
    - Se $$\,i< h\,$$ então
        - Decompõe-se $$\,\mathsf{Auth}(A_{i,j})\,$$ nas componentes $$\,\bar{A}_{i,j}\,$$ e $$\;\mathsf{Auth}(U_{i,j})\,$$.
        - Com $$\,A_{i,j}\,$$, $$\,\bar{A}_{i,j}\,$$$$\,$$ e  a relação *bottom-up ,* acima,  **calcula o ascendente direto$$\,U_{i,j}$$; este é o primeiro elemento da sequência de ascendentes.
        - Os restantes elementos da sequência calculam-se recursivamente aplicando este mesmo algoritmo a $$\,U_{i,j}\,$$ e ao respetivo caminho de autenticação $$\,\mathsf{Auth}(U_{i,j})\,$$. Nomeadamente o último elemento da sequência é a raíz da árvore de “hash”.


| - O nodo $$\,A_{i,j}\,$$ é representado pelo triplo `(a,i,j)` , em que $$\,a\in\mathcal{B}_n\,$$é o conteúdo e $$\,(i,j)\,$$são os índices.<br>    - O ascendente de $$\,A_{i,j}$$ é representado pelo triplo `(u, i_u, j_u)`.<br>    - A rotina `up` aplica a relação “bottom-up” para construir o ascendente direto do argumentos; a implementação usada termina em exceção se os argumentos não são os descendentes diretos de um mesmo nodo. |

**Algoritmo de construção do caminho de autenticação de um nodo e da raíz da árvore**

Este é um algoritmo de travessia da árvore que constrói o caminho de autenticação de uma qualquer folha da árvore $$\,A_{0,j}\,$$ a partir do índice $$\,j\,$$ e da função $$\,\mathcal{L}\,\colon\,\mathbb{Z}_{2^h}\,\to\,\mathcal{B}_n\,$$ que constrói o conteúdo de uma folha a partir desse índice.

O algoritmo em Python é decomposto em duas funções: 

    - uma, designada por `tree_hash` , que calcula a raíz de uma sub-árvore de altura `z` cujas folhas de iniciam na folha `s`  da árvore principal,
    - a segunda, `auth_hash`, calcula o caminho de autenticação da folha na posição `j`, 


    def tree_hash(s, z):
        assert s % (1<<z) == 0
        stack = Stack()
        for j in range(1<<z):
            node = L(s+j)
            while True: 
                try:
                    node_ = stack.top()
                    node = up(node_,node)
                    stack.pop()
                except:
                    break
            stack.push(node)
        return stack.pop()
               
    def auth_hash(j):
        a = dict()
        for i in range(h):
            k = (j//(1 << i)) ^ 1
            a[i] = tree_hash(k << i, i)
        return a
    
    def verify(pk,xj,auth):
        x = xj
        try:
            for i in range(h):
                x = up(auth[i],x)
            return x == pk
        except:
            return False
----------


## Esquemas HORST e FORS

O esquema HORST  usa uma árvore de hash para autenticar a chave pública HORS. Sendo $$\,t=2^\tau\,$$, as folhas da árvore formam o conjunto $$\,\{\mathsf{pk}_i\}_{0\leq i < 2^\tau}\,$$e a altura da árvore é $$\,\tau\,$$.

A chave pública da árvore é, como vimos, uma única palavra de $$n$$ bits

O esquema FORS combina o esquema HORST com o esquema original de Lamport. As mensagens são formadas por $$\,k\,$$ símbolos com valores em $$\,\mathbb{Z}_t\,$$. Essencialmente este esquema é definido por $$\,k\,$$ cópias de um esquema HORST; para cada cópia existe uma $$\,\mathit{seed}_\ell\,$$, com $$0\leq \ell <  k\,$$ , que determina a chave privada para o símbolo na posição $$\,\ell\,$$, e cada cópia tem uma árvore de hash para autenticar as respetivas chaves públicas. 
As chaves públicas do esquema FORS são as $$\,k\,$$ raízes das árvores de “hash”.


## Esquemas MTS (Árvores de Merkle)

Os esquemas HORST e FORS são esquemas FTS, que permitem autenticar apenas algumas (poucas) assinaturas. Para autenticar muitas assinaturas é preciso usar muitas  cópias de esquemas HORST ou FORS. A forma mais simples de o fazer é usar um esquema WOTS+ para assinar as chaves públicas HORST ou FORS. Para isso


1. Usa-se um esquema WOTS+ para assinar cada uma das chaves públicas FTS
2. Usa-se uma árvore de hash para autenticar todas as chaves públicas WOTS+ com uma única chave pública: a raíz desta árvore. Uma árvore assim construída é uma **árvore de Merkle**
3. Em vez de se usar uma única grande árvore de Merkle, o que implica computações longas, é possível usar **muitas**  árvores de Merkle mais pequenas, designadas por árvores do 1º nivel. Cada uma delas produz uma única chave pública: a raíz da arvore.
4. Cada uma das chaves públicas das árvores do 1º nivel podem ser associadas a folhas de uma árvore de Merkle do 2º nivel, cuja chave pública é a raíz dessa árvore.
5. O processo pode-se repetir acrescentando outros níveis.



----------


# Computação Cooperativa e Provas de Conhecimento Zero.

Ao longo de várias sessões analisamos as noções de prova de conhecimento verificável, prova de conhecimento zero, e provas interativas e não-interativas. Vimos com estas relações contribuem para a definição e segurança de esquemas de assinatura digital através das transformações de Fiat-Shamir (FS) e Fiat-Shamir With Aborts (FSWA).

Neste capítulo vamos analisar a classe particular das provas de conhecimento zero que se baseiam em protocolos de computação cooperativa (“multi-party computation” ou MPC). A transformação de um protocolo MPC  numa prova de conhecimento zero é conhecida por “MPC-in-the-Head”  e está na base da candidatura [PICNIC.](https://www.dropbox.com/sh/tjjc5bcoor2z4qw/AAAj9vMhTIjjRMW7dtdzjDWIa?dl=0)

Vamos recordar as noções de partilha de segredos e computação cooperativa que apresentamos no [+Capítulo 6: Provas de Conhecimento e Assinatura Digital](https://paper.dropbox.com/doc/Capitulo-6-Provas-de-Conhecimento-e-Assinatura-Digital-hLb9hJVPeGF0t3mmHe1A9) .


## Partilha de Segredos e Computação Cooperativa

O modelo da computação é o de funções *booleanas*
                                                               $$\,{f}\; \colon\; \{0,1\}^n \;\to\,\{0,1\}$$
que podem ser implementadas por um **circuito** *booleano*  $$\,\mathcal{C}_f\,$$construído a partir de um repertório de operações simples, designadas por **gates** 

Tipicamente usam-se as seguintes *gates booleanas* 

    - a adição e multiplicação por constante:$$\quad x\, \mapsto\,x \oplus c\quad$$ e  $$\quad x \,\mapsto\,x \cdot c\;$$
    - a adição e multiplicação binárias: $$\quad x,y \,\mapsto\, x\oplus y\quad\text{e}\quad x,y\,\mapsto x\cdot y$$


Para implementar a função *booleana* $$\,f\; \colon\; \{0,1\}^n \;\to\,\{0,1\}$$ é necessário um circuito $$\,\mathcal{C}_f\,$$que aceite *inputs* $$x$$ de tamanho $$n$$. Diz-se que o circuito tem **ordem** $$n$$. 

O **tamanho** do circuito, representado por $$\,|\mathcal{C}_f|\,$$ , é o número de *gates* do circuito.

Neste caso o número máximo de *gates* é da ordem $$O(2^n)$$ e, por isso, no pior caso o problema de verificar  $$\,\mathcal{C}_f(x) = 1\,$$tem complexidade da mesma ordem.

O problema da **verificação** ou **aceitação** de um circuito polinomial $$\,\mathcal{C}\,$$de ordem $$n$$ é o de determinar um $$\,x\in \{0,1\}^n\,$$ que seja aceite pelo circuito: i.e.  $$\,\mathcal{C}(x) = 1$$.


> Se $$\,\mathcal{C}\,$$é um circuito polinomial de tamanho. $$\,N\equiv |\mathcal{C}|\,$$ e ordem $$\,n\,$$. Então o problema da verificação de $$\mathcal{C }$$ está na classe $$\text{NP}\,$$:  o candidato a solução é o input aceite $$\,x\in\{0,1\}^n\,$$ ;  o certificado $$\,w\,$$ é o elemento de $$\,\{0,1\}^N\,$$ formado pelos outputs das várias gates do circuito quando o input é $$x$$.

**Cálculo de circuitos com partilha de segredos.**

O cálculo de circuitos parece ser um problema muito mais simples do que o da verificação: se o *input* $$\,x\,$$ for completamente conhecido por um agente, esse agente pode usar as relações que determinam os valores do vários $$w_i$$ até chegar à última *gate*; o esforço computacional é dado por  $$\,|w|\,$$ que, por construção, é polinomial com a ordem $$\,|x|\,$$.

Porém a versão interessante desse problema ocorre quando o conhecimento sobre $$\,x\,$$ está distribuído por vários agentes.  Mais exatamente, quando cada agente conhece cada um dos *inputs* $$x_i$$ e dos ouputs $$w_j$$ a menos de um erro .

Neste caso o cálculo do valor exato do último output só pode ser realizado com a colaboração de todos os agentes. Porém, nessa colaboração, nenhum dos agentes deve revelar aos restantes a sua quota-parte de $$x$$ e $$w$$.

No que se segue vamos sempre considerar

    - $$n$$ é a ordem do circuito; i.e. o número de *inputs*
    - $$m$$ é o tamanho do circuito; i.e. o número de *gates* 
    - $$N>2$$ é o número de *agentes*  participantes na partilha

O índice $$\ell$$ percorre os *inputs*, o índice $$i$$ percorre as *gates* e o índice $$j$$ percorre os participantes.

**Partilha de um segredo** $$s\in \{0,1\}$$ 

O caso mais simples de partilha ocorre quando o segredo $$s$$ tem um único bit.

O segredo $$s$$ está relacionada com as “shares”  $$\,s_j\,$$ por
       $$\,s \;=\; s_0 \oplus s_1 \oplus \cdots \oplus s_{N-1}\,$$
 Um vetor de bits $$\,(s_0, s_1,\cdots, s_{N-1})\,$$ que verificam esta  relação é representado por  $$\,\lbrack s \rbrack\,$$.   
     
As operações básicas de partilha do segredo respondem a duas questões:

- **Sharing:** como deve ser feita a alocação de cotas pelos agentes.
- **Reconstruct**: como é que um participante arbitrário $$j$$ pode determinar o valor do segredo $$\,s\,$$ a partir da sua própria cota $$\,s_j\,$$e da contribuição honesta dos restantes agentes.

Em qualquer das construções deve-se verificar:

    1. Nenhum participante conhece as cotas dos restantes.
    2. Qualquer participante que reconstrua o segredo $$\,s\,$$ pode verificar se algum dos restantes não agiu honestamente.

O protocolo básico, dito **trivial,** é


- $$\text{Share}(s)$$
    - um “Trusted agent” gera aleatoriamente $$N-1$$ bits $$\,s_1,\cdots,s_{N-1}$$ e calcula $$\;s_0 \gets s \oplus s_1 \oplus \cdots s_{N-1}$$.
    - distribui, por canais privados, cada uma das *shares* $$\,s_j\,$$aos respetivos titulares.


- $$\text{Recon}(k)$$
    Para cada $$j$$ sejam $$\quad j^+  \equiv\, (j+1)\bmod N\quad$$e $$\quad j^- \equiv\, (j-1)\bmod N$$
    - O agente $$\,k\,$$ gera aleatoriamente um bit $$\,e\,$$,  calcula $$\,m_{k}\gets e\oplus s_k\,$$ e envia-a a $$k^+$$ por um canal privado.
    - Todos os agentes $$j\neq k$$ calculam $$\,m_j \gets s_j \oplus m_{j^-}$$ e enviam $$\,m_j\,$$ ao agente $$\,j^+$$ por um canal privado.
    - O agente $$\,k\,$$ calcula $$\,s'\gets e \oplus m_{k^-}$$

É trivial verificar que $$\,s = s'$$ desde que todos os agentes ajam honestamente.


## Protocolo “Secret Sharing Multi-Party Circuit Evaluation”

Pretende-se definir um protocolo onde $$\,n\,$$ agentes colaboram para resolver o problema de cálculo de um circuito em que:

    1. a informação de *input* é partilhada e 
    2. o cálculo de *outputs,* que cada agente faz, baseia-se exclusivamente na sua cota do *input e em informação revelada pelos restantes agentes.*

Para simplificar a notação vamos usar a designação genérica de *wire* para representar quer os inputs quer os *outputs* das várias *gates*. O número total de *wires* é $$\,\ell+|\mathcal{C}|\,$$, sendo $$\ell$$ o tamanho do *input .*

A notação fundamental do protocolo usa índices  $$\alpha,\beta,\gamma\,$$ para identificar os vários *wires*. 

Nomeadamente  $$\,w_\alpha\,$$ é o valor do bit no *wire* $$\,\alpha\,$$. Estes valores são, à priori, desconhecidos dos vários agentes que, só no final da execução, conseguem reconstruir os *outputs* das várias *gates*.

**Inputs**
É conhecido públicamente um circuito $$\,\mathcal{C}\,$$ e o número de participantes $$\,n\,$$;  é informação privada um vetor de *inputs* $$\,w\in\{0,1\}^\ell\,$$ que verifica $$\,\mathcal{C}(w)=1\,$$.

**Fase “setup”**

1. Para todos os *inputs* e todos os *outputs* de gates **multiplicação é definido um bit $$\,\lambda_\alpha\,$$aleatoriamente gerado. As cotas $$\,\lbrack\lambda_\alpha\rbrack\,$$ são distribuídas pelos participantes.
2. Para cada *output* de uma soma $$\,w_\gamma = w_\alpha \oplus w_\beta\;$$, o valor de $$\,\lambda_\gamma\,$$é definido como $$\,\lambda_\alpha \oplus\lambda_\beta\,$$.
    Cada participante $$\,j\,$$ constrói a sua cota de $$\,\lambda_\gamma\,$$como   $$\,\lambda_{\gamma}^{(j)}\equiv \lambda_{\alpha}^{(j)}\oplus\lambda_{\beta}^{(j)}$$.
3. Para todas as  multiplicações $$\, w_\alpha \cdot w_\beta\,$$ são distribuídas pelos participantes as cotas $$\;\lbrack \lambda_\alpha\cdot\lambda_\beta\rbrack\;$$.
4. Para todo *input*  $$\,\alpha\,$$ é distribuído por todos os participantes o valor ofuscado $$\;\hat{w}_\alpha \equiv w_\alpha \oplus \lambda_\alpha$$.
| Mesmo conhecendo $$\,\hat{w}_\alpha\,$$um participante não conhece $$\,w_\alpha\,$$porque, do erro $$\,\lambda_\alpha\,$$, apenas conhece a sua cota. |

Para gerar as cotas $$[\lambda_\alpha]\,$$ e o valor de $$\,\lambda_\alpha\,$$ ,  a cada participante $$\,j\,$$ pode ser alocada uma “seed”  $$\,\textit{seed}_j\,$$ e com um XOF podem ser geradas todas as suas shares $$\,\lambda_\alpha^{(j)}\,$$ ; o valor de $$\lambda_\alpha$$ fica determinado, de forma implícita, como  $$\,\lambda_\alpha \equiv \sum_j\,\lambda_\alpha^{(j)} \mod 2$$.

Para todos os participantes, excepto o último, as shares $$\,(\lambda_\alpha\cdot \lambda_\beta)^{(j)}\,$$ podem ser geradas da mesma forma a partir da $$\,\textit{seed}_j\,$$. Porém, para o último participante a sua share tem de ter determinada de modo a verificar
                    $$(\lambda_\alpha\cdot\lambda_\beta)^{(n)} \,\equiv\, \sum_{j<n}\,(\lambda_\alpha\cdot\lambda_\beta)^{(j)}\,+ \,\lambda_\alpha\cdot\lambda_\beta \mod 2$$
Desta forma a informação que é preciso para determinar todas “shares”  $$\,[\lambda_\alpha]\,$$e $$\,[\lambda_\alpha\cdot\lambda_\beta]\,$$ do participante $$j < n$$,  é   uma  “seed”  $$\,\textit{seed}_j\,$$.
O participante $$\,n\,$$ recebe, para além da $$\,\textit{seed}_n\,$$ , um bit de correção para garantir que cada uma das suas “shares”   $$(\lambda_\alpha\cdot\lambda_\beta)^{(n)}\,$$  verificam a relação acima. 
Esses bits de correção formam uma string $$\,\textit{aux}_n\,$$.

**Fase de cálculo intermédio**
Este é o processo em que cada agente, individualmente e colaborativamente, calcula o valor ofuscado $$\,\hat{w}_\alpha \equiv w_\alpha \oplus \lambda_\alpha\,$$ para cada *wire* $$\,\alpha$$.

1. Quando $$\,w_\gamma = w_\alpha \oplus w_\beta\quad$$calcula-se $$\,\hat{w}_\gamma \gets \hat{w}_\alpha \oplus \hat{w}_\beta$$.
2. Quando $$\,w_\gamma = w_\alpha \cdot w_\beta\quad$$calcula-se $$\;\hat{w}_\gamma \gets s \oplus \hat{w}_\alpha \cdot \hat{w}_\beta\;$$em que

   $$\;$$$$\lbrack s\rbrack \,=\, [\lambda_\gamma] \oplus [\lambda_\alpha\cdot\lambda_\beta]\oplus \hat{w}_\alpha\cdot [\lambda_\beta]\oplus\hat{w}_\beta\cdot [\lambda_\alpha]$$

        - Cada agente usa a relação anterior para construir a sua cota de $$\,s\,$$
        - Usando a colaboração dos restantes agentes, reconstrói o valor de $$\,s\,$$e calcula $$\,\hat{w}_\gamma$$


| Note-se que nesta fase do protocolo, em que cada participante é semi-honesto, a reconstrução pública de um qualquer $$\,[x]\,$$ pode ser feita fazendo cada participante revelar publicamente a sua “share”. |

**Fase de conclusão**
Seja $$\,w_\text{out}\,$$o *wire* do *output* final do circuito. Note-se que $$\,\hat{w}_\text{out}\,$$já foi calculado na fase anterior por cada um dos agentes.  Assim, cada agente,

1. Reconstrói, usando a colaboração dos restantes agentes, o erro $$\,\lambda_\text{out}\,$$ a partir das cotas $$\,$$$$\,[\lambda_\text{out}]\;$$
2. Calcula. $$\;w_\text{out} \gets \hat{w}_\text{out} \oplus \lambda_\text{out}$$ . Falha se $$\,w_{\text{out}} \neq 1$$.
3. Recolhe-se a string $$\,\textit{msg}_j\,$$  formada pela concatenação de todas as mensagens$$\,$$ que o participante  $$\,j\,$$ emitiu públicamente durante a execução do protocolo; nomeadamente o seu “share”  nos vários $$\,[s]\,$$ associados à diferentes “gates” AND e o seu “share” no $$\,[\lambda_\text{out}]\,$$.
| 1. O algoritmo precisa de fazer uma reconstrução do bit $$\,s\,$$para cada *gate* de multiplicação. Precisa de fazer uma única reconstrução do erro $$\,\lambda_\text{out}$$. Como referimos anteriormente neste protocolo basta que cada participante revele publicamente a sua cota.<br>    2. Só é feita uma reconstrução $$\,\lambda_\text{out}\,$$se apenas for a gate final do circuito a única para a qual se pretende conhecer o valor do *output* . Se, por acaso, se pretender conhecer os *outputs* de outras *gates* é necessário fazer uma reconstrução do valor $$\,\lambda_\alpha\,$$em cada uma destas *gates*. |

## Protocolo KKW:  versão não-iterada.

O protocolo KKW ([Katz, Kolesnikov e Wang](https://www.dropbox.com/s/rgr1wkzz4jizd4b/Improved-HVZK.pdf?dl=0)) é uma prova de conhecimento construído por simulação ( *MPC-in-the-Head*) do protocolo acima. A prova resultante é um sigma protocolo iterado, corre $$M$$ vezes, mas aqui vamos apresentar apenas a versão básica com   $$M=1$$

**Inputs**
É conhecido públicamente um circuito booleano $$\,\mathcal{C}\,$$ e o número de participantes $$\,n\,$$;  é informação privada um vetor de *inputs* $$\,w\,$$ que verifica $$\,\mathcal{C}(w)=1\,$$.
A chave privada $$\,w\gets \{0,1\}^\ell\,$$ é aleatoriamente gerada.
A chave pública  é o circuito booleano  $$\,\mathcal{C}\,$$ construído da seguinte forma:

1. Gera-se  $$\,\mathcal{S}\colon \{0,1\}^\ell \to \{0,1\}^\ell\,$$  indistinguível de uma permutação aleatoria. A permutação $$\,\mathcal{S}\,$$ é definida por uma algoritmo de cifra simétrica (e.g. AES-128 ou ChaCha20) e  por uma chave de cifra $$\kappa \gets \{0,1\}^\ell\,$$  aleatoriamente gerada;  $$\,\kappa\,$$ é a **chave pública** da prova de conhecimento.
2. Calcula-se a constante  $$\,z \gets \mathcal{S}(w)\,$$ e define-se o circuito $$\,\mathcal{C}\,$$  pela função

                                                              $$\;\mathcal{C}(x) \;\equiv\; \mathcal{S}(x) + z \mathbin{\,\stackrel?=\,} 0 \;$$.

| Note-se que o teste de falha $$\,w_{\text{out}} = 1\,$$ pode ser implementado revelando os outputs de $$\,\mathcal{S}\,$$ e comparandp-os com as componentes respetivas da constante $$\,z\,$$. Elimina-se assim a necessidade de implementar o sub-circuito $$\,x \mapsto x \stackrel?= 0\,$$ que requer  $$\,\ell-1\,$$ “gates”  AND. |

3. É usada uma função de comprometimento não interativa $$\,\mathsf{Com}\,$$ e uma função de “hash” $$\,\mathsf{H}$$ .
    Como $$\textsf{Com}$$ é determinístico é necessário acompanhar o argumento $$\,x\,$$ com um  $$\,r\,$$ aleatoriamente gerado. Por exemplo, pode-se ver $$$$$$\,\textsf{Com}\,$$ como uma simples função de “hash” e calcular o comprometimento como $$\,\vartheta\,r \gets \{0,1\}^\kappa\,\centerdot\,\mathsf{Com}(x\|r)\,$$. Aqui o “disclosure” é simplesmente  $$\,d = (x,r)\,$$.


**Commit**
*1ª Parte*

1. Gera uma “seed” mestra $$\,\textit{seed}^\ast\,$$ e, a partir dela e usando um XOF, gera “seeds”  $$\,\textit{seed}_j\,$$
    para cada um dos participantes $$\,j=1..n\,$$. É também gerado, a partir de $$\,\textit{seed}^\ast\,$$, valores pseudo-aleatórios $$\,r_j\,$$, um por participante.
2. É calculado o vetor dos bits de correção $$\,\textit{aux}\,$$   como indicado atrás.  Para todos participantes $$\,j < n\,$$ define-se $$\,\textit{state}_j \equiv \textit{seed}_j\,$$;  define-se $$\,\textit{state}_n \equiv \textit{seed}_n\|\textit{aux}\,$$ .
3. É calculado, para cada $$j=1..n\,$$,  $$\;\textit{com}_j \gets \mathsf{Com}(\textit{state}_j\|r_j)\,$$ e 

                                  $$\,h \gets \mathsf{H}(\textit{com}_1 \| \cdots\| \textit{com}_n)\,$$
*2ª Parte*

1. Para todo “wire” de input $$\,\alpha\,$$, a partir do valor $$\,\lambda_\alpha\,$$gerado como atrás indicado, e da chave privada $$\,w\,$$, calcula-se o valor ofuscado $$\,\hat{w}_\alpha \gets w_\alpha + \lambda_\alpha\,$$.
2. Cada participante $$j=1..n$$ corre o protocolo MPC, a partir de $$\,\hat{w}_\alpha\,$$e do seu estado  $$\,\textit{state}_j$$. 
    Recolhe-se as mensagens $$\;\textit{msg}_j$$ produzidas pelo participante se o protocolo não falhar.
3. Para cada $$\,j=1..n\,$$ sumariza a informação resultante da sua execução

                                  $$\textsf{exec}_j\,\equiv\,\{\hat{w}_\alpha\}\,\|\,\textit{com}_j\,\|\,\textit{msg}_j$$

4. Calcula $$\;h' \gets \mathsf{H}(\{\hat{w}_\alpha\}\,\|\,\textit{msg}_1\|\cdots\|\textit{msg}_n)$$. O comprometimento final é  

                                     $$a \gets \mathsf{H}(h\,\|\,h')$$
                                    
**Challenge**
Gera aleatoriamente  $$\,c \gets [1,n]$$

**Reply**
A resposta é formada por   $$\,\textsf{exec}_c\,$$ e por $$\,\{\textit{state}_j\|r_j\}_{j\neq c}\,$$

**Verify**


1. Para cada $$\,j\neq c\,$$ , usa-se $$\,\textit{state}_j\,$$ e $$\,r_j\,$$ para calcular $$\,\textit{com}_j\,$$. O valor$$\,\textit{com}_c\,$$ faz parte da resposta. Por isso pode-se calcular $$\,h \gets \mathsf{H}(\textit{com}_1 \| \cdots\| \textit{com}_n)\,$$.
2. A partir de $$\,\{\textit{state}_j\}_{j\neq c}\,$$ , da ofuscação dos inputs $$\,\hat{w}_\alpha$$ e das comunicações $$\,\textit{msg}_c\,$$ , simula-se o protocolo MPC. Neste processo:
    1. Verifica-se se o protocolo MPC não falha; isto é, verifica-se se  $$\,w_{\text{out}}=1\,$$.
    2. Recolhe-se $$\,\textit{msg}_j$$, para $$j\neq c\,$$ ; juntando-lhe $$\,\textit{msg}_c\,$$ passado na resposta, calcula-se  $$\;h' \gets \mathsf{H}(\{\hat{w}_\alpha\}\,\|\,\textit{msg}_1\|\cdots\|\textit{msg}_n)$$   e  $$\,a^\ast \gets \mathsf{H}(h\|h')$$.
3. Verifica-se se $$\,a = a^\ast$$.


## Protocolo KKW: versão optimizada e prova não-interativa

Note-se que o tamanho total das mensagens trocadas neste protocolo KKW não-iterado é essencialmente proporcional ao número de participantes $$\,n\,$$. 
Por outro lado o erro de fiabilidade  é essencialmente determinado pela dimensão do “challenge space”  $$\,[1,n]\,$$. Para obter um erro $$\,\rho \sim 2^{-128}\,$$ o númnero de participantes (e, por isso, o tamanho das mensagens)  seria completamente impraticável.

Repetir o protocolo em $$\,M\,$$ execuções independentes não melhora muito a situação porque o tamanho da “challenge space” aumenta $$M$$ vezes mas também a complexidade espacial e a complexidade temporal aumentam as mesmas $$M$$ vezes.

A solução usada na versão optimizada do KKW usada no esquema PICNIC  aumenta o “challenge space” sem aumentar muito o número de iterações. Para isso

    - Na fase **Commit** são executadas $$M$$ iterações do protocolo MPC
    - No **Challenge** é escolhido um subconjunto de tamanho $$\,\tau\,$$ das $$M$$ iterações;  existem $$\,\binom{M}{\tau}\,$$ combinações diferentes. Para cada uma das iterações selecionadas é também escolhido um participante $$\,j\in [1,n]$$.
        A dimensão do “challenge space” passa a ser $$\,n\,\tau\,\binom{M}\tau\,$$ que é bastante superior a $$\,nM$$.
        Adicionalmente o tamanho do espaço de mensagens passa a ser da ordem de $$\,n\,\tau\,$$

Por exemplo os parâmetros  $$\,n=4\,,\,M=218\,,\,\tau=65\,$$  obtém uma segurança de $$\,128$$ bits.

O esquema PICNIC inclui ainda várias outras optimizações conducentes a comprimir o tamanho das mensagens.

A prova não-interativa (esquema de assinatura digital) é construída pela transformação Fiat-Shamir ou uma sua optimização para protocolos iterados designada por transformação de Unruh.

O circuito booleano usado no PICNIC é definido pela cifra simétrica **LowMC** (“low multiplier complexity” ) que usa um número reduzido de “gates” AND ($$\,\sim 500\,$$) para uma razoável segurança como cifra. Alternativas como o AES-128 ou AES-256  têm um número bastante superior de multiplicações.








