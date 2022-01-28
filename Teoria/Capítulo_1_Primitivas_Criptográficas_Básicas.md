# Capítulo 1: Primitivas Criptográficas Básicas

Primitivas Criptográficas são técnicas simples implementadas por um algoritmo total e determinístico que realiza uma funcionalidade descrita por um operador básico numa estrutura algébrica apropriada.

No contexto de uma aplicação criptográfica onde uma determinada primitiva está inserida ela está sempre associada à atividade de um agente. Isto contrasta com as técnicas criptográficas mais complexas (esquemas e protocolos) que estão associadas a vários agentes.

Neste capítulo vamos ver duas classes de primitivas que são ubíquas nas aplicações:


    - *“Hash’s” criptográficos:* funções de “hash” que verificam, a menos de um erro, as três condições de segurança apresentadas anteriormente:  resistência da pré-imagem e da segunda pré-imagem e resistência a colisões.
    - *Cifras por blocos*:  funções responsáveis pela ofuscação da informação; porque são primitivas muito eficientes e muito flexíveis aplicam-se igualmente a uma grande variedade de outras técnicas.


----------


# Realização de Funções de Hash  Criptográfico

Um “hash” criptográfico autentica uma **mensagem** $$M$$ , de tamanho variável, determinando um “tag” $$\,T\,$$de tamanho fixo que o representa. 
A confiança nessa autenticação depende do grau com que a função de hash  verifica as três propriedades de segurança anteriormente referidas:

 **Resistência da pré-imagem**    (também designada por **unidirecionalidade)**

> Dado um “tag” arbitrário $$\,T\in \{0,1\}^t\,$$ é computacionalmente “hard” determinar um “input”  $$\,M\,$$tal que $$\,h(M) = T$$.

**Resistência da segunda pré-imagem**

> Dado um “input” arbitrário  $$\,M_0\,$$, é computacionalmente “hard” determinar um outro “input” $$\,M_1\neq M_0\,$$ tal que $$\;h(M_1)\,=\,h(M_0)\,$$.

**Resistência a colisões**

> É computacionalmente “hard” determinar  ****um par de “inputs” distintos  $$\;M_1\neq M_0\;$$tal que $$\,h(M_1)= h(M_0)\,$$.


Nesta secção vamos apresentar alguns dos modelos que permitem realizar “hashs” criptográficos eficientes e seguros.

## Modelo de Merkle-Damgård

Em 1979, Merkle apresentou um modelo de funções de “hash” que forma a arquitectura da maioria de funções de hash recentes. O modelo é conhecido por **função de hash iterada** ou **função de Merkle-Damgård** e baseia-se nos seguintes princípios:


1. Existem três parâmetros principais: o tamanho do “hash”  $$\,t\,$$, o tamanho do estado $$\,n\,$$e o tamanho do bloco $$\,b \gg t\,$$
2. Existe uma função unidirecional 
                                                      $$\,r \,\colon\, \{0,1\}^{n+b}\,\to\,\{0,1\}^n$$
    designada por *“round function”,* ou *função de compressão* ou, ainda,  *“digest function”*.
    
    A função é unidirecional no sentido em que, se for  $$\,s' = r(s\|x)\,$$ e forem conhecidos $$\,s'\,$$e $$\,s\,$$, é intratável calcular $$\,x\,$$.
    
![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615137658000_round_function.png)

1. Existe um valor inicial do estado, representado por  $$\mathsf{iv}$$  , que se designa por “initial vector”.
2. Existe uma *função de finalização*  $$\,f \,\colon\, \{0,1\}^n\,\to\,\{0,1\}^t$$   que retira dos $$\,n\,$$ bits do último estado um “output” de tamanho $$t$$.
3. Existe uma *função de “padding”*    $$\,\mathsf{pad}\,\colon\,\{0,1\}^{<b}\,\to\,\{0,1\}^b$$ que expande uma “string” arbitrária $$\,x\,$$de comprimeto menor do que $$b$$ para um “output” com o comprimento exatamemte igual a $$b$$.

