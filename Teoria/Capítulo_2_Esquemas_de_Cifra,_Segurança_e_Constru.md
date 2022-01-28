# Capítulo 2: Esquemas de Cifra, Segurança e Construção.


----------

Neste capítulo vamos continuar a analisar cifras e técnicas associadas tendo em atenção a sua segurança e alguns fundamentos algébricos essenciais à sua formalização. Este é um capítulo introdutório que não esgota o tema. Outras técnicas na mesma família serão discutidas em capítulos futuros.


# Critérios de Segurança

A segurança das cifras simétricas, e das cifras em geral, é formalizada em termos de **imunidade a ataques**.  Os ataques mais frequentes classificam-se em duas classes:

**Plaintext Attacks (PA’s)**
O atacante conhece, para cada chave $$\,k\,$$, um número finito de pares 

                                $$\langle\,x\,,\,E_k(x)\,\rangle$$

**Ciphertext Attacks (CA’s)**
Para além da informação anterior o atacante também tem capacidade para decifrar alguns criptogramas.


## Segurança Perfeita de Cifras Primitivas 

Numa PBC tanto o “plaintext” como “ciphertext” são blocos de tamanho $$\,b\,$$. A chave é finita e tem tamanho $$\ge b$$.

Seja $$\,h\,$$ um “hash” aleatório de tamanho $$\,b\,$$. O “grafo” da cifra é o gerador, função de $$k$$,

                                    $$G(k)\;\equiv\; \vartheta\,x\gets h\,\centerdot\, x\,\|\,E(k,x)$$
| Como tanto $$\,x\,$$ como $$E(k,x)$$ são blocos de tamanho conhecido $$b$$, então a construção de pares pode ser descrita simplesmente por concatenação das “strings”. |

Num modelo computacional, diz-se que a cifra é **PA-perfeita** quando, para toda a chave $$\,k\,$$, o gerador $$G(k)$$ é   $$K$$-trivial.


----------
## Cifras por Blocos: segurança por indistinguibilidade probabilística

A forma mais comum de apresentar a segurança de cifras segue porém uma outra abordagem baseada na indistinguibilidade probabilística de determinados ataques.

Numa cifra por blocos, que lida com “plaintext” e “ciphertext” de tamanho arbitrário, o modelo considera duas funções parciais 

                                $$E,D\;\colon\; \mathbb{N}\,\to\,\mathbb{N}\,$$

e um domínio finito $$\,\mathcal{K}\,$$ que permitem definir famílias de funções de cifra e decifra.

                $$E_k(n)\;\equiv\;E(k,n)\quad$$ e  $$\quad D_k(m) \;\equiv\; D(k,m)$$     para $$k\in\mathcal{K}$$
                

Vamos considerar exclusivamente cifras simétricas por blocos para as quais, para toda a chave $$k\,$$dentro do domínio $$\,\mathcal{K\,}$$, as funções  $$E_k\,\colon\,\mathbb{N}\,\to\,\mathbb{N}$$ são totais.
Nestas cifras  é importante ter em conta que as funções $$\,E_k\,$$ são sempre injetivas mas podem não ser subjectivas;  o conjunto dos criptogramas 
                                   $$\,E_k(\mathbb{N})\;\equiv\;\{\,E_k(n)\,|\,n\in\mathbb{N}\,\}\,$$ 
é isomórfico com $$\,\mathbb{N}\,$$ mas pode não coincidir com $$\,\mathbb{N}\,$$.

Por isso a função de decifrar $$\,D_k\,\colon\,\mathbb{N}\,\to\,\mathbb{N}\,$$ é uma função parcial em que $$\,D_k(m)\,$$ é definido  sse  $$\,m\in E_k(\mathbb{N})\,$$.  Obviamente, restrita a esse domínio, $$\,D_k\,$$é inversa de $$E_k$$.


----------

Nas cifras por blocos ocorrem tanto oráculos que permitem ao atacante obter criptogramas de mensagens escolhidas como oráculos que permite obter blocos de “plaintext” de criptogramas escolhidos.

Vamos considerar o mesmo “hash” de tamanho $$\,b\,$$ considerado na análise anterior. 
O oráculo  que cifra define-se  como o gerador 

                                      $${G}(k)\;\equiv\;\vartheta\,n\gets h^\ast\,\centerdot\,\langle\,n\,,\,E(k,n)\,\rangle$$

O oráculo de decifrar é análogo mas considera a hipótese de o algoritmo de decifrar falhar. Por isso o símbolo $$\,\bot\,$$ é um valor legítimo para o seu “output”

                                    $${H}(k)\;\equiv\;\vartheta\,n\gets h^\ast\,\centerdot\,\langle\,n\,,\,D(k,n)\,\rangle$$


## IND-CPA

O **ataque IND-CPA**  é um protocolo de 3 passos onde intervem um agente designado por **adversary** ($$\mathsf{Ad}$$)  e um agente designado por **chalendger** ($$\mathsf{Ch}$$) que obedecem às seguinte regras:

    - $$\mathbf{Ad}$$ não conhece a chave $$\,k\,$$ mas em contrapartida tem acesso ao oráculo $$G(k)$$.
        O agente intervém em dois passos do protocolo cada um dos quais é descrito por um algoritmo: o algoritmo de **escolha** ($$\mathcal{E}$$) e o algoritmo de **decisão** $$\,\mathcal{D}\,$$.
        Ambos os algoritmos consultam o oráculo $$\,G(k)\,$$ e a sua complexidade, definida pelo número de acessos, é polinomialmente limitada pelo tamanho dos “inputs”.
    - $$\mathbf{Ch}$$ conhece a chave $$\,k\,$$ e, por isso, é o único capaz de cifrar mensagens e decifrar criptogramas.

O protocolo tem os seguintes passos:

1. $$\mathbf{Ad}\;\colon\; m_0,m_1\gets \mathcal{E}(n)$$
    Para uma experiência $$\,n\,$$, a computação  $$\,\mathcal{E}^{G(k)}\,$$ determina duas mensagens. Como referimos $$\,\mathcal{E}\,$$ tem acesso ao oráculo $$\,G(k)\,$$; o oráculo não está explicitamente representado para não sobrecarregar a notação.
2. $$\mathbf{Ch}\;\colon\;c \gets (\vartheta\,d \gets \{0,1\}\,\centerdot\,E(k,m_d))$$
    O “chalendger” gera aleatoriamente um bit $$d$$ e, usando o conhecimento da chave, cifra a mensagem selecionada por esse bit e gera o respetivo criptograma.
3. $$\mathbf{Ad}$$  constrói a “string”  $$\,x \,\equiv\, m_0\|m_1\|c\,$$ , formada pela concatenação das mensagens trocadas nos passos anteriores. Com esse “input” calcula o valor da decisão  $$\,\mathcal{D}^{G(k)}\,$$.
    A decisão tem sucesso quando, consultando o oráculo $$G(k)$$, o agente consegue identificar qual das mensagens $$\,m_0\,$$ou $$\,m_1\,$$ está associada ao criptograma $$\,c\,$$.

