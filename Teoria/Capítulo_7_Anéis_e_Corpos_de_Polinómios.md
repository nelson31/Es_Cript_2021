# Capítulo 7:  Anéis e Corpos de Polinómios

## Espaços Vetoriais e Módulos

**Vetores** são a forma mais comum de agregar informação.  Essencialmente são tuplos finitos de elementos $$\,(x_1, x_2,\cdots,x_n)\,$$ que pertencem todos à mesma estrutura algébrica. 
Quando essa estrutura é um corpo $$\,K\,$$ , os vetores determinam o **espaço vetorial**  $$\,K^n\,$$.
Quando a estrutura dos elementos é apenas um anel $$\,R\,$$, os vetores determinam o **módulo**  $$\,R^n\,$$.

| Exemplos de espaços vetoriais de dimensão finita são $$\,\mathbb{Q}^n\,$$ os vetores de racionais; $$\,(\mathbb{F}_2)^n\,$$, as palavras de $$n$$-bits;  genericamente,  $$\,(\mathbb{F}_q)^n\,$$os vetores de $$n$$ componentes num corpo finito arbitrário.<br><br>Exemplos de módulos de dimensão finita são $$\,\mathbb{Z}^n\,$$ vetores de inteiros e $$\,(\mathbb{F}_2[w])^n\,$$ vetores cujas componentes são polinómios de bits de tamanho arbitrário. |

As noções de espaço vetorial e de módulo podem ser generalizados para além dos espaços de vetores. O ponto de partida é sempre um corpo $$\,K\,$$ ou um anel $$\,R\,$$.

Um  $$K$$-**espaço vetorial** é um grupo abeliano $$\,(V,+,0)\,$$ equipado com uma **aplicação bilinear** $$\,K\times V \to V\,$$ que verifica ainda a propriedade:  $$\,a\cdot (b \cdot x)\,=\, (a\times b)\cdot x\,$$. 
A mesma definição usando o anel $$R\,$$ define um $$R$$-**módulo**.

Um $$K$$-espaço vetorial $$\,V\,$$ diz-se **finitamente gerado** quando existe um sub-conjunto finito $$\,\{g_1,g_2,\cdots\,g_n\}\subseteq V\,$$, designado por **base**, tal que qual qualquer $$x\in V\,$$se escreve de forma única como uma soma $$\,x \equiv x_1 + \cdots+x_n\,$$  com $$\,x_i \in K g_i\,$$. Uma condição análoga, substituindo o corpo $$\,K\,$$pelo anel $$\,R\,$$ , define $$R$$-módulo finitamente gerado.


