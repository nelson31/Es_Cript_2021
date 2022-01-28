# Prólogo  1: Introdução à Complexidade Aritmética

# Computabilidade e Complexidade


## Domínios

$$\mathbb{N}\,$$ denota o domínio dos números naturais e  $$\,\{0,1\}^\ast\,$$ denota o domínio das *strings* de bits finitas. Estes domínios são isomórficos; na maioria dos problema, dos algoritmos e da respetiva complexidade  é indiferente usar um ou o outro.

| $$\,|x|\,$$ denota o *comprimento* da sequência de bits $$\,x\in\{0,1\}^\ast\,$$. Para um inteiro $$\,n\,$$, o seu *tamanho* é o comprimento da menor string $$\tilde{n}\,$$ que codifica $$\,n\,$$; isto é   ** $$\,|n|\,\equiv\,\lceil\,\log_2 n\rceil\,=\,|\tilde{n}|\,$$ . A função que estabelece o isomorfismo $$\,\{0,1\}^\ast \to \mathbb{N}\,$$ é, usualmente, $$\,x\mapsto 2^{|x|}- 1 + \sum_{i=0}^{|x|-1}\,x_i\,2^i \,$$. |

A cardinalidade de domínios  cujos elementos são sequências de bits ou números naturais  permite uma classificação desses domínios. Por exemplo

    - **domínios finitos** têm como exemplo paradigmático o domínio  $$\,\mathcal{B}_n\,\equiv\,\{0,1\}^n\,$$ das *palavras* (“words”) ou *vetores* (“bit-vectors”) com exatamente $$\,n\,$$ componentes. São também exemplos de domínios finitos os domínios da forma
                                           $$[\,t\,]\;\equiv\;\{\,i\in \mathbb{N}\,|\,i < t\}$$
                    
    - **domínios contáveis** são domínios isomórficos com um subconjunto dos números naturais; i.e. domínios $$D$$ para os quais existe uma função injetiva $$\,\mathsf{inx}\,\colon\, D\to\mathbb{N}\,$$.
| Em muitas situações o isomorfismo entre $$\,\mathbb{N}\,$$ e  $$\,\{0,1\}^\ast\,$$ está sempre presente e por isso qualquer definição que envolva um destes domínios gera uma definição análoga envolvendo o outro domínio. <br>        Por isso no que se segue  usamos  $$\,\mathbf{2}\,$$ como abreviatura de $$\,\{0,1\}\,$$ e usamos $$\,\omega\,$$ para representar qualquer domínio contável isomórfico com $$\,\mathbb{N}\,$$.<br>        O símbolo $$\,\omega\,$$  denota o **ordinal dos contáveis** . |

    - **domínios de Cantor** são classes cujos elementos são domínios contáveis.
| Na terminologia da compatibilidade, **conjuntos** identificam-se com coleções de números naturais; coleções de conjuntos designam-se por **classes**  assim como as coleções de classes. |

O paradigma de um domínio de Cantor é a classe  $$\,\{0,1\}^\infty\,$$ (ou $$\,\mathbf{2}^\infty\,$$) de todas as sequências infinitas de bits (também designadas por *streams)*

                                                       $$\,\{w_n\}_{n\in\mathbb{N}}$$ 
                                

As  *streams* $$\,w\in\{0,1\}^\infty\,$$  podem-se identificar ainda com 

                                         
    - Funções       $$\quad w \,\colon\, \omega\,\to\, \mathbf{2}\quad$$ 
        O domínio de tais funções representa-se pelo ordinal  $$\;\mathbf{2}^{\mathbb{N}}\quad\text{ou}\quad\mathbf{2}^{\omega}$$.
        
    - Conjuntos$$\qquad\overline{w} \,\equiv\ \{n \in \mathbb{N}\,|\, w_n=1\}\quad$$.
        Genericamente  tem-se  conjuntos $$\quad\overline{w}\,\equiv\,\{x\in \omega\,|\, w_{\mathsf{inx}(x)}= 1\}$$ .
        
    - séries infinitas
                                                            $$\quad 0\cdot{w}\;\equiv\;\;\sum_{n \in \overline{w}}\; 2^{-n-1}$$  

Cada stream $$\,w\in \mathbf{2}^\omega\,$$ pode   ser associada   uma sequência crescente de conjuntos finitos

                                    $$\overline{w}{(k)}\;\equiv\; \{n < k\,|\,\omega_n=1\,\}$$ 
                

Obviamente o conjunto  $$\overline{w}(k)\,$$pode ser descrito por uma string   $$\,w(k)\,$$ de tamanho  $$\,k\,$$
                                      $$\quad w(k)\,\equiv\,\langle w_0\,,\,w_1\,,\,\cdots\,,\,w_{k-1}\rangle\,$$
                                      
Tanto $$\,\overline{w}(k)\,$$ como $$\,w(k)\,$$ designam-se por **truncaturas.** 

Uma string $$\,y\,$$ é um **prefixo** da stream  $$\,w\,$$ ,  e escreve-se como  $$\,y \preceq w\,$$, quando $$\,y\,$$ coincide com a truncatura de $$\,w\,$$ com  comprimento igual ao comprimento de $$y$$; isto é 

                                            $$y\,=\,w(|y|)\,$$ 

Como conjuntos $$\,A,B \subseteq \mathbb{N}\,$$,  “streams”  podem ser manipuladas com os usuais operadores em conjuntos (união, interseção e complemento) mas também com um operador binário  designado por **união disjunta,** representado por $$\,A\sqcup B\,$$. Tem-se

                    $$A \sqcup B\;\equiv \;\{2\,k\,|\,k\in A\}\,\cup\,\{2\,k+1\,|\,k\in B\}$$
----------

Um outro domínio de Cantor, muito importante em Criptografia, são as **funções de hash**.

Recorde-se que uma *stream*  pode-se descrever como uma função $$\,f\,\colon\,\{0,1\}^\ast\,\to\,\{0,1\}\,$$; uma função de *hash* *de tamanho* $$\,t\,$$  generaliza este conceito para funções 

                  $$\,h\,\colon\ \{0,1\}^\ast\,\to\,\{0,1\}^t\quad$$ ou, equivalentemente, $$\quad h\,\colon\,\mathbb{N}\,\to\,\{0,1\}^t$$
                

A função de *hash*   $$\,h\,$$ pode ser interpretada como uma sequência  $$\;\{h_n\}_{n\in\mathbb{N}}\,$$ de  $$\,t\,$$-palavras. Concatenando todas estas palavras obtemos uma *stream* $$\,{h}^\ast\,$$ 

                              $$h^\ast \;\equiv\; h_0\,\|\, h_1\,\|\,\cdots\,\|\,h_n\,\|\,\cdots$$

A *stream*  $$\,h^\ast\,$$ pode também ser descrita pela relação
                                                                $${h}^\ast_{t\times n + i}\,\equiv\,h_{n,i}\quad$$                      para $$\,n\in\mathbb{N}\;$$e $$\,0\leq i< t$$

                        

As  propriedades da função de *hash* $$\,h\,$$ (por exemplo, a sua segurança criptográfica) são descritas pelas propriedades da *stream* $$\,h^\ast\,$$ que a representa.


----------

As noções de *função computável*  e de *algoritmo* , que iremos discutir em seguida, permitem introduzir uma nova dimensão na classificação de domínios contéveis e de domínios de Cantor.
Assim:

    - Um domínio contável $$\,D\,$$ é *computacionalmente enumerável*   (ou, apenas, **enumerável**) se existe uma função computável e sobrejetiva  $$\,f\,\colon\,\mathbb{N}\,\to\,D\,$$. Equivalentemente $$\,D\,$$ é enumerável se existe um algoritmo de decisão $$\,\mathcal{A}\,$$ que aceita o *input* $$\,x\,$$ se e só se $$\,x\in D\,$$.


| O domínio enumerável genérico isomórfico com $$\,\mathbb{N}\,$$ é representado por  $$\,\mathcal{N}\,$$.<br><br>Enquanto que $$\,\omega\,$$ denota um domínio qualquer isomórfico com $$\,\mathbb{N}\,$$ , sem impor que o isomorfismo seja computável, a designação $$\,\mathcal{N}\,$$ impõe que o isomorfismo com $$\,\mathbb{N}\,$$ seja computável. <br><br>Por exemplo, considere-se uma sequência de conjuntos  $$\,\{S_n\}_{n\in \mathcal{N}}$$  com índices $$\,n\,$$ num qualquer domínio enumrável. Neste caso é possível definir $$\,\bigcup_{n\in \mathcal{N}}\,S_n\,$$.  Porém se tivermos   $$\,\{S_n\}_{n\in \omega}\,$$, com índices $$\,n\,$$num domínio  contável , já não é possível assegurar a existência de  $$\,\bigcup_{n\in \omega}\,S_n\,$$ |




    - Uma sequência de domínios contáveis $$\,\mathcal{D}\;\equiv\;\{\,D_n\,\}_{n\in\mathcal{N}}\,$$ é **uniformemente enumerável** (ou **u-enumerável**) se existe um algoritmo de decisão $$\,\mathcal{A}\,$$ que aceita como *input* o par $$\,(n,x)\,$$ se e só se  $$\,x\in D_n\,$$.
----------
## Computabilidade