Resumidamente, para um par de algoritmos $$\mathcal{E},\mathcal{D}$$ o protocolo é descrito pela decisão 
             $$\mathsf{IND\!\!-\!\!CPA}(\mathcal{E},\mathcal{D})\;\equiv$$
             $$\quad \vartheta\,n\,\centerdot\,m_0,m_1\gets\mathcal{E}^{G(k)}(n)\,\centerdot\,\vartheta\,d\gets\{0,1\}\,\centerdot\,\mathcal{D}^{G(k)}(m_0\|m_1\|E(k,m_d))$$

O ataque tem sucesso quando a probabilidade desta decisão não é negligenciavel com o tamanho dos argumentos.

                                   $$\mathbb{P}[\;\mathsf{IND\!\!-\!\!CPA}(\mathcal{E},\mathcal{D})\;]\;\simeq\!\!\!\!\!/\; 0$$
## IND-CCA1 e IND-CCA2


A possibilidade de o algoritmo de decifrar poder falhar, e a forma como falha, está na origem do ataque por oráculo de “padding” que vimos anteriormente no modo CBC.

Os ataques IND-CCA1 e IND-CCA2, globalmente designados apenas por IND-CCA (“indistinguisable under chosen ciphertext attack”), dão ao atacante a capacidade tentar decifrar alguns criptogramas criteriosamente escolhidos.

Um ataque IND-CCA tem a forma do ataque IND-CPA com as seguintes alterações.


    - Os algoritmos $$\,\mathcal{E}\,$$e $$\,\mathcal{D}\,$$, tal como no ataque IND-CPA, têm acesso ao oráculo de cifra $$\,G(k)\,$$ com um número de consultas polinomialmente limitado com o tamanho do “inputs”.
    - No ataque IND-CCA1 o algoritmo $$\,\mathcal{E}\,$$ tem também acesso ao oráculo $$\,\mathcal{H}(k)\,$$.
    - No ataque IND-CCA2 tanto o algoritmo $$\,\mathcal{E}\,$$ como o algoritmo $$\,\mathcal{D}\,$$ têm acesso ao oráculo $$\,\mathcal{H}(k)\,$$.
    
# Permutações

Permutações são a componente fundamental de qualquer cifra ou função de “hash”. Vimos, por exemplo, como as arquitecturas dos “hashs” criptográfico, que nos modelos de Maerkle-Damgärd como no modelos “Sponge”, dependia crucialmente de um número de permutações.

No sentido criptico, uma **permutação de** $$\,b\,$$ **bits** é uma função injetiva 
                                        $$\,f\,\colon\,\{0,1\}^b\,\to\,\{0,1\}^b\,$$
Dado que o domínio é finito, a função também é subjetiva.

As propriedades das permutações, e das primitivas que elas integram, depende da estrutura algébrica associada ao domínio $$\,D \,\equiv\,\{0,1\}^b\,$$. Na sua forma mais simples $$\,D\,$$ é um espaço vetorial em que a soma $$\,\oplus\,$$ implementa o  $$\,\mathtt{xor}\,$$ bit-a-bit de dois argumentos. Com esta  operação binária, $$\,D\,$$ é um **grupo aditivo**.

A permutação é **linear** quando, para todos $$\,x,y\in D\,$$ se verifica 

                                        $$f(x \oplus y)\,=\,f(x) \oplus f(y)$$

A permutação é **afim**  quando existe uma constante  $$\,c\in D\,$$ tal que, para todos  $$\,x,y\in D\,$$ 

                                        $$f(x \oplus y)\,=\,c \oplus f(x) \oplus f(y)$$

A permutação é **não-linear** se não for afim.

Uma permutação pode também usar outras operações algébricas, nomeadamente


    - **operações vetoriais booleanas:**  operações booleanas e aritméticas que actuam ao nível dos blocos; por exemplo
        - conetivas booleanas $$\,\land\;,\;\lor\;,\;\neg\,$$ aplicadas  bit-a-bit de cada palavra,
        - operação “shift-rotate”   $$\;x\,\mapsto\,x \ll k\;$$  e $$\;x\mapsto x\gg k\;$$ para cada $$k=0..b$$.
        - operação de soma $$\,+\,$$ e multiplicação aritmética $$\,\times\,$$ executadas módulo $$\,2^b\,$$ e  interpretando cada bloco como  um inteiro positivo na gama $$\,0.. 2^b-1\,$$.
        
    - **operações booleanas** $$\,\oplus\;,\;\land\;,\;\lor\;,\;\neg\,$$  actuando sobre os bits individuais de cada bloco.


    - **operações algébricas num corpo finito** $$\,\mathsf{GF}(2^b)\,$$
        O domínio dos bits $$\,\{0,1\}\,$$ pode ser equipado com a estrutura algébrica de um corpo em que a soma  $$\,+\,$$ é identificada com o $$\,\mathtt{xor}\,$$ e a multiplicação $$\,\ast\,$$é identificada com $$\,\mathtt{and}$$ .
        Tal corpo representa-se por  $$\,\mathsf{GF}(2)\,$$: *corpo de Galois* com 2 elementos.
        
        Generalizando, o domínio $$\,\{0,1\}^b\,$$ pode-se identificar com um *corpo de Galois* com $$2^b$$ elementos, representado por $$\,\mathsf{GF}(2^b)\,$$,  da seguinte forma:
        - Cada vetor $$\,x\in\{0,1\}^b\,$$ é identificado com um polinómio univariável de grau inferior a $$\,b\,$$ e coeficientes em $$\mathsf{GF}(2)$$
                                            $$X \;\equiv\; x_1 + x_2*z + \cdots + x_b*z^{b-1}$$
        - É escolhido, para módulo $$\,g(z)\,$$, um polinómio sobre $$\,\mathsf{GF}(2)$$ irredutível e de grau $$\,b\,$$.
        - As operações soma e multiplicação no corpo $$\,\mathsf{GF}(2^b)\,$$ são somas e multiplicações de polinómias executadas com módulo $$\,g(z)\,$$.


| **Exemplo**<br>Na cifra AES existe uma permutação que interpreta bytes como elementos do corpo $$\,\mathsf{GF}(2^8)\,$$. O módulo usada é o polinómio $$\,g(z)\,\equiv\,1+z + z^3 + z^4 + z^8\,$$. A soma e multiplicação de bytes são executadas com a soma e multiplicação de polinómios executadas módulo $$\,g(z)\,$$. |



## Formas de permutações

