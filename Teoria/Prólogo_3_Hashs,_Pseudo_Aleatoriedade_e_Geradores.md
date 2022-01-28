# Prólogo 3: Hashs, Pseudo Aleatoriedade e Geradores

# “Hashs”  aleatórios

Uma “stream” $$\,\omega\,$$  é descrita por uma função $$\,\omega \,\colon\, \mathbb{N} \,\to\, \{0,1\}\,$$; isto é uma função que toma como argumento um inteiro $$\,n\geq 0\,$$ e devolve como resultado um “bit” $$\,\omega_n$$ : o bit na posição $$n$$ de $$\,\omega\,$$.

Equivalentemente, como o domínio $$\,\mathbb{N}\,$$ é isomórfico com o domínio das “strings” finitas $$\,\{0,1\}^\ast\,$$, também se pode associar a “stream” $$\,\omega$$ a uma função  

                                     $$\,\omega\,\colon\,\{0,1\}^\ast \,\to\, \{0,1\}$$

Generalizando estas funções,  podemos considerar a situação em que os resultados não são necessariamente  bits isolados, mas antes são *vetores de bits* de tamanho fixo.
Serão algo do tipo

                               $$\,h\,\colon\,\{0,1\}^\ast \,\to\, \{0,1\}^t$$

Estas funções designam-se por **funções de “hash”** de tamanho $$\,t\,$$:  tomam como argumento um “string” de bits finita de tamanho arbitrário e devolvem um vetor de bits de tamanho $$\,t\,$$ fixo.

Para efeitos da análise da aleatoriedade em funções de “hash” convém usar de novo o isomorfismo  $$\,\mathbb{N}\,\sim\,\{0,1\}^\ast\,$$ e  definir “hashs”  como funções

                            $$h\,\colon\,\mathbb{N}\,\to\,\{0,1\}^t$$

Estes objetos têm duas descrições possíveis sumariadas na seguinte figura


