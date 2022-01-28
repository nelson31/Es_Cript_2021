# Prólogo 2:  Complexidade Descritiva e Aleatoriedade.

# Complexidade  descritiva


## Definição

A **complexidade descritiva** de uma string finita $$\,y\,$$ , representada por $$\,K(y)\,$$, é uma medida da quantidade de informação em $$y$$, avaliada através do *esforço computacional mínimo* necessário para  “construir” $$\,y\,$$.

Pode-se ver a complexidade descritiva de $$y$$ como o comprimento da menor **descrição** de $$\,y\,$$; isto é, a mais curta  string a partir da qual é possível computar $$\,y\,.$$

Como a construção da string $$\,y\,$$ realiza-se sempre através de uma máquina de estados  $$\,\mathcal{M}\,$$, a descrição de $$y$$ pode ser concretizada num programa  $$\,p\,$$ que a máquina aceita e que, para um input de referência $$\,0\,$$,  produz o resultado $$\,y\,$$. Isto é

                                      $$\,\mathcal{M}_p(0)\;\simeq\;y$$

O *esforço* da computação pode ser medido pelo comprimento $$\,|p|\,$$do programa. 

Dado que podem existir vários programas que constroem o mesmo $$\,y\,$$ , e como associamos a complexidade descritiva ao *esforço mínimo,* pode-se definir 

                               $$K_\mathcal{M}(y)\;\equiv\;\min\{|p|\,|\,\mathcal{M}_p(0)\,\simeq\,y\}$$
----------

**Nota**
O “input” da máquina $$\,\mathcal{M}\,$$ descreve a informação que é conhecida *a priori* sobre $$\,y\,$$. O inteiro $$\,0\,$$, equivalente à string vazia $$\,\varepsilon\,$$, denota ausência de informação.

Se for conhecida uma informação arbitrária  $$\,x\,$$ define-se

                          $$K_\mathcal{M}(y\,|\,x)\;\equiv\;\min\{\,|p|\;|\;\mathcal{M}_p(x)\,\simeq\,y\,\}$$

como a ***complexidade descritiva de*** **$$y$$ *****conhecido*** **$$x$$.

Obviamente a complexidade descritiva de $$\,y\,$$ conhecido $$\,x\,$$ é sempre limitado pela complexidade descritiva de $$\,y\,$$; a diferença

                                $$\mathbf{I}(x;y) \;\equiv\; K_\mathcal{M}(y) - K_\mathcal{M}(y\,|\,x)$$

designa-se por **informação de** $$\,x\;$$ **em** $$\,y\,$$.  

----------


## Máquinas livres de prefixos e universais.

Com estas  definições, a complexidade depende da máquina $$\,\mathcal{M}\,$$. Não faz sentido que existam medidas da informação independentes entre si, para a mesma string $$y$$ , apenas porque são usadas máquinas diferentes como referência.
Ao invés é melhor definir uma  classe de máquinas $$\,\mathcal{M}\,$$que permita ter medidas coerentes de complexidade descritiva para qualquer  máquina específica dentro dessa classe.  Assim vamos restringir a classe das máquinas de estado $$\,\mathcal{M}\,$$


1. Todas as máquinas de referência devem ser **livres de prefixos**. 
    Uma máquina $$\,\mathcal{M}\,$$é livre de prefixos quando, para todo o programa $$\,p\,$$ e todo “input” $$\,x\,$$onde  $$\,\mathcal{M}_p(x)\!\downarrow\,$$, não existe qualquer sufixo $$\,q \succ p \,$$ tal que    $$\,\mathcal{M}_{q}(x)\!\downarrow\,$$.  


2. Todas as máquina de referência têm de ser  **universais**. 
    Uma máquina livre de prefixos  $$\,\mathcal{M}\,$$ é universal quando, para toda a função parcialmente  computável  $$\,f\colon \mathbb{N}\to \{0,1\}\,$$existe uma “string” $$\,\sigma\,$$, dependente de $$\,f$$, tal que 
                                            $$\forall\,x \,\centerdot\,\mathcal{M}_{\sigma}(x)\;=\; f(x)$$
    A “string” $$\,\sigma\,$$é a **codificação** de $$\,f\,$$ em $$\,\mathcal{M}\,$$e o seu comprimento  $$\,|\sigma|\,$$ é a **constante de codificação** de $$\,f\,$$.
    