Um **permutação vetorial booleana** , sobre blocos de tamanho $$\,r\times b$$ , é um circuito $$\,r\times\,r\,$$ em que as “gates” implementam as operações vetoriais booleanas sobre palavras de tamanho $$\,b\,$$ e os “wires”  têm tamanho $$\,b\,$$.
 

| **Exemplo**<br>A cifra ChaCha20 baseia-se num gerador pseudo-aleatório em que a “round function” actua sobre um estado $$\,S\,$$ com 512 bits. O estado $$\,S\,$$ está organizado em 16 blocos de 32 bits dispostos numa matriz $$4\times 4$$ como se indica na figura seguinte.<br>A permutação aqui descrita, designada por “quarter-round” atua sobre 4 palavras de cada vez: uma vez como linhas outras vezes como colunas. Usa os operadores $$\mathtt{XAR}$$; isto é, $$\mathtt{xor}$$ , soma aritmética módulo $$2^{32}\,$$ e rotações.<br><br>Em cada “round” a permutação $$\,\mathsf{QR}\,$$ é aplicada às diversas colunas, com uma rotação em cada aplicação, seguida de uma aplicação às linhas, também com uma rotação em cada aplicação. O “round” é repetido 10 vezes. <br><br><br><br>![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1615980668322_ChaCha20.png) |


Uma **permutação booleana** , definida com operações booleanas, é um circuito $$\,b\times b\,$$ em que as “gates” são descritas por conectivas booleanas e os “wires” têm 1 bit de tamanho.


| **Exemplo**<br>A cifra/hash SKINNY é um dos candidatos ao concurso para standartização de “lightweight cryptography” , organizado pelo NIST, e que decorre atualmente. Usa uma permutação não-linear orientada ao bit que actua sobre bytes. A descrição dessa permutação por um circuito booleano $$\,8\times 8\,$$está ilustrado na figura seguinte.<br><br><br>![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1615983080785_Skinny.png) |

 
Um **permutação algébrica** sobre bytes  ****é definida sobre o corpo de Galois $$\,\mathsf{GF}(2^8)$$; é descrita por um polinómio univarariável  com coeficientes nesse corpo.

| **Exemplo**<br>A permutação sobre bytes que ocorre no AES, é definida pelo polinómio<br><br>                                       $$S(X)\;\equiv\; \alpha_0\,+\,\alpha_1\ast X^{254}\,$$<br><br>em que os coeficientes  $$\,\alpha_0,\alpha_1\,$$ são bytes vistos como  elementos de $$\,\mathsf{GF}(2^8)\,$$. |

Uma permutação algébrica, que actua sobre blocos genéricos de $$\,b\,$$ bits, pode ser descrita de várias formas. Como exemplo paradigmático considere-se o caso típico  $$\,b=128\,$$ que é um valor usual em várias cifras (incluindo o AES) e funções de “hash”.

A representação algébrica mais direta do domínio
                                                                    $$\,\mathsf{bloco}\,\equiv\,\{0,1\}^{128}\,$$ 
será a de um espaço vetorial de dimensão 128 cujos elementos pertencem a $$\,\mathsf{GF}(2)$$,              

                                                      $$\,\mathsf{bloco}\,\cong\,\mathsf{GF}(2^{})^{128}\,$$ 

As operações algébricas neste domínio serão as da álgebra matricial sobre o corpo $$\mathsf{GF}(2)$$: somas de vetores ou matrizes $$\,+\,$$ e multiplicação de matrizes $$\,\ast\,$$.

Um outro extremo, numa representação puramente polinomial, pode-se usar o corpo finito $$\,\mathsf{GF}(2^{128})\,$$; os elementos deste corpo são polinómios de grau inferior a 128  cujos coeficientes são elementos de $$\,\mathsf{GF}(2)\,$$.  Temos

                                                      $$\,\mathsf{bloco}\,\cong\,\mathsf{GF}(2^{128})\,$$ 

 As operações algébricas neste domínio são as operações no corpo: soma e multiplicação módulo um polinómio irredutível de grau 128.

Temos ainda representações intermédias que partem do fracionamento do bloco em vários sub-blocos. Por exemplo é  frequentemente fracionar um bloco de 128 bits  em 16 bytes. Desta forma pode-se interpretar o domínio $$\,\mathsf{bloco}\,$$ como um espaço vetorial de dimensão 16 cujos elementos pertencem a $$\,\mathsf{GF}(2^8)\,$$.                                                       

                                                     $$\,\mathsf{bloco}\,\cong\,\mathsf{GF}(2^{8})^{16}\,$$ 

As operações algébricas neste domínio são uma vez mais as da álgebra matricial mas agora efectuadas sobre o corpo $$\,\mathsf{GF}(2^8)\,$$ que descreve bytes.

Finalmente os vetores anteriores podem ser visto como vetores de coeficientes de polinómios de grau inferior a 16 ; portanto estes polinómios têm coeficientes em $$\,\mathsf{GF}(2^8)\,$$; temos assim um corpo
                                                                   $$\,\mathsf{GF}((\mathsf{GF}^8)^{16})\,$$
Como os coeficientes também são representados por polinómios, acabamos por ter  um representante de $$\,\mathsf{bloco}\,$$ que é um polinómio a 2 variáveis: a variável usada em $$\,\mathsf{GF}(2^8)\,$$ e a variável usada em $$\,\mathsf{GF}((\mathsf{GF}^8)^{16})\,$$. Uma vez mais, as operações aqui são a soma e multiplicação destes polinómios módulo um polinómio irredutível de grau 16.

| **Exemplo**<br>Um exemplo de um elemento de $$\,\mathsf{GF}((\mathsf{GF}^8)^{16})\,$$ será<br>                                            $$(z^7+1) + (z^5+z^3)* w^2 + (z^4+z^2+1)*w^{15}$$<br>um polinómio de grau $$15$$ na variável $$\,w\,$$ cujos coeficientes são polinómios de grau inferior a $$8$$  na variável $$\,z\,$$. |


**Circuitos de Feistel**
Frequentemente é difícil construir uma permutação  $$\,f\,\colon\,\{0,1\}^b\,\to\,\{0,1\}^b\,$$ que seja não-linear , fácil de construir e cuja inversa $$\,f^{-1}\,$$   seja  também fácil de construir.  Uma solução para esta questão são as funções realizadas por um modelo  designado por **circuito de Feistel**. 

Seja $$\,g\,\colon\, \{0,1\}^{b/2}\,\to\,\{0,1\}^{b/2}\,$$ uma função não-linear , fácil de construir mas não necessariamente invertível. A seguinte figura ilustra uma função $$\,f\,$$ nas condições requeridas.

![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1616022254299_Feistel.png)


    
    A figura ilustra também como $$\,f\,$$ e $$\,f^{-1}\,$$ se constroem, ambos, a partir de $$\,g\,$$.



## Para que servem as permutações?

Permutações lineares (ou afins) e permutações não-lineares têm papéis distintos na construção de primitivas criptográficas.