A mensagem a autenticar $$\,M\,\in\,\{0,1\}^\ast\,$$é processada da seguinte forma:

    1. O  “plaintext” (ou “padded message”) a autenticar é formadao por uma sequência de $$m+1$$  blocos  de tamanho $$b\,$$,

                                                         $$P\;\equiv\;\langle\,p_0\,,\,\,p_1\,,\,\cdots\,,\,p_m\,\rangle$$
           sendo $$\,m\;\equiv\;\lceil |M|/b\,\rceil\,$$,  calculados como
           

        1. Para $$k<m\,$$  ,  $$\,p_k\,$$ é formado pelo segmento de $$\,M\,$$ iniciado na posição $$k\ast t\,$$ e que termina na posição $$\,(k+1)\ast t - 1\,$$.
        2. $$p_m\,$$ é o “padded block” e é calculado aplicando a função $$\,\mathsf{pad}\,$$  aos restantes  bits de $$M$$.


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615122523419_padded_message.png)



    b. O estado inicial é inicializado com $$\,\mathsf{iv}\,$$. Os restantes estados calculam-se iterando com a função de compressão sobre o estado anterior e sobre os blocos do “plaintext”.


                                $$\left\{\begin{array}{rcl} s_0 &=&\mathsf{iv} \\ s_{k+1} &=& r(s_k,p_k) \qquad k=0,..m \\ \mathsf{tag} &=&f(s_{m+1}) \end{array} \right.$$
    
    O “tag” é calculado aplicando a função de finalização ao último estado.


A função de compressão $$\,r\,$$  é a componente central deste modelo. A heurística para criar uma “boa” função de compressão segue dois objetivos principais:

    - A função deve ser unidirecional, no sentido que o conhecimento do “output” fornece pouca ou nenhuma informação sobre qualquer um dos blocos do “plaintext”, e deve fornecer uma boa **mistura** entre o estado e o bloco do *plaintext*.
    - A função deve fornecer uma boa **difusão** do “input” no “output”; nomeadamente qualquer um dos bits do input deve  influenciar vários bits do “output”; idealmente o “flip” de um único bit do “input” deve causar “flips” em metade dos bits do output.

Para atingir estes objetivos recorre-se fundamentalmente a uma estratégia como a seguir se ilustra.
A função de compressão pode ser construída a partir de um “round” primitivo muito eficiente. Esta transformação  repete muitas vezes uma operação simples (que actua sobre poucos bits de cada vez).

O seguinte diagrama ilustra um arquétipo deste tipo de função compressão.

        
![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615279529949_simple_hash.png)


Nesta construção o estado está organizado numa matriz $$\,4\times 4\,$$de $$\mathtt{bytes}$$. O tamanho de bloco é $$\,b < 128\,$$ e o tamanho de estado é $$\,n = 128$$  bits assim como o tamanho da constante $$\,\kappa\,$$.

São executadas sequencialmente  4 transformações do estado:

            
            $$\mathtt{add\_cons}$$ :   adiciona ($$\mathtt{xor}$$) a constante $$\,\kappa\,$$ ao estado; esta constante contém o bloco $$\,x\,$$e uma chave $$k$$.
            
            $$\mathtt{byte\_sub}$$ :     aplica a mesma transformação não linear (com $$\mathtt{xor}$$’s e $$\mathtt{and}$$’s de bits) a cada um dos bytes; a transformação é descrita por uma tabela de acesso de $$256$$ bytes que se designa, genericamente, por  $$\mathbf{s}$$-box; neste caso a s-box tem dimensão $$8\times 8$$.
            
            $$\mathtt{row\_rotation}\,$$: aplica rotações diferentes a cada uma das linhas da matriz.
            
            $$\Sigma\_\mathtt{linear\_transform}$$ : 
            Actua sobre as colunas do estado que são interpretadas como palavras de $$32$$ bits. 
            Cada uma das transformações $$\,\Sigma_i\,$$é uma função linear construída só com operações $$\mathtt{xor}$$ e $$\mathtt{shift}$$ de palavras. Recebem  os 4  inputs  $$w_0,w_1,w_2,w_3\,$$  e produzem palavras de 32 bits que formam as várias colunas do estado $$\,s_0,s_1,s_2,s_3\,$$. 
            Isto é       $$s_i \,\gets\,\Sigma_i(w_0,w_1,w_2,w_3)\quad$$

As duas primeiras transformações implementam o objetivo *mistura* e as duas últimas implementam o objetivo *difusão*. 


A função de compressão $$\,\mathtt{Comp}\,$$  é definida pela repetição deste ciclo de operações um  número de vezes da ordem das dezenas. 

Cada aplicação da função compressão ao par $$\,(s,x)\in\{0,1\}^{n+b}\,$$ usa uma chave $$\,k\,$$  de tamanho $$n-b$$ de modo que a concatenação  $$\,x\|k\,$$  tem o tamanho $$\,n\,$$.


        1. inicia o estado com $$\,s\,$$ e, em cada repetição, usa a mesma  chave   $$\kappa = x \| k$$ .
        2. soma $$\,x\|k\,$$ ao estado final.


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615278980281_compressao_hash.png)



## Modelo “Sponge”

Para funções de “hash”, os standards NIST usam as construções do tipo Merkle-Damgård  nas funções  $$\mathtt{md5}$$, $$\mathtt{SHA1}$$ e $$\mathtt{SHA2}\,$$. 

Como a construção de uma boa função de compressão unidirecional é difícil tem-se procurado alternativas essencialmente baseadas na ideia de substituir a compressão por uma permutação.
O “standard”  $$\,\mathtt{SHA3}\,$$(e suas variantes) seguem esta abordagem e, para isso, usam um modelo designado por **sponge model** .