No modelo de computação que se  segue considera-se que $$\mathbb{N}$$ (ou $$\{0,1\}^\ast\,$$) tem a ordem dos inteiros e está equipado com um conjunto de **operações primitivas:** 

        1. as constantes $$0,1$$,  
        2. relações binárias $$<\,,\,\neq\,,\,\cdots$$  
        3. os operadores binários soma $$+$$ e  concatenação de strings $$\,x\,y\,$$ ;  
            o par   $$\, (x,y)$$  é equivalente à concatenação  $$0^{|x|}\,1\,x\,y$$.
        4. o operador ternário $$\mathsf{ite}$$ (*if-then-else).* 
        

A concatenação $$\,x\,y\,$$pode também ser representada   com um operador específico:  $$\,x\|y$$.

| Esta  estrutura algébrica descreve essencialmente a designada **aritmética de Presburger.** A propriedade essencial desta aritmética está no no facto de, apesar  de ser um fragmento da Lógica de 1ª Ordem, é ainda decidível tal como a Lógica Proposicional. <br>Por isso é possível construir ferramentas computacionais (“theorem provers” ) que decidam da validade de asserções da LP enriquecida com a aritmética de Presburger. Algumas dessas ferramentas vão ser usadas neste curso. <br>Note-se que tanto  a Lógica de 1ª Ordem  como a aritmética de Peano, sem restrições,  não são linguagens decidíveis e, por isso, não existe nenhuma ferramenta computacional que seja capaz de avaliar a validade de uma asserção arbitrária em qualquer destas linguagens. |

**Máquinas de Estados**
Genericamente as noções de *complexidade computacional* usam um modelo de computação que é uma extensão da noção de máquina de Turing.
Sem perda de generalidade pode-se considerar, como referência, uma máquina de estados $$\,\mathcal{M}\,$$ que tenha $$\mathbb{N}$$ como **espaço de estados,** e seja ****determinada por uma  **relação de transição** 

                                                   $$\,\tau\subseteq \mathbb{N}\times\mathbb{N}\times \{0,1\}^\ast\,$$