Permutações lineares e afins atuam sobre grandes blocos. Nas cifras estas permutações actuam sobre blocos de 128, 256 e 512 bits. Nas funções de “hash” atuam sobre blocos ainda maiores; por exemplo, o algoritmo Keccack , usado na família  SHA-3, atua sobre blocos de 1600 bits.

Nas permutações não-lineares raramente o tamanho de bloco ultrapassa os 8 bits; existem mesmo permutações sobre 5, 4 e 3 bits. 

A razão desta diferença está na complexidade de construção e na eficiência da execução. Por isso, o ChaCha20 , que usa operações não-lineares $$\,\mathtt{XAR}\,$$ que muitos processadores executam diretamente, permite construir permutações não-lineares com blocos de 32 e mesmo 64 bits.

Com algumas poucas exceções, e por motivos de eficiência, as permutações não-lineares são construídas por “**substitution boxes”**  ou “**S-boxes”.** 
Se o tamanho do bloco for $$\, b\,$$, a “S-box” é uma memória com $$\,2^b\,$$ células de tamanho $$b\,$$.

![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1615984966719_S-Box.png)


O argumento $$x$$ da permutação é visto como um endereço da memória; o valor $$\,f(x)\,$$ é visto como o conteúdo da célula de memória endereçada por $$x$$.
O tempo de execução da permutação é apenas o tempo de acesso à memória. 

Em contrapartida é necessário reservar o espaço para essa memória. Por exemplo, $$\,b=8\,$$ exige uma memória com 256 bytes; porém $$\,b=16\,$$ já requer  128 Kbytes o que é, quase sempre, impraticável.

Nos anos 40, Claude Shannon identificou, com propriedades de **diffusion** e **confusion** como as propriedades fundamentais de um cifra segura. 
Originalmente, quando apresentou estes conceitos, definiu “diffusion” como a garantia de um “flip” de um só “bit” à entrada deve repercutir-se em cerca de metade dos “bits” da saída.  Definiu  “confusion” como a exigência de que  cada “bit” do criptograma depender de vários segmentos da chave da cifra ofuscando a relação entre os dois.

Na terminologia contemporânea, “confusion”  é generalizada para a noção de **mixing.** Aplica-se a uma função $$\,f\,$$ que tem por argumentos  “strings”  do mesmo tamanho $$\,x,y\,$$ e  produz um resultado $$\,z\equiv f(x,y)\,$$. A função tem *boas propriedades de mistura* quando, estatisticamente, qualquer “bit” de $$\,z\,$$ depende igualmente de qualquer segmento de $$x$$ e de $$y$$.

Nas primitivas atuais, quase sempre,  a mistura realiza-se com uma função da forma

                                 $$f(x,y)\;\equiv\; \mathsf{S}(x\oplus y)$$

sendo $$\,\mathsf{S}\,$$ uma permutação não-linear. A permutação tem por missão ofuscar o efeito que, isoladamente, cada um dos argumentos tem no resultado final. Este é o principal papel reservado às permutações não-lineares.


## Propriedades das permutações lineares e afins.

Ao invés, permutações lineares ou afins estão orientadas à difusão. A forma como são descritas vai depender da representação algébrica escolhida para o bloco $$\,\{0,1\}^b\,$$.

Por exemplo, usando a representação vectorial $$\,\mathsf{GF}(2)^b\,$$, toda a permutação linear $$\,f\,$$ é completamente descrita por uma matriz invertível $$\,F\in \mathsf{GF}(2)^{b\times b}$$. A aplicação da permutação calcula-se por multiplicação matricial

                                             $$f(x)\;=\;x * F$$

Uma permutação afim tem uma descrição semelhante, somando uma constante $$\,a\neq 0\,$$ à multiplicação matricial

                                             $$f(x)\;=\;a + x * F$$

Numa representação puramente polinomial do bloco, usando $$\,\mathsf{GF}(2^b)\,$$, permutações afins são descritas por polinómios do 1º grau

                                        $$f(X) \;\equiv\,a_0 + a_1*X$$

em que os coeficientes $$\,a_0,a_1\,$$ são elementos do corpo e $$\,a_1\neq 0\,$$. Quando $$\,a_0=0\,$$ a permutação é linear.

A forma como são construídas as permutações lineares e afins pode seguir diretamente a descrição algébrica e efectuar multiplicações matriciais; porém normalmente é muito mais eficiente usar outro tipo de construções como $$\mathtt{xor}$$’s, rotações e negações. Todas estas operações são afins e a sua execução é muito mais eficiente do que a multiplicação matricial.

Para avaliar as suas capacidade de **difusão**, seguindo a definição inicial de Shannon,

> Um”flip” de um bit no input deve provocar um “flip” de metade dos bits no “output”

Partimos da noção de *peso de Hamming: p*ara uma “string”  $$\,x\,$$ , de tamanho fixo $$\,b\,$$, o seu **peso de Hamming** é o número de posições onde o bloco não tem o valor zero.
                                                            $$\mathsf{w}(x) \;\equiv\,\#\{i\,|\, x_i \neq 0\,\}$$

Para uma permutação  qualquer $$\,f\,$$ , sobre $$b$$-blocos, a propriedade de difusão pode-se ser caracterizada pela matriz   $$\,\mathbf{D}(f)\,$$ , designada **matriz difusão** de $$\,f\,$$,  calculada como


                          $$\mathbf{D}(f)_{i,j}\;\equiv\; \mathbb{P}[\,\mathsf{w}(f(x))=i\;|\;\mathsf{w}(x)=j\;,\;x \gets \{0,1\}^b\,]\quad$$com $$\quad i,j=0..b$$
            

Isto é, a probabilidade , com $$\,x\,$$ aleatoriamente gerado no domínio $$\,\{0,1\}^b\,$$,  de no “output” $$\,f(x)\,$$ existirem $$\,i\,$$ posições com o valor $$\,1\,$$ sabendo que no “input” $$\,x\,$$ existem $$\,j\,$$ posições com valor $$\,1\,$$.

No caso em que $$\,f\,$$é uma permutação linear a matriz $$\,\mathbf{D}(f)\,$$ pode-se estimar facilmente a partir do critério de Shannon: isto é considerando apenas o caso em que $$\,\mathsf{w}(x) = 1$$.

Isto porque uma tal permutação é sempre representada por uma matriz   $$\,F\in \mathsf{GF}(2)^{b\times b}\,$$ e um “flip” de mais do que um “bit” pode ser sempre descrito por uma soma de “inputs” cada um dos quais com apenas um bit igual a $$1$$.