| **Exemplo** Considere-se o espaço vetorial $$\,\mathbb{Q}^n\,$$ e uma sua base $$\,\mathcal{B}\equiv\{g_1,\cdots,g_n\}\,$$. <br>As somas formais $$\,x = x_1 + \cdots + x_n\,$$ , em que  $$\,x_i \in \mathbb{Z}g_i\,$$ para todo  $$i=1,\cdots,n\,$$, determinam um  $$\mathbb{Z}$$-módulo  com os mesmos geradores. Vamos designar por $$\,\mathcal{L}(\mathcal{B})\,$$ este $$\mathbb{Z}$$-módulo. <br>Note-se que os  elementos de $$\,\mathcal{L}(\mathcal{B})\,$$ são ***múltiplos inteiros*** dos elementos da base. Por isso formam  um subconjunto de $$\mathbb{Q}^n\,$$ que não coincide com esse espaço vetorial.<br>As estruturas do tipo $$\,\mathcal{L}(\mathcal{B})\,$$ são exemplos de **reticulados** (“**lattices**") e os problemas difíceis que definem estão na origem de quase todas as técnicas criptográficas pós-quânticas. |

## Polinómios em anéis quociente.

Seria interessante equipar o espaço vetorial $$\,K^n\,$$ com uma estrutura algébrica mais rica; por exemplo, adicionando-lhe uma multiplicação e construindo um PID.

Existe uma solução que obtém o primeiro objetivo mas não o segundo. Vendo $$\,K^n\,$$ como o domínio do produto de anéis $$\,K\otimes \cdots \otimes K\,$$ construímos um anel em que a multiplicação se define componente a componente. Porém esta estrutura não é um PID.

O anel de polinómios $$\,K[w]\,$$ é um PID e seria interessante ver de que forma $$\,K^n\,$$se identifica com um sub-domínio desse anel. Em princípio o objetivo não parece difícil de atingir; “basta” codificar cada $$\,(x_1,x_2,\cdots,x_n)\,$$num polinómio  $$\,f \equiv x_1 + x_2\,w + \cdots+ x_n\,w^{n-1}\,$$.

O espaço vetorial $$\,K^n\,$$ identifica-se deste modo com o subconjunto $$\,K[w]_n\,\subset\, K[w]\,$$ formado pelos polinómios de grau inferior a $$n$$ . Mas $$\,K[w]_n\,$$ só  coincide com um sub-anel de $$\,K[w]\,$$ quando $$n=1$$. 

| Multiplicando dois elementos de $$\,K[w]_n\,$$  o resultado está em $$\,K[w]_{(2n-1)}$$ e só se $$n=1$$ se tem $$n = (2n-1)$$. |

 Para cingir um sub-anel de  $$\,K[w]$$ à cardinalidade de $$K^n\,$$ é necessário definir multiplicação como multiplicação modular e a construção de um **anel quociente**. 
 
Esta  estratégia foi já usada para construir, a partir do PID $$\,\mathbb{Z}\,$$os anéis finitos $$\,\mathbb{Z}_n\cong \mathbb{Z}/n\mathbb{Z}\,$$. Como $$\,K[w]\,$$ partilha com $$\,\mathbb{Z}\,$$a propriedade de ser um PID, a mesma técnica pode ser usada.


    1. Escolhe-se um módulo $$\,\phi \in K[w]\,$$ de grau $$n$$.
    2. Define-se o anel quociente  $$\,K[w]_\phi\, \cong \,K[w]/\phi K[w]\,$$.       
        O espaço vetorial  $$\,K[w]_n\,$$ é isomórfico com $$\,K[w]_\phi\,$$.


| Existe uma diferença subtil entre  $$\,\mathbb{Z}_n\,$$ e $$\,\mathbb{Z}/n\mathbb{Z}\,$$ , do mesmo modo que existe uma diferença entre $$\,K[w]_n\,$$ e $$\,K[w]/\phi K[w]\,$$.<br><br>Os elementos de $$\,\mathbb{Z}_n\,$$ são **inteiros** num intervalo com $$n$$ elementos: tipicamente  $$\,\{0,1,\cdots,n-1\}\,$$;  os elementos de $$\,\mathbb{Z}/n\mathbb{Z}$$ são **classes** de equivalência.<br>Somas e multiplicações em $$\,\mathbb{Z}_n\,$$ são modulares; isto é, são executadas em $$\mathbb{Z}$$ com arredondamento módulo $$n$$. Somas e multiplicações em $$\,$$$$\,\mathbb{Z}/n\mathbb{Z}$$ operam em classes e produzem classes: por exemplo, sendo $$x$$ e $$y$$ classes de quivalência, a classe $$\,x \times y\,$$ é formada por todos os inteiros $$a\times b\,$$ com $$\,a\in x\,$$ e $$\,b\in y$$.<br><br>Do mesmo modo os elementos de  $$\,K[w]_n\,$$ são **polinómios** , enquanto que os elementos de $$\,K[w]/\phi K[w]\,$$ são **classes** de equivalência. As somas e multiplicações em $$\,K[w]_n\,$$ **modulares:** são feitas primeiro sobre polinómios e depois são seguidas  de redução módulo $$\phi$$. As somas e multiplicações em $$\,K[w]/\phi K[w]\,$$ operam sobre classes e produzem classes como resultado. |


Várias das técnicas criptográficas mais recorrem a um anel da forma  $$\,K[w]/\phi K[w]\,$$ escolhendo apropriadamente o corpo $$\,K\,$$ e o módulo $$\,\phi\,$$. Nessas técnicas, a multiplicação de polinómios é sempre a operação mais complexa e a escolha desses parâmetros pretende sempre optimizar essa operação. Daí resultam algumas estratégias que são quase “standard”.

Alguns exemplos:


1.  $$\,K \equiv \mathbb{F}_q\,$$  *é um corpo primo e o módulo é*  $$\,\phi \equiv w^n + 1\,$$, *sendo* $$\,n\,$$ *uma potência de* $$\,2\,$$*que verifica* $$\,q \equiv 1 \bmod 2\,n\,$$. 


    Esta é a configuração que permite definir a transformada NTT-CRT #ntt #crt e que vimos anteriormente.


    Neste caso,  todas as $$\,n\,$$ raízes de $$\,(w^n+1)\,$$ são distintas e elementos de $$\,\mathbb{F}_q\,$$; o módulo $$\,\phi\,$$ factoriza em monómios $$\,(w-s)\,$$ definidos pelo seu conjunto de raízes.


    Desta forma cada $$\,f \in K[w]_n\,$$ pode ser descrito pelo vetor $$\hat{f} \equiv (f(s_0),\cdots,f(s_{n-1}))\,$$,  a sua transformada NTT-CRT, determinado pelos valores de $$\,f\,$$em cada uma das raízes de $$\,\phi\,$$.


    No domínio das transformadas somas e multiplicações de polinómios são executadas componente a componente; portanto, com complexidade linear com $$n$$. O cálculo  transformada e da sua inversa têm complexidade $$\,O(n\log n)\,$$; porém se uma primitiva criptográfica usa várias somas e multiplicações, todas as operações intermédias podem ser efectuadas sempre no domínio das transformadas; o cálculo da transformada só se executa uma vez, nos “inputs” da primitiva, e a inversa também só é calculada uma vez, no “output”.
    
2. $$K \equiv \mathbb{F}_q\,$$*é um corpo primo e o módulo tem a forma* $$\,\phi \equiv (w^n-1)\,$$ *sendo* $$\,n\,$$*um primo tal que* $$\,\tau(w) \equiv \phi(w)/(w-1)\,$$  *é irredutível em*  $$\,\mathbb{F}_q[w]\,$$*.*


    Anéis deste tipo são importantes na definição das *matrizes cíclicas* que ocorrem num grande número de códigos criptográficos e também no criptosistema  NTRU.
    
    É conveniente, neste modelo,  representar os elementos de $$\,\mathbb{F}_q$$ por inteiros no **intervalo centrado**  $$\,\{-d,d\}\,$$ com $$\,d \equiv (q-1)/2\,$$. É também frequente usar valores de $$\,q\,$$muito grandes (muito maiores do que $$n$$) de tal forma que, como primeira aproximação, se pode supor que as somas e multiplicações se realizam com polinómios de coeficientes inteiros abstraindo-nos do facto de estas operações serem modulares.


    Como aproximação, pode-se assumir que as operações se realizam em  $$\,\mathbb{Z}[w]/(w^n-1)\mathbb{Z}[w]$$. Note-se que em $$\,\mathbb{Z}[w]\,$$ , o polinómio $$\,\tau(w)\,$$ é o polinómio ciclotómico de ordem $$n$$ e, por isso, é sempre irredutível.


| **Exemplo**<br>Tome-se  o caso $$\,n=5\,$$, o módulo $$\,\phi = (w^5-1)\,$$, e um qualquer  $$\,h\in \mathbb{Z}[w]_5\,$$; por exemplo o polinómio $$\,h(w) \equiv 2 -w + w^3 + 2w^4\,$$. Os coeficientes de $$\,h\,$$ formam o vetor $$\bar{h}\,\equiv \, (2,-1,0,1,2)\,$$.<br><br>Calculando $$\,w\,h(w)\bmod (w^5-1)\,$$obtém-se $$\,(2+2w-w^2+w^4)\,$$ cujos coeficientes formam o vetor $$\,\overline{w\,h}\,\equiv\,(2,2,-1,0,1)\,$$. Note-se que $$\,\overline{w\,h}\,$$ se obtém aplicando “right-shift-rotate” ao vetor $$\,\bar{h}\,$$.<br><br>O operador “right-shift-rotate” denota-se aqui por $$\,\text{rsr}\,$$. <br><br>Procedendo do mesmo modo constrói-se os vetores de coeficientes para os vários polinómios <br><br>                                 $$\,(h(w),w h(w),w^2 h(w),\cdots,w^{n-1}\,h(w))\,$$<br>                                 <br>Os respetivos vetores de coeficientes obtêm-se por aplicações sucessivas do operador $$\text{rsr}\,$$ ao vetor inicial $$\,\bar{h}\,$$. Desta forma  constrói-se uma matriz $$\,\mathbf{rot}(h)$$ de rotações de $$h\,$$ cujas linhas formam o vetor de vetores<br><br>                                $$\mathbf{rot}(h)\,\equiv\,(\bar{h}, \text{rsr}(\bar{h}), \text{rsh}^2(\bar{h}),\cdots,\text{rsr}^{n-1}(\bar{h}))$$<br>                                <br>O nosso exemplo a matriz será<br><br>                               $$\mathbf{rot}(h)\,\equiv\,\begin{pmatrix} 2 & -1 & 0 & 1 & 2 \\ 2 & 2 & -1 & 0 & 1 \\ 1 & 2 & 2 & -1  & 0 \\ 0 & 1 & 2 & 2 & -1 \\ -1 & 0 & 1 &2 & 2 \end{pmatrix}$$<br>                               <br>Isto é um exemplo de uma **matriz cíclica:** uma matriz que é completamente determinada pela sua primeira linha e pelo operador “right-shift-rotate”. |


Se se pretender multiplicar $$\,h\,$$ pelo polinómio $$\,f \equiv f_0 + f_1 w + \cdots + f_4\,w^4\,$$ pode interpretar o produto $$\,f\ast h \,$$ como  $$\,f_0\,h + f_1\,(w\,h) + \cdots + f_4\,(w^4\,h)\,$$. Ou seja

                                                           $$\overline{f \ast h} \,=\, \bar{f} \times \mathbf{rot}(h)\,$$
                                                           
Portanto, como vetores de coeficientes, a multiplicação de $$\,f\ast h\,$$ no anel $$\,\mathbb{Z}[w]/(w^n-1)\mathbb{Z}[w]\,$$ , identifica-se com a multiplicação matricial do vetor de coeficientes $$$$$$\,\bar{f}\in \mathbb{Z}^n\,$$ com a matriz $$\,\mathbf{rot}(h)\in \mathbb{Z}^{n\times n}$$.


----------

O criptosistema NTRU, que iremos descrever na próxima secção, é caracterizado por uma relação com uma forma particular, própria deste tipo de criptosistemas


                                $$\, f \ast h \,\equiv\, g  \mod q \mod (w^n-1)$$
                                

com $$\,f,h,g\,\in\,\mathbb{Z}[w]_n\,$$: isto é, polinómios de coeficientes inteiros de grau inferior a $$n$$.

Esta relação verifica-se se e só se existir algum polinómio  $$\,f'\in \mathbb{Z}[w]_n\,$$ tal que


                        $$f\ast h + f'\ast q \equiv g  \mod (w^n-1)$$ 

Matricialmente pode-se escrever a relação como


                                $$\begin{pmatrix} \,f &  f'\,\end{pmatrix}\times \begin{pmatrix} {1}_n &  \mathbf{rot}(h) \\ 0_n & q\,1_n \end{pmatrix}\;=\;\begin{pmatrix} f & g \end{pmatrix}$$

A matriz $$\,(2n \times 2n)\,$$  que acabámos de construir


                            $$\mathcal{L}_q(h)\;\equiv\; \begin{pmatrix} 1_n & \mathbf{rot}(h) \\ 0_n & q\,1_n\end{pmatrix}$$

é designada por **matriz NTRU** . Vemos que é completamente determinada pelo polinómio $$\,h\,$$ e pelo módulo $$\,q\,$$ e concentra toda a informação que é necessário conhecer sobre as operações modulares num tal sistema.

Vamos ver que o polinómio $$\,h\,$$ é a informação pública do criptosistema enquanto que o par $$\,(f,g)\,$$ é informação privada. A relação matricial diz-nos que a informação privada é uma combinação linear inteira da informação pública.

Isto parece-se, e é, um reticulado. Este tipo de relação matricial ilustra como relações polinomiais inteiras e reticulados estão muito interligados; nomeadamente é possível relacionar a segurança de criptosistemas descritos por relações polinomiais com a complexidade de problemas difíceis definidos nos reticulados.



# Criptosistemas Polinomiais: NTRU e RLWE

Como ilustração de criptosistemas polinomiais, que usam as técnicas que já descrevemos, vamos apresentar os princípios fundamentais de duas das mais populares abordagens à construção de criptosistemas algébricos em criptografia pós-quântica: o NTRU e o RLWE. 

| Das 26 candidaturas aceites à segunda ronda do concurso PQC-NIST,  10 destas candidaturas implementam diretamente um destes paradigmas ou estão relacionadas com eles. |

Em relação aos criptosistemas NTC (“number theoretic cryptography”) , como o RSA ou o DSA, os esquemas PQC apresentam, genericamente, dois tipos de vantagens:

    - **imunidade quântica e segurança operacional** 
            Em termos de segurança, serem resistentes a ataques que envolvam computação quântica, é um objetivo fundamental mas não é único. A par desse objetivo, recentemente têm sido expressas preocupações relacionados com a implementação concreta da NTC que, mais do que a imunidade quântica, tornam urgente a sua substituição. A PQC fornece essas novas garantias de segurança operacional.
    - **eficiência computacional** 
            As implementações PQC oferecem melhorias substanciais em tempos de execução quer na geração de chaves quer ainda na cifra, na assinatura digital e na autenticação.

Estas vantagens têm, como contrapartida, uma grande desvantagem: um aumento substancial da **complexidade descritiva**.  Tanto o NTRU como o RLWE, tal como todas a PQC, usam chaves, criptografias e assinaturas, substancialmente maiores dos que as usadas em NTC.

Assim a melhoria das implementações PQC incide principalmente em metodologias de compressão  da informação sem comprometer a sua segurança e eficiência computacional. 
No NTRU e no RLWE, estratégias distintas de parametrização e optimização da implementação dão origem às suas várias variantes ; isto justifica porque é que  o concurso PQC NIST tem tantas candidaturas diferentes baseadas nos mesmos princípios.

Nesta apresentação vamos concentrar-nos essencialmente nos princípios e não nas várias optimizações possíveis. Obviamente as estratégias de optimização são importantes porque, no final,  é a qualidade dessas optimizações que dita a expectativa de sucesso de cada  variante. 

            


## Criptosistema NTRU

O NTRU tem uma extensa história de variantes umas com sucesso e outras não.  A que vamos aqui apresentar não é nenhuma das candidaturas NIST PQC mas é antes a versão básica descrita no artigo “[NTRU and Lattice Based Crypto. Past, Present and Future” de J.H.Silverman](https://www.dropbox.com/s/izjl28320tqupnn/NTRU%2BSilverman.pdf?dl=0).

**Parametrização**

Definem-se parâmetros $$\,(n,q,p,t)\,$$ de acordo com os seguintes objetivos


1. A estrutura algébrica básica é o anel quociente de polinómios inteiros 
                                $$\mathcal{R}\;\equiv\;\mathbb{Z}[w]/(w^n-1)\mathbb{Z}[w]$$
    sendo $$\,n\,$$ um primo no interalo   $$\,\{250,\cdots,2500\}\,$$. Os elementos deste anel são representados por polinómios  $$\,f\in \mathbb{Z}[w]_n\,$$ ou, equivalentemente, por vetores de coeficientes $$\,\bar{f}\in\mathbb{Z}^n\,$$.


    A multiplicação em $$\,\mathcal{R}\,$$,  $$\,g = f\ast h\,$$, designa-se por *convulsão* e verifica
                                $$\,g_k \,=\, \sum_{j}\,f_j\ast h_{(k-j)\bmod n}$$
    Vimos anteriormente que esta multiplicação pode também ser calculada como uma multiplicação de um vetor por uma matriz
                                $$\bar{g}\;=\; \bar{f} \times \mathbf{rot}(h)$$
2. Dois outros parâmetros são um primo $$\,q > n\log_2(n)\,$$ e um pequeno primo $$\,p=3\,$$.  
    - Dado qualquer inteiro  $$\,x\in\mathbb{Z}\,$$, define-se o  **arredondamento** $$\,{\lceil x \rfloor}_q\,$$ como o inteiro $$\,x'\,$$ tal que $$\,x \equiv x'\bmod q\,$$ e $$\,|x'| < q/2 \,$$. 
    - Define-se o arredondamento $$\,{\lceil x \rfloor}_p\,$$ como $$\,x'\in \{-1,0,1\}\,$$ tal que $$\,x \equiv x' \bmod p\,$$. 
    - Para um polinómio $$\,f\in \mathbb{Z}[w]_n\,$$ ou, equivalentemente,  o seu vetor de coeficientes $$\,\bar{f}\in \mathbb{Z}^n\,$$ , ambos os arredondamentos se aplicam componente a componente.
3. O **espaço das mensagens** é  $$\,\mathcal{M} \,\equiv\, \{-1,0,1\}^n\,\subseteq\,\mathbb{Z}^n\,$$.  
4. O parâmetro $$\,t \leq n\,$$ é usado na definição de “pequeno vetor”.  O espaço dos **pequenos vetores** é o domínio  $$\,\mathcal{M}_t \subset \mathcal{M}\,$$ dos vetores $$\,s\,$$ que verificam $$\,\|s\| \leq t\,$$  e  $$\,|\sum_i s_i| \leq 1\,$$.

**NTRU-PKE**

**Keygen** 

    Como “input” recebe os parâmetros públicos $$(n,q,t)\,$$; usa $$\,p=3\,$$.
        1. Gerar aleatoriamente  $$\,F,G \gets \mathcal{M}_t\,$$; definir $$\;f\equiv 1 + p\,F\;$$ e $$\;g = p\,G\,$$.
        2. Verificar em $$\mathcal{R}$$, se  $$\,f\,$$ é invertivel módulo $$\,q\,$$; isto é, se existe $$\,f'\,$$ tal que
                                $$\,f'\ast f\equiv 1 \bmod q$$
            Se não existir tal $$f'\,$$ repetir a partir de i.
        3. Calcular $$\,h \gets \lceil f'\ast g \rfloor_q\,$$
     Como “outputs” produzir a chave privada  $$\,\mathbf{sk}\equiv (f,g)\,$$ e a chave pública  $$\,\mathbf{pk}\equiv h$$.

 
 **Encrypt** 

    Como “inputs”  recebe a chave pública  $$\mathbf{pk} = h\;$$e a mensagem a cifrar $$\,m\in \mathcal{M}$$.
        1. Gerar aleatoriamente $$\;r\gets \mathcal{M}_t$$
        2. Calcular $$\,e \gets {\lceil m +  h\ast r \rfloor}_q$$
    Como “output”  produz o criptograma  $$\;\mathbf{c} \gets  e$$

**Decrypt** 

    Como “inputs” recebe a chave privada $$\;\mathbf{sk} = (f,g)\;$$e o criptograma $$\;\mathbf{c}\,=\,e$$.
        1. Calcular $$\,a \gets \lceil f \ast e \rfloor_q$$
        2. Calcular $$\;m' \gets \lceil a \rfloor_p$$
    Como “output” produzir a mensagem decifrada  $$\,m'\,$$.


| **Correção** :  $$\,m = m'\,$$<br>Tem-se <br><br>        1.  $$\,e \equiv m + f' \ast g \ast r \bmod q$$ —  pela definição de $$\,h\,$$<br>        2. $$\,a \equiv f\ast e \equiv f\ast m + g\ast r\bmod q$$ — porque  $$\;f\ast f' \equiv 1 \bmod q$$<br>        3.  $$\,a \equiv m + p\,(F\ast m + G\ast r) \mod q\;$$ — por substituição de $$\,f\,$$e $$\,g\,$$ <br>        4.  $$\,a = m + p\,(F\ast m +G\ast r)\;$$ — porque $$\,F,G,r,m\,$$ são pequenos vetores<br>        5. $$\,a \equiv m \bmod p\;$$  — por cancelamento do múltimo de $$p$$.<br><br>Portanto    $$\,m' \,=\,\lceil a\rfloor_p \,=\,  m$$.<br><br>O ponto crítico  é a passagem de (iii) para (iv). O valor de $$\,q\,$$ tem de ser suficientemente elevado, comparativamente com $$\,a\,$$ e $$\,\epsilon\,$$ , para garantir que $$\,a\equiv \epsilon \mod q\,$$ implica a igualdade $$\,a = \epsilon$$. |

| **Segurança** <br>A segurança do NTRU assenta na complexidade de dois problemas:<br><br><br>1. inverter a chave pública $$h$$: <br><br>      — determinar “pequenos”  polinómios $$(f,g)$$  tais que $$\,f\ast h \equiv g \bmod q$$.<br><br>1. inverter o criptograma $$e$$: <br><br>      — determinar  “pequenos” polinómios $$\,(r,m)\,$$ tais que $$\,r\ast h \equiv e - m \bmod q$$.<br><br>Ambos os problemas são difíceis, mesmo num modelo de computação quântica: de fato são ambos redutíveis a problemas standard no reticulado gerado pela matriz  $$\,\mathcal{L}_q(h)\,$$ definido na secção anterior. Mais adiante, quando estudar-mos os problemas difíceis em reticulados, analisaremos de novo esta questão. |




## Problemas  RLWE-PKE/KEM

#LPN #LWE #RLWE

**RLWE**  é uma abreviatura de “Ring Learning With Errors”. Como o nome indica são criptosistemas algébricos assentes em anéis de polinómios e baseados nos problemas de aprendizagem. 

A aplicação do **RLWE**  em esquemas PKE/KEM é essencialmente baseada na abordagem de Lyubashesvky, Peikert e Regev (LPR) publicada em  2013.  A documentação sobre o LPR, incluindo três das candidaturas NIST PQC nele baseadas, pode ser vista [aqui.](https://www.dropbox.com/sh/yudktk90vn2xjet/AAAWaRr5EaP3q7Vqz9TUdi9Ja?dl=0)  Como exemplo de implementação concreta de um tal criptosistema  vamos usar a descrição da [candidatura NewHope](https://newhopecrypto.org) que consta nessa documentação.

O ponto de partida é a versão original do problema  ****designado por **Learning With Errors (LWE)** que foi apresentado por Regev em 2005. Nessa altura provou-se que, num modelo de computação quântica, resolver o LWE era tão difícil quanto resolver o pior caso de problemas difíceis em reticulados. 

O problema  LWE pode ser visto como uma generalização do LPN (“Learning Parity With Noise”) que vimos na sessão anterior.   Essencialmente pretende-se “aprender” ou “recuperar” um vetor segredo $$\,\mathbf{s}\in \mathbb{Z}_q^n \,$$ a partir  de $$\,m\,$$equações lineares perturbadas com um “pequeno” erro

                                $$\,\mathbf{a}_i\cdot \mathbf{s} \equiv {b}_i + e_i \mod q\quad$$                para $$\,i=1,\cdots,m$$

Os vetores $$\,\mathbf{a}_i\in \mathbb{Z}_q^n\;$$ e as constantes $$\;{b}_i\in \mathbb{Z}_q\,$$ são dados do problema; os valores  $$\;e_i\gets \chi\,$$ são “pequenos erros”  desconhecidos,  produzidos em  $$\,\mathbb{Z}_q\,$$ por um gerador aleatório $$\,\chi\,$$. 

Este problema, designado **search LWE**  ou **sLWE,** formaliza-se a partir de um gerador em $$\,\mathbb{Z}_q^{n+1}$$

                    $$\,\mathbf{lwe}({s}) \,\equiv\, \vartheta\,{a}\gets \mathbb{Z}_q^n \,\centerdot \vartheta e \gets \chi \,\centerdot\, ({a}\,,\,b = {a}\cdot{s}+e \bmod q)$$

A solução do “search” LWE é um algoritmo probabilístico polinomial $$\,\mathcal{A}\,$$ que  verifica

                                $$\,\mathbb{P}[s' = s\,|\, s' \gets \mathcal{A}^{\mathbf{lwe}(s)}]\,\simeq 1$$ 

A variante decisional deste problema, designada por  **dLWE,** tem como solução uma decisão $$\,\mathcal{D}\,$$ , polinomial no número de consultas ao oráculo,   tal que

                                $$|\,\mathbb{P}[\mathcal{D}^{\mathbf{lwe}(s)}] \,-\, \mathbb{P}[\mathcal{D}^{\Omega}]\;| \,>\,0$$

em que $$\,\Omega\,$$ é “hash” aleatório  com “output” em $$\,\mathbb{Z}_q^{n+1}\,$$. Essencialmente a solução do problema  decisão consegue distinguir o oráculo $$\,\mathbf{lws}(s)\,$$ de um oráculo aleatório com o mesmo tamanho.

----------

 
É possível construir criptosistemas baseados diretamente neste  **LWE** ; no entanto esses sistemas, para serem verdadeiramente seguros, têm necessidade de armazenar um grande número de amostragens do oráculo $$\,\mathbf{lwe}(s)\,$$; concretamente, o valor de $$\,m\,$$é muito elevado e todas as equações $$\,(\mathbf{a}_i,b_i)\,$$ têm de ser armazenadas.

Para ser possível  construir um sistema verdadeiramente implementáveis é necessário reescrever os problemas na forma polinomial. 

No  LWE   os $$a_i$$ e $$s$$ são vetores e os $$b_i$$ são constantes; cada  $$\,a_i \cdot s \approx b_i$$ produz apenas uma equação aproximada.  No RLWE  os $$\,a_i,s,b_i\,$$ são todos polinómios e, em vez de produto interno, usa-se a multiplicação polinomial; assim cada  $$\,a_i\ast s \approx b_i\,$$ gera tantas equações aproximadas quanto o grau dos $$\,b_i\,$$.


## Criptosistemas RLWE-PKE/KEM

**Parametrização**

Definem-se parâmetros $$\,(n,q,\chi)\,$$ de acordo com as seguintes regras


1. Seja $$\,n\,$$ uma potência de $$2$$ e seja $$\,q\,$$ um primo tal que $$\,q \equiv 1 \mod 2n\,$$. Sejam  $$\,d\equiv\,\lfloor q/2\rfloor$$  e $$\;\ell\,\equiv\, \lceil d/2 \rceil$$. Se $$\,q> 1 +2n\,$$será $$\,d = (q-1)/2\,$$ e $$\,\ell = d/2$$.
2. Os elementos de $$\,\mathbb{Z}_q\,$$ são representados por inteiros no intervalo $$\,[-d,d]$$ ;  o arredondamento de $$\,x\in \mathbb{Z}\,$$  é o inteiro $$\lceil x\rfloor_q$$  nesse intervalo tal que $$\,x\equiv \lceil x\rfloor_q\bmod q$$. 
3. A **norma**  $$\,\|x\|\,$$define-se com $$\,\min\{x,q-x\}\,$$, se $$x\,$$é representado no intervalo $$[0,q-1]\,$$, ou como $$\,|x|\,$$, se $$x$$ está representado no intervalo $$\,[-d,d]$$ .  A **distância**  entre dois $$\,x,y\,\in\mathbb{Z}_q\,$$  define-se, em qualquer dos casos,  como $$\,\|x-y\|\,$$. 
| A máxima distância entre quaisquer  $$\,x,y\in\mathbb{Z}_q\,$$ é sempre $$d$$. Note-se que os valores $$\,-\ell$$ e $$\,+\ell$$ estão à distância máxima. |

4. Seja  $$\,f \in \mathbb{Z}[w]$$  o polinómio $$\, (w^n + 1)\,$$ .
        Em $$\,\mathbb{Z}[w]\,$$ este polinómio é irredutível; de facto coincide com o [polinómio ciclotómico](https://en.wikipedia.org/wiki/Cyclotomic_polynomial) $$\,\Phi_{2n}\,$$. Porém, em $$\,\mathbb{Z}_q[w]\,$$ é factorizável em monómios  $$\,(w-s)\,$$ para cada uma das raízes de $$\,-1\,$$ de ordem $$\,n\,$$ em $$\,\mathbb{Z}_q$$.
5. As estruturas algébricas básicas são os anéis quociente de polinómios
                    $$\mathcal{R}\;\equiv\;\mathbb{Z}[w]/f\,\mathbb{Z}[w]\quad\text{e}\quad\mathcal{R}_q\;\equiv\;\mathbb{Z}_q[w]/f\,\mathbb{Z}_q[w]$$
        Os elementos de $$\,\mathcal{R}\,$$ e de $$\,\mathcal{R}_q\,$$ são representados por polinómios em $$\,\mathbb{Z}[w]_n\,$$ e $$\,\mathbb{Z}_q[w]_n\,$$ , respetidamente, ou então por vetores em $$\,\mathbb{Z}^n\,$$ e $$\,\mathbb{Z}_q^n\,$$. 
6. É definido o gerador gaussiano  $$\,\chi_{q,\alpha}\,$$ que gera inteiros no intervalo  $$\,[-d,d]\,$$ de acordo com uma distribuição proporcional à da forma normal de centro $$\,c=0\,$$  e variância  $$\,{\alpha\,q}\,$$.$$\,\,$$
        Quando o parâmetro $$\,q\,$$ está implícito usamos apenas $$\,\chi_\alpha\,$$. O gerador $$\,\chi_\alpha^n\,$$ gera vetores em $$\,\mathbb{Z}_q^n\,$$ cujos elementos são gerados independentemente por $$\,\chi_\alpha\,$$.


| Ver no Sagemath uma apresentação de [gerador gaussianos sobre os inteiros](http://doc.sagemath.org/html/en/reference/stats/sage/stats/distributions/discrete_gaussian_integer.html).                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Para  $$n=16\,$$, $$\,q=97\,$$e $$\,\alpha = 0.7\,$$ tem-se uma função de distribuição discreta como a representada aqui.<br><br><br>![](https://paper-attachments.dropbox.com/s_40F6E51A9F5A8E1310C301A3C292C77C57A1CC8080F3E8D1341A7415F01A2E2D_1587118800340_gauss.png) |


Dada a forma como o anel $$\,\mathcal{R}_q\,$$ foi gerado sabemos que é possível efectuar somas e nultiplicações no domínio das trans formadas NTT em tempo linear como o grau dos polinómios. As operações mais complexas, com complexidade $$\,O(n\,\log_2 n)\,$$são o cálculo da transformada e da sua inversa; isto é, a conversão do vetor de coeficientes no vetor de valores e vice-versa.

Por isso essas são as operações que se devem evitar. Se possível todas as operações devem ser feitas no domínio das transformadas NTT; nomeadamente a geração dos polinómios de erros $$\,e \gets \chi_\alpha^n\,$$ ou a geração aleatória de polinómios $$\, f \gets \mathbb{Z}_q[w]_n\,$$deve ser feita, tanto quanto possível, no domínio das transformadas. $$\,$$

**RLW-PKE**

São públicos os parâmetros $$\,n,q,\chi\,$$.
$$\,$$
**KeyGen** 

        - Gerar aleatoriamente  $$\,s,e \gets \chi\,$$
        - Gera aleatoriamente $$\,a \gets \mathcal{R}_q\,$$ e calcular  $$\, b \gets a \ast s + e$$ 
        - A chave privada é  $$\;\mathbf{sk}\,\equiv\, s\;$$   e a chave pública é $$\,\mathbf{pk}\,\equiv\,(a, b)$$

**Encrypt**
Como inputs recebe uma mensagem $$\,m\in \{-1,1\}^n\,$$ e a chave pública $$\,\mathbf{pk}\,=\,(a, b)$$.

        - $$m' \gets \ell\times m$$
            codifica o vetor $$\,m\,$$ num polinómio  $$m'\in \mathcal{R}_q\,$$ cujo $$i$$-ésimo coeficiente é   $$\,\ell\times m_i$$. 
        - Gera $$\;r,e_1,e_2 \gets \chi$$  
        - Calcula
                - $$\,\mu \gets a\ast r + e_1$$
                - $$\upsilon \gets b*r + e_2+m'$$  
        - O criptograma é  $$\,\mathbf{c}\gets (\mu,\upsilon)$$

**Decrypt**
Recebe como inputs o criptograma $$\,\mathbf{c}\,=\,(\mu,\upsilon)\,$$ e a chave privada $$\,\mathbf{sk}\,=\,s$$

        - Calcula $$\,\beta \gets \upsilon - \mu\ast s$$
        - $$m \gets \mathsf{decode}(\beta)$$
                o algoritmo  $$\,\mathsf{decode}\,$$ atua sobre cada posição $$i$$ do polinómio $$\beta$$ testando qual dos inteiros $$\,-\ell\,$$ ou $$\,+\ell\,$$ está mais próximo do coeficiente $$\beta_i$$; no primeiro caso devolve o valor $$-1$$ e no segundo caso o valor $$+1$$. 
                Se $$\,\beta_i\,$$estiver aproximadamente à mesma distância de $$\,+\ell\,$$e $$\,-\ell\,$$ , o algoritmo termina em erro.

**Justificação**


        - $$\beta = a*s*r + e*r + e_2 + m' - a*r*s - e_1 * s\, = \, \ell*m + \epsilon\,$$ 
                     em que  $$\,\epsilon \equiv e_2 + e*r -e_1*s\,$$
        - como todos os $$\,r, s, e, e_1, e_2\,$$ são gerados a partir de $$\,\chi\,$$são pequenos polinómios que o algoritmo perturbam pouco os coeficientes de $$\,\ell*m\,$$; portanto o algoritmo de descodificação recupera $$\,m\,$$.

**Segurança**

A segurança deste criptosistema depende da complexidade computacional dos problemas **RLWE** que, por seu lado, dependem da complexidade dos problemas **LWE**.

Considere-se o ideal  $$\,\mathcal{I}_a \subset \mathcal{R}\,$$  definido como  $$\mathcal{I}_a\,\equiv\,\{x \in \mathcal{R}\,|\, x\ast a \equiv 0 \bmod q\}$$. 
Vamos supor de determina um polinómio “pequeno”  $$\,\mu\in\mathcal{I}_a\,$$. Por “pequeno” entendemos um polinómio não-nulo onde todos os coeficientes são $$0$$ ou $$1$$ e o número de $$1$$’s é pequeno.

Se for possível encontrar um tal $$\,\mu\,$$, então a partir do conhecimento da chave pública $$\,(a, b)\,$$ calculamos  $$\,\mu\ast b \equiv \mu* a*s + \mu*e \equiv \mu* e \mod q\,$$ uma vez que $$\mu*a \equiv 0\bmod q\,$$.
Seja $$\,b'\equiv \mu\ast b\,$$; este polinómio pode ser calculado porque tanto $$\mu$$ como $$b$$ são conhecidos. Ficamos assim com uma equação

                                $$\,\mu\ast e \equiv b' \mod q$$

Na hipótese de $$\mu$$ ter poucos coeficientes $$1$$’s e os restantes serem  iguais a  zero então, provavelmente, será possível resolver esta equação e determinar o erro $$\,e\,$$. A partir do erro tem-se $$\,a\ast s \gets  b - e\,$$ e, como $$a\,$$ é conhecido, é possível determinar $$\,s\,$$.

Portanto a segurança do RLWE está intimamente ligada a um outro problema: 

> determinar um pequeno elemento de um ideal $$\,\mathcal{I}\subset \mathcal{R}$$

Como veremos este é um dos problemas difíceis standard em reticulados.