Este modelo consta do documento NIST de Agosto de 2015 intitulado 

> SHA3 standard: Permutation Based Hash and Extendable Output Functions 

Como o nome indica este modelo tem, em relação ao modelo MD, duas alterações fundamentais:

    - Em primeiro lugar não se baseia em funções de compressão unidirecionais mas sim em permutações. Como primitiva básica, uma permutação (i.e uma função invertível com o mesmo tamanho de domínio e co-domínio) é mais simples de construir e mais eficiente a executar.
    - Em segundo lugar, no modelo “sponge” a função de “hash” tem “outputs” de tamanho fixo mas, ao contrário do que ocorre no modelo MD, esse tamanho é um parâmetro de operação: pode variar entre duas execuções do mesmo “hash”.


| Uma função de “hash” , em que o tamanho do “output” pode variar , designa-se por  **XOF** (“eXtendable Output Function”) |

A metáfora “sponge” indica que a computação de um XOF é feita em duas fases ilustradas na figura seguinte.


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615310975561_sponge.png)


**absorb** 
Nesta fase a mensagem $$\,M\,$$ é, tal como no modelo MD, objeto de um processo de “padding” e depois dividida em segmentos de tamanho $$\,r\,$$ (o “rate”).  
O resultado, o “plaintext”  $$\,P \equiv p_0\,\|\,p_1\,\|\,\cdots\,\|\,p_m\,$$ é absorvido num bloco de estado de tamanho $$\,b\gg r\,$$. O resto do bloco, de tamanho $$\,c = b -r\,$$ designa-se por *capacidade*; metade dos bits da capacidade é o *coeficiente de segurança* desta arquitectura.
O  bloco de estados é inicializado com  um vetor  $$\,\mathsf{vi}\,$$ nas suas primeiras $$r$$ posições e por zeros na capacidade.
Em cada iteração, lê-se um  bloco do “plaintext” que é somado aos primeiros $$r$$ bits do estado e aplica-se uma permutação $$\,f\colon\{0,1\}^b\to \{0,1\}^b\,$$ à totalidade do estado.

**squeeze**
 
A partir do estado construído na 1ª fase, são extraídos sucessivos segmentos  $$\,t_i\,$$do “output” e, ao mesmo tempo, o estado continua a ser transformado com $$\,f\,$$. 
Em cada extração são retirados (segundo um critério apropriado) $$\,r\,$$ bits do estado. Concatenando  todos estes segmentos constrói-se  a  $$\,\mathsf{tag}\,$$. O parâmetro $$\,\ell\,$$ é determinado pelo comprimento desejado para a $$\,\mathsf{tag}\,$$:

                                  $$\ell\;=\;\lceil\,|\mathsf{tag}|/r\,\rceil \,$$

Com a concretização da permutação $$\,f\,$$ define-se o algoritmo **Keccaq**  de onde provém os algoritmos para o SHA3 e para os SHAKE.  Todos eles usam um tamanho de estado $$\,b = 1600\,$$bits. A forma como o estado é dividido em “rate” e “capacity” depende das várias configurações


|           | output   | rate | capacity | 1st pre-image security |
| --------- | -------- | ---- | -------- | ---------------------- |
| SHA3-256  | 256      | 1088 | 512      | 256                    |
| SHA3-512  | 512      | 576  | 1024     | 512                    |
| SHAKE-128 | variável | 1344 | 256      | 128                    |
| SHAKE-256 | variável | 1088 | 512      | 256                    |


O modelo “sponge” pode também ser usado como *cifra  autenticada com dados associados* como se ilustra na figura seguinte. 


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615315853786_sponge-aead.png)


Numa 1ª fase “absorb” são absorvidos os segmentos que descrevem os dados associados.
Na 2ª fase, equivalente ao “squeeze”, usa-se uma cifra de Vernam que recebe segmentos $$\,p_i\,$$ sucessivos de um “plaintext” , soma-os com $$r$$ bits do estado e devolve os segmento $$\,c_i\,$$ do criptograma.
Finalmente, após o processamento de todo o “plaintext” existe uma na aplicação da permutação para construir a “tag” de autenticação final.
A chave $$K$$ da cifra, aparece na inicialização do 1º valor do estado e aparece antes e depois da última aplicação da permutação.


# Cifras e Segurança de Cifras

É bem conhecido que a classe das técnicas criptográficas designadas genericamente como **cifras** agrupa esquemas ditos de **chave privada,** ou **simétricos,** e esquemas ditos de **chave pública**, ou **assimétricos**. 

Esta classe abrange ainda outro tipo de técnicas, variantes dos dois tipos anteriores, que apresentaremos em futuros capítulos. Todas estas técnicas  têm, como objetivos principais, a **ofuscação** e o **controlo do conhecimento** dessa ****informação. 