| **Exemplo**<br><br>A **máquina de cópia** $$\,\mathcal{C}\,$$é uma máquina  de estados que só aceita programas da forma <br>                                                         $$p(y)\,\equiv\,0^{|y|}\,1\,y$$<br>e produz a string $$y$$ como resultado de um tal programa.<br>Apesar de $$\,\mathcal{C}\,$$ não ser uma máquina universal, ela é livre de prefixos. Por isso pode simulada numa máquina universal livre de prefixos arbitrária $$\,\mathcal{M}\,$$. Isto significa que existe um programa $$\,\sigma\,$$ tal que<br>                                                                        $$\mathcal{M}_{\sigma\,p(y)}\;=\;\mathcal{C}_{p(y)}\,=\, y$$  <br>Por este motivo tem-se<br>                                               $$K_\mathcal{M}(y)\,\leq\,|\sigma\,p(y)|\;\leq\; |\sigma| + |0^{|y|}| + 1 +|y| \;\leq\;c + 2\,|y|$$  <br>sendo $$\,c\,$$ a constante $$\,1+|\sigma|\,$$. |

----------

O seguinte quadro ilustra algumas propriedades mais importantes desta noção de complexidade descritiva. Considere-se uma máquina livre de prefixos e universal arbitrária $$\,\mathcal{M}$$.