Representa-se $$\,$$$$\,(s,s',e)\in\tau\,$$ como   $$\,s\to^\tau (s',e)$$   ou como $$s\to (s',e)$$, quando $$\tau$$ está implicito.

A particularidade deste tipo de modelo de computação está no espaço de estados, o domínio $$\,\mathbb{N}$$   ou equivalentemente   $$\,\{0,1\}^\ast\,$$, a sua estrutura algébrica e o facto de cada transição ser descrita só por operações primitivas.

**Máquina de estados com oráculo.**
Um oráculo é um conjunto  $$\,\mathcal{O}\subseteq \mathbb{N}\,$$ ou, equivalentemente, uma “stream”  $$\,\mathcal{O}\in \{0,1\}^\infty\,$$ que permite enriquecer o modelo da computação com novas operações primitivas unárias.

Na relação de transição $$\,\tau^\mathcal{O}\,$$ cada transição $$\,s\to s'\,$$ é construída não só com as operações primitivas básicas  mas também  a relação de “pertença” $$\,s\in \mathcal{O}$$. A máquina de estado com a relação $$\,\tau^\mathcal{O}\,$$ é representada por $$\,\mathcal{M}^\mathcal{O}\,$$.

A relação $$\,s\in \mathcal{O}\,$$  passa a fazer parte de um novo repertório de operações primitivas associadas a uma única transição de estados. Cada operação da forma $$\,s\in\mathcal{O}\,$$ designa-se por **consulta ao oráculo** $$\,\mathcal{O}\,$$
 
**Computação**
No contexto da relação $$\,\tau\,$$ (ou $$\,\tau^\mathcal{O}\,$$)

    - Uma **computação** é  um par $$\,(\alpha,\alpha\!\downarrow)\,$$ sendo
        - $$\,\alpha\,$$ é um **traço**   no grafo de $$\,\tau\,$$; isto uma sequência de estados $$\,\alpha \equiv \{\alpha_i\}\,$$ tais que, para todo $$i\geq 0$$, se verifica
                                                         $$\,\alpha_i\to (\alpha_{i+1},e_i)\,$$
        - $$\,\alpha\!\downarrow\,\equiv\, e_0\,e_1\,\cdots\,e_i\,\cdots$$ é o **resultado** da computação formado pela concatenação de todos os $$e_i$$.
| Se não existir ambiguidade usamos o mesmo símbolo $$\,\alpha\,$$ para descrever tanto o traço como a computação na globalidade. |

    
    - Uma computação **termina** se o seu traço for finito. Se $$\alpha$$ termina, a complexidade desse computação, representada por $$\,|\alpha|\,$$, é o comprimento do seu traço; isto é, o total de transições efetuadas neste traço. Numa máquina com oráculo, essa complexidade é também medida pelo número de transições que são consultas ao oráculo. Se $$\,\alpha\,$$ não termina, o seu resultado é indefinido e é representado por $$\bot$$.
    
    - Uma computação $$\,\alpha(x)\,$$ denota o sufixo mais longo de $$\,\alpha\,$$ que tem $$x$$ como estado inicial. Se $$x$$ não ocorrer em $$\,\alpha\,$$ então $$\alpha(x)$$ é indefinido.
    
    - Cada computação $$\,\alpha\,$$ é determinada por uma “string” $$\,p\in\{0,1\}^\ast$$, designada por **programa.** A máquina de estados $$\,\mathcal{M}\,$$ enumera todas as suas computações, usando programas como índices de tal forma que se escreve $$\,\alpha\; \equiv\; \mathcal{M}_p\,$$.
    - Analogamente, para uma máquina com oráculo $$\,\mathcal{O}\,$$, escreve-se  $$\,\alpha\;\equiv\; \mathcal{M}^\mathcal{O}_p$$.

**Máquinas de estado determinísticas, não-determinísticas e probabilísticas**

Uma máquina de estados $$\,\mathcal{M}\,$$ é **determinística**  quando, para cada $$x$$, existe quanto muito uma única computação $$\,\mathcal{M}_p(x)\,$$ que termina. Em caso contrário a máquina diz-se **não-determinística**.

Máquinas de estado **probabilísticas** são definidas por duas máquinas de estado determinísticas $$\,\mathcal{M}_0,\mathcal{M}_1\,$$,  definidas sobre o mesmo reportório de operações primitivas e, eventualmente, com o mesmo oráculo $$\,\mathcal{O}$$. Adicionalmente existe um segundo oráculo $$\,\Omega\in \{0,1\}^\infty\,$$, uma “stream” aleatória de bits. 
Em cada estado $$\,s\,$$ a máquina probabilística $$\,\mathcal{M}\,$$ transita segundo $$\,\mathcal{M}_{b}\,$$  sendo $$\,b\,$$ o bit na posição $$s$$ de $$\Omega$$.   Formalmente

                                $$s\to^\mathcal{M}(s',e)\quad \text{iff}\quad s\to^{\mathcal{M}_b}(s',e)\qquad\text{com}\; b\equiv\Omega_s$$
| A noção de aleatoriedade computacional é uma das mais importantes em computação. Uma das formas possíveis de definir aleatoriedade recorre à noção de incompressibilidade.<br><br>Dado um conjunto $$\,\Omega \subseteq \mathbb{N}$$, seja $$\,\Omega{(n)} \equiv \{s \in \Omega\,|\,s < n\}\,$$. O conjunto é aleatório se todo $$\Omega(n)$$ é incompressível. Isto é, para todo a máquina de estados determinística $$\,\mathcal{M}\,$$ e toda a sequência de programas $$\,\{p_n\}\,$$ tais que $$\,\Omega(n) \gets \mathcal{M}_{p_n}\,$$, tem-se   $$|p_n| + c > n\,$$ para alguma constante $$c>0$$ e para todo $$n$$. |



**Decisão**
Uma **decisão** $$\,\mathcal{D}\,$$é uma computação em que ocorre uma das seguintes situações:

        - $$\,\mathcal{D}(x)\!\downarrow\,=\,0\,$$, para todo $$x$$;  nesse caso a decisão **sucede** e **aceita** $$\,x\,$$.
        - $$\mathcal{D}(x)\!\downarrow\,\neq\, 0\,$$, para todo $$x$$ ; neste caso a decisão **falha**  e **rejeita** $$\,x\,$$.
| Note-se que o resultado $$0$$ tem na definição de “decisão” um papel distintivo . Obviamente que qualquer outra constante poderia desempenhar o mesmo papel. |


**Funções Computáveis e Parcialmente Computáveis** 
Uma função $$\,f\colon \mathbb{N}\to \mathbb{N}\,$$  é $$\,\mathcal{M}$$-parcialmente computável quando existe uma computação $$\,\mathcal{M}_p\,$$ tal que, para todo $$\,x\,$$,   $$\, \mathcal{M}_p(x)\!\downarrow \;\equiv\; f(x)\,$$ .
 Se para todo $$\,x\,$$  a computação $$\,\mathcal{M}_p(x)\,$$ termina, então a função diz-se $$\,\mathcal{M}$$-computável.

**Algoritmo**
Um **algoritmo** é uma descrição finita de uma computação ou conjunto de computações.  Num contexto específico de computações  $$\,\mathcal{M}\,$$ existe uma linguagem $$\,\mathcal{L} \subseteq \{\,0,1\}^\ast\,$$ que contém todos os algoritmos.
 
 A máquina $$\,\mathcal{M}\,$$ fornece as interpretações dos algoritmos em $$\,\mathcal{L}\,$$: cada algoritmo $$\,\mathcal{A}\in \mathcal{L}$$ é interpretado por uma computação $$\,\mathcal{M}_p\,$$ determinado por um programa $$\,p\,$$.   O algoritmo $$\,\mathcal{A}\,$$ sob “input” $$\,x\,$$  determina as computações  $$\,\mathcal{M}_p(x)\,$$.

| O algoritmo $$\,\mathcal{A}\,$$ é um “string”  que pode ser  vista como um elemento de uma  linguagem de “alto nível” $$\,\mathcal{L}\,$$ (como $$\mathtt{C}^{++}$$ , $$\mathtt{Java}$$ ou  $$\,\texttt{Python}$$). Em contraste $$\,p\,$$deve ser vista como “código máquina”. |

Por isso está implícita uma função $$\,\eta\;\colon\; \mathcal{L}\to \{0,1\}^\ast$$  (um “compilador”) $$\,$$que traduz um qualquer $$\,\mathcal{A}\in  \mathcal{L}\,$$ no programa $$\,p\,$$ que o interpreta; para todo “input”  $$\,x\,$$


                                                         $$\,\mathcal{A}(x)\;\equiv\;\mathcal{M}_{\eta(\mathcal{A})}(x)$$$$\,$$

**Definição** 
A linguagem $$\,\mathcal{L}\,$$ é **uniforme**  quando a função de tradução $$\,\eta\,$$ é computável.


| Obviamente uma linguagem algorítmica $$\,\mathcal{L}\,$$ que não seja uniforme não tem muita utilidade porque não é possível computar o programa $$\,p\,$$ que implementa, no modelo de computação $$\,\mathcal{M}\,$$,  os algoritmos em $$\mathcal{L}$$. |


Neste contexto, um algoritmo $$\,\mathcal{A}\in\mathcal{L}\,$$,  interpretado por $$\,\mathcal{M}_p\,$$, é determinístico (respetivamente não-determinístico, probabilístico) sse $$\mathcal{M}_p$$ é determinístico (respetivamente não-determinístico, probabilístico).

A função de $$\,n\,$$

                            $$\,\mu_\mathcal{A}(n)\;\equiv\;\mathbf{P}[\alpha\,\text{termina}\,|\,\alpha\in \mathcal{A}(x) \land |x|=n]$$
                            

designa-se por **probabilidade de paragem** de $$\,\mathcal{A}$$.

        

**Complexidade computacional**
Dado um algoritmo as principais formas de **complexidade computacional** são**:**


    - A **complexidade no pior caso** (“worst case complexity”) é a função de $$n\geq 0$$  
    

          $$\,$$                            $$\mathsf{wcc}_\mathcal{A}(n)\;\equiv\;\mathsf{sup}\,\{ |\alpha|\,|\,|x|=n\land\alpha\in\mathcal{A}(x)\land \alpha\;\text{termina}\}$$
          

    - A  **complexidade** **no caso médio**  ( “average case complexity”) é a função de $$n\geq 0\,$$
    
                            $$\mathsf{acc}_\mathcal{A}(n)\;\equiv\, \mathbf{E}[|\alpha|\,|\,|x|=n\land \alpha\in\mathcal{A}(x)\land \alpha\;\text{termina}]$$


| **Notação assimptótica.**<br>As diversas funções $$\,f(n)\,$$ usadas na caracterização da complexidade raramente se podem definir com exatidão. Quase sempre são definidas de forma assimptótico usando a notação “big O”. <br>Recorde-se que, para quaisquer funções positivas $$\,f,g$$, se tem<br><br>    + $$f(n) = O(g(n))\,$$ se existe uma constante $$c>0\,$$ tal que se tem $$\,f(n) < c\,g(n)\,$$ só não é válido num número finito de valores de $$n$$.<br><br>A partir desta notação existem várias designações que se aplicam ao comportamento assimptótico de uma função positiva $$f(n)$$.<br><br><br>    + $$f(n)$$ é **polinomial** se  $$f(n)=O(n^e)\,$$ para algum $$e\geq 1$$; equivalente a $$f(n)=\mathsf{poly}(n)$$<br>    + $$f(n)$$ é **exponencial** se $$\,f(n) = O(2^{g(n)})\,$$ para algum $$g(n)$$ polinomial; <br>    + $$f(n)\,$$ é **logarítmico** se $$\,2^{f(n)}$$ é polinomial;<br>    + $$f(n)\,$$ é **negligenciável** se  $$\,f(n)\,g(n) = O(1)\,$$ para todo polinomial $$g(n)$$.<br>    + $$f(n)\,$$é **sub-linear** se $$\,\lim_{n\to \infty}\,f(n)/n = 0$$.<br>    + $$f(n)\,$$é **sub-exponencial** se  $$\,f(n) = O(2^{g(n)})\,$$ e $$\,g(n)\,$$ é sub-linear.<br><br>Add a note |

$$$$

## **Funções booleanas**

A título de exemplo vamos considerar os problemas paradigmáticos das funções booleanas.
Estes problemas têm variantes que ocorrem também em outras estruturas: nomeadamente nas fórmulas proposicionais.

Uma função booleana total  $$\,f\,\colon\, \{0,1\}^n \to \{0,1\}\,$$  é completamente determinada por um polinómio booleano a $$\,n\,$$ variáveis. 

Todo o polinómio é definido por operações de soma e multiplicação numa estrutura algébrica aproprida (um *corpo*). Neste caso  a soma $$+$$ é  a operação **xor** e a multiplicação  é o **and**.

| Exemplos de polinómios booleanos com 4 variáveis serão<br>                            $$1 + x_0\, x_2 + x_1\, x_3\quad$$ou $$\quad x_0\, x_1 + x_2+ x_1\, x_2\, x_3\quad$$ou $$\quad x_0 + x_1 + x_2 + x_3$$ |

Um polinómio que usa apenas multiplicações designa-se por *monómio*. Cada monómio é completamente determinado pelo vetor dos seus expoentes. 


| **Exemplo**<br>Nos monómios  com $$4$$ variáveis tem-se<br>         -  $$x_0\,x_2\,x_3\,=\,x_0^1\,x_1^0\,x_2^1\,x_3^1$$                              é representado pela palavra $$\,\mathtt{1011}$$<br>        -   $$x_1\,x_2\,=\,x_0^0\,x_1^1\,x_2^1\,x_3^0$$                                   é representado pela palavra $$\mathtt{0110}$$. |

Nos polinómios booleados os expoentes são sempre $$0$$ ou $$1$$ uma vez que $$\,x^2 = x\,$$. Por isso cada monómio é completamente determinada por um vetor de $$n$$ bits.

Um polinómio é uma soma de monómios e é completamente determinado pelo conjunto dos vetores de expoentes. Note-se que com a soma **xor**  verifica-se $$\,x + x = 0\,$$ para todo $$x$$; por isso na construção do polinómio, dois monómios iguais anulam-se mútuamente.

| Por exemplo<br>$$1 \,=\,x_0^0\,x_1^0\,x_2^0\,x_3^0\;$$ é representado pelo vetor de expoentes $$\;\mathtt{0 0 0 0}$$ enquanto que o monómio $$\,x_0\,x_1\,x_2\,x_3\;$$é representado pelos expoentes  $$\,\mathtt{1 1 1 1}\;$$.<br>Os três polinómios no exemplo acima são descritos pelos seguintes conjuntos de strings<br>                          $$\{\,\mathtt{0 0 0 0}\,,\,\mathtt{1 0 1 0}\,,\,\mathtt{0 1 0 1}\}\quad$$,  $$\quad\{\mathtt{1 1 0 0}\,,\,\mathtt{0 0 1 0}\,,\,\mathtt{0 1 1 1}\}\quad$$,$$\quad\{\mathtt{1 0 0 0}\,,\,\mathtt{0 1 0 0}\,,\,\mathtt{0 0 1 0}\,,\,\mathtt{0 0 0 1}\}$$ |

Considere-se uma linguagem (conjunto de strings)  $$\,\mathcal{L} \subseteq \{0,1\}^n\,$$ como descrição de um polinómio booleano $$\,f\,$$  com $$n$$ variáveis . Vamos esboçar algoritmos para resolver os dois problemas essenciais nas aplicações deste tipo de funções:

    - **valoração** : dado um vetor $$\,x\in \{0,1\}^n\,$$ calcular o valor de $$\,f(x)\,$$.
    - **satisfação** ou **SAT**: determinar se existe algum vetor $$\,x\in \{0,1\}^n\,$$ que “valide”$$\,f\,$$. 
                                     $$\,\exists\,x\in\{0,1\}^n\,\centerdot\,f(x)=1\,$$.

O **algoritmo de valoração** percorre as $$n$$ componentes de $$\,x\,$$ e, para cada uma percorre todos os elementos de $$\,\mathcal{L}$$. É um exemplo paradigmático de algoritmo determinístico.

$$\mathsf{EVAL}(n,\mathcal{L},x)\;\equiv$$

1. Testa o tipo dos argumentos: $$\,n>0\,\land\,|x|=n\,\land\, f\subseteq \{0,1\}^n$$. Se falhar devolve $$0$$.
2. Para $$\,i=0,1,\cdots,n-1$$
    1. Se $$\,x_i=0\,$$ eliminar todos os  $$\,e\in \mathcal{L}\,$$ tais que  $$e_i=1$$          
    2. Fazer $$\,e_i \gets 0\,$$ em todos $$\,e\in \mathcal{L}$$ restantes
    3. Eliminar de $$\,\mathcal{L}\,$$ pares $$\,e,e'\,$$ iguais.
3. Se $$\,\mathcal{L}$$ é vazio o resultado da valoração é $$0$$; em caso contrário será $$\,\mathcal{L}\equiv \{0^n\}\,$$ e o resultado da valoração será $$1$$.

Este algoritmo limita-se a comparar vetores de bits e verificar o valor de componentes individuais de vetores; não executa qualquer operação de soma ou multiplicação.

A sua complexidade computacional  depende crucialmente do número de monómios que ocorrem no polinómio (a cardinalidade de $$\mathcal{L}$$).  No limite o número de monómios é exponencial com $$n$$ e, dado que para cada valor de $$i$$ é necessário percorrer $$\,\mathcal{L}$$ várias vezes, a complexidade máxima do algoritmo não é polinomial.

Porém, muitas vezes o número de monómios é polinomialmente limitado com a dimensão $$n$$; nesse caso já a complexidade deste algoritmo é polinomial. De facto o número de ciclos é linear com $$n$$ e o número de operações executadas em cada ciclo é polinomialmente limitado com $$n$$.

O **algoritmo de satisfação** é mais complexo: mesmo quando o número de monómios é polinomialmente limitado, os melhores algoritmos de SAT têm complexidade exponencial no pior caso. Isto não significa que, no caso médio, não existam algoritmos viáveis.

A computação $$\,\mathsf{SAT}(n,f)\,$$ produz $$\,\bot\,$$ se $$\,f\,$$ não é satisfazível e produz não-deterministicamente algum $$\,x\,$$ tal que $$\,f(x)=1\,$$ quando for satisfazível.
Um polinómio $$f$$ em $$\,n\,$$ variáveis pode ser decomposto  numa soma

                                       $$f \;=\; x_0\,g + h\,$$

em que $$x_0$$ é a primeira variável e $$\,g,h\,$$ são polinómios em $$n-1$$ variáveis que não contém $$x_0$$. Somando $$\,x_0\,h\,$$ duas vezes a decomposição passa a ser

                                     $$f\;=\,x_0\,(g+h) + (1+x_0)\,h$$

Agora, se $$\,y\in\{0,1\}^{n-1}\,$$ é uma solução de SAT para $$\,(g+h)\,$$ então $$\,\langle 1,y\rangle\,$$ é uma solução do SAT para $$f\,$$; analogamente se $$\,y\,$$ é uma solução do SAT para $$\,h\,$$, então $$\,\langle 0,y\rangle\,$$ é uma solução do SAT para $$f\,$$.
Esta decomposição é a base de todos os algoritmos de SAT; o algoritmo é um exemplo paradigmático de algoritmo não determinístico que se define recursivamente

$$\mathsf{SAT}(n,f)\;\equiv$$

1. Se $$\,n=0\,$$ e $$\,f=0\,$$ devolve $$\bot$$ ; se $$\,n=0\,$$e $$f=1$$ devolve a string vazia $$\,\varepsilon\,$$.
2. Se $$n>0\,$$ obtém de $$f$$ os polinómios $$(g+h)$$ e $$h$$ de grau $$n-1$$ como referido atrás.
3. Calcula $$y \gets \mathsf{SAT}(n-1,g+h)\,$$ e  $$\,z\gets \mathsf{SAT}(n-1,h)\,$$.
4. Se $$\,y = \bot\,$$ e $$\,z = \bot\,$$ devolve $$\,\bot\,$$
5. Se $$\,y\neq \bot\,$$então a string  $$\, 1\,y\,$$ é resultado possível; se $$\,z\neq \bot\,$$ então  $$\, 0\,z\,$$ é resultado possível. Escolhe não-deterministicamente um dos resultados possíveis e devolve-o.

Neste algoritmo existem $$n$$ níveis de recursividade (um por variável) e, como a recursividade é dupla, a complexidade no pior caso será $$\,O(2^n)\,$$.

A computação $$\,\mathsf{SAT}(n,f)\,$$ é não determinístico mas tem não-determinismo finito; de facto o número de resultados possíveis está limitado a $$\,2^n\,$$: em cada nível de recursividade, uma execução particular do algoritmo tem um número “escolhas”  $$\leq 2$$  (passo 5).

Como qualquer algoritmo com não-determinismo finito, é sempre possível construir um algoritmo determinístico  $$\,\mathsf{SAT}^\ast\,$$ tal que $$\,\mathsf{SAT}^\ast(n,f)\,$$  devolve, como resultado, o conjunto todos os resultados possíveis de $$\,\mathsf{SAT}(n,f)\,$$.

$$\mathsf{SAT}^\ast(n,f)\;\equiv$$

1. Se $$\,n=0\,$$ e $$\,f=0\,$$ devolve o conjunto vazio $$\,\{\ \}\,$$ ; se $$\,n=0\,$$e $$f=1$$ devolve $$\,\{\varepsilon\}$$.
2. Se $$n>0\,$$ decompõe $$f$$ e obtém os polinómios $$(g+h)$$ e $$h$$ de grau $$n-1$$ como referido anteriormente.
3. Calcula $$y \gets \mathsf{SAT}^\ast(n-1,g+h)\,$$ e  $$\,z\gets \mathsf{SAT}^\ast(n-1,h)\,$$.
4. Calcula $$\,y' \gets  \{1\,a\,|\,a\in y\}\,$$ e $$\,$$$$\,z' \gets \{0\,b\,|\,b \in z\}$$
5. Devolve $$\,y'\,\cup\,z'$$


# Classes de Complexidade

**Problemas e Linguagens**
Genericamente as classes de complexidade agrupam conjuntos numa **hierarquia de classes.** Em computabilidade, um *“conjunto”* (sem qualquer outro qualificativo) é sempre visto como um sub-domínio dos números naturais $$\,\mathbb{N}\,$$; os seus $$\,$$elementos são, geralmente, designados por *objetos*.

A **classe de todos os conjuntos** é representada por $$\,\mathbf{2}^\omega\,$$ (ou  $$\,\mathbf{2}^\mathbb{N}\;$$ou $$\,\{0,1\}^\infty\,$$) e uma classe de complexidade é sempre uma sub-classe de $$\,\mathbf{2}^\omega$$.

Os elementos de uma qualquer classe têm a mesma natureza mas, em complexidade, são interpretados de duas formas distintas: como **linguagens** ou como **problemas**:


    - Uma vez que $$\,\mathbb{N}\,$$ e $$\,\{0,1\}^\ast\,$$ são isomórficos, pode-se interpretar qualquer conjunto como um domínio de strings finitas de bits  $$\,\mathcal{L}\subseteq \{0,1\}^\ast\,$$. Nesse caso $$\,\mathcal{L}\,$$ designa-se por **linguagem** e os seus elementos designam-se por **palavras.**
        
    - Uma segunda opção é ver  $$\,\mathsf{}$$$$\,\mathcal{P}\subseteq \mathbf{2}^\mathbb{N}\,$$ como um conjunto de **soluções** de um determinado problema.
    

No sentido computacional o problema $$\,\mathcal{P}\,$$ representa o processo de, dado um  $$x$$ arbitrário e uma descrição de $$\,\mathcal{P}\,$$, determinar se $$x$$ é ou não solução de $$\,\mathcal{P}\,$$; se for solução, deve-se apresentar uma **prova** (ou **certificado)** de que realmente se verifica $$\,x\in \mathcal{P}$$.

O processo computacional que $$\,$$$$\,\mathcal{P}\,$$ denota é o de “*construir* *uma* *prova da validade de*  $$\,x\in \mathcal{P}$$". Com esta interpretação as classes de complexidade estão diretamente relacionadas com a forma como essas provas são construídas.

Ao invés cada descrição de uma linguagem $$\,\mathcal{L}$$ deve ser interpretada como uma **especificação** de algum sistema feita através de um número, eventualmente infinito, de **restrições.** Os elementos de $$\,\mathcal{L}\,$$  são **modelos** dessa especificação.
O problema que $$\,\mathcal{L}\,$$ representa é o de “*encontrar um modelo* $$\,m\,$$ *que verifique* *todas* *as restrições que a especificação impõe*".

| Note-se que o processo computacional associado a um problema tem ímplícito um quantificador existencial: “*verificar* uma solução” é equivalente a “*encontrar* *******alguma*** prova”. <br><br>Ao invés o processo computacional associado a uma linguagem tem implícito  um quantificador universal: “*encontrar* um modelo” é equivalente a “*verificar* *******todas*** as restrições”. |

Estas duas interpretações estão relacionadas:


    - Verificar  $$\,x\in \mathcal{P}\,$$,  se $$x\,$$ é uma solução do problema $$\,\mathcal{P}\,$$, é equivalente a encontrar uma prova $$\,w\,$$ tal que o par $$\,(x,w)\,$$ é um modelo de uma especificação $$\,\mathcal{L}\,$$.
                                    $$x\in \mathcal{P}\quad\text{sse}\quad \exists\,w\,\centerdot\,(x,w) \in \mathcal{L}$$
        Aqui a linguagem $$\,\mathcal{L}\,$$ determina completamente o problema $$\,\mathcal{P}\,$$.


    - Encontrar um modelo da especificação $$$$$$\, \mathcal{L}\,$$ implica percorrer o espaço dos modelos e verificar, para cada amostragem $$\,m\,$$ e para todas as restrições  $$\,u\,$$, se o par $$\,(m,u)\,$$é solução de um problema específico  $$\, \mathcal{P}\,$$. 
                            $$m\in \mathcal{L}\quad\text{sse}\quad \forall\,u\,\centerdot\, (m,u)\in \mathcal{P}$$
        Agora é o problema $$\,\mathcal{P}\,$$ que determina completamente a especificação.
----------

**Exemplos**

1. O problema da fatorização de inteiros é um problema considerado “difícil” ; é essa dificuldade que permite caracterizar a segurança de criptosistemas como o RSA. 
> Para cada $$\,N>0\,$$ verificar se existe $$\,n> N\,$$ que tenha um factor  menor do que $$N$$.

Neste caso o problema é parametrizado pelo inteiro $$N$$ e define-se como

                    $$\mathcal{P}(N)\;\equiv\; \{n > N \,|\, \exists\,r< N\,\centerdot\, \gcd(r,n) > 1 \}\,$$

O tamanho $$\,|N|\,$$ é o parâmetro que determina a complexidade do problema. 
Neste problema $$\,r\,$$ é a prova e o cálculo de $$\,gcd(r,n) > 1\,$$ é a verificação da prova. O espaço de procura para $$r$$ é limitado por $$N$$; por isso a dimensão do espaço de procura é limitado pelo parâmetro de complexidade do problema.
O máximo dividor comun $$\,\gcd(r,n)\,$$ usa o bem conhecido algoritmo de Euclides que tem complexidade linear com o tamanho do seu maior argumento.

A especificação associada a este problema tem por modelos os conjuntos de pares $$(r,n)$$ que não sejam co-primos: $$\,\mathcal{L}\;\equiv\;\{(r,n)\,|\,r < N\land \gcd(r,n) > 1\}\,$$.


2. A “insatisfabilidade” das funções booleanas ,$$\,\mathsf{unsat}(n)\,$$, parametrizado pelo número de variáveis $$n$$, é um exemplo de uma especificação. 
    Os seus modelos são polinómios $$\,f\,$$ com $$n$$ variáveis e as restrições que têm de verificar é a de não serem satisfazíveis por nenhuma valoração $$\,\upsilon\in\{0,1\}^n\,$$ dessas variáveis.
                        $$\,\mathsf{unsat}(n)\;\equiv\; \{\,f \,|\, \forall\,\upsilon\in\{0,1\}^n\,\centerdot\,f(\upsilon)\neq 1\}$$
    O problema associado a esta especificação é essencialmente o problema da valoração das funções booleanas.
                                             $$\,\mathcal{P}\,=\,\{ (\upsilon,f)\,|\,f(\upsilon)\neq 1\}$$
    Vimos anteriormente que a complexidade do teste $$\,$$$$\,f(\upsilon)\,$$ depende crucialmente do número de monómios que $$f$$ tem (o seu tamanho); quando o “tamanho” de $$f$$ é polinomialmente limitado com $$n$$, a complexidade é polinomial.


----------

**Hierarquia de Classes**

Estes exemplos e as interpretações  às noções de problema e de linguagem, permitem dar uma definição genérica de uma hierarquia de classes.

Uma **hierarquia de classes** é definida por duas sequências crescentes de problemas e linguagens
 $$\,\Sigma_0 \subseteq \Sigma_1 \subseteq \cdots \subseteq \Sigma_n\subseteq \cdots\,$$ e  $$\,\Pi_0 \subseteq \Pi_1 \subseteq \cdots \subseteq \Pi_n\subseteq \cdots\,$$ tais que
 

    1. $$\Sigma_0\;\equiv\;\Pi_0$$
    2. Para $$n>0$$,  $$\mathcal{P}\in \Sigma_n\;$$ sse existe $$\mathcal{L}\in \Pi_{n-1}\,$$ tal que 
                     $$\mathcal{P}\;\equiv\; \{x\,|\,\exists\,w\,\centerdot\, (x,w)\in\mathcal{L}\}\,$$
    3. Para $$n>0$$,  $$\mathcal{L}\in \Pi_n\;$$ sse existe $$\mathcal{P}\in \Sigma_{n-1}\,$$ tal que 
                     $$\mathcal{L}\;\equiv\; \{x\,|\,\forall\,w\,\centerdot\, (x,w)\in\mathcal{P}\}\,$$

Uma hierarquia de classes é completamente determinada pela classe $$\,\Sigma_0\,$$; se $$\,\Sigma_0\,$$ for fechada por complementos (i.e. $$\,\mathcal{P}\in \Sigma_0 \;\text{sse}\; \overline{\mathcal{P}} \in \Sigma_0 \,$$) então a hierarquia diz-se **computável**. 
Numa hierarquia computável tem-se  $$\,\mathcal{P}\in\Sigma_n \;\,\text{sse}\;\, \overline{\mathcal{P}}\in \Pi_n$$ , para todo $$n$$.

Neste curso vamos considerar várias versões da classe $$\,\Sigma_0$$, umas computáveis e outras não, e cada uma delas vai definir uma hierarquia distinta.


1. A primeira hierarquia, designada por **aritmética**, é determinada pela classe dos conjuntos **enumeráveis**. Isto é, cada conjunto $$\,A\in \Sigma_0\,$$ é definido pelos resultados de uma função $$\,f\,$$ computável e crescente:  $$\,A \,\equiv\,\{f(x)\,|\,x\in \mathbb{N}\}$$.
    Equivalentemente cada $$\,A\in \Sigma_0\,$$  pode ser determinado por uma decisão determinística $$D\,$$da seguinte forma: $$\,A\,\equiv\,\{x\,|\,D(x)\;\text{termina com sucesso}\}$$.


    Note-se que todo $$\,A\in\Sigma_0\,$$ é um conjunto enumerável  mas o seu complemento $$\,\bar{A}\,$$ pode não ser enumerável; isto porque $$\,x\in \bar{A}\,$$ pode ocorrer porque $$D(x)$$ não termina ou porque termina em falha.  Por isso a hierarquia aritmética  não é computável.


2. Um conjunto $$\,A\,$$ é **computável** ou **decidível** quando for enumerável e o seu complemento também for enumerável.
    Equivalentemente $$\,A\,$$ é determinado por duas decisões determinísticas $$\,D,D'\,$$ de tal forma que  $$\,x\in A\;\,\text{sse}\;\,D(x)\,$$ termina com sucesso e, também,  $$\,x\in \bar{A}\;\,\text{sse}\;\,D'(x)\,$$ termina com sucesso.


    A hierarquia iniciada com $$\,\Sigma_0\,$$definida pela classe de todos os conjuntos computáveis, designa-se por **aritmética computável.**


3. Ambas as hierarquias anteriores (aritmética e aritmética computável) podem ser relativisadas com a introdução de oráculos. Tomando como parâmetro um oráculo $$\,\Omega\,$$   toma-se como origem da hierarquia a classe $$\,\Sigma_0^\Omega\,$$ dos conjuntos computáveis com a ajuda de consultas ao oráculo $$\,\Omega\,$$.
    A partir desta classe base definem-se as restantes clases da hierarquia $$\,\Sigma_n^\Omega\,,\,\Pi_n^\Omega\,$$.

Na definição destas três hierarquias apenas intervém o grau de compatibilidade da usado na definição da base da hierarquia e o oráculo usado como parâmetro. Nomeadamente não intervêm noções de complexidade.

A complexidade computacional intervém na definição da hierarquia em dois pontos: nos limites à complexidade computacional das decisões usadas (ou, em alternativa, no número de consultas ao oráculo) na definição de $$\,\Sigma_0\,$$ e nos limites à dimensão do espaço de procura nos quantificadores existenciais ou universais usados nas classes de ordem superior.


4. Deste modo define-se uma hierarquia **polinomial** em que a base $$\,\Sigma_0$$ é a classe de todos os conjuntos decidíveis $$\,\mathcal{L}\,$$ com decisões $$D$$ de complexidade polinomial com o tamanho do “input”.  Isto é,  para algum $$b(n)=\mathsf{poly}(n)$$ e para todo $$x$$,


                       $$x\in \mathcal{L}\quad$$sse $$\quad D(x)\;\text{sucede}$$ e $$|D(x)|\leq b(|x|)$$  
                
    Analogamente $$\,\Sigma_0^\Omega\,$$é a classe de todos os conjuntos decidíveis com ajuda ao oráculo $$\,\Omega\,$$e com um número de consultas ao oráculo que é polinomial com o tamanho do “input”.


    Nas classes de ordem superior impõe-se um limite polinomial ao tamanho das variáveis de quantificação.  Por exemplo, a classe $$\,\Sigma_1\,$$é formada por todos os problemas $$\,\mathcal{P}$$ para os quais existe algum $$\,\mathcal{L}\in \Sigma_0\,$$ e um limite $$b(n)=\mathsf{poly}(n)$$  tal que
    
                                $$x\in \mathcal{P}\quad\,\text{sse}\quad\, \exists\,w\,\centerdot\,|w|\leq b(|x|)\,\land\,(x,w)\in \mathcal{L}$$
                            
    Analogamente as classes $$\,\Pi_1\,$$ ou $$\,\Pi_1^\Omega\,$$ são definidas por quantificação universal; $$\,\mathcal{J}\in \Pi_1^\Omega\,$$ quando existe $$\,\mathcal{L}\in \Sigma_0^\Omega\;$$ e $$\;b(n)\in\mathsf{poly}(n)\,$$ tais que 
    
                                      $$z\in \mathcal{J}\quad\text{sse}\quad\forall\,w\,\centerdot\,|w| \leq b\Rightarrow\,(z,w)\in \mathcal{L}$$

      

----------

As hierarquias polinomiais são a referência usual para a caracterização e comparação dos problemas em termos de complexidade. Normalmente, nestas hierarquias, só são relevantes os dois primeiros níveis: $$n=0$$ ou $$n=1$$.
Adicionalmente, como as hierarquias polinomiais são computáveis , as classes $$\Pi_1$$ e $$\Pi_1^\Omega\,$$ são formadas pelos complementos dos problemas em $$\,\Sigma_1$$ e $$\,\Sigma_1^\Omega\,$$ respetivamente. 

Por estes motivos as classes são designadas de forma específica e tem-se


    - A classe $$\,\mathbf{P}\,$$ é outra designação para a classe $$\,\Sigma_0\,$$na hierarquia polinomial. Esta classe designa os problemas ditos “polinomiais”.
    
    - Analogamente  $$\,\mathbf{P}^\Omega\,$$ é outra designação para $$\,\Sigma_0^\Omega\,$$ na mesma hierarquia. Os seus elementos designam-se por “problemas polinomiais com a ajuda do oráculo $$\,\Omega\,$$”.
    
    - A classe $$\,\mathbf{NP}\,$$ é equivalente a $$\,\Sigma_1\,$$na hierarquia polinomial; os seus elementos designam-se por “problemas não-determinísticamente polinomiais”. A versão dessa classe com consultas a num oráculo $$\,\Omega\,$$ , equivalente a $$\,\Sigma_1^\Omega\,$$,  representa-se por  $$\,$$$$\,\mathbf{NP}^\Omega\,$$.
    
    - Designa-se também por $$\,\mathbf{coNP}\,$$a classe $$\,\Pi_1\,$$ na hierarquia polinomial e por $$\,\mathbf{coNP}^\Omega\,$$ a classe $$\,\Pi_1^\Omega\,$$ na mesma hierarquia.


----------

Em princípio $$\,\mathbf{P}\,,\,\mathbf{NP}\,$$e $$\,\mathbf{coNP}\,$$descrevem problemas nos dois primeiros níveis de uma hierarquia de complexidade. Em princípios os níveis superiores, com $$n=2,3,\cdots$$ representam problemas mais complexos que não podem ser descritos nos níveis inferiores.

Porém não é certo que assim seja. Sabemos que, para toda a hierarquia, se verifica $$\,\Sigma_n \subseteq \Sigma_{n+1}\,$$ mas não é certo que as classes sejam distintas: pode acontecer que se verifique $$\,\Sigma_n\equiv\Sigma_{n+1}$$.
Quando isso acontece diz-se que a hierarquia **colapsa** em ****$$n$$. 

Prova-se, com alguma dificuldade, que as hierarquias aritmética, aritmética computável e aritmética computável com oráculo, nunca  colapsam. 
Porém já o mesmo não pode ser dito em relação à hierarquia polinomial. De facto é um dos grandes problemas por resolver nas Ciências da Computação se $$\,\mathbf{NP} \subseteq \mathbf{P}\,$$ se verifica ou não.
O consenso é que muito provavelmente estas duas classes não coincidem.

----------

**Exemplos**
Os algoritmos de “valoração” e “satisfação”  das funções booleanas fornecem  exemplos paradigmáticos nas classes $$\,\mathbf{P}\,$$e $$\,\mathbf{NP}\,$$. 

Considere-se, em primeiro lugar, a seguinte formulação do problema da valoração. Este problema é parametrizado por uma  dimensão $$\,n\,$$ e por uma função boleada descrita por  $$f \subseteq \{0,1\}^n\,$$.

                            $$\mathsf{VAL}_0(n,f)\;\equiv\;\{\,x\;|\;\mathsf{EVAL}(n,f,x) = 1 \,\}\,$$

O problema pertence à classe $$\,\Sigma_0\,$$ na hierarquia aritmética computável; a análise do algoritmo $$\,\mathsf{EVAL}\,$$prova esta afirmação.  
Porém a complexidade desse algoritmo depende de $$\,\#f\,$$; isto é, do número de monómios polinómio $$f$$ ou equivalentemente da cardinalidade de $$\,f\,$$ como linguagem.  De facto, para qualquer limite $$\,b(n)=\mathsf{poly}(n)\,$$existe sempre um par $$(n,f)$$ em que  $$\,|\mathsf{EVAL}(n,f)| > b(n)\,$$.
Por isso o problema $$\,\mathsf{VAL}_0(n,f)\,$$ não está na classe $$\,\mathbf{P}\,$$ apesar de estar na classe $$\,\Sigma_0\,$$.

Uma segunda formulação da valoração parametriza $$\,n\,$$ e inclui $$\,f\,$$ na solução do problema:

                            $$\mathsf{VAL}_1(n)\;\equiv\;\{\,(f,x)\;|\;\mathsf{EVAL}(n,f,x) = 1 \,\}\,$$

Agora, como $$\,f\,$$ faz parte da solução, a complexidade de $$\,\mathsf{EVAL}(n,f,x)\,$$ é comparada com o tamanho do par $$\,(f,x)\,$$.  O tamanho do “input” é aproximadamente $$\,\#\!f\times n\,$$e a complexidade é da ordem de $$\,\#\!f^2\times n\,$$. Por isso $$\,\mathsf{VAL}_1(n)\,\in\,\mathbf{P}$$.

A versão $$\,\mathsf{SAT}\,$$ pode-se formular de forma semelhante

                            $$\mathsf{SAT}(n)\;\equiv\;\{\,f\;|\;\exists\,x\,\centerdot\,\mathsf{EVAL}(n,f,x) = 1 \,\}\,$$

ou, equivalentemente,

                          $$\mathsf{SAT}(n)\;\equiv\;\{\,f\;|\;\exists\,x\,\centerdot\,(f,x)\,\in\,\mathsf{VAL}_1(n) \,\}\,$$

Para cada $$\,n\,$$ este é obviamente um problema da classe  $$\,\Sigma_1\,$$ da hierarquia aritmética computável. A solução do problema é a função booleana $$\,f\,$$ e a prova é o vetor $$x$$.
Como  $$\,\mathsf{VAL}_1\,$$ é um elemento de $$\,\mathbf{P}\,$$, para verificar que  $$\,\mathsf{SAT}(n)\in\mathbf{NP}\,$$ basta verificar que o tamanho da prova é polinomialmente limitada com o tamanho da solução; a menos que o polinómio $$\,f\,$$ seja nulo, esta condição verifica-se trivialmente.

----------


# Redução entre problemas

Em termos gerais o processo de **redução** traduz-se na diminuição da ordem de complexidade de um determinado problema $$\,P\,$$ quando se considera, como oráculo, um outro problema $$\,Q\,$$.

Obviamente a definição e as consequências da redução vão depender da hierarquia usada na classificação dos problemas. Por exemplo:


1. Na hierarquia aritmética, toma-se dois problemas $$\,P,Q\in\Sigma_1\,$$. Se ocorrer   $$\,P\in \Sigma_0^Q$$   diz-se que $$\,P\,$$ é **Turing redutível** a $$\,Q\,$$ e escreve-se  $$\,P\,\leq_T\,Q$$.


    Verifica-se $$\,P \leq_T Q\,$$  quando existe um algoritmo $$\,\mathcal{D}\,$$ que questiona o oráculo $$Q$$ e através de “queries”  da forma $$\,s\in Q\,$$  consegue decidir queries $$\,x\in P$$ através das decisões $$\,\mathcal{D}^Q(x)$$.


2. Na hierarquia polinomial tomam-se dois problemas $$\,P,Q\in \mathbf{NP}\,$$. Se ocorrer $$\,P\in \mathbf{P}^Q\,$$ diz-se que $$\,P\,$$ é **polinomialmente redutível** a $$Q$$ e escreve-se $$\,P \leq Q\,$$. Neste curso esta é a forma implícito de redução quando não se especifica a hierarquia de complexidade.


    Quando ocorre $$\,P \leq Q\,$$estamos a afirmar que existe um algoritmo, de complexidade polinomial com o tamanho do “input”, que a partir de queries $$\,s\in Q\,$$determina a validade das “queries” $$\,x\in P\,$$.

Com a redução polinomial surgem duas noções importantes:


    - Um problema $$\,Q\,$$ é  $$\mathbf{NP}$$-**hard**  quando qualquer problema $$\,P\in \mathbf{NP}\,$$ verifica $$\,P \leq Q$$.


    - Um problema Q é $$\mathbf{NP}$$-**completo**  quando é  $$\,\mathbf{NP}$$-**hard**  e pertence à classe $$\,\mathbf{NP}$$.

Note-se que a classe $$\,\mathbf{NP}\,$$contém $$\,\mathbf{P}\,$$e, por isso, nem todos os problemas $$\,\mathbf{NP}\,$$ são necessaria mente difíceis.  A noção de $$\,\mathbf{NP}$$-**hard** introduz uma complexidade extra porque força qualquer problema $$\,\mathbf{NP}\,$$ a ser redutível ao problema $$\,\mathbf{NP}$$-**hard**.
Porém o problema **hard** pode pertencer a uma classe de complexidade de ordem superior à $$\mathbf{NP}$$; os problemas são **completos** quando além de **hard** pertencem a $$\,\mathbf{NP}$$.




# Circuitos Booleanos e Aritméticos

Circuitos são um modelo importante para os problemas que vamos encontrar ao longo deste curso. 

A função principal de um circuito é a descrição de uma computação funcional complexa através de **operações elementares** numa determinada álgebra.  Por isso, uma parte essencial da descrição do circuito é a escolha do domínio onde se vai realizar a computação e os operadores básicos desse domínio.

Outra componente do circuito é a definição da sua **topologia**; isto é, a forma como as operações básicas se combinam para construir a computação principal.

É possível descrever a topologia de várias formas mas a mais simples é através de **diagramas de operações (“gates”) e conexões (“wires”).**

## Diagramas e Grafos


| Genericamente um **diagrama** é um bi-grafo orientado, acíclico e com pelo menos uma raíz.<br><br>Um bi-grafo orientado é um grafo onde os nodos estão agrupados em dois conjuntos $$\,W\,,\,V\,$$ disjuntos e onde cada ramo tem origem em um nodo de um dos conjuntos e destino num nodo do outro conjunto.<br><br><br>![](https://paper-attachments.dropbox.com/s_C4345B51B4C2741A4C82C3A3DF4848E8816BC4CF429E8B7BF841076C5C08954D_1601237523115_bi-grafo0.png)<br><br><br>Num diagrama os nodos que não são destino de qualquer ramo designam-se por **sources** e os nodos que não são origem de qualquer ramo designam-se por **sinks**. Uma **raíz** do diagrama $$\mathcal{D}\,$$ é um “sink” $$\,r\,$$ tal que, para qualquer “source” $$\,s\,$$ existe um caminho com origem em $$\,s\,$$ e destino em $$r$$. |


Num circuito a sua **topologia** está organizada num diagrama onde os nodos estão agrupados em dois conjuntos,  **gates** e **wires,** e onde  todos os “sinks” são “wires”. As raízes do circuito designam-se por **outputs** e os “wires” que são  “sources”  do circuito designam-se por **inputs**.


![Um circuito $$\,4\times 2$$](https://paper-attachments.dropbox.com/s_C4345B51B4C2741A4C82C3A3DF4848E8816BC4CF429E8B7BF841076C5C08954D_1601241707821_diagram1.png)



O diagrama acima representa um circuito com 6 operadores (três somas, duas multiplicações e uma constante) e 10 conexões. 
Destas conexões, duas são  “outputs do circuito”,  quatro são  “inputs do circuito” e quatro são conexões intermédias ligando “outputs” a “inputs” de operadores. 
Nestes diagramas não existem ciclos: a informação flui sempre dos inputs para os outputs.

Genericamente, um diagrama representa apenas a *topologia do circuito;* isto é, o arranjo das “gates” e de “wires” a que estão ligados. Para completar a definição do circuito é necessária também uma descrição algébrica como veremos em seguida.

O diagrama anterior ilustra como, cada “gate” tem vários “wires” de onde flui informação (os “inputs”) e um só “wire” para onde flui informação (o seu “output”). A informação flui, sempre, na forma de elementos do domínio algébrico do circuito.

Em cada wire, a informação pode fluir  de uma só origem: o exterior do circuito ou uma só “gate”.
Analogamente, cada “wire” envia informação para o exterior do circuito ou então para uma ou mais “gates”.



O bi-grafo que descreve o diagrama anterior é representado em seguida. Note-se os dois tipos de nodos, “gates” e “wires”, que aqui são representados por símbolos distintos.


![](https://paper-attachments.dropbox.com/s_C4345B51B4C2741A4C82C3A3DF4848E8816BC4CF429E8B7BF841076C5C08954D_1601240556945_bi-grafo1.png)




## Descrição algébrica

A descrição algébrica do circuito parte de uma álgebra (um domínio e um conjunto de operadores) e associa a cada “wire” uma variável que toma valores no domínio do circuito e a cada “gate” um operador da álgebra. A descrição é formada por um conjunto de equações, uma por “gate”, da forma
                                             $$\textit{output}\,=\,\textit{operador}(\textit{input}_1,\cdots,\textit{input}_\ell)$$
Em que $$\textit{operador}\,$$ é o operador da “gate” e $$\,\textit{output}\,$$e os $$\,\textit{input}_i\,$$ denotam as variáveis associadas, respetivamente, ao “output” e aos “inputs” da “gate”.

No exemplo anterior associámos multiplicações às “gates” $$g_0$$ e $$g_1$$, somas às “gates” $$\,g_2,g_3\;\text{e}\;g_4$$e uma constante $$\,c\,$$ à “gate” $$\,g_5\,$$. As relações algébricas definidas são, neste caso, 
$$y_0 = w_0\times w_1\;,\quad y_1=w_1\times w_2\;,\quad w_0=x_0+x_1\;,\quad w_1 = x_1+x_2 \;,\quad w_2 = x_3 + w_3 \;,\quad w_3 = c$$
Como no diagrama e no bi-grafo não existem ciclos, e a informação flui sempre dos “inputs” para os “outputs” , é sempre possível manipular as relações eliminando todas as variáveis intermédias.
Neste exemplo teríamos


                          $$y_0\,=\,(x_0+x_1)\times (x_1+x_2) \quad,\quad y_1\,=\,(x_1 + x_2)\times (x_3+c)$$
                        

Após  simplificação, a descrição tem uma equação por cada variável de “output” , o lado esquerdo da equação, e no lado direito tem uma expressão  exclusivamente formada por operadores das “gates” e variáveis de “input”.

Num circuito genérico de dimensão $$\,n\times m\,$$, em que as variáveis de “input” são $$\,x_0,\cdots,x_{n-1}\,$$e as variáveis de “output” são $$\,y_0,\cdots,y_{m-1}\,$$, a descrição é definida por um sistema de equações

                           $$\,y_i\,=\,f_i(x_0,\cdots,x_{n-1})\qquad\text{para}\quad i=0,\cdots,m-1$$

sendo$$\,f_i\,$$ são expressões compostas pelos operadores das “gates” e pela variáveis dos “wires”. 



## Computações e circuitos

Um circuito $$\,\mathcal{C}\,$$ e um valoração $$x$$ das variáveis de  “input” determina sempre uma computação $$\,\mathcal{C}(x)\,$$ da forma que vamos descrever.

Dado que a topologia de um circuito é a de bi-gramo orientado e acíclico, a sua descrição algébrica permite definir computações numa máquina de estados apropriada. 


    - Os estados são **valorações;** isto é, ****conjuntos de associações $$\,(\textit{wire},\textit{value})\,$$ de uma variável a um valor.
    
    - O estado inicia é a valoração $$x$$.
    
    - Uma transição $$\,s\to s'\,$$ ocorre quando existe uma gate $$g$$ cujo “output” $$w$$ não ocorre em $$s$$ e todos os “inputs” $$\,z\,$$ dessa “gate” ocorrem no estado $$\,s\,$$; nesse caso o valor do output $$\,w\,$$ é computado a partir do operador associado à “gate” e dos valores dos “inputs” $$z$$; isto é  
                                                            $$s'\;=\;s \,\cup\,\{\,(w\,,\,g(s.z))\,\}$$

Nesta máquina de estados, podem existir várias computações $$\,\mathcal{C}(x)\,$$; isso depende da ordem com que, em cada estado, são selecionados os diferentes $$w$$ com valor indefinido.
No entanto, qualquer que seja a computação $$\,\mathcal{C}(x)\,$$ela termina no mesmo estado: a valoração em que todo $$w$$ tem um valor definido. 
Por isso, selecionando como resultado os vetor $$\,y\,$$formado pelos valores dos “output wires” do circuito, o resultado $$\,\mathcal{C}(x)\!\downarrow\,$$é sempre o mesmo.
Assim a função

                                  $$\,x\,\mapsto\,\mathcal{C}(x)\!\downarrow\,$$ 

é bem definida e é essa a **função computada** pelo circuito $$\,\mathcal{C}$$.

## Tipos de Circuitos

Essencialmente descrevemos um processo que, a partir da topologia do circuito $$\,n\times m\,$$  sobre o domínio $$\,X\,$$ e dos operadores elementares associados, permite construir uma função computável $$\,f\,\colon\,X^n \to X^m\,$$ .

O processo inverso designa-se por **síntese** do circuito: partindo de uma função computável do tipo $$\,f\;\colon\,X^n\to X^m\,$$pretende-se construir a descrição topológica  e a descrição algébrica que permitem definir essa função.

Obviamente podem existir vários circuitos $$\,\mathcal{C}\,$$ que construam a mesma função. Parece intuitivo afirmar que, se a descrição algébrica é simples, então a descrição topológica será complexa; e vice-versa. Por isso a síntese está associada a uma qualquer forma de optimização: por exemplo, minimizando o número de “gates”.

Existem algumas formas frequentes de circuitos:


    - **circuitos booleanos**
        O domínio é formado pelos valores lógicos $$\,X\equiv\,\{0,1\}\,$$ que também determinam as constantes. Os operadores binários elementares são as conectivas $$\,\mathbf{and}\,,\,\mathbf{or}\,$$e $$\,\mathbf{xor}\,$$, representadas por $$\,\land\,,\,\lor\,,\,\oplus\,$$.
        Quando o número de “outputs” é $$1\,$$, o circuito booleano é completamente determinado por uma única fórmula proposicional.
        
    - **circuitos booleanos vetoriais**
        A informação esta organizada em vetores de bits de um tamanho $$\ell$$ fixo. Assim o domínio é $$\,X\,\equiv\,\{0,1\}^\ell\,$$ e cada elemento desse domínio define uma constante. Os operadores binários são $$\,\land\,,\,\lor\;\text{e}\,\oplus\,$$executadas posição a posição. Cada posição $$\,0\leq i<n\,$$, define um operador unário  que seleciona, em cada $$\,x\in X\,$$, a sua componente $$x_i$$ .


    - **circuitos aritméticos** 
        A informação está organizada em inteiros positivos representáveis com $$\,\ell\,$$ bits. Formalmente o domínio é $$\,\mathbb{Z}_N \,\equiv\,\{k\in\mathbb{Z}\,|\, 0\leq k < N\}\,$$, sendo $$\,N\equiv 2^\ell$$.
        Neste domínio define-se a estrutura algébrica de um anel com soma e multiplicação modular:  $$\,x + y \bmod N\,$$ e  $$\,x\times y\bmod N\,$$. 
        Associando inteiros à sua descrição binárias estão ainda disponíveis todas as operações elementares nos circuitos booleanos vetoriais: $$\,\land\,,\lor\,,\,\oplus\,$$ e seleção de componente.
## Descrição de circuitos e suas complexidades 

O *tamanho de um circuito*  $$\,\mathcal{C}\,$$, representado por $$\,|\mathcal{C}|\,$$, é o seu número de “gates”.  Nesta secção vamos analisar alguns dos principais problemas definíveis através de circuitos, analisar a sua complexidade computacional e relacioná-la com o tamanho do circuito.

        

A maioria destes problemas podem  ser estudados no contexto simplificado dos circuitos booleanos com um único “output”.  Nesse caso a dimensão do circuito coincide com o número dos seus “input wires”.

Em primeiro lugar um circuito é uma entidade finita composto por um número finito de conexões e gates. Por isso, pode ser descrita, numa linguagem apropriada, por uma ‘string’ de bits.

Por outro lado um circuito identifica outras entidades também descritas por uma string finita. Nomeadamente


1. *Linguagem de suporte*
    O circuito $$\,\mathcal{C}\,$$ determina  um conjunto de ‘strings’
                                          $$\mathcal{L}_\mathcal{C}\;\equiv\;\{\,x\;|\; \mathcal{C}(x)\!\downarrow\,=\,1\,\}$$
    Os elementos de $$\,\mathcal{L}_\mathcal{C}\,$$ dizem-se **aceites** pelo circuito $$\,\mathcal{C}\,$$ e $$\,\mathcal{L}\,$$ designa-se por  *linguagem de suporte* de $$\,\mathcal{C}\,$$.
    A linguagem $$\,\mathcal{L}_\mathcal{C}\,$$ é de ordem $$\,n\,$$; isto é todos os seus elementos têm comprimento $$\,n\,$$. É também uma entidade finita e, por isso, também pode ser descrita por uma string de bits.
    
2. *Função booleana*
    Como vimos anteriormente, um circuito booleano $$\,\mathcal{C}\,$$ de dimensão $$\,n\,$$ com um só “output” implementa uma *função booleana* 
                                                    $$\,f_\mathcal{C}(x_1,\cdots,x_n)\,$$
    com exatamente $$\,n\,$$ variáveis. 
    Recorde-se que $$\,f_{C}\,$$, como toda a função booleana, é descrita por um conjunto de monómios é representado  pelo vetor $$\,e\in \{0,1\}^n\,$$dos expoentes das $$\,n\,$$ variáveis. 
    Assim,$$\,f_\mathcal{C}\,$$ identifica-se como um subconjunto de $$\,\{0,1\}^n\,$$; isto é, $$\,f_\mathcal{C}\,$$ é também uma linguagem de ordem $$\,n\,$$ e, portanto, pode ser descrita por uma string finita.


| É importante frisar que o circuito, a função que ele implementa e a linguagem de suporte são entidades distintas. A mesma função pode ser implementada por circuitos diferentes e, igualmente, uma linguagem de ordem $$\,n\,$$ é suporte de circuitos distintos.<br><br>No entanto para cada função booleana $$\,f\,$$ de ordem $$\,n\,$$ existe uma única linguagem $$\,\mathcal{S}_f\,$$formada por todos os $$\,x\in\{0,1\}^n\,$$ que satisfazem $$f$$. Essa linguagem é determinada, a partir de $$\,f\,$$, pelo algoritmo $$\,\mathsf{SAT}^\ast\,$$ que descrevemos anteriormente.<br><br>É interessante comparar a cardinalidade dessas linguagens em alguns casos simples de funções de ordem $$n$$:<br><br><br>1. A função booleana constante $$\,f=1\,$$ tem um único monómio; de facto $$f\equiv \{0^n\}\,$$ . No entanto qualquer $$x\in \{0,1\}^n\,$$ satisfaz $$f$$; por isso o suporte $$\,\mathcal{S}_f\equiv \{0,1\}^n$$.<br>    Neste caso temos uma função em que a função é descrita por um conjunto singular enquanto que o seu suport é a linguagem máxima de ordem $$n$$.<br>2. A *função de Kronecker*  define-se por $$\,f(x)=1 \;\text{sse}\;x = 0\,$$.   O seu suporte é o conjunto singular $$\,\mathcal{S}_f \equiv\{0^n\}\,$$.<br><br>     Esta função pode-se escrever também como<br>                                   $$f(x_1,\cdots,x_n)\,=\,(1+x_1)\,(1+x_2)\,\cdots\,(1+x_n)\,$$<br>     que, por indução em $$n$$,  se verifica que  contém todos os monómios de ordem $$n$$. Portanto a representação de $$f$$ é a linguagem máxima de ordem $$n$$. |



## Família de circuitos e classes de complexidade.

Uma **família de circuitos**   $$\,\mathcal{C}\;\equiv\;\{\mathcal{C}_n\}\,$$ é uma sequência de circuitos em que, para todo $$\,n\,$$, o circuito $$\,\mathcal{C}_n\,$$ tem dimensão $$\,n\,$$.

A família $$\,\mathcal{C}\,$$ é **polinomial** quando  $$\, |\mathcal{C}_n|\,=\,\mathsf{poly}(n)$$ . Uma sequência $$\,\mathcal{C}\equiv\{\mathcal{C}_n\}\,$$ é **uniformemente polinomial** quando for polinomial, computável e a função $$\,n\mapsto \mathcal{C}_n\,$$tem complexidade polinomial.

Note-se que uma sequência $$\,\mathcal{C}\equiv\{\mathcal{C}_n\}\,$$, mesmo que seja polinomialmente limitada, não é  necessariamente computável: pode até ser aleatória. Por isso o facto de ser computável é uma restrição forte; e isso reforça-se com a exigência de a complexidade computacional da função ser polinomial.

Estas condições surgem do  seguinte  teorema

**Teorema** 

> Uma linguagem $$\,\mathcal{L}\,$$ está na classe $$\,\mathbf{P}\,$$se e só se existe uma família de circuitos $$\,\{\mathcal{C}_n\}\,$$ uniformemente polinomial tal que, para todo $$\,n\,$$, a linguagem
>                                                       $$\,\mathcal{L}_n\;\equiv\;\{\,x\,|\,x\in \mathcal{L}\,\land\, |x| = n\}$$
> coincide com a linguagem de suporte do circuito $$\,\mathcal{C}_n\,$$.

Este teorema é muito importante porque permite caracterizar completamente a classe de complexidade $$\,\mathbf{P}\,$$a partir de uma classe particular de circuitos booleanos.

Quando as famílias de circuitos $$\,\mathcal{C}\,$$ são apenas polinomiais (no tamanho dos circuitos) então o mecanismo do teorema determina uma classe de linguagens que contém $$\,\mathbf{P}\,$$ mas também contém outras linguagens que não estão em $$\,\mathbf{P}\,$$. 
Agora pode-se definir

**Definição** 

> $$\,\mathbf{P}/\mathbf{poly}\,$$ é a classe $$\,$$formada por todas as linguagens $$\,\mathcal{L}\,$$ para as quais existe uma família polinomial  de circuitos $$\,\{\mathcal{C}_n\}\,$$ tais que, para todo $$n$$,                                                  
>                                                       $$\,\mathcal{L}_n\;\equiv\;\{\,x\,|\,x\in \mathcal{L}\,\land\, |x| = n\}$$
> coincide com   a linguagem de suporte de $$\,\mathcal{C}_n\,$$.           


Que relação existe entre $$\,\mathbf{P}/\mathbf{poly}\,$$ e $$\,\mathbf{NP}\,$$?

Já vimos que $$\,\mathbf{P}/\mathbf{poly}\,$$ não está contido em $$\,\mathbf{P}\,$$; por isso é natural tentar o nível seguinte : a classe $$\,\mathbf{NP}$$.

Se virmos cada família de circuitos  $$\,\mathcal{C}\,$$ como um oráculo,  é fácil reconhecer cada linguagem  $$\,$$$$\,\mathcal{L}\,\in\,\mathbf{P}/\mathbf{poly}\,$$ como um elemento de  $$\,\mathbf{P}^\mathcal{C}$$  para alguma família de circuitos  polinomial  $$\,\mathcal{C}\,$$. Como os elementos de $$\,\mathcal{C}\,$$ são polinomialmente  limitados em  tamanho, então $$\,\mathcal{L}\,$$ é um elemento de $$\,\mathbf{NP}\,$$.     Portanto $$\,\mathbf{P}/\mathbf{poly} \subseteq \mathbf{NP}\,$$  verifica-se.

Pode-se também  questionar se $$\,\mathbf{P}/\mathbf{poly} \supseteq \mathbf{NP}\,$$verifica-se.
Prova-se que, se for $$\,\mathbf{P}/\mathbf{poly} \supseteq \mathbf{NP}\,$$,  então a hierarquia polinomial colapsa: isto é, tem-se  $$\,\mathbf{P}\,=\,\mathbf{NP}\,$$.  Dado que é credível que a hierarquia polinomial não colapse, as duas classes não coincidem:  deve existir um problema  $$\,\mathbf{NP}$$-**completo** que não está na classe $$\,\mathbf{P}/\mathbf{poly}\,$$.