A formalização do que é um esquema de cifras ou, principalmente, de como se formaliza a sua segurança depende crucialmente do tipo de cifra. Neste capítulo vamos concentrar-nos, por motivos que serão óbvios em breve, nas cifras simétricas.

Uma cifra simétrica, na sua versão mais simples,   é um esquema definido por dois algoritmos determinísticos e  totais que implementam duas funções: uma função para **cifrar** e uma segunda função para **decifrar**. 

Uma exigência específica das cifras simétricas é que ambos os algoritmos têm de ser muito eficientes tanto em tempo de execução como em memória usada. Por causa disso os algoritmos podem, quase sempre, ser implementados em “hardware” com circuitos eletrónicos que usam um número reduzido de “gates”.

Pela sua simplicidade, porque podem ser descritos por circuitos e porque são frequentemente usados como componentes de outras técnicas mais complexas, faz sentido considerar cifras simétricas como primitivas criptográficas.


----------

Alguma terminologia recorrente nestas técnicas simétricas

| cifrar, decifrar | encrypt, decrypt |
| ---------------- | ---------------- |
| mensagem         | plaintext        |
| criptograma      | ciphertext       |
| chave            | key, secret      |

----------
| **Nota importante**<br>Segundo os dicionários de referência, na Língua Portuguesa “encriptar” significa “encerrar em criptas”. Por isso este verbo **não é** uma tradução legítima do verbo inglês “encrypt”.<br>Usado no contexto criptográfico, “encriptar” é um anglicismo grosseiro  que não substitui a terminologia estabelecida há mais de um século: “cifrar” é sempre o verbo correto. |


A formalização do que é um esquema de cifras ou, principalmente, de como se formaliza a sua segurança depende crucialmente do tipo de cifra.
Uma cifra simétrica é descrita por um par de funções parcialmente computáveis
                                                                        $$E,D\,\colon\,\mathbb{N}\,\to\,\mathbb{N}\,$$
tais que, para todos inteiros $$\,k,n,m\,$$ tem-se 

                         $$E(k,n)\simeq m\quad$$ se e só se $$\quad D(k,m)\,\simeq\,n$$

Esta condição designa-se por **condição de correção.**


Para cada $$\,k\,$$, é conveniente definir um par de funções $$\,E_k,D_k\,\colon\,\mathbb{N}\,\to\,\mathbb{N}\,$$  como 

                     $$E_k \;\equiv \; n\mapsto E(k,n)\quad$$    e     $$\quad D_k \;\equiv\; m \mapsto D(k,m)$$
            

Seja $$\,\mathcal{K}\,$$ um domínio finito  tal que, para cada $$\,k\in \mathcal{K}\,$$, a função $$\,E_k\,$$ é total.  

Para  valores de $$\,k\,$$ nesse domínio,  o domínio dos criptogramas

                              $$E_k(\mathbb{N})\;\equiv\;\{\,E_k(n)\,|\,n\in \mathbb{N}\,\}$$

é um conjunto isomórfico com $$\,\mathbb{N}\,$$ (devido à condição de correção) mas que pode não coincidir com $$\,\mathbb{N}$$. Isto é, podem existir valores de $$\,m\,$$que não são  cifra de algum $$n$$; equivalentemente,  $$\,D_k(m)\,$$ é indefinido.

Restringindo $$\,D_k\,$$ ao seu domínio, a condição de correção é equivalente à afirmação de que $$\,D_k\,$$ é a função inversa de $$\,E_k\,$$$$\,$$.

Nem todas as cifras simétricas asseguram que $$\,E_k\,$$ seja uma função total. Por exemplo a cifra pode só aceitar mensagens que tenham um determinado formato. Uma tentativa de fornecer à cifra uma mensagem mal formatada origina um erro.

No que se segue vamos considerar apenas cifras simétricas em que, para valores da chave $$\,k\,$$ dentro de um determinado domínio, a cifra é completamente descrita por uma função computável e total.

**Segurança**

A condição de correção é insuficiente para garantir a **ofuscação** da informação. É necessário garantir também **condições de segurança**.
Isto é, enquanto que o conhecimento dos parâmetros $$\,k,x,y\,$$  permite verificar a  condição de correção, as condições de segurança vão garantir que o conhecimento de apenas $$\,x,y\,$$ não permite verificar a condição de correção.

A segurança de uma cifra simétrica exprime a sua **imunidade a ataques**. O objetivo desses ataques é o de obter conhecimento sobre o parâmetro $$\,k\,$$a partir da operação corrente da cifra.

O arquétipo de um ataque é um protocolo em que o atacante interage com a operação corrente da cifra e, sem conhecer o parâmetro $$\,k\,$$, obtém um número elevado de pares $$\,(x,y)\,$$ que verificam $$\,y=E(k,x)\,$$. O ataque terá sucesso se, dessa informação, é possível computar eficientemente informação sobre $$\,k\,$$.