![](https://paper-attachments.dropbox.com/s_396F530D9AB28AC533B234EF2E3067F94EFC077FE8155D62835DC8525AC2A12E_1612988521961_hash.png)


Na primeira  versão, $$\,h\,$$ é  descrito por uma **sequência infinita de palavras  de** $$\,t\,$$ **bits.**

Selecionando, em  cada palavra $$\,h(n)\,$$, o bit na 1ª posição constrói-se uma  “stream” que representamos por $$\,h_1\,$$. Em geral, selecionando  as componentes de índice $$\,i\,$$ das várias palavras $$\,h(n)\,$$, constrói-se a“stream”   $$\,h_i\,$$.
Nesta descrição a função de “hash” de pode ser vista como um vetor de “streams”. 

                                  $$\,h \sim \langle\,h_1\,,\,h_2\,,\,\cdots\,h_t\,\rangle\,$$ 
                                

Na segunda versão, $$\,h\,$$ é descrito por uma “stream”  $$\,h^\ast\,$$ formada pela **concatenação** de todas os elementos de $$\,\vec{h}$$ 

                             $$h\,\sim\, h^\ast \;\equiv\; h(0)\,\|\,h(1)\,\|\,h(2)\,\|\,\cdots\,\|\,h(n)\,\|\,\cdots$$

Cada uma destas descrições conduz a uma definição própria de aleatoriedade :


1. Um “hash” $$\;h\,\colon\,\mathbb{N}\,\to\,\{0,1\}^t\;$$, representado por  $$\,\langle\,h_1\,,\,h_2\,,\,\cdots\,h_t\,\rangle\,$$ , é **aleatório**  se e só se cada $$\,h_i\,$$ é $$K$$-aleatório e, adicionalmente, é $$K$$-aleatórios em relação a qualquer outro $$\,h_j$$, com $$i\neq j$$.


2. Um “hash” $$\;h\,\colon\,\mathbb{N}\,\to\,\{0,1\}^t\;$$, representado pela “stream”  $$\,h^\ast\,$$ acima definida, é **aleatório** se e só se essa stream for $$\,K$$-aleatória.

**Teorema**
As duas definições apresentadas atrás são equivalentes. Isto é, a função de “hash”  $$\,h\,$$é aleatória para a primeira representação se e só se é aleatória para a segunda representação.


| **Detalhes**<br>Este resultado é uma generalização simples do teorema de van Lanbalgen para $$K$$-aleatoriedade. Para detalhes consultar a secção 6.9 do livro “*Algorithmic Randomness and Complexity*" (R.G. Downey e D.R.Hirschfeldt, Springer, 2010).<br><br>É um resultado importante porque permite estudar completamente as propriedades de um “hash” aleatório como se tratasse de uma única “stream” aleatória. Assim as propriedades da aleatoridade em “streams” ou conjuntos transferem-se para as funções de “hash”.<br><br>O teorema de van Lanbalgen considera conjuntos $$\,Z\,\equiv\,X\sqcup Y\,$$, formados pela união disjunta de conjuntos $$\,X,Y\,$$ , e prova que $$\,Z\,$$ é aleatório se e só se $$\,X\,$$ é aleatório e é também aleatório relativamente a $$Y$$.<br>Vendo as “streams” como conjuntos, a construção que apresentamos é equivalente à igualdade<br>                                                    $$h^\ast \;\equiv\; h_1 \sqcup h_2\sqcup\cdots\sqcup h_t$$<br>e, por isso, é possível aplicar esse teorema. |



## Propriedades de segurança de funções de “hash”

Funções de “hash” $$\;h\,\colon\,\mathbb{N}\,\to\,\{0,1\}^t\;$$ são primitivas criptográficas que ocorrem na maioria dos esquemas criptográficos, nomeadamente quando se pretende aproximar geração aleatória de objetos  (inteiros, “strings”)ou se pretende obter  um representante (“hash tag” ou só “tag”), de tamanho fixo, que identifique um qualquer objeto de tamanho não limitado (o “input”).

Existe um conjunto de propriedades que, tradicionalmente, são usadas para caracterizar o que se entende por  uma “boa”função criptográfica de “hash”.

 **Resistência da pré-imagem**    (também designada por **unidirecionalidade)**

> Dado um “tag” arbitrário $$r\in \{0,1\}^t$$ é computacionalmente “hard” determinar um “input”  $$\,n\,$$tal que $$\,h(n) = r$$.

**Resistência da segunda pré-imagem**

> Dado um “input” arbitrário  $$\,n_0\,$$, é computacionalmente “hard” determinar um outro “input” $$\,n_1\neq n_0\,$$ tal que $$\;h(n_0)\,=\,h(n_1)\,$$.

**Resistência a colisões**

> É computacionalmente “hard” determinar  ****um par de “inputs” distintos $$\;n_0\neq n_1\;$$tal que $$\,h(n_0)= h(n_1)\,$$.


----------

Pode-se provar facilmente que um “hash” $$\,h\,$$ aleatório verifica cada uma destas propriedades. Resumidamente

Para provar a resistência da pré-imagem  vamos considerar, na “stream” $$\,h^\ast\,$$, o Facto 3 da secção anterior. 
Dado $$\,r\,$$, encontrar um argumento $$\,n\,$$ tal que $$\,h(n)=r\,$$ é executado por um algoritmo que faz $$\,n\,$$ consultas ao oráculo. Encontrar $$n$$ é equivalente a encontrar na posição $$\,n\,t\,$$ de $$\,h^\ast\,$$ uma sequência igual a $$r$$. 
O resultado referido diz que, para todo $$\,c\,$$, temos de ter $$\,n\,t \geq c\,2^{t/2}\,$$, uma vez que $$\,|r|=t\,$$. Logo

                                  $$\,n \,> \,(c/t)\,\times\,2^{t/2}$$

a menos de um número finito de exceções. Por isso, o algoritmo para encontrar $$\,n\,$$ consultando $$\,h^\ast\,$$ , tem complexidade mínima quase exponencial.


----------

Para provar a resistência da segunda pré-imagem, dado $$\,n_0\,$$  calcula-se $$\,r=h(n_0)\,$$ e seleciona-se o sufixo de $$\,h^\ast\,$$ iniciado na posição   $$n_0\,t$$ . Qualquer sufixo de uma “stream” aleatória é também aleatório. Nesse sufixo procura-se a posição $$\,n_1\,t\,$$ onde se inicia um  “run” igual a $$\,r\,$$. Usando os argumentos anteriores teremos de ter, quase sempre,

                              $$n_1 \,>\,n_0\,+\, (c/t)\times\,2^{t/2}$$  

e por isso a complexidade mínima é ainda  “quase exponencial”.   


----------

Para provar a resistência a colisões vamos considerar o domínio de pares de naturais

                                 $$\,\mathbb{N}_2\;\equiv\;\{\langle n,k\rangle\,|\,n > k\}$$

É simples verificar que a função $$\,f(n,k) = (n-1)\,n/2 + k\,$$ é um isomorfismo entre  $$\,\mathbb{N}_2\,$$e $$\,\mathbb{N}\,$$.  Seja  $$\,h_1(m) \;\equiv\; h(n) \oplus h(k)\,$$, sendo $$\,m \equiv f(n,k)\,$$. É simples verificar que, dado que $$\,h\,$$ é um “hash” aleatório, também $$\,h_1\,$$ é um “hash” aleatório.

Procurar uma colisão em $$\,h\,$$ é procurar  $$\langle n,k\rangle$$, com $$\,k< n\,$$, tal que $$\,h(n)=h(k)$$ . Sendo $$\,m\equiv f(n,k)\,$$ isso equivale a procurar em $$\,h_1\,$$ a posição $$\,m\,$$ onde $$\,h_1(m) = 0$$ . 
Tal como nos dois casos anteriores, isto equivale também a procurar na “stream” aleatória $$\,h_1^\ast\,$$ a posição $$\,m\,t\,$$ onde se inicia um “zero run” de comprimento $$\,t\,$$.
Tem-se    $$\,m\,t \,\geq\,c\,2^{t/2}$$  e, dado que  $$\,m\sim n^2/2\,$$, conclui-se
                                              $$n\,>\,\sqrt{2c/t}\,\times\, 2^{t/4}$$
                                              
Note-se que a complexidade mínima da procura de uma colisão é aproximadamente a raíz quadrada da complexidade da procura de uma pré-imagem.


# Pseudo-Aleatoriedade

Por definição um conjunto $$\,A\,$$ aleatório ou um “hash” $$\,h\,$$ aleatório não podem ser efetivamente construídos porque, desde  já, não são computáveis. Por isso não existe qualquer algoritmo que gere, por exemplo, uma “stream”aleatória de bits.

No entanto este tipo de funcionalidade está constantemente a ser exigida nas técnicas criptográficas porque, nomeadamente, 

    - “strings” aleatoriamente gerados são  sempre vistas como “informação sem vícios ou armadilhas”
    - muitas vezes, para verificar propriedades do tipo “para um $$\,x\,$$ arbitrário  …”  substitui-se a qualificativo “arbitrário”  por “aleatoriamente gerado”.
    

Por isso é sempre necessário implementar eficientemente uma geração de objectos que simule, aos olhos de quem os observa, uma sequência aleatória.  

Vamos então considerar uma conjunto computável  $$\,A\,$$ que seja  “próximo” de um conjunto verdadeiramente aleatório $$\,\Omega\,$$.  Como se pode aferir essa “proximidade”?

Obviamente o observador só pode comparar $$\,A\,$$ com $$\,\Omega\,$$ durante até um determinado limite finito $$L$$ de observações. Portanto a pergunta mais precisa seria 

> Observando prefixos de comprimento limitado a $$\,L\,$$ de $$\,A\,$$ e de $$\,\Omega\,,$$como é possível aferir a “proximidade” destes dois conjuntos?

Existem várias respostas a esta pergunta diretamente associadas aos princípios que definem a aleatoriedade.


## $$K$$-pseudo-aleatoriedade

Nesta abordagem pretende-se verificar se o conjunto $$A$$ tem um prefixo suficientemente longo 
 
Se o conjunto $$\,A\,$$ fosse aleatório verificaria a condição

                                    $$\exists\,c\,\centerdot\,\forall\,n\,\centerdot\,K(A(n)) + c \,\geq\, n$$

Isto é, existe um $$c$$ tal que todo o prefixo $$\,A(n)\preceq A\,$$ é $$c$$-incompressível. 

Quanto menor for este $$\,c\,$$ mais difícil é garantir a $$c$$-incompressibilidade; por isso faz sentido definir um limite superior $$C$$ para os quais a $$c$$-incompressibilidade tenha sentido. Uma condição mais forte seria 

                                               $$\exists\,c\leq C\,\centerdot\,\forall\,n\,\centerdot\,K(A(n)) + c \,\geq\, n$$

Como $$\,A\,$$ não é aleatório então, negando a definição de $$K$$-aleatoriedade, para todo $$\,c\,$$ vai existir algum $$\,n\,$$ tal que $$\,K(A(n))+c < n\,$$.  Ou seja, $$A(n)\,$$ é $$c$$-compressível.

Este valores de $$\,n\,$$ vão depender não só de $$A$$ mas também de $$c$$ e, como são sempre positivos, existe um valor mínimo para o conjunto desses $$n$$’s.  Seja então

                                  $$\ell_A(c)\;\equiv\; \min\,\{n\,|\, K(A(n)) + c < n\}$$

A condição da eventual  $$K$$-aleatoriedade do conjunto $$\,A\,$$ é equivalente à condição

                                                                    $$\exists\,c\,\centerdot\,\ell_A(c) \,=\,\infty$$

                       
É simples provar que, quando $$\,A\,$$ é computável, a função $$\,c \mapsto \ell_A(c)\,$$é computável e é sempre estritamente crescente. Por isso existe sempre algum $$\,c\,$$ tal que $$\,\ell_A(c) \geq L$$.

Note-se também que, como $$\,\ell_A(c)\,$$ é o valor mínimo dos $$n$$’s para os quais $$\,A(n)\,$$  é $$c$$-compressível, então todos os prefixos $$A(n)$$ com $$n< \ell_A(c)\,$$ são $$c$$-incompressíveis tal como seriam se $$A$$ fosse aleatório. Sendo $$\,\ell_A(c) \geq L\,$$ então todos os prefixos $$A(n)$$ , com $$n < L$$, são também $$c$$-incompressíveis,

O conjunto$$\,A\,$$será próximo de $$\,\Omega\,$$ para prefixos limitados a $$\,L\,$$ se o valor de $$c$$ está limitado por $$C$$. Ou seja, as constantes $$L$$ e $$C$$ permitem determinar a proximidade de $$A$$ é um conjunto aleatório.


> O conjunto $$A$$ é  ($$C,L,K$$)-pseudo-aleatório quando 
                                 $$\exists\,c\leq C\,\centerdot\,\forall\,n\leq  L\,\centerdot\;K(A(n)) + c \,\geq\, n$$

Equivalentemente

                                                      $$\exists\,c\leq C\,\centerdot\,\ell_A(c) \geq L$$



## Martin-Lof pseudo-aleatoriedade .

Recorde-se a definição de aleatoriedade de Martin-Löf. Definiu-se um ML-teste como uma sequência uniformemente enumerável $$\,\varphi\;\equiv\;\{\varphi_c\}_{c\in\mathbb{N}}\,$$  de decisões tais que, para todo $$c\,$$, se tem $$\,0<\mathbb{P}[\varphi_c]\,\leq\,2^{-c}$$. 

Esta definição de testes é bastante aberta: impõe apenas que $$\,(c,x) \mapsto \varphi_c(x)\,$$seja uma função computável em $$\,c\,$$ e parcialmente computável em $$\,x\,$$.

Vimos também que um conjunto $$\,X\,$$ é aleatório num ML-teste  $$\,\varphi\,$$ quando existe alguma decisão $$\,\varphi_c\,$$ onde nenhum prefixo de $$\,X\,$$ é  sucesso.  Em síntese

               $$X\;\text{é aleatório em}\;\varphi\;\quad\text{sse}\quad\; \exists\,c\,\centerdot\,\forall\,x\preceq X\,\centerdot\,\varphi_c(x)\!\!\uparrow$$ 
    

Definiu-se $$\,X\,$$ como ML-aleatório quando  $$X$$ for aleatório em todos os ML-testes; por fim, referimos que tal ocorre se e só se $$\,X\,$$ for  $$\,K$$-aleatório. Daí a designação “conjunto aleatório” aplica-se tanto à ML-aleatoriedade como à $$K$$-aleatoriedade.

O nosso objetivo é usar a metodologia de ML para também definir *pseudo-aleatoriedade*.  Para definir uma classe de conjuntos pseudo-aleatórios  pode-se considerar formas mais fracas de aleatoriedade, restringindo a classe dos testes. 


**Aleatoriedade de Schnorr**

Pode-se restringir os ML-testes $$\,\varphi\,\equiv\{\varphi_c\}_{c\in\mathbb{N}}$$  aos casos em que todos os $$\,\varphi_c\,$$ são decisões computáveis.  Nesse caso diz-se que $$\,\varphi\,$$ é **uniformemente computável**. 

A condição de aleatoriedade para o teste  $$\varphi\,$$ é, como em qualquer ML-teste,


            $$X\;\text{é aleatório para}\;\varphi\quad\text{sse}\quad\;\{\,c\;|\; \forall\,x\preceq X\,\centerdot\,{\varphi_c(x)\!\uparrow}\,\}\;\neq\;\emptyset$$ 

Os ML-testes definidos por tais sequências dizem-se **testes de Schnorr** ou **S-testes**.  Um conjunto $$X\,$$ que seja aleatório para todos os testes de Schnorr  $$\,\varphi\,,$$ diz-se  S-aleatório. 

    

Obviamente, como os $$S$$-testes são um caso particular de ML-testes, todo o conjunto aleatório é também S-aleatório. 

O inverso, porém, não é verdade: prova-se que existem conjuntos S-aleatórios que não são aleatórios.  Por esse motivo poderia pensar-se que a aleatoriedade de Schnorr seria uma boa definição para a pseudo-aleatoriedade.

Isso não é possível porque um conjunto pseudo-aleatório $$\,X\,$$ tem de ser computável  e prova-se que 

    
> Para qualquer S-teste $$\,$$$$\varphi\,$$, existe sempre um conjunto computável  $$\,X\,$$ (que depende do teste) para o qual esse conjunto é aleatório. 
> No entanto não existe nenhum conjunto computável que seja aleatório para todos os S-testes $$\varphi$$ e, por isso, nenhum conjunto computável é  $$\,$$S-aleatório.


**Pseudo-Aleatoriedade NP**

O nosso objetivo é encontrar uma noção suficientemente fraca de “aleatoriedade” , que algum conjunto computável $$\,X\,$$ possa verificar,  mas também seja forte suficiente para, de alguma forma, não poder ser distinguível de um conjunto verdadeiramente  aleatório.

Recorde-se que um conjunto $$\,X\,$$ é computável quando são  computavelmente enumeráveis (*c.e*.) tanto $$\,X\,$$como  o seu complemento $$\,\mathbb{N}\setminus X\,$$.

Equivalentemente $$\,X\,$$ é computável quando é computável a seu **predicado característico** $$\,x\,\mapsto\, {x\in X}\,$$ ; equivalentemente quando é computável o seu **predicado prefixo**  $$\,x\,\mapsto \,{x\preceq X}\,$$.

Assim, num teste de Schnorr $$\,\varphi \equiv\{\varphi_c\}$$, os predicados  $$\,x\in \varphi_c\!\downarrow\,$$ são funções computáveis e o predicado $$\,\varphi\,\equiv\, (c,x) \mapsto \varphi_c(x)\,$$ é  computável.

Portanto, para cada $$\varphi$$,   o conjunto

                                 $$X\colon \varphi \;\equiv\;\{\,c\;|\; \exists\, x\preceq X\;\centerdot\; \varphi(c,x)\,\}$$

é um elemento da classe de complexidade computável $$\,\Sigma_1\,$$.

O seu complemento  $$\,\mathbb{N}\mathbin{\setminus} {X\colon\varphi}\,$$  é, por isso, um elemento da classe   $$\,\Pi_1\,$$ . 
Com é habitual tem-se 

> $$\,X\,$$  é aleatório para $$\,\varphi\,$$ sse  o  complemento  $$\,\mathbb{N}\mathbin{\setminus} {X\colon\varphi}\,$$  não é vazio. 

e também

> $$X$$ é S-aleatório sse é aleatório para todos os S-testes  $$\varphi$$. 

 Sendo $$\,X\,$$ computável prova-se  que  $$\,\mathbb{N}\mathbin{\setminus} {X\colon\varphi}\,$$ é sempre vazio e, por isso,  nenhum $$\,X\,$$ computável é aleatório.
 
Para enfraquecer estas restrições vamos impor  duas condições adicionais a estes testes $$\,\varphi\,$$

    1. A complexidade computacional de $$\,\varphi\,$$ deve ser polinomial  com  $$|\langle c,x\rangle|\,$$ .
    2. Existe uma função limite $$\,b(c)\,$$ computável e polinomialmente limitada em $$\,c\,$$ tal que a probabilidade de ser $$\,|x| > b(c)\,$$ nunca ocorre quando  $$\,\varphi(c,x)\,$$ é válido,

Com estas condições cada conjunto $$\,X\colon\varphi\,$$  é um elemento da classe **NP** e, por isso, o seu complemento é um elemento da classe **coNP**.  Vamos designar estes testes por **NP**-testes.

Vamos considerar como **pseudo-aleatório** um conjunto computável $$\,X\,$$ que seja aleatório para todo o **NP-**testes.

A proximidade com conjuntos aleatórios é feita em relação aos conjuntos aleatórios segundo Schnorr. Considere-se para cada teste de Schnorr $$\,\varphi\;\equiv\;\{\varphi_c\}_{c\in\mathbb{N}}$$  , um segundo teste de Schnorr $$\,\varphi'\;\equiv\;\{{\varphi'_c}\}_{c\in\mathbb{N}}\,$$ definido por decisões 


                                  $$\varphi'(c,x) \;\equiv\; (|x| < b(c))\,\land\,\varphi(c,x)\,$$.

