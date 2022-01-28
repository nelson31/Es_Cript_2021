# Capítulo 8: Reticulados. Problemas “Standard” . Redução Linear.

# Terminologia

Algebricamente um reticulado   $$\,\mathcal{L}\,$$  (“lattice”)  é um $$\mathbb{Z}$$-módulo finitamente gerado.

| **Nota** Em Matemática, e no SageMath, a palavra  “lattice” ocorre também no contexto da Teoria da Ordem, designando um conceito completamente distinto. O contexto onde a palavra ocorre permite distinguir se ela se aplica a um módulo ou a uma ordem parcial. |


Ser “finitamente gerado” significa que existe um conjunto finito de *geradores* $$\,\mathcal{B}\equiv \{g_1,\cdots,g_n\}\,$$:  isto é, elementos de $$\mathcal{L}$$ tais que todo o  $$\,x\in\mathcal{L}\,$$ é uma combinação linear inteira dos $$\,g_i$$’s. 


                                $$x\in \mathcal{L}\quad\text{sse}\quad\exists\,a_1,\cdots,a_n\in\mathbb{Z} \; \centerdot\; x = a_1\,g_1 + \cdots + a_n\,g_n\,$$ 
                                

Se os $$g_i$$’s são linearmente independentes então $$\,\mathcal{B}\,$$ é uma **base** de $$\,\mathcal{L}\,$$ e $$n$$ é a **dimensão** do reticulado.  Nesse caso escreve-se

                                                            $$\,\mathcal{L}\,\equiv\, \Lambda(\mathcal{B})$$

para designar o facto de que $$\,\mathcal{L}\,$$ é **gerado** pela base $$\,\mathcal{B}$$.

| Uma segunda base $$\,\mathcal{B}'\equiv \{g'_1,\cdots,g'_n\}\,$$ pode gerar o mesmo reticulado; como cada $$\,g'_i\,$$é um elemento de $$\,\mathcal{L}\,$$ pode ser escrito como uma combinação linear inteira dos geradores da 1ª base<br><br>                                $$\,g'_i \;= \;\sum_j\,a_{i,j}\,g_j\qquad \text{com}\quad a_{i,j}\in \mathbb{Z}$$<br><br>Seja. $$\,A\in \mathbb{Z}^{n\times n}$$ a matriz formada pelas componentes $$\,a_{i,j}\,$$.  Da mesma forma pode-se representar cada $$\,g_i\,$$ como uma combinação linear inteira dos elementos de $$\,\mathcal{B}'$$.<br><br>                                $$g_i \,=\, \sum_i\,a'_{i,j}\,g'_j\qquad \text{com}\quad a'_{i,j}\in \mathbb{Z}$$<br><br>Portanto a matriz $$\,A'\in\mathbb{Z}^{n\times n}\,$$ ,definida pelos elementos $$\,a'_{i,j}$$, tem de ser inversa de $$A$$.<br><br>A conclusão é que uma base $$\,\mathcal{B}'\,$$ obtém-se de $$\,\mathcal{B}\,$$ multiplicando os seus elementos por uma **matriz unimodular** ; isto é, uma matriz de inteiros que tem uma inversa que também é uma matriz de inteiros.<br><br>                                $$\begin{pmatrix}g'_1 \\ \cdots \\ g'_n\end{pmatrix} \,=\, A\times \begin{pmatrix} g_1 \\ \cdots \\ g_n\end{pmatrix}$$ |


Ao longo das  últimas sessões referimos reticulados várias vezes; sempre no sentido de que neles existem **problemas standard** que são difíceis mesmo em modelos de computação quântica, e que muitas das técnicas PQC provam a sua segurança reduzindo uma instância de um desses problemas standard a um ataque a essa técnica.

Em Criptografia os reticulados não são apenas fonte de problemas difíceis em PQC; são também, e cada vez mais, fonte de **ataques algébricos** (por vezes inesperados) à NTC; por exemplo um dos ataques mais recentes ao RSA usa um problema de reticulados, designado por **redução de base**, que tem soluções polinomiais mesmo em computação clássica.

Reticulados são estruturas algébricas muito flexíveis que assumem várias formas e se adaptam a muitas técnicas criptográficas. Aquilo que é comum a todas elas é a existência dos problemas difíceis que têm de ser formalizados de acordo com o tipo de reticulado que é usado.


1. Uma  característica comum a todos os reticulados $$\,\mathcal{L}\,$$ é a existência de um espaço, designado por $$\,\mathbf{span}(\mathcal{L})\,$$, que verifica as condições:
        1. $$\,\mathbf{span}(\mathcal{L})\,$$ é um $$K$$-espaço vetorial (ou um $$\mathcal{R}$$-módulo), com a mesma dimensão de $$\,\mathcal{L}$$ ,  e que contém $$\,\mathcal{L}\,$$.
        2. o corpo $$K$$  (ou o anel $$\,\mathcal{R}\,)$$  é uma extensão dos inteiros $$\,\mathbb{Z}$$,
        
    Estas duas condições forçam, nomeadamente, a que $$\,\mathcal{L}\,$$ esteja contido no fecho algébrico $$\,\overline{K}\,$$ (ou $$\overline{\mathcal{R}}\,$$) de um corpo $$K$$ ou de um anel $$\mathcal{R}$$ que estendem os inteiros $$\mathbb{Z}$$.
    
    Seja$$\,\{g_1,\cdots\,g_n\}\,$$ é uma base  de $$\,\mathcal{L}$$.
    Se fôr $$\,\mathcal{L}\subset \overline{K}\,$$ ,  então tem-se   $$\,\mathbf{span}(\mathcal{L})\;\equiv\; \{a_1\,g_1+\cdots+a_n\,g_n\,|\, a_i\in K\}$$  . De forma análoga,  se fôr $$\,\mathcal{L}\subset \overline{\mathcal{R}}\,$$, então  tam-se  $$\,\mathbf{span}(\mathcal{L})\;\equiv\; \{a_1\,g_1+\cdots+a_n\,g_n\,|\, a_i\in \mathcal{R}\}$$ .


2. Todos os problemas em $$\,\mathcal{L}$$, standard ou não, baseiam-se no conceito de **tamanho** dos elementos  $$\,x,y\in \mathcal{L}\,$$. Por vezes esse tamanho está associada a um valor real positivo: uma **métrica** $$\,\mathbf{d}(x,0)\,$$ou uma **distância**  $$\mathbf{d}(x,y)\,$$. Outras vezes a métrica é definida por uma **norma** $$\,\|x\|\,$$e, nesse caso, a distância define-se como $$\,\mathbf{d}(x,y)\equiv \|x-y\|\,$$. 


    Muitas vezes não é possível definir nem distância nem norma  mas é possível identificar um conjunto  $$\,\mathcal{S}\subset \mathbf{span}(\mathcal{L})\,$$ dos **short vetors** : isto é, vetores curtos não-nulos. Normalmente $$\,\mathcal{S}\,$$ é definido por restrições algébricas e pode (ou não) conter elementos de $$\mathcal{L}$$.


----------

Os **problemas standard**  em $$\,\mathcal{L}\,$$ ligam-se a estes dois conceitos; todos estes problemas caem em três grandes classes:


## Vetores Curtos 

Dado um reticulado $$\,\mathcal{L}\,$$, onde existe uma noção de distância, pretende-se 

        > encontrar  o elemento $$\,x\in\mathcal{L}\,$$, não-nulo,  mais próximo da origem.
| Na figura seguinte, a verde estão indicados os pontos do reticulado.<br><br>-  $$\lambda_1\,$$ é a menor distância entre pontos: o raio do menor cículo que contém um ponto não nulo.<br>- $$\,\lambda_2\,$$ é o raio do menor círculo que contém dois pontos linearmente independentes. |