“Informação sobre $$\,k\,$$” pode significar conhecer completamente $$\,k\,$$ , apenas alguns dos seus bits ou ainda, mais genericamente, pode significar conhecer os resultados de decisões $$\,\varphi(k)\,$$ “sem vícios”.

**Arquitetura**

Por muito simples que seja, uma cifra simétrica é formada por primitivas mais simples. A hierarquia de técnicas que culmina com a descrição da cifra designa-se por **arquitetura** da mesma.

Algumas das componentes são, elas próprias, cifras simétricas. Por exemplo

Uma “**Primitive Block Cipher**” (PBC) é uma cifra que recebe como “input” um bloco de $$\,b\,$$ bits e produz um “output” um bloco também com $$\,b\,$$ bits. A chave $$\,k\,$$ é também um bloco com um tamanho $$\,t\geq b\,$$.

![Primitive Block Cipher](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615459578824_pbc.png)


Neste modelo, para cada $$\,k\,$$,  as funções  $$\,E_k\,$$e $$\,D_k\,$$são permutações num alfabeto de $$\,2^b\,$$ símbolos.

| **Nota**<br>Em rigor uma PBC não deve ser classificada como uma técnica primitiva porque é decomponível em técnicas criptográficas mais  elementares. No entanto, para efeitos da formalização de segurança e de integração com outras técnicas criptográficas mais complexas é conveniente abstrair os detalhes  da sua construção. |

A partir de uma PBC é possível construir outras cifras (ou variantes) que usam apenas uma chave privada. Nomeadamente vai ser possível definir

    1. Geradores Pseudo-Aleatórios (PRG) e as cifras sequenciais (“stream ciphers”) a eles associadas.
    2. Cifras por Blocos (BC)


## Geradores Pseudo-Aleatórios (PRG’s)

Muitos dos PRG’s usados atualmente baseiam-se numa primitiva designada por “*tweakable PBC*” (TPBC). Na sua forma genérica uma TPBC é análoga a uma PBC com um “input” adicional $$\,w\,$$ designado por *“tweak”.*


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615460205160_tpbc.png)


O papel do “tweak” $$\,w\,$$ é análogo ao da chave $$\,k\,$$e a diferença só se manifesta quando a TPBC está integrado numa outra cifra onde cada execução inclui várias execuções do TPBC.  Neste caso cada execução da cifra usa uma só chave $$\,k\,$$ mas cada execução do TPBC usa um “tweak” distinto.

Nas aplicações mais simples, o “tweak” é integrado na chave de um PBC “standard”. Em arquiteturas mais complexas o “tweak” é processado tal como a chave mas de forma independente desta.


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615462118643_Canvas+2.png)


Esta figura ilustra o arquétipo de um PRG construído com um TPBC.  Essencialmente,

        1. O estado é formado por duas componentes; a primeira é o “input”  do TPBC, aqui representado por ST ; é inicializado com o “seed” e , em cada invocação , é atualizado com o resultado da invocação anterior.
        2. A segunda componente do estado é um contador CTR que é inicializado com $$\mathsf{iv}\,$$e, em cada invocação, é incrementado uma unidade. O valor de CTR  é usado como “tweak”.
        3. Do resultado do TPBC, em cada invocação, são extraídos $$s$$  bits como “output”.

Este gerador tem três parâmetros livres: o vetor de inicialização do contador, o “seed” que determina o estado inicial e a chave $$\,k\,$$ do TPBC.  Quando este gerador é usado numa cifra sequencial, tanto a “seed” como a chave (ou a combinação dos dois) podem ser usados como chave da cifra.


![stream cipher](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615463846277_Canvas+3.png)

## Cifras por Blocos

Uma cifra por blocos é uma cifra simétrica formada por uma cifra primitiva por blocos e por um algoritmo designado por **modo**. O seu objetivo é estender a funcionalidade das PBC a *strings* de tamanho arbitrário. 

Para isso o “plaintext” é dividido  em blocos de tamanho fixo que são cifrados pela PBC segundo uma disciplina definida pelo modo. O modo também determina a forma como os blocos produzidos pelo PBC são combinados para reconstruirem o “ciphertext”. 

Como a PBC exige “inputs” de um tamanho $$\,b\,$$ fixo, e como geralmente o comprimento do “plaintext” não é um múltiplo inteiro de $$\,b\,$$, é necessário usar um algoritmo de **padding** para ajustar o tamanho do  “input”. 
Como vimos para as funções de “hash” , o algoritmo de “padding” aumenta o último bloco da divisão com  bytes (o “pad”) suficientes para ele ter o tamanho $$b$$.