| **Nota**<br>Recorde-se que a distribuição binomial<br>                                          $$\,\mathtt{binomial}(n,k,p)\,\equiv\,\binom{n}{k}\,p^k\,(1-p)^{n-k}$$<br>fornece a probabilidade de  em $$\,n\,$$experiências independentes , com probabilidade de sucesso $$\,p\,$$ , exatamente  $$\,k\,$$ terem sucesso.<br><br>A distribuição binomial tem média $$\,\mu\,=\,n\,p\,$$  e variância  $$\,\sigma^2\,=\,n\,p\,(p-1)\,$$.<br><br>Por esse motivo, se $$\,x\,$$ é aleatoriamente gerado no domínio $$\,\{0,1\}^b\,$$ , então $$\,p=1/2\,$$ e assim<br>                                       $$\mathbb{P}[\,\mathsf{w}(x) = i\;|\;x \gets \{0,1\}^b]\;=\;\binom{b}i\,2^{-b}$$<br>                                       <br>A média e desvio padrão desta distribuição de probabilidade são, respetivamente,  $$\,\mu = b/2\,$$   e  $$\sigma = \sqrt{b}/2$$. |


Vamos supor agora que a matriz  $$\,F$$$$\,$$ é aleatoriamente gerada. 
Nomeadamente cada coluna da matriz é um vetor cujo peso de Hamming tem a distribuição de probabilidade atrás descrita: tem valor médio $$\,\mu=b/2\,$$ e desvio padrão $$\,\sigma=\sqrt{b}/2$$ .

Dado que      $$f(x)\;\equiv\; x\ast F$$ , e seguindo a definição de Shannon para difusão, precisamos  considerar um vetor “input”   $$\,x\,$$   que que tenha apenas uma componente igual a $$1\,$$. 

Então a multiplicação $$\,x\ast F\,$$ seleciona a coluna cuja posição em $$\,F\,$$coincide com a posição em $$x$$ do valor  $$1$$.

Todas as colunas de $$F$$ têm pesos de Hamming com a mesma distribuição probabilística: a que vimos na nota anterior. Por isso $$\,\mathsf{w}(f(x))\,$$, apesar não ter garantidamente, o valor $$\,b/2\,$$ que Shannon requeria, tem-o   como  expectável e tem o desvio padrão $$\sqrt{b}/2$$.

Este processo ilustra como se pode analisar as propriedades de difusão de qualquer permutação linear $$\,f\,$$ que actue sobre “grandes” blocos.

    1. Em primeiro lugar é preciso determinar a matriz $$\,F\in \mathsf{GF}(2)^{b\times b}\,$$ que descreve $$\,f\,$$
    2. Em seguida, determina-se a distribuição probabilística associada  ao peso de Hamming de cada uma das colunas de $$\,F\,$$ 
    3. Um “input” com um único bit igual a 1 seleciona a coluna na respetiva posição e o “output” da permutação coincide com essa coluna.


# Segurança de permutações não-lineares

Uma permutação $$\,f\,$$  não linear sobre blocos de tamanho $$\,b\,$$ tem, por objetivo, “misturar” um par de inputs $$\,x,w\,$$ através de uma construção da forma 

                                                     $$\,f(x\oplus w)$$     

numa descrição vetorial, ou da forma 
                                                              $$f(x + w)\,$$
numa descrição algébrica. No que se segue vamos escolher a descrição algébrica mas os conceitos que iremos apresentar aplicam-se igualmente à descrição vetorial.

Segundo Shannon, uma boa mistura  ocorre quando,  todo o bit do resultado depende igualmente de $$\,w\;\text{e de}\;x\,$$. Esta é uma definição aparentemente simples mas que pode ser formalizada de forma muito diversa.

Uma abordagem frequente consiste em interpretar $$\,w\,$$ como uma “preturbação” de $$\,x\,$$ e  analisar a diferença entre os resultados de $$\,f\,$$ aplicados ao argumento não perturbado $$\,x\,$$ e o argumento perturbado $$\,x+w\,$$. Isto é, considerar a diferença


                                              $$\delta_f(x,w) \;\equiv\; f(x+w) + f(x)$$
                    

Esta abordagem designa-se por **análise diferencial**.


| Note-se que<br>                                                      $$\delta_f(x,w)\,=\,\delta_f(x+w,w)$$<br>Por isso, para cada $$\,w\neq 0\,$$e $$\,z\neq 0\,$$ então o número de blocos $$\,x\,$$ que verificam $$\,\delta_f(x,w)=z\,$$ é sempre par. |

Vamos considerar uma 1ª hipótese onde se considera $$\,f\,$$ como linear. Atendendo à definição de permutação linear

                                       $$\forall \,x,w\;\centerdot\;f(x+w) \,=\,f(x)\,+\,f(w)\,$$

O que é equivalente à afirmação de que, para todo $$\,x,w\,$$se verifica

                                                  $$\delta_f(x,w) \,=\,f(w)\,$$

Portanto, para $$\,f\,$$ linear, a diferença $$\,\delta_f(x,w)\,$$ não depende $$x$$: depende apenas da perturbação $$\,w\,$$. Neste caso não se pode considerar que exista uma boa mistura dos efeitos de $$\,x\,$$e de $$\,w\,$$no resultado já que este não depende de $$\,x\,$$.

Portanto, na perspetiva das diferenças, uma permutação linear não produz qualquer mistura.

Este exemplo sugere um critério para analisar “boa mistura” em termos de diferenças.  Para cada diferença de resultados possível $$\,z\,$$ e cada possível perturbação $$\,w\,$$, conta-se o número de diferentes valores de $$\,x\,$$ perturbados com $$w$$ dão origem a uma diferença $$w$$. Define-se


                                 $$\Delta_f(z,w)\;\equiv\;\#\{\,x\;|\; \delta_f(x,w) = z\,\}$$