![](https://paper-attachments.dropbox.com/s_D292A0D14B3B2CAD18DD6E867E248BC403E3442E9F00B434D2FA3F6EEF062822_1587287878307_ret5.png)


Genericamente este problema designa-se  **SVP** (“shortest vector problem”);  algumas variantes do SVP  são também importantes. Por exemplo  $$\gamma$$-SVP  define-se, para algum   $$\gamma > 1$$, como

> encontrar um ponto $$\,x\neq 0\in\mathcal{L}\,$$ tal que $$\|x\| < \gamma\lambda_1\;$$

ou o $$\,\gamma$$-uSVP definido como

> encontrar  $$\,x\neq 0\in\mathcal{L}\,$$ que seja único (a menos de dependências lineares) tal que  $$\|x\| < \gamma\lambda_1\;$$

Depois temos alguns reticulados de inteiros, como o reticulado $$\,\mathcal{L}(h)\,$$que vimos no  NTRU,  onde não existem distâncias. Aqui é necessário  usar um  conjunto $$\,\mathcal{S}\,$$ de vetores curtos definido por restrições algébricas. O problema, que agora se designa por  **SIS** (“short integer solution”), formaliza-se de forma diferente:  

        > encontrar  $$\,x\in \mathcal{L}\,$$ , não nulo,  que pertença a  $$\,\mathcal{S}\,$$.
        
## Vetores Próximos 

Nesta classe de problemas, para além do reticulado $$\,\mathcal{L}\,$$ é dado um ponto $$\,y\in \mathbf{span}(\mathcal{L})\,$$ e pretende-se 

        > determinar o vetor $$\,x\in\mathcal{L}\,$$ mais próximo de $$\,y\,$$. 

Genericamente o problema designava-se por “closest vector problem” (CVP).  A formalização do CVP que é mais usual  toma o nome de **BDD** (“bounded distance decoding”). No problema designado por $$\,\alpha$$-BDD impõe-se limites à distância entre $$\,y\,$$ e “pontos próximos” no reticulado.


> dado $$y\in \mathbf{span}(\mathcal{L})\,$$, tal que $$\;\mathbf{dist}(y,\mathcal{L}) < \alpha\lambda_1\;$$,  determinar $$\,x\in\mathcal{L}\,$$que minimiza  $$\,\|y-x\|\,$$.

A distância $$\,\mathbf{dist}(y,\mathcal{L})\,$$ define-se como $$\;\min \{\|y-x\|\,|\,x \in \mathcal{L}\}\,$$.

![](https://paper-attachments.dropbox.com/s_D292A0D14B3B2CAD18DD6E867E248BC403E3442E9F00B434D2FA3F6EEF062822_1587288803786_BDD.png)



Obviamente o objetivo “mais próximo”  implica que o reticulado tenha uma noção de distância. Se não existir tal noção é necessário recorrer  aos conjuntos $$\,\mathcal{S}\,$$de “short vectors”. O problema  **BDD** agora formaliza-se de forma diferente:  

        > determinar um vetor $$\,x\in \mathcal{L}\,$$ tal que $$\,(x-y)\in \mathcal{S}\,$$.
        
## Redução de Bases 

As duas classes SVP/SIS ou CVP/BDD  denotam problemas que se pretendem difíceis mesmo em modelos de computação quântica. Por isso são usados nas provas de segurança de técnicas criptográficas pós-quântica.

Ao invés os problemas de redução de bases têm soluções eficientes e no entanto conseguem resolver situações criptográficas “aparentemente difíceis”. De fato estes problemas são usados na construção de ataques ou então, e principalmente, na construção de  “trap-doors” de funções unidirecionais (“one-way functions”).


----------

Um facto essencial em qualquer reticulado é que uma base $$\,\mathcal{B}\,$$ determina um reticulado $$\,\mathcal{L} \equiv \Lambda(\mathcal{B})\,$$ mas o reticulado  $$\,\mathcal{L}\,$$ não determina a base: o mesmo reticulado pode ser gerado por várias bases diferentes. 

![Uma má base](https://paper-attachments.dropbox.com/s_D292A0D14B3B2CAD18DD6E867E248BC403E3442E9F00B434D2FA3F6EEF062822_1587296505378_ret3-1.png)



![Uma boa base](https://paper-attachments.dropbox.com/s_D292A0D14B3B2CAD18DD6E867E248BC403E3442E9F00B434D2FA3F6EEF062822_1587295723611_ret2.png)

----------

Num reticulado munido de uma noção de distância é possível classificar as suas várias bases pelo tamanho dos vetores geradores.

O problema da **redução de bases** pode ser descrito sumariamente como

> Dado uma base  $$\,\mathcal{B}\,$$ determinar uma base $$\,\mathcal{B}'\,$$ que seja “mais curta” do que a base original e que gere o mesmo reticulado.

A formalização deste problema e a construção de algoritmos eficientes que o resolvam  vai depender do tipo de reticulado e será apresentada em seguida.

Conforme o tipo de reticulados, as três classes de problemas assumem formas distintas. Por isso é conveniente identificar os tipos de reticulados mais frequentes.

# Reticulados Euclidianos


## Terminologia

Reticulados euclidianos são definidos dobre um espaço vetorial $$\,\mathbb{R}^m\,$$ equipado com a norma euclidiana  $$\,\|x\| = \,(\sum_{i=1}^m\,x_i^2)^{1/2}$$. 

| Pode-se ainda considerar qualquer espaço isomórfico com $$\,\mathbb{R}^m\,$$; por exemplo o espaço  $$\,\mathbb{R}[w]_m\,$$ formado pelos polinómios univariáveis, de grau inferior a $$\,m\,$$e coeficientes reais. |



1. Se o reticulado tiver dimensão $$\,n\,$$, então ele é gerado por bases $$\,\mathcal{B} = \{g_1,\cdots,g_n\}\,$$ formadas por $$\,n\,$$vetores $$\,g_i\in \mathbb{R}^m\,$$.   
    A base pode ser representada pela matriz $$\,{G}\,\in\,\mathbb{R}^{n\times m}$$  cuja $$i$$-ésima linha é o vetor $$\,g_i\,$$. 
    
    Desta forma pode-se descrever a geração do reticulado como
    
                                $$\;\mathcal{L} \equiv \Lambda(G)\,\equiv\, \{ a\,{G}\,|\,a\in \mathbb{Z}^n\}\,$$ .
                                
    A norma da matriz gerador $$\,G\,$$ define-se como
                                $$\|G\| \;\equiv\; \max_{\|x\|=1}\;\|x\,G\|$$
                                
2. Todo o reticulado $$\,\mathcal{\mathcal{L}}$$  tem um **reticulado dual** $$\,\mathcal{L}^\ast\,$$  , com o mesmo espaço “span”, definido por


                               $$\,\mathcal{L}^\ast\;\equiv\;\{z\in\mathbb{R}^m\,|\,\forall\,x\in\mathcal{L}\,\centerdot\,\langle z\cdot x\rangle = 0 \}$$
| Aqui $$\,\langle z\cdot x \rangle\,$$denota o produto interno em $$\,\mathbb{R}^m\,$$:  $$\,\sum_{j=1}^m\,z_j\,x_j\,$$ |

| Se for conhecida uma base $$\,\mathcal{B}\,\equiv\,\{g_1,\cdots,g_n\}\,$$ do reticulado $$\,\mathcal{L}$$, então a definição do reticulado dual pode ser feita de forma mais simples<br><br>                         $$\,\mathcal{L}^\ast\;\equiv\;\{z\in\mathbb{R}^m\,|\,\forall\,g\in\mathcal{B}\,\centerdot\,\langle z\cdot g\rangle = 0 \}$$<br><br>Ou ainda, se $$G$$ for a matriz geradora cujas linhas são os vetores $$g_i\,$$, então também se pode escrever<br><br>                         $$\,\mathcal{L}^\ast\;\equiv\;\{z\in\mathbb{R}^m\,|\,z\,G^\top\,=\,0 \}$$ |

3.  Genericamente uma forma alternativa de definir o  reticulado $$\,\mathcal{L}$$ recorre a uma **matriz verificadora** ou **matriz de paridades,**   $$\,H\in \mathbb{R}^{m\times \ell}\,$$ , com colunas  $$\,h_1,\cdots,h_\ell\,\in\mathbb{R}^m\,$$ linearmente independentes ,  tal que
                        $$\,\mathcal{L}\,\equiv\, \{\,z\in\mathbb{R}^m\,|\, z\,H\,=\,0\}$$
    ou, equivalentemente, 
                        $$\,\mathcal{L}\,\equiv\, \{\,z\in\mathbb{R}^m\,|\,\forall\,j=1..\ell \,\centerdot\,  \langle z\cdot h_j\rangle \,=\,0\}$$
    Os vetores $$h_j$$’s são designados por **paridades.** A matriz **** $$H$$ pode também ser identificado com o conjunto $$\,\mathcal{H}\equiv \{h_1,\cdots,h_\ell\}\,$$ formado por estas paridades.


    $$G\,$$ e $$H\,$$ geram o mesmo reticulado se e só se    $$\,G\,H = 0$$.
| Da álgebra elementar sabe-se que $$\,m = n + \ell\,$$. É  simples calcular as paridades a partir dos geradores, e vice-versa, usando o seguinte algoritmo.<br>1. Através de eliminação Gaussiana determina-se uma matriz invertível $$S\in \mathbb{R}^{n\times n}\;$$ tal que,  para algum $$\,P\in \mathbb{R}^{n\times\ell}$$, se verifica    $$S\,G \,=\,\begin{pmatrix}\mathbf{1}_n &\!|\!& P\end{pmatrix}$$     <br><br>2. A matriz $$\,H\,$$ determina-se pela relação   $$H^\top \,=\,\begin{pmatrix}-P^\top &\!|\!& \mathbf{1}_\ell\end{pmatrix}$$ |

4. O **cubo fundamental** em $$\,\mathbb{Z}^n\,$$ é formado pelos $$\,2^n\,$$ vértices $$\,\{0,1\}^n\,$$. O **paralelepípedo** **fundamental** em $$\,\mathcal{L}\,$$ é definido por $$\,\{a\,G\,|\, a\in\{0,1\}^n\}\,$$.
    
5.  $$G'$$ é uma outra base para o mesmo reticulado, isto é verifica-se $$\,\Lambda(G)\equiv \Lambda(G')\,$$ , se e só se existe uma matriz unimodular  $$\,U\in \mathbb{Z}^{n\times n}$$   tal que $$\,G' \,=\,U\times G$$. 


6. O volume do paralelepípedo fundamental calcula-se como
                                $$\;\text{vol}\,\equiv\, \sqrt{\text{det}(G^\top\,G)}\;$$ 
                                
    É um valor que$$\,$$ não depende da base $$G$$ escolhida: é um **invariante** do reticulado.

     O teorema de Minkowski prova que a mínima distância $$\lambda_1$$  verifica

                                        $$\,\lambda_1 /(\text{vol})^{1/n} \,\leq\,\sqrt{\gamma}_n$$
    para algum $$\,\gamma_n\leq n\,$$, designado por **constante de Hermite**.



## Redução de Base: LLL e BZK

Intuitivamente, se todos os vetores da base fossem ortogonais dois a dois, teríamos uma **base ideal.** Então a quantidade $$\,(\text{vol})^{1/n}\,$$ seria a média geométrica do tamanho dos vetores de tal base. Portanto a fração $$\,\lambda_1/(\text{vol})^{1/n}\,$$ denota o tamanho do vetor mais curto relativo a essa “média ideal”.

No estudo da redução de bases é comum enumerar os vetores da base do menor para o maior : $$\|g_1\| \leq \cdots \leq \|g_n\|$$.  Assim a quantidade   $$\,h \,=\, \|g_1\|/(\text{vol})^{1/n}\,$$    dá uma medida do grau de proximidade de uma base concreta para essa base ideal.

O algoritmo LLL  publicado em 1982 por Lenstra, Lenstra e Lovasz é um dos algoritmos mais famosos das Ciências da Computação. É um algoritmo polinomial que  consegue reduzir  para valores de $$h$$ melhores do que  $$1+ 0.075\,n$$ . Como $$n$$ pode ser da ordem das muitas centenas, este não é um valor tão bom quanto parece.
Na maioria dos casos o LLL comporta-se bastante melhor. Uma optimização deste algoritmo, designado por BKZ, é o algoritmo “default” no SageMath. è sensivelmente melhor que o LLL mas tem mais parâmetros que o tornam mais difícil de “afinar”.

O algoritmo LLL é relativamente simples e está descrito no livro [“Introduction to Mathematical Cryptography”](https://www.dropbox.com/s/563yget5v3rxsqc/HPS%20An%20Introduction%20to%20Mathematical%20Cryptography.pdf?dl=0).
(secção 6.12, pag. 411). É muito semelhante ao clássico algoritmo de redução Gaussiana em sistemas de equações lineares mas usa passos intermédios onde faz arredondamentos a inteiros. 
O algoritmo de redução de bases, LLL ou BKZ, é usado na construção de **soluções aproximadas** para os problemas SVP e  BDD.

O resultado fundamental da redução de bases é

**Teorema**

> Se $$G\in \mathbb{R}^{n\times n}\,$$ é matriz geradora de um reticulado $$\,\mathcal{L}\equiv\Lambda(G)\,$$ de dimensão $$n$$, então é possível determinar, em tempo polinomial com $$n$$, um vetor  $$\,y\in \mathcal{L}\,$$ tal que 
>                                  $$\|y\|\,\leq 2^{(n-1)/4}\,\text{det}(G)$$ 


## Algoritmos aproximados

Uma **algoritmo aproximado** para um problema difícil em reticulados é uma algoritmo polinomial que usa, como um dos parâmetros input, uma base $$G$$ do reticulado. Se a base fôr “boa” então o algoritmo  termina com uma solução que, com grande probabilidade, coincide com a solução exata do problema. Se a base for “má” o algoritmo aproximada termina com um resultado que está longe da solução exata.

| **Solução aproximada do SVP**<br><br>Dada a base $$G\in\mathcal{R}^{n\times m}\,$$ usa-se o algoritmo de redução, LLL ou BKZ, para construir uma versão reduzida da base $$G$$. Toma-se o elemento mais curto da base reduzida como aproximação do SVP. |

| **Solução aproximada do BDD**<br><br>Dados a base $$\,G\in \mathbb{R}^{n\times m}\,$$ e o “target”  $$y\in \mathbb{R}^m\,$$  constrói-se uma matriz $$(n+1)\times (m+1)$$ por blocos<br>                                                                     $$G' \;\equiv\; \begin{pmatrix} G & | & 0 \\ -y & | & L\end{pmatrix}$$  <br>em que $$0$$ denota uma coluna de $$n$$ zeros e $$L> n\times m$$  é um inteiro positivo grande.<br><br>Calcula-se agora a redução da base $$G'$$ usando LLL ou BKZ.<br><br>Qualquer uma das linhas do resultado vai ser uma combinação linear inteira das linhas de $$G'$$. Por isso, para algum $$z\in \mathbb{Z}^n$$ e inteiro $$\,\mu\,$$,  a linha “reduzida” é<br>                      $$(z,\mu)\times G' \,= \,(z\,G - \mu\,y , \mu\,L)$$<br>Porque $$L$$ é muito grande e a base está reduzida, em todas as linhas excepto a última temos de ter $$\,\mu=0$$. Todas essa linhas vão ser da forma $$\,(z\,G,0)\,$$, para algum $$z$$, e devem ser “pequenas”.<br><br>Na última linha, porém, tem de ser $$\mu=1$$, pois em caso contrário a matriz reduzida teria uma coluna de zeros. Essa linha vai ter a forma $$\,(z\,G - y\,,\, L)\,$$.<br><br>Portanto as primeiras componentes da última linha fornecem o valor $$\,e \equiv z\,G - y\,$$ que é o “erro”  $$\,(x-y)\,$$ na solução do BDD.  A partir desse erro constrói-se a solução do do problema $$\,x \equiv y + e\,$$. |



## “Hidden Number Problem”

Recorde-se que o problema do **número escondido ,** definido por  um primo $$p$$  e um $$k < \log_2 p\,$$, tem por objetivo determinar  um segredo $$\,s\neq 0\in\mathbb{Z}_p\,$$  , a partir de uma sequência de $$n$$  pares $$\,(x_i,u_i) \in \mathbb{Z}_p\times \mathbb{Z}_p\,$$ que verificam


                                $$u_i \,=\, \text{msb}_k(\lfloor s\times x_i\rfloor_p)\qquad\text{para todo}\;i=1..n$$
                                

Neste problema  usam-se vária convenções:

    - o domínio $$\,\mathbb{Z}_p\,$$ identifica-se com $$\; \{y\in\mathbb{Z}\,|\,0\leq y < p\}\,$$ 
    
    - para   $$\,z\in \mathbb{Z}\,$$,  designa-se por  $$$$$$\,\lfloor z\rfloor_p\,$$ o inteiro $$\,z'\in\mathbb{Z}_p\,$$ que verifica $$\,z'\equiv z \bmod p\,$$.
    
    - são relevantes os parâmetros   $$\lambda \equiv 2^k\quad$$ , $$\quad A\equiv 1/\lambda\quad$$e $$\quad B\equiv p/\lambda\,$$.
    
    - $$\,\text{msb}_k\colon \mathbb{Z}_p \to \mathbb{Z}_p\,$$ é qualquer função que   verifica  para todo $$\,y\in \mathbb{Z}_p\,$$
    
                       $$\,u = \text{msb}_k(y)\,$$    se e só se $$\quad 0 \leq y - B\,u < B$$ 
| Uma boa implementação de $$\,\text{msb}_k(y)\,$$ , com $$y\in\mathbb{Z}_p\,$$ ,  é simplesmente  $$\,\lfloor\,y/B\,\rfloor$$. |

O HNP reduz-se ao problema  BDD da seguinte forma :


1. Constrói-se um reticulado  $$\,\mathcal{L} \equiv \Lambda(G)\,$$ de dimensão  $$\,m = n+1\,$$ em que a matriz geradora  $$G\in\mathbb{Q}^{m\times m}$$  é construída como


                                $$G\,\equiv\,\begin{bmatrix}  p & 0 & \cdots & 0 & 0 \\ 0 & p & \cdots & 0 & 0 \\ \cdots & \cdots & \cdots & \cdots & \cdots \\ 0 & 0 &\cdots& p & 0 \\x_1 & x_2 & \cdots&x_n & A  \end{bmatrix}$$
                                
2. Constrói-se o “target”  $$\,y\in \mathbb{Z}^m\,$$  como o vetor
                                $$y \,\equiv\,\begin{bmatrix} B\,u_1 & B\,u_2 & \cdots & B\,u_n & 0 \end{bmatrix}$$
3. Recorrendo a um algoritmo que resolva o BDD, determina-se o ponto $$\,z\,G$$ do reticulado $$\,\mathcal{L}\,$$ que está mais próximo de $$\,y\,$$ e a uma distância inferior a $$\,B\,$$.
4. Determinado esse ponto pode-se determinar  $$\,z\in \mathbb{Z}^m\,$$ como  $$\,z = (z\,G)\,G^{-1}\,$$ e escrevendo 
                                $$z\,\equiv\,\begin{bmatrix}  w_1 & w_2 & \cdots & w_n & s \end{bmatrix}$$
    determinar o segredo $$\,s\,$$ como última componente de $$\,z\,$$.


| **Justificação**<br><br>Sendo $$\,z\,G\,$$ a solução do BDD para o “target” $$y$$ e “bound”  $$\,B\,$$, então  verifica-se<br><br>                                $$z\,G\,=\,y + e$$<br><br>para um erro    $$e \,\equiv\,( e_1 , e_2 , \cdots , e_{n} , e_{n+1})\,$$   tal que $$\,\max_i\,|e_i| < B$$. <br><br>Expandindo  as formas específicas de $$\,e\,,\,G\,,\,z\,,\,y\,$$  , a relação acima decompõe-se em $$n+1$$ equações<br><br>        <br>        $$w_i\,p + s\times x_i \,=\,B\,u_i + e_i \qquad\text{para}\; i=1,\cdots n$$<br><br>          $$s\,A \,=\,e_{n+1}$$<br>          <br>O  primeiro conjunto de equações traduz-se, pela definição de $$\,\text{msb}_k\,$$,  em <br>                          $$\text{msb}_k(\lfloor\,s\times x_i\,\rfloor_p) \,=\, u_i$$  para todo  $$\,i=1..n$$<br>A última equação serve apenas para confirmar que o valor de $$s\,A \,=\,s/\lambda\,$$ , com o $$s$$ determinado,  está dentro dos limites de um erro. |

A viabilidade de esta redução ser usada para resolver o HNP depende crucialmente da disponibilidade de existir um algoritmo eficiente para resolver o problema BDD com os parâmetros dados.

Normalmente seria difícil obter uma solução eficiente. Porém, neste caso particular e para o tipo de matriz geradora aqui usada, o algoritmo aproximado que apresentámos antes fornece frequentemente boas soluções.

Seguindo a abordagem indicada atrás constrói-se a matriz $$\,G'\in\mathbb{Q}^{m\times m}\,$$ com $$m=n+2$$.


                                $$G'\,\equiv\,\begin{bmatrix}  p & 0 & \cdots & 0 & 0 & 0\\ 0 & p & \cdots & 0 & 0 & 0 \\ \cdots & \cdots & \cdots & \cdots & \cdots &\cdots\\ 0 & 0 &\cdots& p & 0 & 0 \\x_1 & x_2 & \cdots&x_n & A & 0 \\ -B\,u_1 & -B\,u_2 &\cdots& -B\,u_n & 0 & M\end{bmatrix}$$
                                

Usa-se um qualquer grande inteiro $$M \gg \lambda$$ .

Após a redução BKZ de $$\,G'\,$$ ,  a última linha da matriz reduzida vai  ter a forma

                                $$\begin{bmatrix} e_1 & e_2 & \cdots & e_{n+1} & M\end{bmatrix}$$

e, como   $$\,e_{n+1} \,=\,s\,A\,$$  e  $$\,A=1/\lambda\,$$,  determina-se  o segredo $$\,s\,$$ como  $$\,\lceil \lambda\times e_{n+1}\rfloor$$

De acordo com [Nguyen & Shparlinsk](https://www.dropbox.com/s/76k1zkz9wautty0/igor-slides.pdf?dl=0) , se for  $$\,p\approx 2^d\,$$,  $$\,k >\sqrt{d} + \log_2 d$$  e $$\,n > 2\,\sqrt{d}\,$$ , então a probabilidade de o algoritmo não fornecer a solução exata é inferior a  $$\,$$$$2^{-\sqrt{d}\,\log_2d}$$.


## Redução da FI  ao BDD  (algoritmo de Schnorr)

A factorização de inteiros (FI) é, como se sabe, o problema “difícil” (pelo menos em computação clássica) que está na base dos criptosistemas da família RSA. Os problemas “standard”  em reticulados são substancialmente mais difíceis e nada ilustra melhor esse facto do que um algoritmo eficiente que mostre a redução do FI a um desses problemas. 

Vamos aqui descrever sucintamente o algoritmo de Schnorr que converte soluções de um desses problemas “standard” , nomeadamente o BDD, num algoritmo para factorizar inteiros.

**Escolha do reticulado**

O ponto de partida desse algoritmo é a escolha do reticulado apropriado à representação do FI.

Um reticulado é um qualquer sub-grupo de um grupo abeliano que seja finitamente gerado. Em todos os exemplos que já referimos esse grupo (o $$\mathbf{span}$$ do reticulado) tem sido um grupo aditivo de dimensão finita: tipicamente o  espaço vetorial $$\,\mathbb{R}^n\,$$.

No entanto o grupo pode, igualmente, ser multiplicativo. Vamos aqui usar um grupo multiplicativo que não é um espaço vetorial: o grupo $$\,\mathbb{Q}_+\,$$dos racionais positivos não nulos.

                        $$\mathbb{Q}_+\,\equiv\, \{1\} \,\cup\, \{\,u/\upsilon \;|\; u,v > 1\; \text{e}\; \text{mdc}(u,\upsilon) = 1\}$$

Isto é, cada $$\,r\neq 1\,$$ é determinada por uma par de inteiros $$\,u/\upsilon\,$$ maiores do que $$1$$ e co-primos.

A operação de grupo define-se como: $$\,1 \times r \equiv r\,$$   e   $$(u/\upsilon)\times (u'/\upsilon') \,\equiv \,(u\,u'/\mu)/(\upsilon\,\upsilon'/\mu)$$     sendo  $$\,\mu\equiv\text{mdc}(u,\upsilon')\,\text{mdc}(u',\upsilon)$$.
A distância entre dois racionais $$\,r,s\in \mathbb{Q}_+\,$$ é medida como $$\,|r-s|\,$$.

| No grupo multiplicativo $$\,\mathbb{Q}_+$$ é possível definir uma métrica  que dependa do tamanho do numerador e denominador. Essa métrica designa-se por **peso** e define-se  <br>                                                         $$\, \|1\| \, = \, 0 \quad\text{e}\quad \|u/\upsilon\| \, = \, \log_2\max\{u,\upsilon\}$$<br> É fácil constatar que esta é realmente uma métrica para a estrutura do grupo. Nomeadamente é uma função real positiva que  verifica  $$\,\|r \times r'\|\,\leq \|r\| + \|r'\|$$  e  $$\,\|r\|=0 \;\text{sse}\;r=1$$. |

O grupo $$\,\mathbb{Q}_+\,$$ tem uma base : a sequência  infinita  $$\mathcal{P}\,\equiv\,\{2,3,5,7,11,\cdots\}$$  formada por todos os números primos ordenados de forma crescente. A fatorização dos inteiros $$\,$$faz com que seja possível representar cada $$\,r\in \mathbb{Q}_+$$ por uma sequência finita de expoentes  $$\,e\in \mathbb{Z}^\ast\,$$.  Tem-se

                          $$\,\left\{\begin{array}{rcl} 1 & = & q_1^0 \\ u/\upsilon &= & q_1^{e_1}\times q_2^{e_2}\times \cdots \times q_\kappa^{e_\kappa}\end{array}\right.$$ 

em que  $$\kappa = |e|\,$$  e   $$q_1,q_2,\cdots,q_\kappa\,$$ é a sequência dos primeiros $$\,\kappa\,$$ primos.

| É também possível definir um reticulado aditivo convertendo racionais em reais aplicando função logaritmo.<br>                                        $$\left\{\begin{array}{rcl} \log_2 1 & = & 0  \\ \log_2 u/\upsilon & = & e_1\,\log_2 q_1 + e_2\log_2 q_2+\cdots+e_\kappa\log_2 q_\kappa\end{array}\right.$$<br>Define-se assim uma base  $$\,\mathcal{B}\,\equiv\,\{\log_2q_1\,,\,\log_2q_2\,,\, \cdots\,,\,\log_2q_\kappa\,,\,\cdots \}$$ |

Para construir uma base finita de dimensão $$\,n\,$$ truncamos a sequências $$\,\mathcal{P}\,$$ aos seus primeiros $$\,n\,$$ elementos:    $$\mathcal{P}_n\,\equiv\,\{q_1,q_2,\cdots,q_n\}\;$$. Os elementos de $$\,\mathcal{P}_n\,$$são designados  “pequenos primos”.
A sequência  $$\,\mathcal{P}_n\,$$ será a base geradora de um  reticulado multiplicativo  contido em $$\mathbb{Q}_+$$.

                                   $$\,\Lambda(\mathcal{P}_n) \equiv \{\; \prod_{\kappa=1}^n\,q_\kappa^{e_k}\;|\;e_1,\cdots,e_n\in\mathbb{Z}\;\}\quad$$ 

Os elementos deste reticulado são racionais $$\,r = u/\upsilon\,$$em que o numerador e o denominador têm fatores primos “pequenos” $$\,q\in \mathcal{P}_n\,$$;  tais racionais dizem-se “smooth”.

**Algoritmo de Schnor**
​​
Seja $$\,\mathcal{P}_n\,\equiv\,\{q_1,q_2,\cdots,q_n\}\,$$ a sequência crescente dos $$n$$ primeiros pequenos primos. 

        1. Pretende-se factorizar  um inteiro positivo  composto $$N$$ cujos fatores são substancialmente maiores do que $$q_n$$. 
        2. O objetivo do algoritmo é construir dois dois inteiros $$X\neq \pm Y\,$$ que verifiquem a relação  $$\,X^2 \equiv Y^2\mod N$$ .  
        3. Uma vez obtidos $$\,X,Y\,$$ a fatorização de Fermat obtém um fator não-trivial de $$N$$ como $$\text{mdc}(X+Y,N)\,$$ ou como $$\,\text{mdc}(X-Y,N)$$.


1. Fixemos o reticulado  multiplicativo  $$\,\mathcal{L}\equiv \Lambda(\mathcal{P}_n)$$ ;  
2. Definimos uma sequência de “targets”    $$\,N_j \equiv p_j\,N\,$$ , com $$\,j=1..m\,$$, em que os $$\,p_j\,$$ são primos maiores do que $$\,q_n\,$$
3. Usando o oráculo BDD  com limite  $$\alpha \leq q_n\,$$ construímos, para cada um dos targets $$\,N_j\,$$ o ponto $$\, u_j/\upsilon_j\in \mathcal{L}\,$$ mais próximo de  $$\,N_j\,$$  e determinamos o erro  respetivo
                                                                     $$\epsilon_j \,=\,|\upsilon_j\,N_j - u_j|$$
    Se o erro for suficientemente pequeno todos os seus fatores primos serão pequenos e, por isso, teremos  $$\,\epsilon_j \in \mathcal{L}$$$$\,$$.
4. Desta relação conclui-se  que  $$\,u_j \equiv \pm \epsilon_j \mod N$$. Desta forma constrói-se $$m$$ triplos de inteiros positivos “smooth” $$\,(u_j,\epsilon_j,s_j)\,$$,  com um “sinal” $$\,s_j\in\{0,1\}$$, que verificam 
                                                        $$u_j \equiv (-1)^{s_j}\,\epsilon_j \mod N$$          
5. Os inteiros $$X,Y$$  vão ser construídos como o numerador e denominador de um racional  $$\,r = (X/Y)\in \mathcal{L}\,$$ que verifica  $$\,r^2 \equiv 1 \mod N\,$$ .
        1. O racional $$r\,$$ vai ser  a raiz quadrada de um racional  escrito como uma combinação linear dos $$(u_j/\epsilon_j)$$;  isto é, tem-se  $$\,r^2 = s$$  com $$\,s\in\mathcal{Q}_+$$ dado por
                                $$s  \,\equiv\,\prod_{j=1}^m\,(u_j/\epsilon_j)^{z_j}$$
            Pretende-se determinar o valor das incógnitas $$\,z_j\,$$ de forma a que $$\,s\,$$ tenha uma raiz quadrada e verifique  $$\,s\equiv 1 \mod N$$.
        2. Sejam  $$\,a_{j,i}$$  e $$\,b_{j,i}\,$$ os expoentes de $$\,q_i\,$$ em $$u_j$$ e $$\epsilon_j$$ respetivamente; $$\,u_j \,=\,\prod_{i=1}^n\,q_i^{a_{j,i}}$$    e  $$\,\epsilon_j \,=\,\prod_{i=1}^n\,q_i^{b_{j,i}}$$  . Então temos                    
                               $$s \,=\, \prod_j \,\prod_i q_i^{z_j(a_{j,i}-b_{j,i})}\,=\,\prod_i\,q_i^{\sum_j\,(a_{j,i}-b_{j,i})z_j}$$
                e, como  $$(u_j/\epsilon_j) \equiv (-1)^{s_j} \mod N$$, temos também
                                     $$s \,\equiv\,(-1)^{\sum_j\,s_j\,z_j}\mod N$$.
        3. Como se pretende que $$s$$ tenha raiz quadrada, os expoentes $$\,\sum_j\,(a_{j,i} - b_{j,i})z_j\,$$ de cada um dos $$q_i$$   têm de ser inteiros pares . Como se pretende que seja $$\,s\equiv 1\mod N\,$$, também o expoente $$\,\sum_j\,s_j\,z_j\,$$ tem de ser um inteiro par. Ficamos assim  com um conjunto de equações lineares   
                    $$\left\{\begin{array}{lcl} \sum_j\,s_j\,z_j & \equiv & 0 \mod 2 \\ \sum_j\,(a_{j,i}-b_{j,i})z_j & \equiv & 0 \mod 2 \quad\text{para todo}\;i=1..n\end{array}\right.$$
        4. Obtida uma solução não trivial $$(z_1,\cdots,z_m)$$ deste sistema de equações lineares constrói-se
                        $$\,r \;\equiv\; \prod_i\,q_i^{c_i} \quad \text{sendo}\quad c_i\equiv \frac{\sum_j\,(a_{j,i}-b_{j,i})\,z_j}2$$
            O numerador  $$X$$ e o denominador $$Y$$ de $$r\,$$  são
                          $$X \,\equiv\, \prod_{c_i>0}\,q_i^{c_i}\quad$$e  $$\quad Y \,\equiv\,\prod_{c_i < 0}\, q_i^{-c_i}$$
# Redução Linear

O algoritmo para construir uma solução aproximada do BDD através de redução de uma base de reticulado, é um exemplo de uma técnica designada por **redução linear** e que é extremamente útil num número de problemas com relevância criptográfica. Vamos aqui mencionar alguns.

## Polinómios de “pequenos” inteiros

Existem vários problemas onde a solução é um polinómio univariável de coeficientes “pequenos” inteiros. Formalmente, para parâmetros   $$d,B > 0$$ define-se

O conjunto $$\,\mathbb{Z}[w]_{d,B}\,$$ é formado pelos polinómios numa só variável $$\,w\,$$, de grau inferior a $$d$$,  em que todo o coeficiente $$f_i$$  é limitado $$\,|f_i| \leq B\,$$.

O exemplo paradigmático de problema deste tipo é

> Dado um número racional positivo   $$\,r \,=\,p/q\,$$,  com $$\,p,q \gg B\,$$, determinar   $$\,f\in\mathbb{Z}[w]_{d,B}\,$$ que verifique  $$\,f(r) = 0\,$$.

Se não existisse a restrição de os coeficientes $$f_i$$’s estarem limitados a $$B$$, o problema tinha uma solução trivial: o polinómio do 1º grau  $$\,f(w) \,\equiv \, p - w\,q\,$$.  Como $$p$$ e $$q$$ são positivos e muito maiores do $$B$$, um tal polinómio não é solução do problema.

A solução pretendida constrói-se do modo seguinte:


1. Define-se  um reticulado por uma matriz geradora  $$G\in\mathbb{Q}^{d\times(d+1)}\,$$ construída 


                         $$G \equiv \left[\begin{array}{ccccc|l} 1 & 0 & 0 & \cdots & 0 & L \\ 0 & 1 & 0 & \cdots & 0 & L\,r \\ 0 & 0 & 1 &\cdots&0& L\,r^2 \\ \cdots & \cdots & \cdots & \cdots & \cdots&\cdots \\0 & 0& 0&\cdots& 1&  L\,r^{d-1} \end{array}\right]\quad = \quad \begin{bmatrix}\mathbf{1}_d \,|\, L\, \mathbf{r}^\top \end{bmatrix}$$


    As primeiras $$d$$ colunas formam a matriz identidade; a última coluna é formado pelos  vetor das potências  $$\,\mathbf{r} \,\equiv (r^0,r^1,r^2,\cdots,r^{d-1})\,$$ multiplicado por um “grande inteiro”  $$L\gg B$$.
| **Nota**<br>Uma qualquer combinação linear inteira das linhas desta matriz será $$\,z\,G\,$$ para algum  vetor $$z\in\mathbb{Z}^d\,$$ .<br>Se $$\,z\,$$ for interpretado   como o vetor dos coeficientes de um polinómio de grau inferior a $$d$$<br>                                             $$\, \hat{z}(w) \equiv (z_0 + z_1\,w + \cdots+ z_{d-1}\,w^{d-1})\,$$, <br>então, porque  <br>                                            $$\,z\,\mathbf{r}^\top\,=\,\sum_{i=0}^{d-1}\,z_i\,r^i\, = \, \hat{z}(r)$$ , <br>teremos<br>                                            $$\,z\,G \, = \, \begin{bmatrix} z \;|\; L\times z\,\mathbf{r}^\top \end{bmatrix} \,=\, \begin{bmatrix} z \;|\; L\times \hat{z}(r) \end{bmatrix}$$ |

2. Constrói-se uma matriz  $$\,G'\,$$ aplicando à matriz $$\,G\,$$ um dos algoritmos de redução de base. 
    A primeira linha de $$G'$$  contém o gerador mais curto desta base reduzida.  As primeiras $$d$$componentes dessa linha formam um vetor $$\,z\,$$ que que verifica $$\,\hat{z}(r) = 0$$ e é, provavelmente, uma solução do nosso problema: isto é  $$|z_i| \leq B\,$$ para todo $$i=0..d-1$$.
| **Justificação**<br>Cada linha da matriz reduzida é uma combinação linear das linhas de $$G$$ . Como vimos anteriormente essa linha tem a forma  $$\,\begin{bmatrix} z \;|\;L\,\hat{z}(r)\end{bmatrix}\,$$.<br>Se a linha tem pequeno norma, todas as componentes devem ser pequenas e aproximadamente do mesmo tamanho.  Como $$\,L \gg B$$ então a única forma da última componente ser pequena ocorre quando $$\,\hat{z}(r) = 0.$$<br>Portanto $$\,r\,$$ é raíz do polinómio de coeficientes $$\,z\,$$.<br>Quanto à condição $$\,|z_i|\leq B\,$$ não há garantia que ela seja cumprida. Se não for verificada então a solução está em aumentar o parâmetro $$d$$ ; procura-se um polinómio de maior grau até que a condição se verifique. |

## Algoritmo de Coppersmith

O teorema e algoritmo de Coppersmith derivam diretamente da metodologia de redução linear que esboçámos atrás.

Na sua versão mais simples  o algoritmo de Coppersmith pretende calcular todas as  **pequenas raízes modulares (PRM)** de polinómios inteiros. O problema **PRM** define-se como


> Dados um polinómio  mónico $$\,f\in \mathbb{Z}[w]\,$$ de grau $$d$$ , um inteiro $$\,N>1\,$$ de factorização desconhecida e um limite $$\,X>0\,$$ , determinar todos os  inteiros $$\,r\,$$ tais que $$\,|r|\leq X$$  e 
>                                                                   $$f(r)\,\equiv\, 0 \mod N$$

Este problema pode ser estendido da seguinte forma:


> Dado  um polinómio mónico $$\,f\in \mathbb{Z}[w]\,$$ de grau $$d$$ , um inteiro $$\,N>1\,$$ de factorização desconhecida , um limite $$X>0$$  e um parâmetro racional  $$\,0< \beta \leq 1\,$$, determinar todos os inteiros $$r$$ tais que      $$\,|r| < X\,$$       e.      $$\text{mdc}(f(r),N)\,\geq\,N^\beta\,$$.


| **Note-se que**, <br>No caso particular de ser $$\,\beta=1\,$$, um divisor de $$N$$ só pode ser maior ou igual a $$N^\beta\,$$ se coincidir com $$N$$. Portanto só ocorre $$\,\text{mdc}(f(r),N)=N\,$$ quand $$f(r)$$ é um múltiplo de $$\,N\,$$o que é equivalente a afirmar <br>                                                                             $$\,f(r) \equiv 0 \mod N$$. <br>Portanto o caso $$\,\beta=1\,$$ coincide com o problema **PRM** não estendido. |

O designado **algoritmo de Coppersmith** prova o seguinte resultado

**Teorema de Coppersmith-Graham (versão inteira)** 

> Existe um algoritmo polinomial em $$d$$ e no tamanho de $$N$$ que, sendo   $$X \geq N^{\beta^2/d}\,$$, resolve o problema **PRM** estendido.


| **Esboço do algoritmo de Coppersmith**<br><br>Procurarmos os $$r$$’s tais que $$\,M \equiv \text{mdc}(f(r),N)\,$$ é grande. Se $$M$$ divide tanto $$f(r)$$ como $$N$$ então, para algum $$k$$ que determinaremos em seguida, $$\,M^k\,$$  divide qualquer um dos valores $$\,r^j\,f(r)^i\,N^{k-i}\,$$. <br><br>Considere-se os polinómios $$\,\phi_{i,j}(w)\equiv w^j\,f(w)^i\,N^{k-i}\,$$ com $$i <  k\,$$ e $$\,j < d\,$$. Todos estes polinómios verificam  $$\,\phi_{i,j}(r)\equiv 0 \bmod M^k\,$$e  são linearmente independentes.  Toda a combinação linear inteira dos polinómios $$\,Q(x) = \sum_{i,j}\,z_{i,j}\,\phi_{i,j}\,$$ verifica também $$\,Q(r)\equiv 0 \bmod M^k$$.<br><br>Se os coeficientes de $$Q(w)$$ forem suficientemente pequenos e $$M$$ for suficientemente grande vais-se verificar a relação $$Q(r)\equiv 0 \bmod M^k\,$$ se e só se $$\,Q(r) = 0$$. As raízes de $$Q$$ podem ser calculadas por simples fatorização desse polinómio.<br><br>Por isso, para determinar essas raízes basta determinar $$Q$$.<br><br>Temos $$\,n \equiv k\times d\,$$ polinómios  cujo grau é $$\,\text{deg}(\phi_{i,j})\,=\,j+i\,d\,$$.  O maior grau, é $$\,k\times d - 1$$. <br>Seja $$\Phi\in \mathbb{Z}^{n\times n}$$ a matriz quadrada que se obtém colocando, por linhas, os coeficientes dos vários polinómios $$\,\phi_{i,j}\,$$ ordenados de forma crescente pelo respetivo grau. <br><br>Note-se que $$\Phi$$ é uma matriz triangular; portanto  $$\,\text{det}(\Phi)\,$$é o produto dos elementos na diagonal que são os coeficientes de maior grau dos polinómios $$\,\phi_{i,j}$$: i.e. $$\prod_{j<d}\prod_{i<k}\,N^{k-i} = N^{n\,(k-1)/2}$$. O teorema da redução diz-nos que se determina um vetor $$Q$$ de tamanho $$\,\|Q\|\leq 2^{(n-1)/4}\,N^{n(k+1)/2}$$.<br><br>Aplica-se à matriz $$\Phi$$ um dos algoritmos de redução de base (LLL ou BKZ). A primeira linha da base reduzida (o vetor mais curto) determina o polinómio $$Q$$. <br><br>As condições da redução de base vão determinar o limite mínimo para $$M$$ e para $$X$$. A constante $$k$$ tem de ser suficientemente grande para que a redução da matriz produza um polinómio $$Q(w)$$ com coeficientes suficientemente pequenos; adicionalmente se $$M^k\,$$ for suficientemente grand só é  $$Q(r)$$ um multiplo de $$M^k$$ quando $$Q(r)=0$$. |


O teorema e algoritmo de Coppersmith podem ser aplicada a polinómios em $$w$$ cujos coeficientes são polinómios numa outra variável $$\,\upsilon\,$$.

A versão não estendida do **problema das raízes modulares polinomiais**  será

> É dado um polinómio bivariável $$\,f\in \mathbb{Z}[\upsilon,w]$$ de  grau $$d$$ em $$w$$. É dado um polinómio $$\,N(\upsilon)\,$$de grau $$n>0$$.  Procura-se determinar  todos os polinómios $$\,r(\upsilon)\,$$ de pequeno grau tais que  
>                                                        $$\,f(\upsilon,r(\upsilon)) \,\equiv\, 0 \mod N(\upsilon)$$ 

Mais formalmente o teorema de Coppersmith na sua versão polinomial será.

**Teorema de Coppersmith-Graham (versão polinomial)**

> Dado o polinómio mónico $$\,f\in \mathbb{Z}[\upsilon,w]$$ de  grau $$d$$ em $$w$$; dado um módulo $$N \in \mathbb{Z}[\upsilon]\,$$ de factorização desconhecida e grau $$\,n> 0\,$$; dado um parâmetro racional $$0<\beta \leq 1$$. Em tempo polinomial com $$\,d,n\,$$ é possível  determinar todos $$\,r\in \mathbb{Z}[\upsilon]\,$$ tais que
>                    $$\,\text{deg}_\upsilon r(\upsilon) < \beta^2\,n/d\,$$               e           $$\text{deg}_\upsilon\,\text{mdc}(f(\upsilon,r(\upsilon))\,,\,N(\upsilon))\,\geq\,\beta\,n$$

Esta versão do teorema prova-se precisamente da mesma forma que a versão inteira usando $$\,\mathbb{Z}[\upsilon]\,$$ em substituição de $$\,\mathbb{Z}\,$$ e usando $$\,\text{deg}_\upsilon\,r(\upsilon)\,$$  em substituição do tamanho $$\,|r|\,$$. 


##  Aplicações do algoritmo de Coppersmith

**Inversão do criptograma RSA gerado com pequenas chaves públicas**

No início da operação do RSA era vulgar, por questões de eficiência, usar como chaves públicas, pequenos primos. Nesse caso, pela definição de um RSA  com módulo $$N\,$$e chave pública $$d$$, o criptograma $$\,c < N\,$$ para a mensagem desconhecida $$\,0 < m< N\,$$  verifica

                                             $$\,m^d \equiv c \mod N$$

Vamos supor que são conhecidos alguns bits de representados por um inteiro $$m_0$$; seja $$\,r = m - m_0\,$$ e vamos supor que $$\,|r|\,< \,N^{1/d}\,$$. Defina-se o polinómio

                            $$\,f(w)\,\equiv\, (w+m_0)^d - c\,$$

Então as raízes módulo $$\,N\,$$  de $$\,f(w)\,$$ são inteiros $$r$$ tais que $$(r+m_0)\equiv c \mod N\,$$e que, portanto, permitem calcular a mensagem $$\,m\,$$. 
Os valores de $$r$$ estão nas condições do teorema de Coppersmith (com $$\beta=1$$) e portanto podem ser calculados pelo algoritmo de Coppersmith. 

**Fatorização de um módulo RSA**

Com uma técnica semelhante ao caso anterior. Seja $$\,p\,$$ o maior divisor primo de um módulo RSA $$\,N\,$$; então $$\,p > N^{1/2}$$.  
Suponhamos que são conhecidos pelos menos metade dos bits de $$p$$; isto é, é conhecido um inteiro $$\,p_0 < p\,$$ e pretende-se calcular $$\,r \equiv p - p_0$$  que verifica $$\,r < p^{1/2}$$; ou seja $$\, r < N^{1/4}$$.

Definimos o polinómio   $$f(w) \equiv w + p_0\,$$; este é um polinómio do 1º grau; temos $$d=1$$.

Usando $$\beta=1/2$$ algoritmo  de Coppersmith diz-nos que é possivel calcular eficientemente todos os $$r$$’s que verificam  $$\,\text{mdc}(f(r),N) > N^{1/2}\,$$ e $$\,|r| < N^{1/4}$$. 

Uma vez determinado $$r$$ temos de calcular $$p$$.

Como o maior divisor de $$N$$ é $$p$$, concluimos que $$r + p_0 \equiv 0 \bmod p$$; dado que $$p_0$$ é menor do que $$p$$  e $$\,r < \sqrt{p}\,$$ temos de concluir que tem de ser $$\,r + p_0 = p\,$$.

**CRT** **com erros**

Sejam $$\,\{q_1,q_2,\cdots,q_n\}\,$$módulos CRT ; seja  $$\,N = q_1\times\cdots\times q_n\,$$ . Considerem-se $$n$$ resíduos $$\,y_1,y_2,\cdots,y_n\,$$, com $$\;0\leq y_i < q_i\;$$. O problema CRT é definido pelo conjunto de soluções


                $$\text{CRT}\,\equiv\; \{ x < N \,|\, x \equiv y_i\bmod q_i\;\;\text{para todo}\; i=1..n\}$$
                

e, como sabemos, existe um algoritmo polinomial para as calcular.

No problema **CRT com erros (CRTwe)**   não se exige que todas as relações

                                $$\,x\equiv y_i\bmod q_i\,$$

se verifiquem; abre-se a possibilidade de algumas não se verificarem, e essas são designadas por **erros.** Seja $$\,\mathcal{I}(x)$$ o conjunto formado pelos índices dos não-erros de $$x$$: isto é,

                       $$\mathcal{I}(x)\,\equiv\,\{i\in 1..n\,|\, x \equiv y_i\bmod q_i\}$$
| Como sempre os  subconjuntos  $$\,s\subseteq \{1..n\}\,$$ identificam-se com os  vetores de $$n$$ bits $$\,s\in \{0,1\}^n$$. $$\,$$ |

No problema **CRTwe**   são fornecidos pois parâmetros adicionais: um limite superior $$\,X<N\,$$ ao tamanho da solução $$\,x\,$$ e um limite inferior $$\,t\leq n\,$$ ao número de “não-erros” de $$x$$.


            $$\text{CRTwe}(X,t)\,\equiv\,\{x \leq X\,|\, \exists\, s\in\{0,1\}^n\,\centerdot\,|s| \ge t \,\land\, s \subseteq \mathcal{I}(x) \}$$
            

Claramente este é um problema da classe $$\mathsf{NP}$$; vamos ver que, para valores apropriados dos parâmetros,  é também da classe $$\mathsf{P}$$.

Com o algoritmo CRT pode-se calcular a solução, que designamos por $$\,x_0\,$$, do problema CRT sem erros.  Se se verificar $$\,x_0\leq X\,$$então temos também uma solução do CRT com erros. 

Normalmente isso não ocorre. Sejam $$\,(x, s)\,$$ uma eventual solução do problema e a sua testemunha. Seja $$\,M(s)\equiv \prod_{i\in s}\,q_i\,$$ o produto de todos os módulos  de índices $$i\in s\,$$. Todos os $$M(s)\,$$ são divisores de $$N$$ e, como $$|s|\geq t$$, muito provavelmente $$M(s)> N^{t/n}\,$$.  

| Note-se que $$\,N^{1/n}\,$$é a média geométrica dos módulos $$q_i$$. |

Finalmente, como para todo $$\,i\in s\,$$  se verifica  $$\;x \equiv y_i\bmod q_i\,$$, para, e porque $$x_0$$ também verifica as mesmas relações, terá de se verificar   $$\,x \equiv x_0\mod M(s)\;$$;  portanto $$(x_0-x)$$  é um múltiplo de $$\,M(s)$$.

Isto sugere que se defina o polinómio  $$\,f(w) \equiv w-x_0\,$$. Este é um polinómio com $$d=1$$; usando um $$\beta \simeq t/n\,$$e o algoritmo de Coppersmith, determina-se todos os  $$x$$’s  tais que  $$\,0 < x \leq N^{(t/n)^2}\,$$ e$$\,\text{mdc}(f(x),N) > N^{t/n}$$.  
Se for $$X\geq N^{(t/n)^2}\,$$ , então qualquer valor de $$x$$ assim determinado  é solução do  $$\text{CRTwe}(X,t)$$.

**“Polynomial List Decoding” (PLD)**

O problema PLD pode ser visto como a versão polinomial do problema CRT com erros que acabámos de analisar.  Sumariamente o problema é caracterizado por três parâmetros inteiros $$[n,k,t]\,$$ e pode-se descrever da seguinte forma


> São dados $$\,n\,$$ pares de pontos $$(x_i,y_i)\in \mathbb{Z}_p\times\mathbb{Z}_p\,$$ e procura-se determinar um polinómio de coeficientes inteiros $$\,r \in \mathbb{F}_p[x]\,$$,  de grau menor do que $$k$$,  que verifica em $$\mathbb{F}_p$$
>                                               $$\,r(x_i) \equiv y_i \mod p$$  
> em pelo menos $$t$$ desses pares.


| Uma vez mais é importante realçar o facto de que todo  $$\,x\in\mathbb{Z}_p\,$$ é um inteiro  representante de uma classe de equivalência em $$\,\mathbb{Z}/p\mathbb{Z}$$. Esse inteiro verifica $$\,0\leq x < p\,$$$$\,$$ ou $$\,|x|\leq \lfloor p/2\rfloor\,$$ consoante as aplicações.<br>Desta forma todo o polinómio $$\,r\in \mathbb{F}_p[x]\,$$ é representado por um polinómio em $$\,\mathbb{Z}_p[x]\subset \mathbb{Z}[x]\,$$ cujos coeficientes são representantes dos coeficientes de $$r$$. |

Note-se que a relação acima se pode escrever 

                                 $$\,r(x) \equiv y_i \mod (x-x_i)\,$$ 

e, como $$\,\mathbb{F}_p[x]\,$$ é um PID, pode-se aplicar o CRT a esta situação.

Neste CRT os módulos são os polinómios   $$\,q_i(x) \equiv (x-x_i)\,$$ e  $$\,N(x)\,$$ é, como sempre,  dado por $$\,N(x) \equiv \prod_{i = 1}^n\,q_i(x)\,$$. Todos estes polinómios são módicos  e por isso o seu tamanho é dado pelo grau; temos  $$\,\text{deg}_x(q_i) = 1\,$$ e  $$\,\text{deg}_x(N) = n\,$$.

Usando a mesma estratégia que foi usada no CRTwe, começa-se por calcular a solução deste CRT  sem erros. Seja  $$\,r_0(x)\,$$ essa solução; se for $$\,\text{deg}_x(r_0) < k\,$$ temos encontrada a solução do nosso problema. Se $$\,\text{deg}_x(r_0) \geq k\,$$  vamos recorrer ao algoritmo de Coppersmith na versão polinomial.

Sejam  $$\,(r, s)\,$$ uma solução genérica  e a sua testemunha $$\,s \equiv \{i\in\{1..n\}\,|\, r \equiv y_i \bmod q_i\}\,$$. Seja $$\,M(x)\equiv \prod_{i\in s}\,q_i(x)\,$$. O polinómio  $$M(x)\,$$é mónico , é divisor de $$N$$ e  $$\,\text{deg}_x(M) = |s|\,$$. Como, pelas condições do problema $$|s| \geq t\,$$, definindo $$\,\beta = t/n\,$$, será $$\,\text{deg}_x M > \beta\,n$$.

A construção do CRT força a que se verifique a relação $$\,r \equiv r_0 \mod M\,$$. Isto sugere a construção de um polinómio bivariável  $$\,f \in \mathbb{F}_q[x][w]\,$$ dado por
                                               $$\, f(w) \equiv w - r_0\,$$
Desde que seja $$\,k\geq n\,\beta^2\,$$, o algoritmo de Coppersmith, na versão polinomial, determina de forma eficiente  todas as soluções $$r\in\mathbb{F}_p[x]$$ da relação 
                                          $$\text{deg}_x(\text{mdc}(f(r),N)) \,>\, n\,\beta$$


| É preciso ter em atenção que o algoritmo de Coppersmith polinomial aplica-se a polinómios bivariáveis de coeficientes inteiros; aqui o polinómio $$f$$ é bivariável de coeficientes em $$\mathbb{F}_p$$ e todas as operações algébricas devem ser executadas nesse corpo. Porém, com algum cuidado técnico, pode-se sempre converter $$f$$ num polinómio de coeficientes inteiros. |

| O aspeto mais importante é a relação entre as constantes $$\,n,k,t\,$$. <br>Para ser possível obter soluções do algoritmo de Coppersmith é necessário que se verifique $$\,k \geq n\,\beta^2\,$$. Uma vez que $$\,\beta = t/n\,$$ tem de se verificar<br>                                                       $$\,k/n \geq (t/n)^2\,$$<br>que é a condição fundamental para ser possível a descodificação.<br><br>Frequentemente esta relação exprime-se em termos da *taxa de erros*  $$\,e = n - t\,$$. Dessa forma a condição pode ser escrita como<br>                                                  $$e/n \,\leq\, 1 - \sqrt{k/n}$$ |




# Hard Lattices

Por vários motivos as aplicações criptográficas nos reticulados envolvem, quase sempre e em alternativa aos reticulados euclidianos, os **reticulados inteiros**: isto é, subgrupos de $$\,\mathbb{Z}^n\,$$para algum $$n$$. Entre esses motivos pode-se apontar, por ordem de relevância,

    1. A formalização dos problemas difíceis e a análise da sua complexidade é mais simples em reticulados inteiros do que em reticulados euclidianos. Nomeadamente em reticulados inteiros existem várias reduções de problemas que não não têm formulação análoga nos reticulados euclidianos;
    2. Os geradores de um reticulado euclidiano são elementos de um domínio $$\,\mathbb{R}^m\,$$ ; não é possível, por exemplo, gerar aleatoriamente elementos desse domínio;
    3. Os algoritmos de redução de bases e os os resultados a eles associados (como o teorema de Coppersmith) são mais eficientes e mais flexíveis em reticulados inteiros. 

Um reticulado inteiro tem sempre uma descrição finita: tem uma base finita e cada elemento da base é um vetor de inteiros. Porém a classe dos reticulados inteiros não é finita uma vez que não existe limite aos valores das componentes da base.

Nas aplicações criptográficas é essencial ter classes finitas de reticulados nomeadamente porque a geração aleatória de reticulados só pode ser feita dentro de um domínio finito. Também a análise da complexidade de muitos problemas  exige classe finitas. As classes finitas de reticulados inteiros são sempre **periódicas**, uma vez que é preciso ter um limite máximo para o tamanho das descrições dos  elementos dessa classe.

 Uma **classe periódica** de reticulados inteiros  $$\,\mathcal{L}\subset \bigcup_n\mathbb{Z}^n\,$$  é determinada por  parâmetros $$\,[n,k,q]\,$$ em que 

        1. $$n$$ é a **dimensão do**  **“span”** do reticulado: $$\,\mathbf{span}(\mathcal{L})\,\equiv\,\mathbb{Z}^n\,$$;
        2. $$k$$  é a **dimensão do reticulado**  $$\,\mathcal{L}\,$$ como subgrupo de $$\,\mathbb{Z}^n$$ ;
        3. $$\,q\,$$ é o **período** do reticulado: isto é, um número primo tal que $$\,q\,\mathcal{L}\,\equiv\, \mathcal{L}$$ ;

Um reticulado genérico da classe $$\,[n,\kappa,q]\,$$ pode ser definido de duas formas: através de uma **base de geradores**  $$\,\mathcal{B}\,$$ ou de uma **base de paridades** $$\,\mathcal{H}$$, 


    - Uma base de geradores é formada por $$\,\kappa\,$$ vetores linearmente independentes
                                $$\,\mathcal{B}\,\equiv\,\{g_1,\cdots,g_\kappa\}\,\subset \mathbb{Z}^n_q$$
        e define a matriz **** $$\,B\in \mathbb{Z}_q^{\kappa\times n}$$ cuja linha de ordem $$\,i\,$$ coincide com o gerador $$\,g_i\,$$. Nesse caso
                            $$\mathcal{L} = \Lambda(\mathcal{B}) \,\equiv\,\{y\in\mathbb{Z}^n \;|\;\exists\,z\in \mathbb{Z}^\kappa\,\centerdot\, y \equiv z\,B \mod q\}$$
                    
    - Uma base de paridades é formada por $$\,\ell\equiv n-k\,$$ vetores linearmente independentes
                                $$\mathcal{H}\,\equiv\,\{h_1,\cdots, h_\ell\} \,\subset\,\mathbb{Z}_q^n$$
        e define a matriz $$\,P\in \mathbb{Z}_q^{\ell\times n}\,$$ cuja linha de ordem $$\,i\,$$é a paridade $$\,h_i\,$$; agora
                        $$\mathcal{L}\,=\,\Lambda^\ast(\mathcal{H})\,\equiv\,\{y\in \mathbb{Z}^n\;|\; y\,P^\top \equiv 0 \mod q\}$$

O reticulado é periódico porque, se $$y\in\mathcal{L}\,$$ então qualquer vetor da forma  $$\,y + q\,x\,$$ com $$\,x\in \mathbb{Z}^n\,$$também é um elemento do reticulado.

| É simples verificar que, se se for  $$\,B\,P^\top \equiv 0 \mod q\,$$, então<br><br>1. $$\,(\Lambda(\mathcal{H}))^\ast \,\equiv\, \Lambda^\ast(\mathcal{H}) \,\equiv\,\Lambda(\mathcal{B})$$<br>2. $$\,(\Lambda(\mathcal{B}))^\ast\,\equiv\, \Lambda^\ast(\mathcal{B})\,\equiv\,\Lambda(\mathcal{H})$$<br><br>A condição $$\,B\,P^\top \equiv 0 \mod q\,$$ é equivalente à condição<br>                                                      $$\langle g_i\cdot h_j\rangle \equiv 0 \mod q$$                 para todo $$i=1..\kappa$$  e todo $$j=1..\ell$$ |



## Matrizes Geradores e de Paridades de “Hard Lattices”

As “hard lattices” na classe $$\,[n,\kappa,q]\,$$ são essencialmente  reticulados inteiros e, portanto, subgrupos de algum $$\,\mathbb{Z}^m$$. Como tal têm uma matriz geradora $$G$$ e uma matriz de paridades $$H$$ geradas a partir das matrizes $$\,B\,$$ e $$\,P\,$$ que definimos atrás.

Num reticulado periódico $$\,\mathcal{L}\equiv\Lambda(\mathcal{B})\,$$ cuja base determina a matriz $$\,B\in\mathbb{Z}_q^{\kappa\times n}\,$$ e define
                                        $$\,\mathcal{L}\,\equiv\,\{y\in \mathcal{Z}^n\,|\,\exists z\in \mathbb{Z}^\kappa\,\centerdot\, y \equiv z\,B \mod q \}\,$$ 
o que é equivalente a escrever

                              $$\,\mathcal{L}\,\simeq \,\{(z,y)\in\mathbb{Z}^\kappa\times \mathbb{Z}^{n}\;|\;\exists\, (z,w)\in \mathbb{Z}^\kappa\times \mathbb{Z}^n\,\centerdot\, y = z\,B + w\,q \}\,$$ 

Obtém-se  assim um reticulado de dimensão $$\,\kappa+n\,$$, isomórfico  com $$\,\mathcal{L}\,$$, e definido pela matriz geradora 

                                                   $$G\,\equiv\,\left[\begin{array}{c|c} \mathbf{1}_\kappa & B \\  \mathbf{0}_n & q\,\mathbf{1}_n \end{array}\right]$$

De forma análoga, se o reticulado tem a forma $$\,\mathcal{L}\, \equiv \Lambda^\ast(\mathcal{H})$$ e as paridades $$\mathcal{H}$$ determinam a matriz $$\,P \in\mathbb{Z}^{\ell\times n}\,$$ cuja $$j$$-ésima linha é a paridade $$\,h_j\in\mathcal{H}$$, então

                                                $$\mathcal{L}\,\equiv\,\{y \in \mathbb{Z}^n\;|\; y\,P^\top \equiv 0 \mod q\}$$

o que é equivalente a 

                           $$\mathcal{L}\;\simeq\; \{ (w,y)\in \mathbb{Z}^\ell\times \mathbb{Z}^n \;|\; w\,q + y\,P^\top = 0 \}\,$$

Obtém-se um reticulado que é subgrupo de $$$$$$\,\mathbb{\ell+n}\,$$ e tem a matriz de paridades $$\,H\in \mathbb{Z}^{\ell\times (\ell + n)}$$ 

                                                    $$\,H\,\equiv\, \left[\begin{array}{c|c} q\,\mathbb{1}_\ell & P \end{array}\right]$$

A dimensão desse reticulado será $$\,(\ell + n) - \ell = n$$.
        $$$$

## Problemas SIS e LWE

A maioria dos criptosistemas algébricos pós-quânticos deriva a segurança de dois problemas cuja complexidade computacional se analisa no caso médio: **Short Integer Solution (SIS)** e **Learning With Errors (LWE).**

| Recorde-se que em quase todos os problemas ditos “difíceis” a análise de complexidade é feita para o “pior caso”; um problema que seja muito complexo “no pior caso” não impede que os casos onde ele é “pouco complexo” sejam frequentes e previsíveis. Por isso um problema  que tenha elevada “complexidade média “ dá maelhores garantias de segurança do que um que tenha elevada complexidade no pior caso. |

Ambos os problemas são definidos numa classe $$\,[n,\kappa,q]\,$$ de reticulados inteiros periódicos em que $$\,n = \text{poly}(\kappa)\,$$ e $$\,q = \text{poly}(\kappa)\,$$. No grupo $$\,\mathbb{Z}^n\,$$ usa-se a norma $$\ell_2$$: i.e.  $$\,\|y\| = \sqrt{y_1^2 +\cdots+y_n^2}\,$$.

O problema $$\,\mathbf{SIS}_\beta\,$$ , com $$\,\beta < q\,$$,  é definido por uma matriz $$\,H\in \mathbb{Z}_q^{(n-\kappa)\times n}\,$$  de “rank” completo e aleatoriamente gerada. Pretende-se determinar um $$\,y\in\Lambda^\ast(H)\,$$  que  verifique $$\,\|y\| \leq \beta\,$$.
                                                         $$\,y\,H \equiv 0 \mod q$$
                                                         
Para $$\,\beta > \sqrt{\kappa\log_2\,q}\,$$  existe sempre uma solução. Para estes parâmetros Ajtai provou que existe uma *redução do pior caso ao caso médio*; isto é, provou que na classe $$\,[n,\kappa,q]$$

> resolver $$\,\mathbf{SIS}_\beta\,$$ no caso médio é pelo menos tão complexo quanto resolver no pior caso  problemas standard $$\gamma$$-SVP ,  com $$\,\gamma = O(\beta\,\sqrt{\kappa})$$.

O problema $$\,\mathbf{LWE}_\alpha\,$$, com $$\,0< \alpha < 1\,$$ um parâmetro que mede, de alguma forma, a dispersão dos erros. Nomeadamente, numa distribuição  gaussiana discreta no domínio $$\,\mathbb{Z}_q\,$$centrada em $$0$$,  o parâmetro $$\,\alpha\,$$  determina o desvio padrão $$\,\sigma\equiv \alpha\,q$$ ;  tal distribuição é representada  por $$\,\chi_\alpha\,$$.

O problema é definido por  um segredo $$\,s\in\mathbb{Z}_q^{\kappa}\,$$ , por uma matriz  $$\,A\in\mathbb{Z}_q^{\kappa\times n}\,$$ “full rank” e gerada aleatoriamente e por um vetor de erros  $$\,e\in \mathbb{Z}_q^n\,$$ gerado pela distribuição  $$\,\chi^n\,$$.  O  problema consiste em determinar o par  $$(s,e)$$ a partir do conhecimento da matriz $$\,A\,$$ e de um vetor $$\,b\in \mathbb{Z}^n\,$$
 que verifica   $$\;b \equiv s\,A + e \bmod q\,$$.

| Nos problemas  $$\,\mathbf{LWE}\,$$ ou $$\mathbf{RLWE}$$   o domínio $$\,\mathbb{Z}_q\,$$ identifica-se com  $$\,\{x\in\mathbb{Z}\,|\,|x| \leq \lfloor q/2\rfloor\}\,$$. |

O problema foi formulado por Regev em 2005 que veio mais tarde a provar que, 

> Com $$\,\alpha\,q \geq 2\,\sqrt{\kappa} \,$$ resolver $$\,\mathbf{LWE}_\alpha\,$$ no caso médio é pelo menos tão complicado como resolver,  o pior caso de  $$\gamma$$-SVP ,  com $$\,\gamma = O(\sqrt{\kappa}/\alpha)$$,  usando computação quântica.


Para comparar os dois problemas temos de recorrer a uma mesma fonte $$\mathcal{S}$$ de vetores curtos. Este gerador tanto pode ser a esfera $$\{y \;|\;\|y\|\leq \beta\}\,$$ , usada no $$\,\mathbf{SIS}_\beta\,$$, como a distribuição $$\,\chi_\alpha^n\,$$  usada no $$\,\mathbf{LWE}_\alpha\,$$. Porém tem de ser a mesma para os dois casos.

Cada um dos problemas determina,  uma função;

    - No SIS , define-se  a função $$\,f_{A} \colon \mathcal{X}\,\to\, \mathbb{Z}_q^\ell\;$$  , indexada por uma matriz $$\,A\in\mathbb{Z}_q^{n\times\ell}$$,  como
                                        $$\,f_A\,\colon\, y \,\mapsto\, y\,A \mod q$$
    - No LWE,  define-se  $$\,g_{A}\;\colon\; \mathbb{Z}^\kappa \times \mathcal{X}\;\to\;\mathbb{Z}^n\,$$  , indexada por uma matriz $$\,A\in\mathbb{Z}_q^{\kappa\times n}$$,  como
                                      $$g_{A} \;\colon\; (s,e) \;\mapsto\; s\,A + e\mod q$$

A inversão destas funções caracteriza a complexidade de cada um dos problemas. Prova-se que, com $$\,\ell + \kappa = n\,$$ e as matrizes $$A$$ aleatoriamente geradas, a função $$\,g_A\,$$ é unidirecional se e só se $$\,f_A\,$$ for unidirecional. Isto permite supor que cada dos problemas é tão difícil quanto o outro.