Como veremos adiante, o “padding” tem uma importância fundamental na segurança da cifra. Uma cifra com uma PBC muito segura pode tornar-se insegura com um “pad” descuidado e um modo que mostre a sua vulnerabilidade.


----------

**Modo ECB (“eletronic code book”)**
O modo mais direto é designado por “electronic code book” e é ilustrado na figura seguinte. Essencialmente cada bloco do “plaintext” é cifrado independentemente dos restantes e produz um bloco do “ciphertext”.

![Eletronic Code Book](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615672665085_ECB.png)


Este modo é extremamente inseguro a menos que seja usado em situações muitos particulares. A razão reside na vulnerabilidade desta cifra a ataques que removem blocos ou substituem blocos por outros blocos na mesma mensagem.


----------

**Modo CBC (“cipher block chaining”)**
Um outro exemplo, com maior imunidade a repetições e remoçoes de blocos, é o modo designado por CBC. Este modo aparece por defeito em muitas aplicações. Infelizmente este modo pode também ser objeto de ataques.

Considere-se um “plaintext” $$\,P\;\equiv\;\langle\,P_0,P_1,\cdots,P_{n-1},P_n\,\rangle\,$$ em que todos os blocos $$\,P_i\,$$ têm tamanho $$\,b\,$$.  Porém o último bloco foi construído por “padding”

                               $$P_n\,=\, P'_n\,\|\,\mathsf{pad}$$

O prefixo $$P'_n\,$$ provém da mensagem (i.e. $$\,M \,=\,P_0\|P_1\|\cdots\|P'_n\,$$) e o sufixo $$\mathsf{pad}$$ foi adicionado pelo algoritmo de “padding”.
O criptograma é formado pela sequência de blocos $$\,C\,\equiv\,\langle\,C_0,C_1,\cdots,C_n\,\rangle\,$$ todos de tamanho $$b$$.

