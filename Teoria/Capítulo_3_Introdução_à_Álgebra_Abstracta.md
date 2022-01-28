# Capítulo 3:  Introdução à Álgebra Abstracta

| Notebooks [aqui](https://www.dropbox.com/sh/6d59qy8uxhylckb/AAB5Yq6eFX4Z-XuhMmNfn8Fja?dl=0) |


Vimos que para criar técnicas criptográficas de ***baixo*** *******conteúdo algébrico*** apenas são necessárias algumas operações simples sobre *strings* de bits: funções de *hash*, cifras simétricas, partilha de segredos, computação cooperativa e sigma protocolos, são exemplos de técnicas que, em grande medida, podem ser concretizadas com operações booleanas básicas, AND  e XOR, e com concatenação de *strings*.

Porém o **poder expressivo** deste conjunto de operações é muito limitado para a maioria das aplicações criptográficas; essencialmente por dois tipos de razões:

1. Por falta de **eficiência descritiva:** a descrição de informação apenas com *strings* de bits é muito menos eficiente do que, por exemplo, uma descrição aritmética.
2. Por necessidade de caracterizar **problemas difíceis**. 

Um a das crenças fundacionais da segurança criptográfica é a existência de problemas da aritmética que não poder ser resolvidos com “recursos computacionais razoáveis”. Um **ataque** a uma técnica criptográfica é muitas vezes  reduzido  a uma solução de um desses problemas; a imunidade da técnica ao ataque baseia-se na crença de que “o problema não pode ser resolvido”.

Por isso sempre existiu, nomeadamente após o aparecimento de ataques quânticos, uma forte motivação para a criação de problemas aritméticos cada vez mais difíceis. Esta motivação tem vindo a gerar, para a criptografia, estruturas algébricas cada vez mais complexas onde esses problemas podem ser definidos.

Nomeadamente a concretização de técnicas de chave pública (a.k.a técnicas assimétricas) requer, com raríssimas exceções, uma formalização derivada da Teoria dos Números e, de forma mais geral, da Álgebra Abstrata. 


Uma **álgebra** $$\,\mathcal{A}\,$$ é definida num domínio $$\,A\,$$ por **operadores;** isto é,  *constantes* $$\,a\in A^k\,$$, *relações* $$\,r \subseteq A^k\,$$ e funções$$\,f\colon A^k \to A\,$$; o inteiro positivo  $$k$$ depende do operador e designa-se por **aridade** do mesmo.

As estruturas criptográficas  impõem algumas restrições a esse modelo genérico:

    1. O domínio $$A$$ é contável e  pode-se identificar com um subconjunto de $$\mathbb{N}$$.
    2. A álgebra é aritmética no sentido em que contém o par aditivo $$(+,0)$$, o par multiplicativo $$(\times,1)\,$$ ou, pelo menos, um destes pares.
    3. Os operadores verificam um conjunto de axiomas *standard*. Por exemplo:
        1.  a menos que seja dito em contrário, somas e multiplicações são comutativas, associativas e têm elemento neutro ($$0$$ ou $$1$$ respetivamente),
        2. Multiplicações são distributivas em relação às somas.



## Grupos

Um grupo é um semi-grupo $$\,\mathcal{G} \equiv(G,\mathbin{\square},e)\,$$ onde cada elemento tem **inversa;** isto é, para cada $$\,x\in G\,$$, existe $$\,x'\in G\,$$ tal que $$\,x \mathbin{\square} x' = e\,$$.

Um **sub-grupo**  $$\,\mathcal{G}'\subseteq \mathcal{G}\,$$ é definido por um sub-conjunto $$\,$$$$\,G'\subseteq G\,$$ que contém $$\,e\,$$, e é fechado por inversa e operação de grupo $$\,\square\,$$. Isto é, para todos $$\,x,y\in G'\,$$ , os inversos $$\,x',y'\,$$e o resultado$$\,x\mathbin{\,\square\,}y\,$$ são também elementos de $$\,G'\,$$.

Quando a função binária $$\,\mathbin{\square}\,$$ é associativa e comutativa o grupo diz-se **abeliano**.

| **Exemplos**<br><br>No domínio dos números naturais  $$\,\mathbb{N}\,$$, equipado com as habituais soma e multiplicação de naturais, não forma um grupo uma vez que nem a soma nem a multiplicação têm invers. No então, através das noções de relação e espaço quociente podem ser definidos  grupos no domínio $$\,D \equiv \mathbb{N}\times \mathbb{N}$$ ou $$\,D_+\equiv \mathbb{N}_+\times\mathbb{N}_+$$**.**<br><br>Por exemplo:<br><br>**1**<br>Pode-se definir soma no domínio $$\,D\,$$como  $$(a , b) + (a',b') \equiv (a+a',b+b')$$ ; $$\,(0,0)$$ é elemento neutro desta soma.<br><br>Considere-se a relação binária $$\sim$$ definida em $$D$$ por  $$(a,b) \sim (a',b')$$ sse $$a+b' = a'+b$$. Todo $$\,(a,a)\,$$é equivalente a $$\,(0,0)$$. Esta relação é uma relação de equivalência. Cada classe de equivalência é representada por um elemento $$(a,b)$$ escrito como $$(a-b)$$. A inversa do par $$(a, b)$$ é o par $$\,(b, a)\,$$. É fácil verificar o espaço formado pelas classes de equivalência, o espaço quociente $$D/\sim$$, é isomórfico com os inteiros $$\mathbb{Z}$$ e, por isso, forma um grupo aditivo. <br><br>**2**<br>Apesar de $$\,\mathbb{Z}\,$$ser um grupo aditivo não é multiplicativo porque os únicos inteiros com inversa multiplicativa em $$\,\mathbb{Z}\,$$ são $$\,1\,$$e $$\,-1\,$$. Para construir um grupo multiplicativo considere-se o domínio $$D_+$$ com multiplicação<br> $$\,(a, b) \times (a',b') \equiv (a\times a',b\times b')$$  e $$\, (1,1)\,$$ como elemento neutro. <br> <br> Define-se a relação binária $$\sim$$   por  $$(a,b) \sim (a',b')$$ sse $$\,a\times b' = a'\times b\,$$.  Esta relação também é uma relação de equivalência e o espaço das classes de equivalência em $$\,D_+/\sim\,$$ é  isomórfico com os racionais positivos não-nulos $$\,\mathbb{Q}_+$$.<br><br>De fato note-se que   $$\,a,b,a',b'\neq 0$$ e todo $$\,(a,a)\,$$é equivalente a $$\,(1,1)\,$$;   a inversa multiplicativa do par $$(a,b)$$ é o par $$(b,a)$$; por isso faz sentido representar $$\,(a, b)\,$$como a fração  $$\,a/b\,$$. |

Um outro grupo de números naturais merece uma referência especial devido à sua importância na História da Criptografia. É designado por **grupo simétrico** $$\,\mathcal{S}_n\,$$ e foi fundamental na criptoanálise da famosa máquina *Enigma* na 2ª guerra mundial.

Considere-se o domínio $$\,\mathbb{N}_n \equiv \{0,1,\cdots,n-1\}$$ formado pelos primeiros $$\,n\,$$naturais. 
O domínio $$\,{S}_n\,$$ é formado por todas as permutações (i.e. bijeções) $$\,\pi,\sigma \;\colon\; \mathbb{N}_n\to \mathbb{N}_n$$.  
A operação binária, vista como uma multiplicação, é a composição de permutações, $$\,\pi\circ\sigma$$ (ou,  $$\,\sigma\,\pi\,$$) e o elemento neutro é a permutação identidade, representada por $$\,\text{id}\,$$. 
A inversa de $$\,\pi\,$$ é a função inversa $$\,\pi^{-1}\,$$que existe sempre porque $$\,\pi\,$$é, por definição, uma bijeção. O **grupo simétrico**  é então definido pelo triplo $$\,\mathcal{S}_n \equiv (S_n,\circ,\text{id})\,$$.

Na máquina Enigma cada rotor é representado por uma permutação e a transposição de um rotor para outro é descrito pela composição de permutações. 

O domínio $$S_n\,$$tem $$\,n!\,$$elementos que podem ser descritos de várias formas. Como exemplo vamos considerar $$\,S_6\,$$, o domínio das permutações dos primeiros $$6$$ números naturais. Pode-se ter:

        1. **vetores de permutação,** ex: $$\,\langle 1,0,5,3,2,4\rangle \,$$, são vetores de tamanho $$6$$, cujos elementos são naturais $$< 6$$ sem repetições. A permutação é dada pela função $$\pi\,$$em que $$\pi(i)$$ é o elemento do vetor na $$\,i$$-ésima posição.
        2. **matrizes de permutação**: são matrizes $$P \in \{0,1\}^{n\times n}$$ em que, cada linha e cada coluna existe contém uma única entrada com o valor $$1$$. Tem-se $$\,P_{i,j}=1$$ se e só se $$\,\pi(i) = j\,$$.
        3. **ciclos**, ex: $$\,(2,4,1)\,$$, são tuplos de tamanho $$\leq 6$$ que representam um rotação; neste exemplo, o elemento na posição $$2$$ move-se para a  posição $$4$$ deslocando o elemento nessa posição que se move para a posição $$1$$, deslocando o elemento nessa posição que se move para a posição $$2$$. Todos os restantes elementos não se deslocam. A identidade é o ciclo de tamanho zero $$\,(\ )\,$$.
        4. **transposições** $$\,\tau_i\,$$ denota uma troca de posição entre o elemento em $$\,i\,$$ com o elemento na posição seguinte $$\,i^+ \equiv (i+1)\bmod n$$.  É equivalente ao ciclo $$\,(i,i^+)\,$$.
     

 O grupo simétrico $$\,\mathcal{S}\,$$ não é comutativo (normalmente $$\,\pi\circ \sigma \neq \sigma \circ \pi$$) no entanto é finitamente gerado; de facto
 

> Todo o elemento $$\,\pi \in \mathcal{S}_n\,$$é factorizável como um produto formado pos  apenas dois elementos: a transposição $$\,(0,1)\,$$ e o ciclo máximo $$\,(0,1,2,\cdots,n-1)\,$$.


## Grupos Abelianos

Seja $$\,\mathcal{G} = (G,\mathbin{\square},e)\,$$ um qualquer grupo abeliano;   $$a'$$ denota o simétrico de um qualquer  $$a\in G$$. Vimos que $$\,\mathcal{G}\,$$é abeliano quando $$\,\square\,$$ é uma operação associativa e comutativa.

Em $$\,\mathcal{G}\,$$define-se sempre uma **multiplicação escalar.** 
                                                           ****$$\,\mathbb{Z}\times G \,\to\, G\,$$
definida, para um inteiro $$\,\ell\,$$ e um $$\,a\in G\,$$, como 
              $$\,\ell\,a \,=\,\left\{\begin{array}{lcr} e &\;\text{se}\;& \ell=0 \\ a \mathbin{\square} \cdots \mathbin{\square} a\quad (\ell\,\text{vezes}) &\;\text{se}\;& \ell > 0 \\ ((-\ell)\,a)' &\;\text{se}\;& \ell < 0  \end{array}\right.$$
              
Quando o grupo é multiplicativo é usual designar a multiplicação escalar por **exponenciação** e representa-la por $$\,a^{\ell}\,$$.

Um subgrupo de **torção**  $$\,\mathcal{C} \subseteq \mathcal{G}\;$$ é um grupo em que qualquer dos seus elementos $$\,a\in \mathcal{C}\,$$  tem **ordem finita;** isto é, existe um inteiro $$\,\ell > 0\,$$ tal que $$\,\ell\,a = e\,$$; o menor destes $$\ell$$’s é a **ordem** de $$\,a\,$$.


    - A **ordem** do grupo de torção $$\,\mathcal{G}\,$$ é o número dos seus elementos e é representado por $$\,\#\mathcal{G}\,$$.
    - Todos os sub-grupos $$\,\mathcal{G}'\subseteq \mathcal{G}\,$$ são também grupos de torção e a respetiva ordem $$\,\#\mathcal{G}'\,$$ é um divisor da ordem $$\,\#\mathcal{G}\,$$. 
    - Adicionalmente para todo o divisor $$\,d\,|\,\#\mathcal{G}\,$$ existe pelo menos um sub-grupo de ordem $$\,d\,$$.

O subgrupo é **cíclico** quando é de torção gerado por um só elemento; isto é, existe um elemento $$\,g\in \mathcal{C}\,$$, designado **gerador** ou **elemento primitivo** de $$\,\mathcal{C}\,$$, tal que todo $$\,a\in \mathcal{C}\,$$ pode ser escrito como $$\,a = \ell\,g\,$$ para algum inteiro $$\,\ell\,$$. 

Concretamente a função $$\,\ell \mapsto \ell\,g\,$$ determina um isomorfismo de grupos $$\,\mathbb{Z}_{\#\mathcal{G}}\,\to\,\mathcal{G}\,$$; o isomorfismo preserva a estrutura de grupos porque  $$\,0\,g\;=\;e\;$$ e, para todos os inteiros $$\,\ell,\mu\,$$

                                                  $$\,$$ $$\, (\ell + \mu)\,g \;=\;(\ell\,g)\mathbin{\,\square\,}(\mu\,g)$$

A função inversa desta multiplicação escalar, isto é a função que mapeia $$\,a\in G\,$$ no menor inteiro positivo $$\,\ell\,$$  tal que $$\,a \,=\,\ell\,g\,$$, designa-se por **logaritmo discreto** ($$\mathsf{DL}_g$$). Equivalentemente

                                          $$a\,=\,\ell\,g\quad\;\text{sse}\;\quad \ell = \mathsf{DL}_g(a)$$

O problema em que, dados $$\,a\,$$e $$\,g\,$$, se procura determinar $$\,\ell\,$$ designa-se por **problema do logaritmo discreto** ou **DLP** ( “discret log problem”).

----------

O subgrupo $$\,\mathcal{C}\,$$é **livre** quando é isomórfico com $$\,\mathbb{Z}\,$$: quando existe $$\,a\in\mathcal{C}\,$$ tal que a transformação $$\,\mathbb{Z}\to G\,$$ definida por $$\,\ell \,\mapsto\, \ell\,a \;$$é injetiva.


> Todo o grupo abeliano finito $$\,\mathcal{G} = (G,\mathbin{\square},e)\,$$ é um grupo de torção e é a soma direta de um número finito de grupos cíclicos  $$\mathcal{G} \;\simeq \; \mathcal{G}_1 \oplus \mathcal{G}_2\oplus \cdots \oplus \mathcal{G}_m$$.

Concretamente isto significa que existem $$m$$ geradores, $$\,g_1,g_2,\cdots,g_m\,$$ , tais que qualquer $$\,a\in G\,$$pode ser escrito de forma única como uma combinação linear 

                                    $$\,a \;=\; \ell_1\,g_1 \mathbin{\,\square\,} \ell_2\,g_2 \mathbin{\,\square\,}\cdots \mathbin{\,\square\,} \ell_m\,g_m$$

com $$\,\ell_1,\ell_2,\cdots,\ell_n\in\mathbb{Z}\,$$. 

| Num grupo multiplicativo a combinação linear acima escreve-se:  $$\,a \,=\ g_1^{\ell_1}\times g_2^{\ell_2}\times \cdots\times g_m^{\ell_m}\,$$. |



# Anéis

Genéricamente um anel $$\,\mathcal{R}\equiv(R,+,0,\times,1)\,$$ é um grupo abeliano aditivo $$\,(R,+,0)\,$$ao qual se junta uma multiplicação associativa  $$\times\,$$com o seu elemento neutro $$\,1\,$$que é distributiva em relação a $$+$$.

A menos que seja um anel trivial (i.e. quando $$1 = 0$$) um anel nunca pode ser um grupo multiplicativo: existem elementos de $$\,R\,$$ que são invertíeis e outros que não o são. Os elementos invertíeis de $$\,{R}\,$$ designam-se por **unidades**; é simples verificar que o conjunto das unidades de $$R$$  define um grupo multiplicativo; usamos  $$\mathcal{R}^\ast$$ para representar esse grupo.

Cada anel $$\mathcal{R}$$ determina ainda os seguintes anéis:

    - O **anel de polinómios** $$\,\mathcal{R}[w]$$ numa variável $$\,w\,$$ e coeficientes em $$\,\mathcal{R}$$.
    - O **anel quociente** $$\,\mathcal{R}/\mathcal{I}\,$$ determinado por um **ideal** $$\,\mathcal{I}\,$$.
    - O **anel produto** $$\,\mathcal{R}\otimes \mathcal{S}\,$$ definido por um segundo anel $$\,\mathcal{S}\,$$.


| Um **ideal** $$\,\mathcal{I} \subseteq \mathcal{R}\,$$é um sub-espaço linear de $$\,\mathcal{R}\,$$ que é também um $$\mathcal{R}$$-módulo: isto é, se $$\,a\in \mathcal{I}\,$$ e $$\,u\in \mathcal{R}\,$$ , então  $$\,a\times u \in \mathcal{I}\,$$.<br><br>Se $$\,\mathcal{I},\mathcal{J}\in\mathcal{R}\,$$ são ideais então:<br><br>    - $$\mathcal{I}+\mathcal{J}\,$$é o ideal formado pelas somas $$\,a+b\,$$ com $$\,a\in\mathcal{I}\,$$ e $$\,b\in\mathcal{J}$$.<br>    - $$\mathcal{I}\times\mathcal{J}\,$$ (também $$\,\mathcal{I}\,\mathcal{J}\,$$) é o ideal formado pelas multiplicações $$\,a\times b\,$$ com $$\,a\in\mathcal{I}\,$$ e $$\,b\in\mathcal{J}$$; nomeadamente a definição de ideal implica $$\,\mathcal{I}\,\mathcal{R}\equiv \mathcal{I}$$.<br>    - $$\,u\,\mathcal{I}\,$$ é o ideal formado pelos  elementos $$\,a\times u\,$$ com $$\,a\in\mathcal{I}\,$$;  em particular $$\,a\,\mathcal{R}$$ é o ideal formado por todos os múltiplos de $$\,a\,$$e designa-se por **ideal principal** gerado por $$\,a\,$$.<br><br>Cada ideal $$\,\mathcal{I}\,$$ determina a relação de equivalência $$\,a\equiv b \pmod \mathcal{I}\,$$ sse $$\,a-b\in \mathcal{I}\,$$.  O espaço quociente $$\,\mathcal{R}/\mathcal{I}\,$$ é o anel cujo domínio é o espaço das classes de equivalência definidas pela relação$$\,{}\pmod \mathcal{I}\,$$.<br><br>A definição da relação de equivalência implica que, se  $$\,a \equiv a'\pmod \mathcal{I}\,$$ e  $$\,b\equiv b'\pmod \mathcal{I}\,$$, então $$\,(a + b) \equiv (a'+b')\pmod \mathcal{I}\,$$ e $$\,(a\times b) \equiv (a'\times b')\pmod\mathcal{I}\,$$.<br><br>Por isso as operações do anel podem ser definidas com: $$\,(a \bmod \mathcal{I})+(b\bmod\mathcal{I})\,=\,((a+b) \bmod \mathcal{I})$$e analogamente para a multiplicação. |

| O **anel produto**  $$\,\mathcal{}$$$$\,\mathcal{R}\otimes \mathcal{S}\,$$ tem um domínio formado por pares $$\,(a,b)\,$$, com $$\,a\in \mathcal{R}\,$$ e $$\,b\in\mathcal{S}\,$$.<br>As operações de soma e multiplicação são  feitas componente a componente. Isto é    $$\,(a,b) + (a',b')\;\equiv (a+a',b+b')\;$$ e   $$\,(a,b)\times (a',b')\;\equiv\; (a\times a',b \times b')$$.<br><br>Como exemplo, os racionais $$\,\mathbb{Q}\,$$ são definidos no anel $$\,\mathbb{Z}\otimes\mathbb{Z}\,$$pela relação de equivalência<br>                                                     $$\,(a, b) \sim (a',b') \quad \text{sse}\quad a\times b' = a'\times b$$ |

## Anéis Inteiros
| [Exemplos aqui](https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/integer_mod.html) |

Exemplos paradigmáticos de “anéis criptográficos” são os **anéis inteiros.** São anéis inteiros o anel $$\,\mathbb{Z}\,$$, o anel  $$\,\mathcal{R}[w]$$ dos polinómios a uma variável $$\,w\,$$com coeficientes num anel inteiro $$\,\mathcal{R}\,$$, o **anel quociente** $$\,\mathcal{R}/\mathcal{I}\,$$ em que $$\mathcal{R}\,$$é um anel inteiro e $$\,\mathcal{I}\subseteq \mathcal{R}\,$$  é um seu ideal, e o produto $$\,\mathcal{R}\otimes \mathcal{S}\,$$de anéis  inteiros.

O caso mais simples de anel quociente inteiro é  $$\,\mathbb{Z}_n \equiv \mathbb{Z}/n\mathbb{Z}\,$$ que usa diretamente o anel $$\,\mathbb{Z}\,$$ e o  ideal principal $$\,n\mathbb{Z}\,$$ (i.e. os múltiplos de $$n$$). 

Neste anéis a relação de equivalência é escrita como $$a\equiv b\bmod n\,$$.  Cada classe de equivalência é representada por um dos seus elementos escolhido de acordo com uma determinada regra; é usual escolher como representante o elemento da classe o inteiro$$\,x\,$$ que  verifica $$\,n > x \geq 0\,$$ ou, em alternativa, que verifica  $$\,n/2 \geq x > n/2 - n\,$$.


| Considere-se $$\,\mathbb{Z}_5\,$$; na 1ª hipótese os seus elementos são representados por inteiros no intervalo $$\,\{0,\cdots,4\}\,$$ e, na 2ª hipóteses, por inteiros no intervalo $$\,\{-2,\cdots,2\}\,$$. |

> Um inteiro $$0 < x < n\,$$ representa um elemento invertível de $$\,\mathbb{Z}_n\,$$ se e só se  $$\,\text{mdc}(x,n) = 1\,$$. Diz-se  (com um pouco de abuso de linguagem)  que  $$\,x \in \mathbb{Z}^\ast_n\,$$. 

Por essa razão, se $$\,n\,$$for primo, então todo o elemento de $$\,\mathbb{Z}_n\,$$  não nulo é invertível. Como veremos adiante um tal anel designa-se por **corpo**.

O número de elementos do grupo multiplicativo $$\,\mathbb{Z}_n^\ast\,$$representa-se por $$\,\phi(n)\,$$. A função  $$\,n \mapsto \phi(n)\,$$ designa-se por **função de Euler** e é uma das funções mais importantes da teoria dos números em geral e da criptografia em particular. 

Várias das  propriedades de $$\,\phi(\cdot)\,$$ são essenciais à “number theoretic cryptography”.   Resumimos algumas delas no seguinte quadro.


----------

**Propriedades da função de Euler** $$\,\phi\,$$


- $$\,\sum_{d|n}\,\phi(d)\,=\,n\,$$

     Este resultado diz-nos que, se tomarmos todos os divisores $$d$$ de $$n$$ e somarmos o número de elementos  invertíveis em todos os $$\,\mathbb{Z}_d\,$$, obtemos o número de elementos de $$\mathbb{Z}_n$$.
     

- A função $$\,\phi\,$$ é  **multiplicativa**; isto é, se $$\,\text{mdc}(m,n)=1\,$$, então $$\,\phi(m\times n) = \phi(m)\times \phi(n)\,$$.


- Se $$\,n\,$$é primo, então $$\,\phi(n^k) \,=\,n^{k-1}\times (n-1)\,$$.


- **Teorema de Fermat** (sec. XVII):  para todo o número primo $$n$$  e  para todo $$a\,\mathop{\equiv\!\!\!\!\!/}\, 0\bmod n\,$$ 

                  — verifica-se $$\,a^{k}\,=\,1$$ se e só se $$\,k\equiv 0 \bmod \phi(n)$$.
     

- **Teorema de Euler** (sec XVIII): para todo $$\,n>0\,$$ e para todo $$a\in\mathbb{Z}_n^\ast\,$$ 

                  — verifica-se $$\,a^{k}\,=\,1$$ se e só se $$\,k\equiv 0 \bmod \phi(n)$$.


- **Teorema RSA** (sec XX): para todo $$\,n>0\,$$ livre de quadrados (i.e. factorizável num produto de primos distintos) e para todo $$a\,\mathop{\equiv\!\!\!\!\!/}\, 0\bmod n\,$$

                  — verifica-se $$\,a^{k}\,=\,1$$ se e só se $$\,k\equiv 0 \bmod \phi(n)$$.


----------

Estes resultados ajudam-nos a perceber a estrutura do grupo multiplicativo $$\,\mathbb{Z}_n^\ast\,$$. Sabemos que tem $$\,\phi(n)\,$$elementos e uma questão fundamental é saber se é cíclico. 


> Quando  $$\,n=1,2,4$$ ou quando, para algum primo $$\,p>2\,$$ se tem $$\,n = p^d\,$$ ou  $$\,n=2\,p^d\,$$,  então  o grupo multiplicativo  $$\,\mathbb{Z}_n^\ast\,$$ é cíclico.

Nomeadamente o caso em que $$\,n=p\,$$ , com $$p$$ um grande primo, tem particular importância porque o grupo $$\,$$$$\,\mathbb{Z}_p^\ast\,$$ fornece a estrutura algébrica básica onde são definidas as técnicas criptográfica originais da família Diffie-Hellman.

Em qualquer dos casos, quer seja cíclico ou não, $$\,\mathbb{Z}_n^\ast\,$$é um grupo de torção e por isso pode-se aplicar o teorema fundamental da representação dos grupos de torção que vimos atrás.

Para isso vamos supor que é possível construir uma factorização da ordem do grupo

                        $$\quad n \;=\; n_1\times n_2\times\cdots \times n_m\quad$$

em que cada um dos $$n_i$$ tem a forma $$\,n_i = p_i^{d_i}\,$$ (com  $$p_i\,$$primos distintos); por convenção os $$\,p_i\,$$são apresentados de forma decrescente. Desta forma todos os $$\,Z_{n_i}^\ast\,$$ são cíclicos.

Esta fatorização indica-nos que existem sub-grupos $$\,\mathcal{G}_i \subseteq \mathbb{Z}_{n}^\ast\,$$ de ordem $$\,n_i\,$$ tais que $$\,$$$$\,\mathbb{Z}_n^\ast\,$$
se pode identificar com a soma direta destes sub-grupos. Concretamente, isto significa que existem geradores $$\,g_1,\cdots,g_m\,$$tais que qualquer unidade $$\,a\in\mathbb{Z_n^\ast}\,$$se pode escrever como uma combinação linear destes geradores. Isto é

                                              $$\,a \;=\; g_1^{\ell_1}\times g_2^{\ell_2}\times \cdots\times g_m^{\ell_m}$$                 para $$\,\ell_i\in \mathbb{Z}_{\phi(n_i)}$$


----------

**Exemplos**
No caso particular em que $$\,n = p^2\,$$ , sendo $$p>2$$  um primo, tem-se $$\,\phi(n) = p\times(p-1)\,$$. 
Os divisores primos de $$\,\phi(n)\,$$ inclui o próprio $$\,p\,$$ e divisores primos de $$\,(p-1)\,$$que são, obviamente, menores do que $$\,p\,$$.
Cada um desses divisores $$\,d\,$$ determina um sub-grupo de $$\,Z^\ast_{n}\,$$de ordem $$\,d\,$$. Nomeadamente o maior sub-grupo de $$\,\mathbb{Z}_{n}^\ast\,$$ de ordem prima tem ordem precisamente igual a $$\,p\,$$.

----------

**Algoritmo de Pohlig-Hellman**
Em criptografia é muito importante encontrar sub-grupos de ordem prima de um qualquer grupo cíclico  $$\,\mathcal{G} \equiv (G,+,0,g)\,$$.  Isto porque existe um algoritmo muito eficiente que permite reduzir o DLP  neste grupo ao mesmo problema mas nos sub-grupos de ordem prima de $$\,\mathcal{G}\,$$; como a ordem dos sub-grupos é, normalmente, muito menor do que a ordem do grupo original, o DLP nesses sub-grupos é  muito  menos complexo que o mesmo problema no grupo inicial.

| Sem perda de generalidade vamos considerar que o grupo é cíclico e aditivo. No entanto  os mesmos argumentos aplicam-se igualmente a quaisquer outros  grupos abelianos finitos. |


Seja $$\,n\,$$ a ordem do grupo $$\,\mathcal{G}$$ e, por simplicidade, vamos supor que $$\,n\,$$ factoriza em

                                   $$n\,=\,p\times q$$$$\,$$

em que $$\,p\,$$ é primo,  tem-se $$\,p > q\,$$ e tem-se  $$\,\gcd(p,q)\,=\,1$$. 

Vamos procurar resolver o DLP neste grupo.  Considere-se um elemento qualquer $$\,a\in\mathcal{G}\setminus 0\,$$  e vamos calcular $$\,\mathsf{DL}_g(a)$$:  i.e.  procurar  $$\,0 \leq \ell < n\,$$ tal que  $$\,a = \ell\,g\,$$.

Calcula-se $$\,a' \gets q\,a\,$$ e  $$\,g' \gets q\,g\,$$.
Note-se que o elemento  $$\,g'\,$$  tem ordem $$\,p\,$$ porque $$\,p\,g'\, = p\,(q\,g)\,=\,(p\times q)\,g \,=\,n\,g \,=\,0\,$$. 

Da  equação  $$\,a = \ell\,g\,$$ conclui-se 
                                                  $$\,a' \,=\,\ell\,g'$$
Este é um problema $$\mathsf{DL}_{g'}\,$$  num sub-grupo de  ordem  $$\,p < n\,$$. Se for possível resolver este  problema determina-se  um $$\,0 \leq \ell_p < p\,$$  tal que   

                            $$\ell \,\equiv\,\ell_p \bmod p$$

Se $$\,q\,$$ for primo, usa-se o mesmo  processo para encontrar  $$\,0\leq \ell_q< q\,$$ tal que
                                     $$\ell \,\equiv\, \ell_q\bmod q$$
Veremos, no próximo capítulo, que um resultado designado *Teorema Chinês dos Restos*  (CRT) permite resolver estas duas equações e determinar $$\,\ell\,$$.

Se $$\,q\,$$ não for primo aplica-se este mesmo algoritmo  substituindo $$\,n\,$$ por $$\,q\,$$, e  recursivamente determina—se também  $$\,\ell_q\,$$. Usa-se novamente o CRT , com este $$\,\ell_q\,$$ e com o $$\,\ell_p\,$$ determinado acima, para calcular $$\,\ell\,$$.

----------

A consequência  imediata da existência deste algoritmo é a constatação que a complexidade computacional do DLP , para um grupo de ordem $$\,n\,$$, é condicionado essencialmente pelo tamanho do maior factor primo de $$\,n\,$$.

Quando $$\,n\,$$ é primo, pode-se provar que, no pior caso, a complexidade do DLP nesse grupo  é  $$\,O(2^{|n|/2})\,$$.

----------
## Os criptosistemas assimétricos  RSA e DH

As técnicas RSA (“Rivest-Shamir-Adleman”) e DH (“Diffie-Hellman”) criaram essencialmente a criptografia de chave públicas. Na literatura surgiram quase em simultâneo, DH em 1976  e o RSA em 1978, numa década onde em grande medida nasceu toda a criptografia que se pode classificar como “contemporânea” ou “do dia-a-dia”. 

| Nessa mesma década apareceu também a cifra simétrica DES (“Data Encryption Standard”), e o processo de standartização da tecnologia criptográfica. <br>Toda esta dinâmica contribuiu para dar à criptografia o papel fundacional na confiança que os sistemas de informação modernos necessitam.<br>É interessante é que ambos os sistemas se baseiam em técnicas elementares de Teoria dos Números bem conhecidas, algumas, desde o século XVIII; isto sugere que poderiam ter sido criadas há muito mais tempo. |

As técnicas da **família RSA**, que incluem cifras assimétricas e esquemas de assinatura digital. Baseiam a sua segurança na complexidade computacional do problema da fatorização de números inteiros grandes e baseiam a sua correção nos teoremas Fermat/Euler/RSA.

Todas elas são construídas a partir dos mesmos passos:


1. Gerar aleatoriamente  dois primos $$\,p,q\,$$ grandes tais que a recuperação de um desses primos a partir do produto  $$\,p\times q\,$$ é difícil. $$\,$$
2. Definir o módulo $$\,n \,\equiv\,p\times q\,$$ e determinar $$\,\phi(n)\,=\,(p-1)\times(q-1)$$.
3. Gerar aleatoriamente inteiros $$\,s,r\in \mathbb{Z}^\ast_n\,$$ tais que $$\,s\times r \equiv 1 \bmod \phi(n)$$.

Pelo teorema RSA tem-se

> para todo inteiro $$\,0 < a < n\,$$ e todo inteiro $$\,b\,$$,
>              — verifica-se $$\,(a^{s\,r}) \equiv b \bmod n\,$$se e só se  $$\,b \equiv a \bmod n$$

Nas técnicas assimétricas da família RSA o módulo $$\,n\,$$é informação pública enquanto que  o valor $$\,\phi(n)\,$$ é informação privada. O conhecimento de $$\,\phi(n)\,$$é equivalente ao conhecimento dos factores primos de $$\,n\,$$.

| É simples verificar que, sendo $$\,n\,$$ público, o conhecimento de $$\,\phi(n)\,$$ é equivalente à factorização de $$\,n\,$$.  De facto, sendo conhecidos $$\,n\,$$e $$\,\phi(n)\,$$, é simples resolver o sistema de duas equações nas variáveis $$\,p,q\,$$<br>                          $$\left\{\begin{array}{rcl} n &=& p \times q  \\ \phi(n)&=& (p-1)\times(q-1)\end{array}\right.$$ |

Agora pode-se construir o seguinte esquema de cifra assimétrica:

    1. **KeyGen**
        1. Um agente que conheça $$\,n\,$$ pode gerar aleatoriamente e por tentativas um inteiro $$\,0< r < n\,$$ tal que $$\,\gcd(r,n) = 1\,$$. O valor $$\,r\,$$vai ser informação pública.
        2. Fornecendo $$\,r\,$$ a um agente que conheça $$\,\phi(n)\,$$ este, usando o algoritmo de Euclides, calcula $$\,s< n\,$$tal que $$\, s \equiv r^{-1}\bmod n\,$$. O valor $$\,s\,$$vai ser informação privada.
    2. **Encrypt** 
        Para cifrar o inteiro $$\,0<x<n\,$$, calcula-se o inteiro $$\,0<c < n\,$$    que verifica
                                                          $$\,c \equiv x^r\bmod n\,$$.
    3. **Decrypt** 
        Para decifrar $$\,0< c < n\,$$ calcula-se o inteiro $$\,0<y<n\,$$ que verifica 
                                                                   $$y \equiv c^s\bmod n$$
        
    **Correção:** 
        As condições deste esquema obrigam a que seja $$\,y \equiv x^{s\times r}\bmod n\,$$. O teorema RSA obriga a que seja $$\,y\,=\,x\,$$.
    **Segurança**: 
        Se, dados $$\,r\,$$ e $$\,n\,$$ fosse possível determinar $$\,s\,$$ tal que $$\,s\times r \equiv 1 \bmod \phi(n)\,$$, então seria possível determinar $$\,\phi(n)\,$$  que  seja um divisor de  $$\,(s\times r - 1)\,$$. 
    
----------

As técnicas da **família Diffie-Hellman** usam as propriedades de um grupo cíclico multiplicativo  $$\,\mathcal{G}\,\equiv\,\mathbb{Z}^\ast_p\,$$  em que  $$\,p\,$$ é  número primo grande (i.e.$$\,|p| \geq {1024}\,$$) e em que  se conhece  um elemento  primitivo $$\,g\in\mathcal{G}$$.

| A ordem desse grupo é $$\,n = p - 1\,$$ e para que o DLP seja  complexo não basta apenas que $$\,p\,$$ seja grande: é também necessário que o maior factor primo de $$\,(p-1)\,$$ seja também grande. <br>Para garantir estas condições o primo $$\,p\,$$ é gerado de uma determinada forma:<br><br>1. Gera-se um primo $$\,q\,$$ grande: com pelo menos  160 bits de tamanho; este vai ser o maior factor de $$\,(p-1)\,$$<br>2. Gera-se sucessivamente inteiros  $$\,p_i\;=\;q\,2^i + 1\,$$ até que $$\,p_i\,$$ seja  um primo suficientemente grande . |

A técnica DH original (publicada em 1976) é o *protocolo de acordo de chaves Diffie-Hellman,* designado normalmente por ***DH key exchange****.* O protocolo  envolve dois agentes $$\,A\,$$ e $$\,B\,$$ que executam exatamente as mesmas computações; na sua versão mais simples o protocolo é:


1. É gerado um primo $$\,p\,$$ grande tal que $$\,\phi(p)\,$$ tem um divisor primo $$\,q\,$$ grande. É gerado $$\,g\in\mathbb{Z}_p^\ast\,$$de ordem $$\,q\,$$. Os parâmetros $$\,p,q,g\,$$ são públicos.
2. São executados os seguintes passos
        1. $$\mathbf{A}\,: \vartheta\,a\gets \mathbb{Z}_q\,\centerdot\,\vartheta\,\beta_A\gets g^a \bmod p\,\centerdot\,\beta_A$$
        2. $$\mathbf{B}\,:\,\vartheta\,b\gets \mathbb{Z}_q\,\centerdot\,\vartheta\,\beta_B \gets g^b\bmod p\,\centerdot\,\beta_B$$
        3. $$\mathbf{A}\,:\,\kappa_A \gets (\beta_B)^a\bmod p$$
        4. $$\mathbf{B}\,:\,\kappa_B \gets (\beta_A)^b \bmod q$$
    No final tem-se $$\,\kappa_A\,=\,\kappa_B\,=\,g^{a\times b}\bmod q$$.

O protocolo DH key exchange pode facilmente ser convertido num KEM, designado por ***El Gamal***, 


1. **KeyGen** : 
        1. Parâmetros públicos  $$\,p,q,g\,$$ como no protocolo DH
        2. A chave privada é $$\,a\neq 0\in \mathbb{Z}_q\,$$ gerada aleatoriamente; 
        3. A chave pública é $$\,\beta \equiv  g^a\bmod p$$
2. **KEM**$$(\beta)$$ $$\equiv \vartheta \,r \gets \mathbb{Z}_q\!\setminus 0\,\centerdot\, \vartheta \,\mathsf{key}\gets \beta^r\bmod p\,\centerdot\, \vartheta\,\mathsf{enc}\gets g^r\bmod p\,\centerdot\,(\mathsf{key}\,,\,\mathsf{enc})$$$$\,$$
3. **KRev**$$(a,\mathsf{enc})\;\equiv\;\mathsf{enc}^a\bmod p$$


----------
## Raíz Quadrada Modular

Um **resíduo quadrado**  módulo $$\,n\,$$ é um inteiro  $$\,x\,$$ tal que $$\,x \equiv y^2\bmod n\,$$para algum inteiro $$\,y\,$$.  Nesse caso diz-se que $$\,y\,$$ é uma **raíz quadrada modular** de $$\,x\,$$.

Quando $$\,n\,$$ é um número primo as propriedades da raíz quadrada modular são semelhantes às da relação análoga nos  reais; nomeadamene todo $$\,x\neq 0\,$$ ou não tem qualquer raíz quadrada módulo $$\,n\,$$ ou e raizes quadradas distintas, $$\,y\neq y'\,$$,  verificam  $$\,y + y'\equiv 0 \bmod n$$.

De facto, 

> se $$\,n\,$$ é um inteiro primo ímpar, então exatamente metade dos inteiros  $$\,0<x < p\,$$  verifica
>   $$x^{(n-1)/2}\;\equiv\;1\mod n\;$$ e a outra metade verifica  $$\;x^{(n-1)/2}\equiv -1 \mod n\,$$. O primeiro grupo de inteiros forma precisamente os resíduos quadrados módulo $$\,n\,$$.


| **Raiz Quadrada módulo um primo ímpar** $$\,\mathbf{n}$$<br> <br>O inteiros $$\,x\,$$ tem raíz quadrada módulo $$\,n\,$$ se e só se   $$x^{(n-1)/2}\;\equiv\;1\mod n\;$$. Note-se que, pelo 1º teorema de Fermat,  $$\,x\equiv x^n\bmod n\,$$. Portanto<br>                                       $$x\,\equiv\,x^n \,\equiv\,x^{(n-1)/2}\times x^{(n+1)/2}\,\equiv\, x^{(n+1)/2}\mod n$$<br>A partir desta relação podem-se considerar vários casos<br><br><br>1. $$n \equiv 3 \bmod 4\,$$; isto é, $$(n+1)\,$$ é múltiplo de $$\,4\,$$. Neste caso define-se<br><br>                                                           $$y\,\equiv\,x^{(n+1)/4}\mod n$$<br>      Como $$\,y^2\,\equiv\,x^{(n+1)/2}\,\equiv\, x\mod n\,$$ , este valor $$\,y\,$$ é uma raíz quadrada de $$\,x\,$$<br>      <br><br>2. Como $$\,n+1\,$$é par , se não for múltiplo de  $$\,4\,$$, então verifica  $$\,n \equiv 1 \bmod 4\,$$. Neste caso restam duas hipóteses: $$\,n \equiv 1\bmod 8\;$$ou então $$\;n\equiv 5\bmod 8$$. Analisando individualmente cada um destes casos é possível encontrar eficientemente uma raíz quadrada. $$y$$<br><br>*Consultar a literatura para detalhes* |

A informação mais relevante no problema da raíz quadrada módulo $$\,n\,$$, quando $$\,n\,$$ é um inteiro primo, é a de que existem vários algoritmos de complexidade polinomial com o tamanho de $$\,n\,$$que determinam essas raízes quadradas. Adicionalmente cada $$\,x\neq 0\,$$ tem exatamente duas raízes quadradas módulo um primo $$\,n\,$$: se $$\,y\,$$ é uma destas raízes a outra será $$\,-y\bmod n$$.

Porém quando $$\,n\,$$ é um numero composto, nomeadamente quando $$\,n = p\times q\,$$ é o produto de dois primos (como nos criptosistemas RSA) o cálculo da raíz quadrada é , em termos de complexidade, equivalente ao problema da factorização de $$\,n\,$$. 

| De facto, se for conhecida a factorização $$\,n\,=\,p\times q\,$$,  então, usando o algoritmo anterior,  é possível determinar $$\,\pm y_p\bmod p\,$$e $$\,\pm y_q\bmod q\,$$ tais que<br><br>                                                  $$\,x \equiv y_p^2\bmod p\quad$$e $$\quad x \equiv y_q^2\bmod q$$<br><br>Apenas metade dos possíveis valores não-nulos de $$\,x\,$$têm raíz quadrada módulo $$\,p\,$$ e metade dessa metade tem raíz quadrada módulo $$\,q\,$$. Por isso têm raíz quadrada módulo $$\,n\,$$ cerca de $$1/4$$ dos valores possíveis de $$\,x\,$$.<br><br>Para cada um desses valores $$\,x\,$$, usando o **Teorema Chinês dos Restos**, determina-se $$\,y\,$$ tal que <br><br>                                                  $$y\,\equiv\,y_p\bmod n\quad\;$$e $$\;\quad y \equiv y_q\bmod n$$<br><br>e, portanto $$\,x \equiv y^2\bmod n$$.<br><br>Como existem dois possíveis valores de $$\,y_p\,$$e dois possíveis valores de $$\,y_q\,$$cada combinação destes valores produz uma raíz quadrada $$y$$: portanto, se $$\,x\,$$ tem alguma raíz quadrada, terá 4 raizes quadradas módulo $$\,n\,$$ distintas.<br><br><br>----------<br><br>Inversamente se for conhecido o valor de $$\,n=p\times q\,$$ (com $$p$$ e $$q$$ desconhecidos), se for conhecido um resíduo  quadrático $$\,x\,$$ módulo $$\,n\,$$ e duas das suas raízes quadradas $$\,y,z\,$$ tais que $$\,y\neq \pm z \bmod n\,$$, então é possível factorizar $$\,n\,$$ usando a **Factorização de Fermat**. <br><br>Tem-se  $$\,x\equiv y^2\equiv z^2\bmod n\,$$; isto  implica que $$\,y^2 - z^2\,=\,(y+z)\,(y-z)\,$$  é um múltiplo não nulo de $$\,n\,$$. Note-se que a condição imposta em $$\,y,z\,$$ força a que nenhum dos inteiros $$\,(y+z)\,$$ou $$\,(y-z)\,$$ seja múltiplo de $$\,n\,$$; portanto um destes valores é múltiplo de um dos primos $$\,p\,$$ e o outro é múltiplo do outro primo $$q$$.<br>Assim pode-se calcular estes primos através do cálculo de $$\,\gcd(n,y+z)\,$$ e $$\,\gcd(n,y-z)\,$$.<br><br><br>----------<br><br>A conclusão fundamental é então<br>*calcular raízes quadradas modulares para um módulo RSA  é equivalente ao problema da sua factorização* . |



A situação referida no quadro anterior pode ser generalizada de várias formas:


1. No caso em que $$\,n\,$$é livre de quadrados e factorizável em $$\,m\,$$ primos distintos, usando o mesmo argumento, que vimos no quadro anterior o número de valores de $$\,x\,$$ que têm raíz quadrada é $$\,\approx 2^{-m}\,n$$, mas cada um desses valores tem $$\,2^m\,$$ raízes quadradas distintas.


2. Se o grupo multiplicativo $$\,\mathbb{Z}_n^\ast\,$$ for cíclico, existe um relação directa as propriedades deste grupo e  a existência e cálculo da raíz quadrada  módulo $$\,n\,$$. 
    Nesse grupo considere-se um gerador primitivo $$\,g\,$$ e defina-se $$\,\upsilon = \mathsf{DL}_g(-1)\,$$; isto é,  $$\,g^\upsilon + 1 \equiv 0 \bmod n\,$$.


    1. Em primeiro lugar,  todo o  $$\,0 < x < n\,$$  que tenha raíz quadrada módulo $$\,n\,$$ ,  tem sempre inversa multiplicativa e, por isso, identifica-se com um elemento de $$\,\mathbb{Z}_n^\ast\,$$. 
    2. O inverso não é  verdadeiro: existem inteiros $$\,0< x < n\,$$que têm inversa multiplicativa mas não  têm raíz quadrada módulo $$\,n\,$$. 
    3. Tomemos um qualquer $$\,x\,$$ com inversa multiplicativa módulo $$\,n\,$$e seja $$\,\alpha =\mathsf{DL}_g(x)\,$$; então, $$\,x\,$$ é resíduo quadrático módulo $$\,n\,$$ se e só  existe uma solução $$\,\beta\,$$ para a  equação   
                                    $$2\,\beta \equiv \alpha \mod \phi(n)$$ 
        Se tal $$\,\beta\,$$ existir então são raízes quadradas de $$\,x\,$$ os inteiros $$\,y\,$$ que verifiquem 
                           $$y\,\equiv\,g^\beta\bmod n\qquad$$ou $$\qquad y\,\equiv\,g^{\beta + \upsilon}\bmod n$$


## “Principal Ideal Domais” (PID’s)

Um **domínio  integral**  é um anel $$\,\mathcal{R}\,$$ onde a multiplicação $$\,a\times b\,$$ de dois elementos não-nulos é sempre não-nula. Um **domínio ideal principal** (PID) é um domínio integral $$\,\mathcal{R}\,$$ onde todo o ideal  $$\mathcal{I}$$, não vazio,  é formado pelo múltiplos de algum elemento $$\,a\in \mathcal{R}$$ (isto é,  $$\,\mathcal{I}\equiv a\,\mathcal{R}\,$$).


> São PIDS’s o anel dos inteiros $$\,\mathbb{Z}\,$$, qualquer corpo $$\,K\,$$ e qualquer anel de polinómios a uma variável $$\,K[w]\,$$ com coeficientes num corpo.
> Não são PID’s os anéis  $$\,\mathbb{Z}[w]\,$$dos polinómios  inteiros ou $$\, K[w,z]\,$$dos polinómios a duas ou mais variáveis, mesmo que neste caso os coeficientes estejam num corpo.

Os PID’s são estruturas algébricas que partilham muitas das propriedades dos inteiros $$\mathbb{Z}$$ ; nomeadamente:

    1. Num PID existe a noção de **elemento irredutível** análoga à noção de inteiro primo. Um $$\,x\in \mathcal{R}\,$$é irredutível  se só é divisível por $$1$$ ou pelo proprio $$x$$. 
    2. Num PID existe a noção de **factorização por elementos irredutíveis**: qualquer $$\,x\in \mathcal{R}\,$$ ou é irredutível  ou então é um múltiplo de um elemento irredutível não trivial (um que seja divisor de qualquer elemento, i.e. $$1$$ ou $$-1$$).
    3. Adicionalmente, a factorização é única; a menos da ordem dos factores existe uma forma única de escrever $$\,x\,$$ como o produto dos seus divisores irredutíveis.
    4. Definindo uma ordem parcial nos elementos do anel $$\,\mathcal{R}\,,$$ existe a noção de **máximo divisor comum**   $$\,\text{mdc}(x,y)$$:  um factor máximo que ocorra tanto na factorização de $$x$$ como na factorização de $$y$$.

Quando $$\,x\,$$ é um elemento irredutível do PID $$\mathcal{R}$$, o ideal  $$\,x\mathcal{R}\,$$ por ele gerado também não pode ser  decomposto como o produto de outros ideais. Por esse motivo prova-se que 


> O espaço quociente $$\,\mathcal{R}/x\mathcal{R}\,$$ é um corpo.

Em seguida exploramos a noção de **corpo** fundamental em criptografia.


# Corpos

Corpos sáo anéis $$\,\mathcal{K} \,=\, (K,+,0,\times,1)\,$$em que todos os elementos, excepto $$0$$, são unidades.
Em criptografia são comuns os corpos de **característica** $$0$$ como os racionais $$\,\mathbb{Q}\,$$ e as suas extensão $$\,\mathbb{Q}(\beta)\,$$, designadas como **corpos de números**.

Porém os corpos mais comuns são os corpos com um número finito de elementos $$q$$, designados naturalmente como **corpos finitos (**ou corpos de **característica prima** ou **corpos de Galois)** e ****representados por ****$$\,\mathbb{F}_q$$.
                                       $$q = p^d$$

Um corpo cujo grupo aditivo é livre é um corpo de característica zero. O exemplo paradigmático é o corpo dos racionais $$\,\mathbb{Q}\,$$.

Outros corpos com as mesmas características são os **corpos de números algébricos (**ou simplesmente **corpos de números**). O corpo $$\,\mathbb{Q}(\beta)\,$$é definido como


> a menor extensão de $$\,\mathbb{Q}\,$$ que contém o número algébrico $$\,\beta\,$$.

Um **número algébrico** é uma raiz $$\,\beta\,$$ de um polinómio de coeficientes inteiros. O seu  **grau**,  $$\,\text{deg}(\beta)\,$$, é o menor grau de um polinómio não nulo $$f\in \mathbb{Z}[w]$$ que verifique $$\,f(\beta)\,=\,0\,$$. 

Seja $$d=\text{deg}(\beta)\,$$.
Os elemento de $$\,\mathbb{Q}(\beta)\,$$ identificam-se com os polinómios $$\,x\in \mathbb{Q}[\beta]\,$$de grau inferior a  $$d$$.
Isto significa que $$\,\mathbb{Q}(\beta)\,$$ é isomórfico com $$\,\mathbb{Q}^d$$.

| **Exemplo** <br>Como exemplo  de números algébricos considere-se dois polinómios em $$\mathbb{Z}[w]\,$$: o polinómio $$\,f \,\equiv\,(w^2 -2)\,$$<br>e o polinómio $$\,g\equiv (w^2+1)\,$$ ambos do 2º grau. <br><br>Uma das raízes de $$\,f\,$$ é normalmente designa por $$\,\sqrt{2}\,$$ enquanto que uma das raízes de $$\,g\,$$ é a unidade dos números complexos $$\,i\,$$. <br><br>Os elementos de $$\,\mathbb{Q}(\sqrt{2})\,$$ têm a forma genérica  $$\,a + b\,\sqrt{2}\,$$ com $$a,b\in\mathbb{Q}\,$$. Os elementos de $$\,\mathbb{Q}(i)\,$$têm a forma genérica  $$\,a + b\,i$$.<br><br>Se $$\text{deg}(\beta) = d\,$$, o elemento genérico de $$\mathbb{Q}(\beta)\,$$tem a forma $$\,a_1 + a_2\,\beta +\cdots+a_{d}\,\beta^{d-1}\,$$ com $$a_1,\cdots,a_d \in \mathbb{Q}$$. |


Os corpos mais comuns em criptografia são os corpos finito $$\mathbb{F}_q$$. 


> Existe o corpo finito $$\,\mathbb{F}_q\,$$ se e só se $$\,q = p^d\,$$ sendo  $$\,p\,$$ um primo designado por **característica** do corpo e $$\,d>0\,$$a sua **dimensão**.

Quando $$\,d=1\,$$o corpo $$\,\mathbb{F}_p\,$$ designa-se por **corpo primo**. 

A partir de um corpo primo $$\mathbb{F}_p$$ define-se o anel de polinómios univariáveis $$\mathcal{R}_p \equiv \mathbb{F}_p[w]\,$$. Como vimos anteriormente este anel é um PID: todos os seus ideais têm a forma $$\,\varphi\,\mathcal{R}_p\,$$ para algum polinómio $$\varphi\in\mathcal{R}_p$$.

Se $$\,\varphi\,$$ for irredutível  então (como em qualquer PID) o espaço quociente $$\,\mathcal{R}_p/\varphi\mathcal{R}_p\,$$ é um corpo.
Esta facto é explorado para definir uma representação para os corpos $$\,\mathbb{F}_q$$ nos casos em que $$\,q=p^d\,$$ e se tem  $$d>1$$.

Para tal escolhe-se  um polinómio irredutível    $$\varphi\in \mathcal{R}_p\,$$   de grau $$d$$, designado como **módulo do corpo,**  e define-se 
                                                       $$\,\mathbb{F}_{q}\;\equiv\; \mathcal{R}_p/\varphi\,\mathcal{R}_p\,$$
                                                       
Os elementos de $$\mathbb{F}_q\,$$ são representados por polinómios $$\,x\in \mathcal{R}_p\,$$ de grau menor do que $$d$$ ou, alternativamente, pelo seu vetor de coeficientes.



## Extensões de corpos

Sejam $$\,K\,$$e $$\,E\,$$ dois corpos tais que existe um homomorfismo de corpos $$\,h\,\colon\,K \to E\,$$.

| Um **homomorfismo de corpos** $$\,h \colon K \to E\,$$ mapeia somas de $$K$$ em somas de $$\,E\,$$<br>                                                    $$h(x + y) \,=\,h(x) + h(y)$$<br>e mapeia multiplicações de $$\,K\,$$ em multiplicações em $$\,E\,$$<br>                                                  $$h(x\times y)\,=\,h(x)\times h(y)$$<br>Mapeia também os elementos neutros de $$\,K\,$$ nos respetivos elementos neutros de $$\,E\,$$<br>                                                  $$h(0)\,=\,0\quad$$e $$\quad h(1)\,=\,1$$<br>Um tal homomorfismo é sempre injetivo: $$\,x\neq y\;\text{implica sempre}\;h(x)\neq h(y)$$. |

Nestas circunstâncias diz-se que $$\,E\,$$ é uma **extensão** de $$\,K\,$$e escreve-se $$\,E/K\,$$.  Se tal extensão existir então necessáriamente os corpos tem a mesma característica.


| **Exemplo**<br><br>O corpo dos reais $$\,\mathbb{R}\,$$ é uma extensão do corpo dos racionais $$\,\mathbb{Q}\,$$ e o corpo dos números complexos $$\,\mathbb{C}\,$$ é uma extensão do corpo $$\,\mathbb{R}\,$$. <br><br>No caso $$\,\mathbb{R}/\mathbb{Q}\,$$ o homomorfismo em causa traduz o facto de que todo o real é definido como o limite de uma sequência de números racionais; portanto um racional é mapeado no limite de uma sequência constante.<br><br>No caso $$\,\mathbb{C}/\mathbb{R}\,$$ o homomorfismo reflete o facto de que um número complexo é sempre um par de reais (as partes real e imaginária) e o homorfismo mapeia cada real $$\,x\,$$ num complexo $$\,x + \mathsf{i}\,0\,$$. |

Algumas situações particulares:


1. Um corpo de números  $$\,\mathbb{Q}(\beta)\,$$ é a menor extensão de $$\,\mathbb{Q}\,$$ que contém o número algébrico  $$\,\beta\,$$. Se $$\,n\,$$ é o grau do menor polinómio que tem $$\,\beta\,$$ como raíz (isto é: $$\,n=\deg(\beta)\,$$)  então verifica-se $$\,\mathbb{Q}(\beta)\,\simeq\,\mathbb{Q}^n\,$$ e diz-se que $$\,\mathbb{Q}(\beta)\,$$ é uma extensão de grau $$\,n\,$$ de $$\,\mathbb{Q}\,$$.


2. Seja $$\,K \,\equiv\,\mathbb{F}_p\,$$ o corpo finito primo de característica $$\,p\,$$.  
    Seja $$\,\phi \in K[x]\,$$ um polinómio irreditível de coeficientes em $$\,K\,$$ e grau $$\,n\,$$.  O corpo $$\,\mathbb{F}_{p^n}\,$$ é isomórfico com o corpo quociente $$\,K[x]/\phi(x)\,$$ e é também uma extensão de grau $$\,n\,$$ de $$\,K\,$$. 
    

Os exemplos anteriores podem ser generalizados nas noções de **extensão e fecho algébricos.**

Seja $$\,K\,$$ um qualquer corpo e $$\,L/K\,$$ uma qualquer extensão. Seja $$\,\beta\in L\,$$ uma raíz de algum polinómio $$\,\varphi\in K[x]\,$$; então $$\,K(\beta)\,$$ é a menor extensão de $$\,K\,$$ que contém $$\,\beta\,$$. 
Extensões construídas da forma $$\,K(\beta)\,$$, para algum $$\,\beta\,$$, designam-se por **extensões algébricas**.

O **grau** da extensão $$\,K(\beta)/K\,$$ é o grau $$\,n\,$$ do menor polinómio $$\,\varphi\in K[x]\,$$ do qual $$\,\beta\,$$é raíz.
Neste caso ,$$\,\varphi\,$$designa-se por  **polinómio mínimo** da extensão e  prova-se que

        - $$K(\beta)\,$$ é um espaço vetorial isomórfico com $$\,K^n\,$$
        - Se $$\,K\,$$ é  finito, então existe um isomorfismo de corpos  $$\,K(\beta) \simeq K[x]/\varphi(x)$$. 

O menor corpo $$\,L\,$$ que contém todas as raízes de todos os polinómios $$\,\varphi\in K[x]\,$$ designa-se por **fecho algébrico** de $$\,K\,$$ e representa-se por $$\,\overline{K}\,$$. 
Equivalentemente, o fecho algébrico de $$\,K\,$$ é o menor corpo que extende todas as extensões algébricas de $$\,K\,$$; isto é, para todo $$\,\beta\,$$ tem-se $$\;\overline{K} /K(\beta)\,$$.


| **Exemplo**<br>O corpo dos números complexos $$\,\mathbb{C}\,$$ é o fecho algébrico dos reais porque todo o polinómio de coeficientes reais tem todas as suas raízes nos corpo dos complexos.<br>O corpo $$\,\mathbb{R}\,$$ dos  números reais  não é o fecho algébrico dos racionais $$\,\mathbb{Q}\,$$  porque existem polinómios de coeficientes racionais cujas raízes não são números reais. Porém tais raízes são sempre números complexos e, por isso, $$\,\mathbb{C}\,$$ é também o fecho algébrico de $$\,\mathbb{Q}\,$$. |

## Representação em Corpos Finitos

**Automorfismos, Morfismo de Frobenius. Grupo de Galois**
Considere-s a extensão de corpos finitos  $$\,\mathbb{F}_q\,/\,\mathbb{F}_p\,$$, sendo $$\,p\,$$ um primo e $$\,q\equiv p^d\,$$ para algum $$d$$.
Nesse caso 


> Os elementos não nulos de do corpo $$\,\mathbb{F}_q\,$$ identificam-se com as soluções , no fecho algébrico  $$\,\overline{\mathbb{F}}_p\,$$, da equação
>                                                                         $$X^{q-1} \equiv 1$$ 

Automorfismos em $$\,\mathbb{F}_q\,$$ são funções $$\,\sigma\,\colon\,\mathbb{F}_q\,\to\,\mathbb{F}_q$$  que preservam as somas e multiplicações; tais funções são necessariamente injetivas. 
Um $$\,p$$-automorfismo de $$\,\mathbb{F}_q\,$$ é um automorfismo que **fixa** $$\,\mathbb{F}_p\,$$; isto é, para todo $$\,z\in\mathbb{F}_p\,$$, tem-se $$\,\sigma(z) = z$$.
Os $$\,p$$-automorfismos de $$\,\mathbb{F}_p\,$$, com a operação binária de composição de funções e a identidade como elemento neutro, formam um grupo cíclico de ordem $$d$$ que tem como gerador o morfismo

                                                                  $$\sigma\;\equiv\; x \;\mapsto\; x^p$$      

Este automorfismo designa-se por **morfismo de Frobenius** e o grupo $$\,\mathsf{Gal}(\mathbb{F}_q)\,$$ por ele gerado designa-se por **grupo de Galois**  da extensão ****$$\,\mathbb{F}_q\,/\,\mathbb{F}_p\,$$.


----------

**Traços e produto interno**

O morfismo de Frobenius $$\,\sigma\,\equiv\,x\mapsto x^p\,$$ pode ser usado para  definir funções  

                                                          $$g \,\colon\,\mathbb{F}_q\,\to\,\mathbb{F}_p\,$$ 

que, funcionalmente, são semelhantes a paridades: fornecem um representante de um elemento arbitrário do corpo maior $$\,\mathbb{F}_q\,$$ no corpo menor $$\,\mathbb{F}_p\,$$.

A função **traço** define-se como

                                $$\mathsf{tr}(x)\;\equiv\;\sum_{i=0}^{d-1}\,\sigma^i(x)\;=\;\sum_{i=0}^{d-1}\,x^{p^i}$$
                                

É simples demonstrar que $$\,\mathsf{tr}(x)\,$$ é  sempre um elemento  de $$\,\mathbb{F}_p$$ e que, para todo $$\,x\in \mathbb{F}_q\,$$ , tem-se 

    - $$\,\mathsf{tr}(x)=x\,$$ se e só se $$\,x\in\mathbb{F}_p\;$$,
    - para cada $$\,c\in\mathbb{F}_p\,$$ ,  $$\,\mathsf{tr}(c*x) \,=\,c*\mathsf{tr}(x)$$
    - a função traço $$\,\mathsf{tr}(\cdot)\,$$ preserva somas mas, a menos que restrita a $$\,\mathbb{F}_p\,$$, não preserva multiplicações. 

Com a ajuda dos traços é possível definir um **produto interno** no espaço vetorial $$\,\mathbb{F}_q\,$$ como

                                                              $$\langle\,x\centerdot y\,\rangle\;\equiv\;\mathsf{tr}(x\ast y)$$

Com esta noção de produto interno, como é usual em espaços vetoriais munidos desta estrutura, é simples representar cada elemento $$\,x\,$$ do espaço vetorial  $$\,\mathbb{F}_q\,$$ através das suas sucessivas projeções numa **base** do espaço.



----------

**Representação e Bases**

Numa extensão finita  $$\,\mathbb{F}_q\,/\,\mathbb{F}_p\,$$ de grau $$\,d\,$$,  cada elemento   $$\,x\in \mathbb{F}_q\,$$ pode ser representado
 por um vetor $$\,\vec{x}\,\in\,(\mathbb{F}_p)^d\,$$.  

Recorde-se que uma **base** de um espaço vetorial qualquer $$\,X\,$$ , sobre um corpo $$\,K\,$$ e de dimensão $$\,n\,$$,  é um conjunto de  $$\,n\,$$ elementos do espaço

                                     $$\mathcal{B}\;\equiv\;\{\,w_0\,,\,w_1\,,\,\cdots\,,\,w_{n-1}\,\}\,$$

tal que todo $$\,x\in X\,$$ se pode escrever como uma combinação linear dos elementos $$\,w_i\,$$ 

                                          $$x\;=\,a_0*x_0 + a_1*x_1 + \cdots\, a_{n-1}*x_{n-1}\qquad$$com $$\,a_i\in K$$ 

e essa combinação linear é única . O vetor $$\,\vec{x}\,$$ é definido pela sequência de coordenadas $$a_i$$

                                   $$\vec{x}\;\equiv\; \langle\,a_0\,,\,a_1\,,\,\cdots\,,\,a_{n-1}\,\rangle$$

As coordenadas  $$\,a_i\,$$ podem ser calculadas usando produtos internos. Primeiro é preciso determinar a chamada  base dual   $$\;\mathcal{B}' \;\equiv\;\{w_0'\,,\,\cdots\,,\,w'_{n-1}\,\}$$  que  verifica
                                    $$\langle\,w_i\,\centerdot\,w_i'\,\rangle\,=\,1\quad,\quad \langle\,w_i\,\centerdot\,w_j'\,\rangle\,=\,0$$   para todo $$i$$ e todo  $$\,j\neq i$$  
                                    
Nessas circunstâncias cada coordenada $$\,a_i\,$$ calcula-se facilmente como

                                                  $$a_i\;=\;\langle x\,\centerdot\,w'_i\,\rangle$$

Uma vez que existe uma forma explícita para calcular o traço de qualquer $$\,x\,$$, é possível agora determinar a representação vetorial do corpo finito $$\,\mathbb{F}_q\,$$.

## Corpos de Frações

 Uma outra forma de construir corpos é através da noção de **fração**.
 

> Dado um PID  $$\,\mathcal{R}\,$$ , o **corpo de frações** é definido no produto $$\,\mathcal{R}\otimes \mathcal{R}_+\,$$ pela relação de equivalência
>                    $$\,(a, b) \simeq (a',b')\quad\text{sse}\quad a\times b' = b\times a'\,$$
> Então 
>                    $$\,\text{Frac}(\mathcal{R}) \;\equiv\; \mathcal{R}\otimes\mathcal{R}_+/\simeq$$

Como é usual os pares $$\,(a, b)\,$$ representam as frações $$\,a/b\,$$.

| Na definição acima $$\mathcal{R}_+ \,\equiv \mathcal{R}\setminus \{0\}$$. |

## 
## $$\mathcal{R}$$-Módulos

Um $$\mathcal{R}$$-módulo é um grupo abeliano $$\,\mathcal{G}\,$$  equipada com uma operação $$\, \mathcal{R}\times \mathcal{G}\,\to\,\mathcal{G}\,$$ tal que,

    -  para quaisquer $$\,g\in\mathcal{G}\,$$ e $$\,z\in \mathcal{R}\,$$  as funções  $$\,x \mapsto x\,g\,$$   e $$\,a \mapsto z\,a\,$$ são morfismos de grupos.
    - para quaisquer $$\,x,y\in\mathcal{R}\,$$ e $$\,a\in\mathcal{G}\,$$  tem-se $$\,x\,(y\,a)\,=\, (x\,y)\,a$$. $$\,$$

Nomeadamente todo o grupo abeliano tem a operação de multiplação escalar que lhe dá a estrutura de um $$\,\mathbb{Z}$$-módulo.

Também um ideal $$\,\mathcal{I}\subseteq \mathcal{R}\,$$ é um exemplo de $$\,\mathcal{R}$$-módulo.

Finalmente o exemplo mais importante são os **reticulados,** que estudaremos num dos  próximos capítulos,  e que são a estrutura  essencial em muitas das técnicas criptográficas pós-quânticas.