Quando $$\,f\,$$ é linear, tem-se
                       $$\Delta_f(z,w)\;=\;\left\{\begin{array}{lcl} 2^b & \text{se} & z = f(w)\\ 0 & \text{se} & z\neq f(w)\end{array}\right.$$

Uma indicação de boa “mistura” ocorre quando o total  dos $$\,2^b\,$$ possíveis valores de $$\,x\,$$ estão igualmente distribuídos por todas as diferenças possíveis. Isto é quando ocorre


                                         $$\,\max_{z\neq 0,w\neq 0}\,\Delta_f(z,w)\,\,=\,2$$ 

Uma permutação que verifica esta condição designa-se por **”almost perfect non-linear”** (APNL) e são essas permutações que produzem, em relação às diferenças, a melhor mistura.

Se $$\,f\,$$ é uma permutação linear para blocos de tamanho pequeno (por exemplo, uma S-Box com  $$b=8$$) é simples computar $$\,\Delta_f\,$$ como uma matriz. A análise dessa matriz permite decidir se essa permutação está perto de ser uma APNL e assim fornecer o grau optimo de mistura.


## “Confusion-Diffusion Permutations”

“Confusion-Diffusion Permutation” (CDP’s) e “Substitution Permutation Networks”  (SPN’s) estão na origem de uma parte considerável das modernas cifras simétricas.  As alternativas a estes modelos são quase só as cifras que originam em funções de “hash” da classe “sponge”.

Uma CDP é uma permutação que, actuando sobre grandes blocos, alia a “boa mistura” de uma permutação não-linear com a “boa difusão” de uma permutação linear ou afim.

Como o bloco da permutação tem um tamanho $$\,b\,$$que  não permite construir permutações APNL com esta dimensão, o bloco tem de ser dividido em $$\,n\,$$  sub-blocos mais pequenos, de  tal forma que o tamanho $$\,b/n\,$$ seja adequado a construir S-Boxes com boa mistura (idealmente APNL’s).



![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1616329651502_CDP.png)


A componente de “mistura/confusion” é formada por $$\,n\,$$ S-Boxes que actuam sobre sub-blocos distintos de tamanho $$\,b/n\,$$. Na cifra AES, por exemplo, o bloco de 128 bits é dividido em 16 sub-blocos de 8 bits.
A camada de difusão tem por finalidade distribuir os efeitos individuais de cada S-Box por todo o bloco do “output”.

Existem muitas e variadas formas de construir difusão atendendo à eficiência computacional das operações e ao nível de proximidade com o ideal de difusão de Shannon. Independente da forma, no final cada permutação linear vai ser representada por uma matriz e são as propriedades dessas matriz que vão caracterizar a qualidade da difusão.

Uma CDP construída com uma única camada não-linear seguida por uma única camada afim é normalmente implementada com uma única execução em cada ronda.

Este é o tipo de modelo usado, por exemplo, no Rinjdael e em todas as candidaturas apresentadas ao concurso NIST-AES (Novembro 2001). Não é porém o modelo usado pela maioria das candidaturas ao concurso mais recente NIST-LWC (em curso) e em cifras como o ChaCha20 standard do IETF  (RFC 7539, Maio 2015).

A aplicação de S-Boxes é uma operação pesada; a sua aplicação a todos os sub-blocos pode colocar uma carga  excessiva no processamento. Também a aplicação uma única vez da difusão exige permutações afins bastante complexas.

Nos últimos anos têm aparecido propostas em que as apenas alguns dos sub-blocos são afetados pelas S-Boxes e os restantes sub-blocos passam diretamente para a camada de difusão.

Também a camada de difusão é bastante simplificada. Tipicamente envolvem apenas algumas rotações de sub-blocos e/ou rotações de bits em palavras formadas por vários sub-blocos.

Em contrapartida esta permutação simplificada é executada em várias rondas.  Neste modelo  a mistura e a difusão aparecem intercaladas  e espalhadas por várias rondas.
A camada de difusão “espalha” os sub-blocos que não são afetados por S-Boxes num única ronda por outros sub-blocos que nas próximas rondas vão ser afetados por S-Boxes. A difusão faz com que cada sub-bloco do input inicial vá ser afectado por uma S-Box em alguma ronda do CDP.




![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1616361857732_CDP-1.png)




## “Substitution Permutation Networks”

“Substitution Permutation Nestworks” é uma arquitetura de cifras simétricas muito popular. Aparece tanto nas cifras mais clássicas do concurso NIST-AES como em muitas das candidaturas no concurso NIST-LWC.

Essencialmente uma SPN é um encadeamento de rondas formadas por CDP’s intercaladas com a adição de chaves. Pode ser representado pelo diagrama seguinte.


![](https://paper-attachments.dropbox.com/s_985FFBF4196A6C677B9241C19444AF749E1B40A310E0BB9024F75DE97540F7B0_1616365096060_SPN.png)


  
Num modelo com $$\,n\,$$ rondas tem-se

    1. Um PRG, controlado pela chave mestra da cifra $$\,\kappa\,$$, gera $$\,n+1\,$$ “chaves de ronda”.
    2. A ronda de ordem $$\,i\,$$ , com $$i=1..n\,$$, tem o “input” adicionado com a chave $$\,k_{i-1}\,$$ e o “output” adicionado com a chave $$\,k_i\,$$
    3. Frequentemente todos os CDP’s são permutações iguais. Muitas vezes a última CDP é uma exceção à norma. 
        Ainda ocorrem SPN que usam CDP’s distintas nas várias rondas; esta solução é ineficiente principalmente nas implementações em “hardware” porque exige mais do que um circuito para implementar os CPD’s.


# Cifras assimétricas


## Segurança

A segurança das cifras assimétricas, ou de chave pública, é ditada por duas características essenciais:

    1. Qualquer atacante pode cifrar qualquer mensagem.
    2. Qualquer criptograma só deve ser decifrável por quem conheça a chave privada.


> Na análise destas cifras pode-se ignorar completamente o papel das chaves se se considerar que o que é público é o algoritmo de cifra $$\,E\,$$ e o que é privado é o algoritmo de decifra $$\,D\,$$.

Uma cifra assimétrica só pode ser correta e segura quando verifica:


    - **Condição de unicidade do criptograma**
        O acto de cifrar é executado por um algoritmo probabilístico $$\,E\,$$ tal que:
        - da mesma mensagem e em experiências sucessivas, $$E\,$$gera quase sempre diferentes criptogramas, 
                    $$\forall\, x\,\centerdot\quad\mathbb{P}[\,y = y'\,|\,y \gets E(x)\,,\,y'\gets E(x)\,]\; \simeq\; 0$$
            O número de criptogramas distintos, para a mesma mensagem $$\,x\,$$ deve ser de ordem igual ou superior a $$\,2^{|E|}\,$$.
            
        - a  partir de duas mensagens diferentes,  $$\,E\,$$  gera sempre  criptogramas distintos.
                    $$\forall\, x\neq x'\,\centerdot\quad\mathbb{P}[\,y = y'\,|\,y \gets E(x)\,,\,y'\gets E(x')\,]\; =\; 0$$
            
    - **Condição de correção**
        O acto de decifrar é  executado por um algoritmo parcial e determinístico; o algoritmo de decifrar, aplicado a uma “string”  $$\,y\,$$,  falha se $$\,y\,$$ não for criptograma de alguma mensagem; em caso contrário o algoritmo devolve a única mensagem da qual $$\,y\,$$ é criptograma.
        
                                      $$y \gets E(x)\quad\text{sse}\quad D(y)\simeq x$$

 