para uma determinada função polinomial  $$\,c\mapsto b(c)$$.

Como se compara as probabilidades de $$\,\varphi_c\,$$  com $$\,\varphi'_c\,$$? Nomeadamente se $$\,\varphi_c(x)\,=\,\mathtt{True}$$ , indicando a não  S-aleatoridade, qual é a probabilidade de ser $$\,\varphi'_c(x)=\mathtt{False}\,$$ sugerindo pseudo-aleatoriedade? 
É fácil verificar que 

                                            $$\mathbb{P}[\,\neg \varphi'_c\;|\;\varphi_c\,]\;\leq\;2^{-b(c)}$$

Portanto a probabilidade de um determinada decisão dar uma mensagem errónea sobre a aleatoriedade de um qualquer $$\,X\,$$ decresce rápidamente com $$\,c\,$$.


# Geradores Aleatórios

Geradores aleatórios são abstrações de algoritmos criptográficos. Normalmente um algoritmo criptográfico pertence à classe de complexidade PPT (“probabilistic, polynomial time”) . Nos geradores, ignora-se a dimensão da complexidade e concentra-se o estudo apenas na dimensão probabilística.

Nesta secção vamos introduzir a terminologia e a notação básica necessária à descrição deste tipo de entidades.

Essencialmente, neste curso, um gerador aleatório é um algoritmo probabilístico acompanhado por uma noção de **evento** (ou **experiência**). Para captar esta noção vamos usar uma notação 

                                                $$y\,\gets\, G$$

para descrever a asserção

> No próximo evento , o gerador  $$\,G\,$$ produz um resultado e esse resultado coincide com  $$\,y\,$$.


## Geradores básicos

Vamos analisar algumas formas particulares de geradores com vista a  construir, para cada um, uma definição genérica deste conceito.


1. *Gerador determinístico:* $$\,\mathcal{A}\,$$.


    Um algoritmo $$\,\mathcal{A}\,$$  é determinístico;  recebe um *input* $$\,x\,$$ , eventualmente vazio, e produz em qualquer evento sempre o resultado $$\,$$ $$\,\mathcal{A}(x)\,$$
                                      $$\,y\gets \mathcal{A}(x)\quad$$sse $$\quad y = \mathcal{A}(x)$$
    Em particular, se o *input* for vazio tem-se
                              $$\,y\gets \mathcal{A}\quad$$sse $$\quad y = \mathcal{A}(\,)$$


2. *Gerador determinístico que consulta um oráculo aleatório:*  $$\,\mathcal{A}^\mathcal{R}\,$$.


    O oráculo $$\,\mathcal{R}\,$$é uma “stream” aleatória de bits ou, equivalentemente, um conjunto aleatório. O algoritmo $$\,\mathcal{A}\,$$é implementado por uma máquina de estados probabilística tal como foi descrito em [+Prólogo  1: Introdução à Complexidade Aritmética](https://paper.dropbox.com/doc/Prologo-1-Introducao-a-Complexidade-Aritmetica-iGjUs3jVQKwqtv8LH8Bf7).


    Agora é necessário gerir as experiências definidas pelo mecanismo de geração. 
    Para isso usa-se um quantificador $$\,\vartheta\,$$ que cria   sempre um “novo nome” (um *nome local*) que vai associar à próxima experiência. 
    Genéricamente  o quantificador ocorre com alguma função  $$\,f\,$$ (ou algoritmo) numa construção da forma
                                             $$\,\vartheta\,n\,\centerdot\,f(n)\,$$   
    Esta construção determina um gerador que impões  que a próxima experiência é identificada pelo inteiro $$\,n\,$$ e que o resultado gerado é o resultado de $$\,f(n)\,$$.   


    No caso, o gerador $$\,\mathcal{A}^\mathcal{R}\,$$ é definido por
                                             $$\mathcal{A}^\mathcal{R}\;\equiv\; \vartheta\,n\,\centerdot\,\mathcal{A}(\mathcal{R}(n))$$   
                 
    Esta definição indica que, após criar o identificador $$\,n\,$$ da próxima experiência, esse inteiro é usado para selecionar o prefixo $$\,\mathcal{R}(n)\preceq \mathcal{R}\,$$; essa *string* é usada como argumento do algoritmo determinístico $$\,\mathcal{A}\,$$ e o resultado do algoritmo é o resultado final do gerador. 
     
                              $$y \gets \mathcal{A}^\mathcal{R}\;\;\equiv\;\;\vartheta\,n\,\centerdot\;y = \mathcal{A}(\mathcal{R}(n))$$
                
3. *“Hash” aleatório*


    Um “hash” aleatório de comprimento $$\,t\,$$ é uma forma particular do caso anterior. 
    
    Por exemplo, pode-se construir um algoritmo determinístico $$\,\mathcal{H}\,$$ que, sob *input* de uma “string”  $$\,x\,$$ , devolve os últimos $$\,t\,$$ bits de $$\,x\,$$, caso $$\,|x|\geq t\,$$, ou devolve uma constante arbitrária $$\,u\,$$  de comprimento $$t$$ (um “salt”)  no caso de $$\,|x|<t$$.
    
    Então o “hash” define-se, com este algoritmo e uma “stream” aleatória $$\,\mathcal{R}\,$$, como
                                                               $$\,h\;\;\equiv\;\;\mathcal{H}^\mathcal{R}$$
----------
> Genericamente, dados dois geradores aleatórios arbitrários $$\,\mathcal{Z}\,\text{e}\,\mathcal{A}\,$$, o quantificador $$\,\vartheta\,$$permite construir um terceiro gerador
>                                                                 $$\mathcal{G}\;\;\equiv\;\vartheta\,z \gets \mathcal{Z}\,\centerdot\,\mathcal{A}(z)$$
> Aqui, $$\,z\gets\mathcal{Z}\,$$ designa o próximo evento gerado a  partir de $$\,\mathcal{Z}$$ ao qual é dado o nome $$\,z\,$$; no evento seguinte procura-se um resultado de $$\,\mathcal{A}\,$$ e esse será também o resultado de $$\,\mathcal{G}\,$$.
>                                                        $$y\gets \mathcal{G}\;\;\equiv\;\;\vartheta\,z\gets\mathcal{Z}\;\centerdot\;y \gets \mathcal{A}(z)$$

O quantificador $$\,\vartheta\,$$ e a existência de recursividade na definição  permite construir uma grande variedade de de geradores. Vamos dar alguns exemplos.

**Exemplos**
Em algoritmos criptográficos é frequente definir variantes da repetições de um gerador base $$\,\mathcal{G}\,$$. Vamos apresentar duas variantes 


1. Repetição $$\,k\,$$ vezes de $$\,\mathcal{G}\,$$ acumulando os diferentes resultados numa só ‘string’.

        $$\mathcal{G}^0\;\;\equiv\;\; \varepsilon$$
        $$\mathcal{G}^n\;\;\equiv\;\; \vartheta\,w\gets \mathcal{G}^{n-1}\,\centerdot\,\vartheta\,z\gets \mathcal{G}\,\centerdot\,w\|z$$                     para $$n>0$$
         
  2. Repetição de $$\,\mathcal{G}\,$$ até que o resultado gerado verifique uma condição $$\,\phi\,$$.

      
                $$\mathcal{G}\mathbin{|}\phi\;\;\equiv\;\;\vartheta\,z\gets \mathcal{G}\,\centerdot\,\mathtt{if}\,\phi(z)\;\mathtt{then}\,z\;\mathtt{else}\;\mathcal{G}$$


----------


## Geradores pseudo-aleatórios

Todos os geradores aleatórios têm um único tipo de **fonte de aleatoriedade**:  uma “stream” aleatória $$\,\mathcal{R}\,$$ (“random”). 
Como referimos, “streams” aleatórias são entidades ideais, que não podem ser computadas, e por isso “streams”  pseudo-aleatórias são importantes. 

Porém é sempre possível  aproximar a fonte de aleatoriedade $$\,\mathcal{R}\,$$ por uma “stream” pseudo-aleatória . Dessa forma definem-se **geradores pseudo-aleatórios**.


## Aleatoriedade de um gerador.

Um gerador é realizado a partir de uma “stream”: a sua fonte de aleatoriedade. Inversamente uma fonte de aleatoriedade pode ser realizada a partir de um  gerador.

Dado um gerador $$\,\mathcal{G}\,$$ é possível construir uma sequência  de “strings” $$\,\{\,w_n\}_{n\in\mathbb{N}}\,$$ da seguinte forma

                               $$\,w_0\,\gets\,\varepsilon\quad\;\text{e}\;\quad w_n \,\gets\,(\,\vartheta \,z\gets \mathcal{G}\,\centerdot\,w_{n-1}\|z\,)$$ 

Esta sequência é formada pela concatenação dos sucessivos “outputs” do gerador $$\,\mathcal{G}\,$$: a posição $$\,n\,$$ da sequência é formada pela concatenação de $$\,n\,$$  resultados de $$\,\mathcal{G}\,$$.

É óbvio que cada $$\,w_n\,$$ é prefixo de qualquer outro $$\,w_m\,$$ com $$\,m>n\,$$. Por isso faz sentido definir uma “stream”  $$\,\mathcal{G}^\infty\,$$ como um limite

                               $$\mathcal{G}^\infty\;\,\equiv\,\; \lim_{n\to\infty}\,w_n$$

Assim o grau de aleatoriedade de um gerador exprime-se nas propriedades de aleatoriedade da “stream “ $$\,\mathcal{G}^\infty\,$$.  De facto todas as noções ligadas a “streams” aleatórias ou pseudo-aleatórias transportam-se para geradores através da mapeamento $$\,\mathcal{G} \mapsto \mathcal{G}^\infty$$.

Um outro gerador construído por esse mecanismo é $$\,\mathcal{G}^\ast\,$$ que gera os diversos prefixos de $$\,\mathcal{G}^\infty\,$$.

                            $$G^\ast \;\equiv\; \varepsilon \;|\; \vartheta\,u\gets \mathcal{G}^\ast\,\centerdot\,\vartheta\,z\gets \mathcal{G}\,\centerdot\,z\,\|\,u$$

Em particular $$\,\mathcal{}$$$$\,\mathcal{G}^\infty\,$$ pode ser usado como fonte de aleatoriedade . Nomeadamente

**Facto**   

> A asserção  
>                                   $$\;\mathcal{F}\;\equiv\;\vartheta\,w \gets \mathcal{G}^\ast\,\centerdot\,\mathcal{A}(w)\;$$ 
> é equivalente a       
>                                   $$\;\mathcal{F}\;\equiv\;\mathcal{A}^{\mathcal{G}^\infty}\,$$



## Probabilidade de um gerador booleano

 Um gerador booleano  $$\,\mathcal{B}\,$$, isto é um gerador com resultados em $$\,\{0,1\}\,$$, pode ser associado à noção de probabilidade.
Basta contar, para cada $$\,\mathcal{B}^n\,$$, o número de experiências onde o resultado é $$1$$ e dividir por $$\,n\,$$
                              $$\mathbb{P}[\mathcal{B}]\;\equiv\;\lim_{n\to\infty}\,\vartheta\,x\gets \mathcal{B}^n\,\centerdot\,\#x/n$$