Para cifrar os blocos  $$\,C_i\;,\;i=0..n\,$$, são construídos sequencialmente com as regras seguintes

    $$\left\{\begin{array}{rcl}C_0 &=&E_k(P_0 \oplus \mathsf{iv}) \\ C_i & = & E_k(P_i\oplus C_{i-1})\quad\text{para}\quad i> 0\end{array}\right.$$



![Cifra em modo CBC (Cipher Block Chaining)](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615546042544_cbc.png)


Para decifrar os blocos $$\,P_i\,$$ são construídos, sequencialmente, como

    $$\left\{\begin{array}{rcl}P_0 &=& D_k(C_0) \oplus \mathsf{iv} \\ P_i & = & D_k(C_{i})\oplus C_{i-1}\quad\text{para}\quad i> 0\end{array}\right.$$

**“Unpadding” e um  ataque protocolo TLS**

O algoritmo para decifrar o modo CBC recupera o bloco $$P_n$$ do “plaintext” após o “pad” mas, por si só, não consegue recuperar a mensagem $$\,M\,$$ porque não se consegue saber qual é o prefixo $$\,P'_n\,$$ de $$\,P_n\,$$ que faz parte de $$\,M\,$$. Para ser possível recuperar $$\,P'_n\,$$ é necessário que, em $$\,P_n\,$$, seja transmitido o comprimento do “pad”.
Este processo designa-se por “unpadding” e  está diretamente ligado ao algoritmo de “padding”.

Por exemplo, o protocolo TLS usado universalmente como garantia de segurança na comunicação digital, usa blocos de 16 bytes. Nele ocorrem duas circunstâncias que permitiu construir um ataque que veio a ter consequências desastrosas:

1.  O  “padding” enche o último bloco com bytes cujo código hexadecimal é igual ao comprimento do próprio “pad”.  
    Assim  um “pad” de 1 byte é $$\,\mathtt{01}$$; de dois bytes será $$\,\mathtt{0202}$$; três bytes será $$\,\mathtt{030303}$$; até ao máximo de 15 bytes que será  uma sequência de 15 bytes iguais a  $$\,\mathtt{0f}$$.
2. Frequentemente um atacante consegue distinguir, quando o algoritmo de decifrar falha, se o erro provém de violação das regras de “padding” ou por qualquer outro motivo; por exemplo por a chave ser errada. 
    O tempo que decorre até à falha permite distinguir estes dois casos.  Se isso for possível diz-se que existe um *oráculo de “padding”*. 
    Várias implementações do TLS davam origem a oráculos de “padding”.

O objetivo do ataque é, em primeiro lugar, recuperar o último byte de  $$\,P_n\,$$;  porém o ataque generalizável para recuperar todos os bytes de $$P_n$$ e, por repetições, recuperar todos os blocos $$\,P_i$$ do “plaintext”.


1. O ataque desenvolve-se por tentativas percorrendo todos os possíveis bytes $$\,x=0..255$$. 
2. Incide sobre os dois últimos blocos $$\,P_{n-1},P_n$$ do “plaintext” e os dois últimos blocos do criptograma $$C_{n-1},C_n$$. 
    Com um $$k$$ desconhecido do atacante, a relação entre estes 4 blocos é
                $$P_n = D_k(C_n)\,\oplus C_{n-1}\quad,\quad P_{n-1} = D_k(C_{n-1}) \oplus C_{n-2}$$
3. O atacante modifica apenas o penúltimo bloco  do criptograma do criptograma  para
                                $$C'_{n-1}\;\equiv\;C_{n-1} \oplus x \oplus \mathtt{01}$$
4. Se a chave $$k$$ fosse conhecida o algoritmo de decifra iria recuperar exatamente os mesmo blocos com exceção dos blocos nas posições $$n$$ e $$n-1$$ que passaremos a designar por $$\,P_n'\,$$e $$\,P_{n-1}'\,$$.  É simples verificar que o antigo e novo valor do último bloco estão relacionados por
                                           $$P_n\,\oplus\,P_n'\,=\,\mathtt{01}\oplus x$$
5. Se, tentando decifrar  com uma chave arbitrária, o oráculo de “padding” indicar que o “pad” está corretamente construído, então o último byte de $$\,P_n'\,$$ coincide com $$\,\mathtt{01}\,$$ o que significa que o último byte de $$\,P_n\,$$é $$\,x\,$$.
6. Conhecido $$x$$ , o último byte de $$\,P_n\,$$,  procura-se o penúltimo byte $$y$$   modificando $$\,C_{n-1}\,$$ com  $$\mathtt{0202}\oplus y0 \oplus 0x$$.  E assim sucessivamente constrói-se todo $$P_n$$.


----------


## Cifras Autenticadas (AEAD)

De modo a evitar ataques que modificam o “ciphertext” ou o “plaintext” , todas as cifras modernas de uso  genérico autenticam essas strings de forma integrada com o próprio mecanismo de cifra.

Adicionalmente o algoritmo de cifra também autentica meta-informação que é passada em claro juntamente com o criptograma. Esses meta-dados, neste contexto, são vulgarmente designados por *dados associados* e mecanismo resultante é designado por **AEAD** (“authenticated encryption with associated data”).

Um exemplo de um algoritmo AEAD foi já  apresentado quando descrevemos o modelo “sponge” para funções de “hash” e adaptamos esse modelo a esta funcionalidade. Vimos nesse exemplo uma construção que recebe como “inputs” o “plaintext” e os dados associados e produz como “output” o “ciphertext” e uma “tag” de autenticação.

Vamos ver alguns outros exemplos

“**Galois Counter Mode” (GCM)**

Nos últimos anos este modo tem sido o modo “standard” em cifras autenticadas de uso genérico. Nomeadamente vem quase sempre associada à cifra AES quando esta é usada de forma assíncrona e com mensagens longas.


![Retirado de https://en.wikipedia.org/wiki/Galois/Counter_Mode](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615567156258_GCM.png)


 

Neste diagrama os blocos têm 128 bits (tal como op AES).
O diagrama descreve razoavelmente bem todo o mecanismo de autenticação. A única dúvida é a descrição do operador $$\,\mathsf{mult}_H\,$$; de facto é deste operador que vem a referência “Galois” no nome do modo.
 
Veremos num dos próximos capítulos, em detalhe, o que significa Corpos de Galois. Essencialmente as palavras de $$128$$ bits são vistas como coeficientes de um polinómio booleano de grau menor do que 128. Os polinómios, com operações de soma e multiplicação módulo um polinómio irredutível de grau 128, formam um corpo. 

Nesta construção a variável dos polinómios é $$\,z\,$$; o módulo usado é  o polinómio

                             $$\,\varphi(z)\;\equiv\; z^{128} + z^7 + z^2+ z +1$$

A constante $$\,H\,$$ resulta da aplicação da  cifra primitiva $$\,E_k\,$$  ao bloco $$\,0^{128}\,$$ seguida da interpretação de  $$\,H = E_k(0^{128})\,$$ como polinómio.
A operação $$\,\mathsf{mult}_H\,$$ é a multiplicação do argumento por $$\,H\,$$ , no corpo binário.

                              $$\mathsf{mult}_H(x) \,\equiv\, x * H \bmod \varphi$$

  

## AEAD com “Tweakable Block Ciphers”

**Tweakable Primitive Block Ciphers” (TPBC)**
De forma cada vez mais frequente a cifra autenticada recorre a cifras de blocos baseadas em “tweakable primitive block ciphers” (TPBC) em vez de simples “primitive block ciphers” (PBC).

Vimos anteriormente que um TPBC é uma primitiva análoga a uma PBC mas com dois parâmetros de controlo em vez de um único, a chave, como ocorre numa PBC.

Os parâmetros de controlo num TPBC são uma chave de “longa duração” $$\,k\,$$ e uma chave de “curta duração” $$\,w\,$$ designada por “tweak”.  
Quando uma TPBC está integrada numa cifra autenticada, a chave de longa duração $$\,k\,$$ tem sempre o mesmo valor nas várias invocações da primitiva. Ao invés o “tweak”  , a chave de curta duração , varia sempre entre invocações.


> Como construir uma TPBC  $$\,\tilde{E}(w,k,x)\,$$  a partir de uma PBC   $$\;E(k,x)$$  ?

A abordagem mais simples, e que é a mais usada nas cifras “lightweight”, passa por expandir a chave de longa duração com o “tweak”. O parâmetro de controlo passa a chamar-se “tweaked key” e pode ser apenas a concatenação dos parâmetros $$\,w\,$$e $$\,k\,$$.

Fazendo     $$\kappa\;\equiv\; w\,\|\,k$$  ,  então

                                  $$\tilde{E}(w,k,x)\;\equiv\;E(\kappa,x)$$
                        

Noutras cifras a “tweaked key” é construída por uma função $$\,\mathsf{tkey}(w,k)\,$$ optimizada para tornar tão eficiente quanto possível a expansão de $$\,k\,$$ com o “tweak” $$\,w\,$$. 
De qualquer forma, usando $$\,\kappa \equiv \mathsf{tkey}(w,k)\,$$, a relação anterior aplica-se.

Numa segunda abordagem, em vez de o “tweak”  modificar a chave, passa a modificar antes o “plaintext” $$x\,$$.  Nesse caso é comum definir-se

                                  $$\tilde{E}(w,k,x)\;\equiv\;E(k, w \oplus E(k,x))$$


| **Nota**<br>Em ambas as construções  de $$\,\tilde{E}\,$$ existe, em relação a $$\,E\,$$,  algum custo computacional adicional; na 1ª abordagem existe o custo da expansão da chave, enquanto que na 2ª abordagem a PBC é invocada duas vezes por cada invocação da TPBC. |


**O modo TAE (“tweaked authentication encryption”)**

Este é um modo de cifra autenticada que não usa dados associados.

Vamos supor que que o  “plaintext”  é formado por $$m$$ blocos de tamanho $$\,b\,$$ e terminado num blocos $$\,P_m'\,$$ de tamanho $$\,\tau < b$$. Após o “padding” o “plaintext” é

                               $$\,P\;\equiv P_0\,|\,P_1\,|\,\cdots\,|\,P_m\,$$

sendo o  “pad” uma sequência de $$(n-\tau)\,$$ zeros; isto é, $$\,P_m\,\equiv\,P_m'\|0^{(n-\tau)}\,$$.  O valor de $$\,\tau\,$$ vai também ser cifrado em conjunto com os blocos $$\,P_i\,$$.

A seguinte figura ilustra o mecanismo geral de cifra


![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615655562499_Canvas+1.png)



    - Os primeiros $$\,m\,$$ blocos $$\,P_i\,$$ são cifradas com a $$\,\text{TPBC}\,$$ controlada por uma só chave $$\,k\,$$ mas com “tweaks”  $$\,w_i\,$$ distintos.
    
    - O último bloco $$\,P_m\,$$ é cifrado de forma distinta: como um XOR de uma máscara gerada cifrando $$\tau$$.
    
    - O último passo é a geração de um “tag” de autenticação a partir da paridade do “plaintext”.
    
    - Os “tweaks”  $$\,w_i\,$$ e  $$\,w^\ast\,$$ são construídos como se ilustra em seguida.
    
        - Existe um “nounce”  (“name only used once”) que ocupa os primeiros $$b/2\,$$ bits de cada “tweak”.
        - Os $$m+1$$ “tweaks” usados na cifra distinguem-se do restante por terminarem num bit $$0\,$$. O “tweak” da autenticação termina em $$1$$.
        - A componente intermédia é um contador, incrementado uma unidade em cada bloco, no 1º caso, ou então é um parâmetro $$\ell$$ igual ao comprimento total do “plaintext” (sem “pad”).
        
![](https://paper-attachments.dropbox.com/s_B1054BDA5AC312A4FB9A5763C788D22B1CCD183EF0DF33A2A6FDC7FDD5358446_1615655577238_Tela+2.png)


Sem os “tweaks” esta cifra seria  análoga ao modo ECB e, por isso, muito insegura. 
Os “tweaks” impedem as repetições e as remoções porque cada “tweak” contém informação sobre a posição do bloco. 
Isto por si não impede que um bloco seja substituído por outro bloco que, em outra mensagem, ocupe precisamente a mesma posição. Para isso os “tweaks” contém um “nounce”.
Recorde-se que “nounce” funciona como um número pseudo-aleatoriamente gerado sem repetições. Se esta restrição for cumprida à risca  então este modo é seguro.