**Facto 1**
A complexidade descritiva é definida a menos de uma constante aditiva. Isto é, para qualquer outra máquina $$\,\mathcal{M}'\,$$ existe uma constante $$\,c\,$$  tal que, para todo  $$\,x\,$$, 

                                          $$\,K_\mathcal{M}(x)\,\leq \,c + K_{\mathcal{M}'}(x)$$
            

Como corolário  $$\,\mathbf{I}(x;y)\,$$ é independente da máquina $$\,\mathcal{M}\,$$.
     
**Facto 2**
Se a função  $$\,f\colon\,\mathbb{N}\to\mathbb{N}\,$$ é computável, então  existe uma constante $$\,c\,$$ tal que para todo $$\,x\,$$ 

                                     $$K_\mathcal{M}(f(x))\,\leq\,c + K_\mathcal{M}(x)$$

Adicionalmente,  não existe uma função $$\,f\,$$ parcialmente computável e de domínio ilimitado que   verifique $$\; f(x)\,\leq\,K_\mathcal{M}(x)\,$$, para todo $$\,x\,$$onde  $$\,f(x)\,$$é definido.

**Facto 3**
Existe uma constante $$\,c>0\,$$ tal que, para todo $$\,x\,$$

                                $$K_\mathcal{M}(x)\,\leq\,c + |x| + K_\mathcal{M}(|x|)$$
----------

A construção de pares de $$\,\langle x, y\,\rangle\,$$e da sua complexidade descritiva, representada por $$\,K_\mathcal{M}(x,y)\,$$, é uma aspeto fundamental em muitas aplicações desta medida de informação.

| O primeiro ponto a analisar é a forma como se pode codificar um par de strings  $$\,x,y\,$$ numa única string. <br>No documento Prólogo apresentamos, sem justificação, uma tal codificação.<br>Note-se que, dado que o comprimento das strings é arbitrário, não é possível codificar o par na simples concatenação $$\,w\,\equiv\,x\,y\,$$ das duas strings; isto porque dado $$\,w\,$$ tem de existir um mecanismo “separar”  $$\,x\,$$ de $$\,y\,$$: para selecionar cada componente independentemente da outra.<br><br>Para tal pode-se usar a codificação<br><br>                                               $$\,\langle x,y\rangle\;\equiv\;0^{|x|}\,1\,x\,y$$<br><br>O prefixo $$\,0^{|x|}\,1\,$$ permite descrever o comprimento da 1ª componente: uma sequência de $$0$$’s de comprimento igual à informação que se quer transmitir, seguida de um $$\,1\,$$que marca a terminação da mesma. Com essa informação é possivel separ no sufixo $$\,x\,y\,$$ a componente $$\,x\,$$da componente $$\,y\,$$. |

Nestas circunstâncias prova-se

**Teorema**
Existe uma constante $$\,c\,$$ tal que, para todo o par de “strings” $$\,x,y\,$$ , tem-se
                                          $$K_\mathcal{M}(x, y)\,\leq c + K_\mathcal{M}(x) + K_\mathcal{M}(y\,|\,x^\ast)$$
sendo $$\,x^\ast\,$$ a descrição óptima  de $$\,x\,$$; isto é, o programa mais curto tal que $$\,\mathcal{M}_{x^\ast}(0)\simeq x$$.
Add a note


----------
## Máquinas  óptimas e complexidade descritiva ótima

A complexidade descritiva é frequentemente usada para comparar a quantidade de informação em duas “strings” distintas. Note-se que, pelo resultado anterior, tem-se sempre

                                      $$K_\mathcal{M}(y)-K_\mathcal{M}(x)\;=\;K_{\mathcal{M}'}(y)-K_{\mathcal{M}'}(x)$$

Portanto as diferenças entre complexidades descritivas independente da máquina de referência usada. O seguinte teorema dá uma ajuda adicional à definição de complexidade descritiva

**Teorema**

> De entre todas as máquinas de estado universais e livres de prefixos existem **máquinas óptimas**  $$\,\mathbb{U}\,$$ que verificam, para todo $$\,y\,$$,  $$\,K_\mathbb{U}(y) \leq 1 + |y| + K_\mathbb{U}(|y|)$$.

Desta forma, a menos que a máquina de estados $$\,\mathcal{M}\,$$ seja explicitamente escolhida,  toma-se como referência na definição de complexidade descritiva uma máquina óptima.
 
                                             $$K(y)\;\equiv\; K_\mathbb{U}(y) \;=\; \min\,\{|p|\,|\, \mathbb{U}_p(0)\,\simeq y\}$$
                                            
  Com esta definição de máquina de referência temos, para qualquer $$y$$,
  

                                 $$K(y)\;\leq\;1 + |y| + K(|y|)$$
                        
## Complexidade descritiva relativa a um oráculo.

A máquina  óptima $$\,\mathbb{U}\,$$ pode consultar um oráculo $$\,X\,$$. Por isso faz sentido  estender a noção de complexidade descritiva  impondo uma relação com um oráculo

                              $$K^X(y)\;\equiv\;\min\,\{|p|\,|\, \mathbb{U}^X_p\simeq y\}$$
                    

Uma descrição de $$y$$ com a ajuda de um oráculo $$X$$ permite verificar se alguma da informação própria de $$y$$  é mais simples de extrair com o oráculo ou sem o oráculo. 

Como, em último caso, a computação com oráculo pode simplesmente ignorá-lo, então as descrições com oráculo são sempre mais curtas com oráculo do que sem oráculo. Por isso tem-se sempre

                                          $$K^X(y) \leq K(y)$$


## $$K$$-“lowness”  e $$K$$-trivialidade

Pode acontecer também que o oráculo $$X$$ não forneça qualquer ajuda às descrições dos $$y$$’s. Nomeadamente pode acontecer que o oráculo $$\,X\,$$ verifique a seguinte condição


> Existe uma constante $$c>0$$ tal que, para todo  $$\,y\,$$ , se verifica
>                                        $$K^X(y) + c \geq K(y)$$  
> Neste caso  diz-se que $$X$$ é   $$K$$-**low**.

Esta condição exprime o ponto de vista que extrair informação de uma “string” arbitrária $$\,y\,$$é equivalente à capacidade de comprimir essa “string”. 
A condição compara duas situações: comprimir com a ajuda do oráculo $$\,X\,$$ e sem ajuda de $$X$$. Quando, a menos de uma constante $$c$$, a ajuda do oráculo não permite ganhar qualquer vantagem na compressão, então o oráculo é $$K$$-low.

| **Nota**<br>A propriedade de “lowness” é muito importante na caracterização das condições de segurança de várias técnicas criptográficas. <br>De facto muitas vezes é possível modelar ataques criptográficos a uma determinada técnica criptográfica, como computações com oráculos em que o oráculo descreve a informação disponível pelo atacante.<br>Se o oráculo for “low”, isso significa que não é possível extrair, de qualquer string $$y$$, mais informação com o oráculo do que a que é possível extrair sem esse oráculo. <br>Com esta condição é possível caracterizar  a resistência ao ataque já que a informação proveniente de um oráculo “low” acaba por ser equivalente à informação nula. Do acesso ao oráculo o atacante não extrai qualquer vantagem. |


Dado que esta “incapacidade de extrair informação” é algo essencial não só à segurança das técnicas criptográficas mas também a muitas outras aplicações, é natural pensar em obter formas alternativas de caracterizar esta propriedade.

Recordemos o **facto 2** acima onde se afirma que, dada qualquer função computável $$\,f\colon\mathbb{N}\to\mathbb{N}\,$$, então


> existe uma constante $$\,c\,$$, tal que 
>                                    $$\,\forall\,n\,\centerdot\; K(f(n))\, \leq\, c + K(n)$$

Pode-se interpretar esta condição, de uma forma mais geral, como a definição de uma propriedade de uma função $$\,f\,$$ arbitrária.
Uma  função que verifique esta condição diz-se  $$\,K$$-**trivial**. 

O referido **facto 2** afirma, simplesmente, que toda a função computável é $$\,K$$-trivial. Porém o inverso não é verdade: de facto é possível construir uma função não computável que seja $$K$$-trivial.

Uma “stream”/conjunto $$X$$ define uma função  $$\,{X}\,\colon\, \mathbb{N}\to \mathbb{N}\,$$ através da noção de prefixo:    $${X}(n)\;=\;\sum_{k<n}\,X_k\,2^{k}$$ . 
Assim é possível aplicar a noção de $$K$$-trivialidade  também a “streams” ou conjuntos.  A condição
                            $$\,\forall\,n\,\centerdot\,K(X(n)) \leq c + K(n)\,\leq\,c + 2\,|n|$$
diz que, para todo $$n$$, o tamanho da compressão ótima do prefixo $$\,X(n)\,$$ é, aproximadamente, proporcional ao número de bits de $$n$$.

Um teorema fundamental é o que afirma que estes dois conceitos, “lowness” e trivialidade, são realmente um só

**Teorema**

> Um conjunto $$X$$ é $$\,K$$-low se e só se  é $$\,K$$-trivial.

Adicionalmente o teorema diz-nos que a capacidade de extrair informação do oráculo $$X$$ está diretamente ligada ao número de bits necessários para descrever o comprimento de cada prefixo de $$X$$.

# Incompressibilidade de “strings”
                                

Existe uma relação fundamental entre as noções de *descrição*  e *compressão* de uma string $$\,y\,$$. A complexidade descritiva $$\,K(y)\,$$é o comprimento da mais curta descrição de  $$y$$: isto é, de um programa $$\,p\,$$que permite construir $$\,y\,$$ numa máquina universal livre de prefixos.  Sendo $$p$$ a mais curta descrição, então $$\,p\,$$ pode ser visto como uma ***compressão*** ótima de  $$y$$.

                                

Por isso faz sentido definir, dado uma constante $$\,c>0\,$$

                                
    - $$y\,$$ é  $$c$$**-incompressível** quando
                                  $$\,K(y) + c > |y|$$
    - $$y\,$$ é **fortemente** $$c$$**-incompressível** quando 
                                  $$K(y) + c > |y| + K(|y|)$$

Um programa $$\,p\,$$ que verifique
                                           $$\,\mathbb{U}_p(0)\simeq y\,\land\, |p| = K(y)\,$$
é, como referimos, interpretado como uma **compressão óptima** de $$\,y\,$$.  Pode-se ordenar lexicograficamente todos estes  $$\,p\,$$’s  de definir o mínimo dessa ordenação como $$\,y^\ast\,$$.
Seria ideal poder calcular esta compressão óptima $$\,y^\ast\,$$ a partir de $$\,y\,$$; se tal fosse possível não seria necessário investigar  outros algoritmos de compressão porque a função  $$\,y \,\mapsto\, y^\ast\,$$ seria sempre melhor. 
Infelizmente **a função** $$\,y \,\mapsto\,y^\ast\,$$ **não é computável** e é, quanto muito, aproximada por funções computáveis.

| Um recente artigo de Paul Vitányi (*”How Incomputable is Kolmogorov Complexity”* , Março 2020,*ArXiv* :*07674v2*) , incluído na documentação da disciplina, faz uma revisão dos principais argumentos usados para provar essa incomputabilidade. |

Também a função $$\,y \mapsto K(y)\,$$ não é computável e pode apenas ser aproximada. Porém essa função está relacionada com o conjunto das strings $$c$$-compressíveis. 

Para cada $$\,c\geq 0\,$$ represente-se por $$\,\mathcal{R}_c\,$$ o conjunto das strings $$c$$-compressíveis. Pela definição acima, tem-se

                                 $$\mathcal{R}_c\;\equiv\;\{\,y\,|\, K(y) + c \leq |y|\,\}$$

Então

**Teorema**
A família de conjuntos  $$\,\{\mathcal{R}_c\}_{c\in \mathbb{N}}\,$$ é uniformemente enumerável.  Isto é, existe uma função computável  $$\,f\,$$ tal que $$\,y\in \mathcal{R}_c\,$$ se e só se $$\,y = f(c,n)\,$$ para algum $$n$$.

Adicionalmente a **probabilidade** de se verificar $$\,y \in \mathcal{R}_b$$ $$\,$$, medida como
                                                 $$\mu(\mathcal{R}_c)\;\equiv\;\sum_{y\in\mathcal{R}_c}\,2^{-|y|}$$
é fortemente limitada: verifica-se  $$\,\mu(\mathcal{R}_c)\,\leq\,2^{-c}$$. 

Portanto a probabilidade de alguma string $$\,y\,$$ ser $$c$$-compressível  diminui muito rapidamente quando $$\,c\,$$ cresce.

# Aleatoriedade


## Conceitos de aleatoriedade

A noção de aleatoriedade é das mais importantes em criptografia; é usada para descrever obscurantismo (a incapacidade de extrair informação concreta de um objeto) e imprevisibilidade das transformações nesses objetos. É  também o mecanismo preferencial na geração de segredos, chaves, etc.

Informalmente um objeto é aleatório se é desorganizado; isto é, não contém padrões nem regularidades. Nomeadamente, é imprevisível no sentido em que não é possível computar, a partir de uma visão parcial do objeto, qualquer informação que não esteja contida nessa “visão”.

Uma definição precisa de aleatoriedade é muito difícil e subtil e são frequentes, na literatura, “definições” que parecem simples e naturais mas que são incorrectas. Para as evitar é preciso ter em conta alguns pontos fundamentais. 

Em primeiro lugar, o qualificativo aleatório aplica-se exclusivamente a objetos que têm uma representação infinita.  Só podem ser aleatórios conjuntos infinitos $$\,A\subseteq \mathbb{N}\,$$ ou entidades que lhe são isomórficas: streams infinitas  $$\omega\in \{0,1\}^\infty\,$$, reais de Lebesgue ou funções  da forma$$\,h \colon \mathbb{N} \to \{0,1\}^t\;$$ (adiante designadas por  **funções de hash**). 
Strings finitas, conjuntos finitos ou números inteiros podem ser *aleatóriamente gerados* mas não são aleatórios: o que é eventualmente aleatório é o mecanismo para os gerar.

Em segundo lugar, testes estatísticos  não servem para definir aleatoriedade.
Na sua forma mais simples um teste estatístico conta o número de bits $$1$$’s em cada truncatura $$\,\omega(k)\,$$  da stream $$\,\omega\,$$  e verifica se esse  número é aproximadamente  $$1/2$$ do número total de bits. A cardinalidade de $$\,\omega(k)\,$$, visto como conjunto, coincide com o número de $$1$$’s; o valor máximo é $$k$$. Portanto testa-se se 

                                $$\lim_{k\to\infty}\,\#\omega(k)/k\;=\; 1/2$$ 
                            

Esta propriedade designa-se por  **lei dos grandes números** (LLN). Parece natural  mas não define aleatoriedade.


| É simples construir uma stream que verifica a LLN e, obviamente, não é aleatória. Basta escolher um padrão finito com tantos $$1$$’s quantos $$0$$’s e definir $$\omega$$ como a repetição infinita deste padrão; por exemplo<br><br>                                   $$\omega\;\equiv\; 1\,0\,1\,0\,1\,0\,\cdots\,\,1\,0\,\cdots$$ <br><br>verifica LLN e não é aleatória.<br><br>Pode-se melhorar a relação entre a LLN e aleatoriedade introduzindo um filtro que elimina alguns bits de $$\,\omega\,$$e verifica se a stream resultante verifica a LLN. <br><br>Genericamente um teste estatístico aplicado a uma stream $$\,\omega\,$$é determinado por uma função computável   $$\,S\colon \{0,1\}^\ast \to \{0,1\}\,$$  que, como conjunto, é infinito. Esta função, designada de *seleção,* constrói uma seleção de bits de  $$\,\omega\,$$ calculando sucessivamente  $$S(\omega(k))\,$$e, consoante este valor, mantém o  bit $$w_k$$ na stream ou elimina-o.  Formalmente constrói-se a stream “selecionada” $$\,s(\omega)$$ da seguinte forma<br><br>  $$s(\omega;0)\;\equiv\;\varepsilon$$<br>  $$s(\omega;k)\;\equiv \;\left\{\begin{array}{ll}s(\omega;k-1) & \text{se}\;S(\omega(k))=0\\ s(\omega;k-1)\,\omega_k & \text{em caso contrário}\end{array}\right.$$<br><br><br>> Se para todas as seleções $$\,S\,$$ a stream  $$\,s(\omega)\,$$ verifica a LLN, então a stream $$\omega$$ diz-se **estocástica.**<br><br>Pode parecer que o facto de uma stream ser estocástica é uma boa garantia de aleatoriedade. Tal não é verdade;  prova-se que existem streams que são estocásticas mas não são aleatórias. Isto é o resultado de todas as seleções $$S$$ serem computáveis; só se existisse uma seleção aleatória é que ser estocástico garantia a aleatoriedade |

----------

Na Teoria da Computabilidade ocorrem alguns (poucos) princípios que permitem abordar corretamente a aleatoriedade.

A “*aleatoriedade como incompressibilidade”* parece ser  um desses princípios  isto porque strings incompressíveis verificam algumas propriedades que intuitivamente associamos a aleatoriedade.
Por exemplo pode-se provar que

    - Strings incompressíveis só contêm curtas sequências de zeros  (“zero runs”).
    - Numa string incompressível, o número de ocorrências de $$0$$’s é, aproximadamente, metade do comprimento da string. No limite, quando o comprimento da “string” tende para infinito, verifica-se a “lei dos grandes números” nessa string.

Formalmente prova-se que

**Facto 1  #incompressibilidade_zero_runs**

> Seja $$\,x\,$$ uma string finita; se existir um “zero run” em $$\,x\,$$ de comprimento $$\,t\geq  4\,\log|x|\,$$,   então, para algum $$\,d\,$$, tem-se $$\,K(x) < d + |x| - \log |x|\,$$.

**Facto 2  #incompressibilidade_lei_dos_grandes_numeros**

> Para todo $$\,c>0\,$$, se $$\,x\,$$ for  $$c$$-incompressível e  $$\,|x|\,$$  crescer  para o infinito, então $$\,x\,$$ verifica a lei dos grandes números; isto é, o números de $$\,0$$’s em $$\,x\,$$é, muito aproximadamente, igual ao número de $$\,1$$’s. 


## Definição de $$K$$-aleatoriedade  (Kolmogov)

As observações anteriores sugerem a seguinte definição de aleatoriedade


> **Definição**
> Uma stream $$\,\omega\,$$ é  $$K$$-**aleatória** quando existe algum $$\,c>0\,$$ tal que, para todo $$\,n>0\,$$o prefixo $$\,\omega(n)\,$$ é  $$c$$-incompressível. 

Isto é, a “stream”   $$\,\omega\,$$ é $$K$$-aleatória se e só se

                              $$\exists\,c>0\,\centerdot\; \forall\,n\,\centerdot\; K(\omega(n)) + c  \,\geq\, n$$

Obviamente esta noção transfere para conjuntos e para reais de Lebesgue com a descrição da “stream” $$\,\omega\,$$ como um conjunto $$\,\overline\omega\,$$ ou com um real $$\,\tilde\omega\,$$.

Esta definição e a noção de complexidade relativa a um oráculo permite também relativizar a aleatoriedade. Assim, 


> **Definição**
> $$\,A\,$$ “stream” $$\,\omega\,$$  é  $$K$$-**aleatório relativo** a ****$$\,X\,$$ quando
> 
>                           $$\exists\,c>0\,\centerdot\; \forall\,n\,\centerdot\; K^X(\omega(n)) + c  \,\geq\, n$$
| Informalmente esta definição pode ser interpretada como:<br><br>> mesmo consultando um oráculo $$\,X\,$$ aleatório não é possivel comprimir os prefixos de $$\,\omega\,$$ $$\,$$ |





## Probabilidade e aleatoriedade de Martin-Löf

Uma formalização de aleatoriedade bastante importante é baseado o princípio dos **testes excecionais**; informalmente


> a “stream” $$\,\omega\,$$ é  aleatória, quando não é possível construir um teste computável e excecional (i.e.  a probabilidade de uma “stream” a satisfazer é negligenciável) que $$\,\omega\,$$satisfaça.

Uma **decisão**  é  uma função $$\,\phi\,\colon\, \mathbb{N}\,\to\, \mathbb{N}\,$$  parcialmente computável. Um argumento $$\,x\,$$ onde  $$\,\phi\,$$ esteja definida é um **sucesso** dessa decisão.  

Quando $$\,x\,$$ não é um sucesso de $$\,\phi\,$$ diz-se que é uma **falha** dessa decisão.  

O conjunto de sucessos de $$\,\phi\,$$ (o seu *domínio*) representa-se aqui  por $$\,\phi\!\downarrow\,$$. O conjunto de falhas (i.e.  o complemento $$\mathbb{N}\setminus \phi\!\downarrow\,$$) representa-se por $$\,\phi\!\uparrow\,$$.  

Por definição o domínio de uma função parcialmente computável é sempre computacionalmente enumerável  (ou simplesmente “enumerável”).  Portanto o domínio $$\,\phi\!\downarrow\,$$é sempre enumerável. Quando o seu complemento (o conjunto de falhas)  $$\,\phi\!\uparrow\,$$ também for enumerável,  a decisão  diz-se computável.

| **Nota**<br>Recorde-se que $$\,\phi(x)\!\downarrow\,$$é o predicado que designa *“*$$\phi\,$$ *está definida para o argumento* $$\,x\,$$*”:* isto é*,*  $$x$$ é um sucesso de $$\phi$$.  Daí que $$\,\phi\!\downarrow\,\equiv\,\{x\,|\,\phi(x)\!\downarrow\}\,$$.<br>Igualmente $$\,\phi(x)\!\uparrow\,$$ designa que $$\,\phi\,$$ *não está definida*  para o argumento $$\,x\,$$:  ou seja, $$x$$ é uma falha de $$\phi\,$$. Portanto $$\,\phi\!\uparrow\,\equiv\,\{x\,|\,\phi(x)\!\uparrow\}\,$$. |

Neste curso a noção de **probabilidade** é baseada na contagem do número de sucessos de uma  **decisão .** Formalmente

                                                 $$\mathbb{P}[\phi]\;\equiv\;\sum_{x\in\phi\!\downarrow}\,2^{-|x|}$$

A probabilidade de $$\,\phi\,$$ conta o número de sucessos $$\,x\,$$ e divide-o pelo número total de possíveis argumentos que têm tamanho igual ao de $$x$$ (isto é, $$2^{|x|}$$). Assim cada sucesso contribui com a probabilidade $$\,2^{-|x|}$$.

----------

Uma sequência **uniformemente enumerável** de decisões $$\,\varphi\,\equiv\,\{\varphi_c\}_{c\in\mathbb{N}}\,$$ é definida por uma função $$\,(c,x)\mapsto \varphi_c(x)\,$$, computável no argumento $$\,c\,$$ e parcialmente computável no argumento $$\,x\,$$.

Um **teste de Martin-Löf**  **(**ou **ML-teste**) é uma enumeração uniforme de decisões $$\,\{\varphi_c\}\,$$ tal que, para todo $$c$$, se tem $$\,0\,<\,\mathbb{P}[\varphi_c]\,\leq\,2^{-c}\,$$.

O conjunto $$\,A\,$$ **satisfaz** a decisão $$\,\phi\,$$, e escreve-se $$\,A\mathbin{\colon} \phi\,$$, quando existe um prefixo de $$\,A\,$$que é sucesso em $$\phi\;$$. Isto é

                                $$\,A\mathbin{\colon} \phi\quad\text{sse}\quad \exists\,x\preceq\,A\,\centerdot\,\phi(x)\!\downarrow$$    
                                

O conjunto  $$\,A\,$$ **falha** o   ML-teste $$\,\varphi\equiv\{\varphi_c\}\,$$  quando satisfaz todo o $$\,\varphi_c\,$$. Isto é, quando é válido     $$\,\forall\,c\,\centerdot\, A\mathbin{\colon} \varphi_c$$  ou

O conjunto  $$\,A\,$$ é **ML-aleatório** quando  $$\,A\,$$ não falha qualquer ML-teste.


| **Nota**<br>A aleatoriedade de Martin-Lof descreve a impossibilidade de construir decisões computáveis que isolem um conjunto $$A$$ de outros conjuntos. De facto<br><br>1. Um ML-teste tem duas características : é uma sequência computável, e portanto previsível, e as decisões individuais $$\,\varphi_c\,$$ têm uma probabilidade de ser satisfeitas que, quando $$\,c\,$$cresce,  decresce muito rapidamente para zero.<br>2. Se o conjunto $$\,A\,$$ for previsível (de algum modo) então será possível construir um ML-teste $$\,\varphi\,$$ tal que cada $$\,\varphi_c\,$$ captura um prefixo de $$A$$. Se não existir numa forma de construir um ML-teste que consiga capturar todos os prefixos de $$\,A\,$$ então é porque esses prefixos não são previsíveis: i.e. $$A$$ é aleatório. |

O resultado fundamental da aleatoriede computacional  é o que afirma 

**Teorema** 

> Um conjunto $$\,A\,$$ é ML-aleatório se e só se for  $$K$$-aleatório.

Por isso a $$K$$-aleatoriedade e a ML-aleatoriedade são essencialmente dois pontos de vista para exatamente o mesmo conceito: o de aleatoriedade computacional de conjuntos/”streams”.


----------

Existem ainda outros princípios nos quais é possível basear noções de aleatoriedade; nomeadamente o **princípio da imprevisilidade**; informalmente


> se $$\,\omega\,$$ for aleatória, mesmo que se conheça completamente um prefixo $$\,\omega(n)\,$$, não é possível extrair  dessa informação  qualquer conhecimento  sobre o valor de qualquer dos bits futuros $$\,w_k\,$$, com  $$\,k\geq n\,$$ .


A formalização deste princípio é bastante técnica e não é muito relevante alongar este texto com detalhes. É importante referir, porém, que todos eles conduzem à mesma noção de aleatoriedade. Uma “stream” só é aleatória de acordo com um destes três princípios se e só se também for aleatória de acordo com qualquer um dos restantes princípios.


## Propriedades de conjuntos/streams $$\,K$$-aleatórios.

Os seguintes factos são demonstrados na literatura. Em todos eles $$\,\Omega\,$$ e $$\,\omega\,$$ denotam respetivamente  um conjunto e uma “stream” $$\,K$$-aleatórios arbitrários.

**Facto 1**
$$\,\Omega$$ verifica sempre a lei dos grandes números; isto  é

                    $$\lim_{n\to \infty}\;\#\{k< n\,|\,k\in \Omega\}/n\;=\;1/2$$

**Facto 2**
Seja $$\,f \colon \mathbb{N}\,\to\,\mathbb{N}\,$$  uma função injetiva e computável; então também é $$\,K$$-aleatório o conjunto

                           $$f^{-1}(\Omega)\;\equiv\,\{\,n\,|\,f(n)\in \Omega\,\}$$

**Teorema**
Para todo $$\,r>0\,$$ e para quase todo $$\,n\,$$, uma sub-sequência de $$\,\omega\,$$  só de zeros e iniciada na posição $$\,n\,$$, tem  comprimento limitado a $$$$$$\,K(n)-r$$.
O número de posiçoes $$\,n\,$$ que são exceções a esta regra é finito e decresce quando $$\,r\,$$ cresce.

**Facto 3**
Para toda a constante $$\,c \geq 1\,$$ e para quase todas as “strings” $$\,x\,$$, a posição $$\,n\,$$ em $$\,\omega\,$$ onde se inicia uma subsequência coincidente com $$\,x\,$$verifica

                                                  $$n \,\geq\, c\,2^{|x|/2}$$

As exceções a esta regra são em número finito e decrescem quando $$\,c\,$$ aumenta.