![](https://paper-attachments.dropbox.com/s_015CB3ECB2B4BB92494D5D827DEC325D4251DBF130E58A2A1142C9248927F4B3_1616515786743_assimetricas.png)


Apesar de existirem cifras assimétricas definidas por algoritmos determinísticos (ex. o RSA) o  seu uso seguro exige que o s seus algoritmos de cifra e decifra sejam embebidos num esquema probabilíssimo; por exemplo, o OAE (“optimal assymetrical encryption”).

De facto é simples construir um ataque IND-CPA que tem sucesso em qualquer cifra assimétrica determinística. 


| **IND-CPA de uma cifra assmétrica determinística**<br>Considere-se uma cifra assimétrica definida por dois algoritmos determinísticos $$\,E,D\,$$. O algoritmo $$E$$ é total e público; nomeadamente está acessível ao adversário $$\mathsf{Adv}$$. O algoritmo $$D$$ é parcial e privado: só é acessível ao agente “challendger” $$\,\mathsf{Ch}\,$$.<br><br>Como $$\,E\,$$ é determinístico e público tanto o algoritmo de escolha $$\,\mathcal{E}\,$$ como o algoritmo de decisão não têm necessidade  de consultar qualquer oráculo de cifra: toda a informação que tal oráculo poderia fornecer já está no conhecimento de $$E$$.<br><br>Recorde-se que o ataque  $$\,\text{\textsf{IND-CPA}}(\mathcal{E},\mathcal{D})\,$$é o gerador<br>                       $$\vartheta\,n\,\centerdot\,\vartheta\,m_0,m_1\gets\mathcal{E}(n)\,\centerdot\,\vartheta\,d\gets\{0,1\}\,\centerdot\,\vartheta\,c\gets E(m_d)\,\centerdot\,\mathcal{D}(m_0,m_1,c)$$<br>Neste caso, qualquer que seja o algoritmo de escolha,  é muito simples construir um algoritmo de decisão que tem elevada probabilidade de terminar em sucesso.<br>                                               $$\mathcal{D}(m_0,m_1,c)\,\equiv\,\vartheta\,c_0\gets E(m_0)\,,\,c_1\gets E(m_1)\,\centerdot\,\mathsf{if}\;(c = c_0) \lor (c=c_1)\;\mathsf{then}\;\text{sucesso}\;\mathsf{else}\;\text{erro}$$<br><br>Sendo  $$E$$  determinístico,  gerar $$\,c_0\gets E(m_0)\,$$ ou $$\,c_1\gets E(m_1)\,$$ , duas ou mais vezes,  produz sempre o mesmo par de resultados. Sendo $$\,c \gets E(m_d)\,$$, então um desses resultados tem de coincidir com $$\,c\,$$.<br><br>Se $$\,E\,$$ for probabilísto, mesmo que seja público,  então o gerador $$\,\vartheta\,c\gets E(m_d)\,\centerdot\,\vartheta\,c'\gets E(m_d)\,\centerdot\, c = c'$$ , produz  o resultado $$\mathsf{False}$$ com elevada  probabilidade. |



## KEM’s (“key encapsulation mechanisms”)

As cifras assimétricas dão origem a diferentes variantes: técnicas criptográficas com objetivos diferentes dos das cifras mas com construções análogas. Duas dessas técnicas são particularmente importantes: os “key encapsulation mechanisms” (KEM’s) e os algoritmos “key-establishment” (KE). 
Os últimos são essencialmente formas particulares de protocolos de acordo de chaves. 
Nesta terminologia os algoritmos das cifras assimétricas são classificados como  “public-key encryption” (PKE).

Uma característica marcante de todas as técnicas criptográficas assimétricas é a sua elevada complexidade computacional quando comparada, por exemplo, com a das técnicas simétricas com objetivos similares.

Por isso, para combinar as vantagens de ambas as famílias de técnicas, a ofuscação de grandes volumes de dados requer sempre o uso de dois mecanismos: um DEM (“data encapsulation mechanism”), no essencial uma cifra simétrica que actua sobre os dados a ofuscar, e um KEM (“key encapsulation mechanism”); isto é, uma técnica assimétrica que gera, comunica e ofusca a chave privada requerida pelo DEM.

Tal como o nome sugere, um KEM é um algoritmo vocacionado  ofuscar (**encapsular**) pequenas quantidades de informação, “chaves”, que ele próprio gera. 

Concretamente o KEM pode ser idealizado como um gerador aleatório que, em cada experiência,   produz um par de resultados:  um elemento privado, a chave usada pelo DEM, e um elemento público, o encapsulamento dessa chave.
                                                        $$\,(e,k) \,\gets\,\mathsf{KEM}\,$$
Associado ao KEM existe um algoritmo de **revelação** ou KRev (“key revelation”), que a partir do encapsulamento de uma chave, *revela* essa chave. 
Naturalmente, por analogia com as cifras assimétricas, o KEM é um algoritmo  público, total e probabilístico,  enquanto que o KRev é um algoritmo privado, parcial e determinístico.

A **condição de correção** será
                                            $$(e,k)\,\gets\,\mathsf{KEM}\quad\;\text{sse}\;\quad \mathsf{KRev}(e)\,\simeq\, k$$

                           $$$$

Como em qualquer esquema assimétrico, um esquema KEM é determinado por um gerador aleatório (idealmente) que produz tanto o KEM como KRev. Concretamente, o algoritmo $$\,\mathsf{KeyGen}_\lambda\,$$é público e probabilístico e, a partir de um parâmetro de segurança $$\,\lambda\,$$, gera um par de chaves pública e privada $$\,(\mathsf{pk}\,,\,\mathsf{sk})\,$$ ; tais chaves concretizam, respetivamente, o algoritmo público $$\,\mathsf{KEM}_{\mathsf{pk}}\,$$e o algoritmo privado $$\,\mathsf{KRev}_\mathsf{sk}\,$$.

A configuração global de um PKE (esquema de cifra assimétrica) , construído por uma associação genérica KEM $$\,+\,$$DEM , pode ser sumariada no seguinte diagrama. A negro representam-se as entidades, algoritmos e canais, públicos enquanto que a vermelho estão identificadas as entidades privadas.



![PKE genérico KEM+DEM](https://paper-attachments.dropbox.com/s_015CB3ECB2B4BB92494D5D827DEC325D4251DBF130E58A2A1142C9248927F4B3_1616788658235_Canvas+1.png)


Em particular, quando o KEM é combinado com um DEM de segurança perfeita como o “one time pad” (OTP), obtém-se o esquema



![PKE standard KEM + OTP](https://paper-attachments.dropbox.com/s_015CB3ECB2B4BB92494D5D827DEC325D4251DBF130E58A2A1142C9248927F4B3_1616788711736_Canvas+2.png)


A formalização da segurança de um KEM é descrita pela formalização de segurança do PKE standard KEM+OTP.   Este esquema pode-se descrever pelo par de algoritmos


                            $$\left\{\begin{array}{lcl}E(x) & \equiv & \vartheta\,(e,k)\gets\mathsf{KEM}()\,\centerdot\,(e\,,\,k\oplus x) \\ D((e\,,\,c)) & \equiv & \vartheta\,k \gets \mathsf{KRev}(e)\,\centerdot\,k\oplus c\end{array}\right.$$

Para que este esquema de cifra seja IND-CPA seguro  é suficiente que o algoritmo $$\mathsf{KEM}$$ seja suficientemente aleatório; nomeadamente é necessário que o número de pares $$(e,k)\,$$ que gera seja de ordem igual ou superior a $$\,2^\lambda\,$$ (recorde-se que $$\lambda$$ é o parâmetro de segurança).

Normalmente a construção de um esquema de cifra que seja IND-CCA seguro é algo mais complicado. No entanto existe um mecanismo, designado por **transformação de Fujisaki-Okamoto (FOT)**, que permite (dentro de um contexto bastante lato) converter um esquema PKE com segurança IND-CPA  num esquema PKE com segurança IND-CCA.


## Fujisaki-Okamoto
| Documentação sobre este tipo de técnica, a sua definição e a sua evolução, pode ser obtida em na diretoria `Docs>FujisakiOkamoto` [na área da disciplina](https://www.dropbox.com/sh/qyakq1vm9gnvytf/AAA3mLthztBUnzYbZbTUBWKUa?dl=0) do `DropBox`. |

**Transformar um  PKE-IND-CPA em um PKE-IND-CCA**

Seja $$\,(E,D)\,$$ um par de algoritmos que determina um esquema de cifra assimétrica (PKE) com segurança IND-CPA.  Como vimos

    - $$\,E\,$$ tem de ser  público, total e probabilíssimo; o número de criptogramas distintos deve ser igual ou superior a $$\,2^\lambda\;\text{com}\; \lambda\simeq{|E|}$$.
    - $$D\,$$ tem de ser privado, parcial e determinístico.

Adicionalmente vamos supor que é possível decompor $$\,E\,$$ num gerador aleatório $$\,h\,$$ de tamanho $$\,\lambda\,$$ e um núcleo determinístico $$$$$$\,f\,$$. Isto é, tem-se


                                              $$E(x)\;\equiv\;\vartheta\,r\gets h\,\centerdot\, f(x,r)$$

Neste caso 

    - A condição de correção  obriga a que
                                             $$\,\forall\,x,r\,\centerdot\, D(f(x,r)) \simeq x$$
    - As condições de unicidade do criptograma obrigam a que
        - Se $$\,x\neq x'\,$$ então $$\quad\forall\,r,r'\,\centerdot\,f(x,r)\neq f(x',r')$$
        - Para cada $$\;x\;$$, a função $$\;r\mapsto f(x,r)\;$$é uma função de “hash” segura; nomeadamente é unidirecional para 1ª e 2ª pré-imagens e resistente a colisões.
----------

A transformação FO original constrói um novo esquema de cifra assimétrica $$\,(E',D')\,$$ , usando um novo “hash” aleatório $$\,g\,$$ de tamanho igual ao da mensagem $$\,x\,$$.

O algoritmo de cifra é


              $$E'(x)\;\equiv\;\vartheta\,r\gets h\,\centerdot\,\vartheta\,y \gets x\oplus g(r)\,\centerdot\,\vartheta\,c\gets f(r,h(r\,\|\,y))\,\centerdot\,(y\,,\,c)$$
                            

As características essenciais deste algoritmo de cifra são

    1. O parâmetro $$\,r\,$$ , que na cifra original introduz a  aleatoriedade, é nesta cifra transformado de duas formas diferentes
        1. Em primeiro ligar, via o “hash” $$\,g\,$$, é usado para construir uma ofuscação $$\,y\,$$ da mensagem original.
        2. Em segundo lugar, $$\,r\,$$ é misturado com $$\,y\,$$ para construir uma nova fonte de aleatoriedade $$\,h(r\,\|\,y)\,$$ e, com essa aleatoriedade, cifra-se o próprio $$\,r\,$$como no algoritmo de cifra assimétrica original; obtém-se um novo criptograma $$\,c\,$$.
    b. O par formado por estes dois criptogramas parciais $$\,(y\,,\,c)\,$$ é o resultado da nova cifra.
    

O objetivo destas transformações da cifra original é construir um um algoritmo de decifra  $$\,D'\,$$  que permita recuperar a mensagem $$\,x\,$$ mas também verificar a autenticidade do criptograma.

O algoritmo $$\,D'\,$$ rejeita o criptograma se detecta algum sinal de fraude. 


            $$D'(y,c)\;\equiv\;\vartheta\,r \gets D(c)\,\centerdot\,\mathsf{if}\;\;c\neq f(r,h(r\|y))\;\;\mathsf{then}\;\;\bot\;\mathsf{else}\;\;y\oplus g(r)$$
| De certo modo o algoritmo de cifra $$\,E'\,$$ é uma forma de cifra com autenticação: no criptograma $$\,(y\,,\,c)\,$$ a 1ª componente faz o papel de “ciphertext” e a 2ª componente faz o papel de “tag” para autenticação.<br><br>Note-se que o “tag”  $$\,c\,$$ contém informação sobre $$\,r\,$$ e sobre a ofuscação $$\,y\,$$ da mensagem $$\,x\,$$. Qualquer ataque que tente modificar a componente $$\,y\,$$ ou criar um $$$$ $$\,r\,$$ fraudulente , vai afectar o valor deste “tag”. |


**Transformação de um KEM-IND-CPA em um PKE-IND-CCA**

A FOT pode ser aplicada diretamente a um KEM. Para isso é necessário que se possa decompor o KEM num “hash” aleatório $$\,h\,$$ e um “hash” seguro $$\,f\,$$ de tal modo que 

        - $$\mathsf{KEM}\;\equiv\; \vartheta\,r\gets h\,\centerdot\,f(r)$$
        - $$\forall\,r\;\centerdot\;\;(e,k) = f(r)\quad\;\text{sse}\;\quad\mathsf{KRev}(e)\simeq k$$

A transformação é análoga à anterior: constrói um esquema assimétrico $$\,E',D'\,$$  através de

     $$E'(x)\;\equiv\;\vartheta\,r \gets h\,\centerdot\,\vartheta\,y \gets x\oplus g(r)\,\centerdot\, (e,k) \gets f(y\|r)\,\centerdot\,\vartheta\,c\gets k\oplus r\,\centerdot\,(y, e, c)$$
     
Como anteriormente o criptograma é formado pela ofuscação da mensagem $$\,y\,$$, pelo encapsulamento da chave $$\,e\,$$ e por uma ofuscação da chave  $$\,c\,$$.

O algorimo de decifrar será

      $$D'(y,e,c) \;\equiv\;\vartheta\,k \gets \mathsf{KREv}(e)\,\centerdot\,\vartheta\,r \gets c \oplus k\,\centerdot\,\mathsf{if}\;\;(e,k)\neq f(y\|r) \;\;\mathsf{then}\;\;\bot\;\;\mathsf{else}\;\;y \oplus g(r)$$



