# Capítulo 4:  Fatorização e Teorema Chinês dos Restos. 

# Problemas Difíceis, Redução e Provas de Segurança.

Na criptografia contemporânea cada técnica criptográfica é apresentada, quase sempre, com uma **prova de segurança.** Tal prova baseia-se  em 


- na existência de um **problema difícil** ; isto é, um problema aritmético que não é resolúvel com com recursos computacionais razoáveis.
- numa transformação de um qualquer ataque na resolução desse problema; isto é, na **redução** de uma solução do problema ao sucesso do ataque.

Qualquer destes pressupostos são essencialmente **crenças** ; é uma crença que existam realmente problemas difíceis tal como é uma crença que a redução desse problema a um ataque assegura a imunidade a esse ataque.

Por isso é importante analisar cada um desses conceitos (problema difícil e redução) e os fundamentos destas crenças.


## Problemas Difíceis e Redução

Problemas difíceis são definidos por linguagens numa classe $$\,A\text{-NP}\,$$ para um determinado oráculo $$A$$. Recorde-se que essa classe se identifica com uma subclasse de $$\,\Sigma_1^A\,$$ , na hierarquia da aritmética, com limites polinomiais no tamanho da prova e no número de consultas a $$A$$.

Explicitamente uma linguagem $$\,\mathcal{L}\,$$ na classe $$\,A\,\text{-NP}\,$$ é determinada por uma decisão computável determinística  $$\,D^A\,$$ de tal forma

                            $$\,x\in \mathcal{L}\quad$$sse $$\quad \exists\,w\,\centerdot\,D^A(x,w)\quad$$tem sucesso 

com a restrição de que $$\,|w| \leq \text{poly}(|x|)\;$$  e o número de consultas ao oráculo é igualmente limitado por $$\,\text{poly}(|x|)$$.

Também relevante a este estudo é a classe $$\,A\,\text{-P}\,$$. Cada linguagem $$\,\mathcal{P}\in A\text{-P}\,$$ é igualmente determinado  por uma decisão determinística $$\,D^A\,$$de tal forma que 

                        $$\,x\in \mathcal{P}\quad$$sse $$\quad D^A(x)\quad$$tem sucesso 

com a restrição de que o número de consultas ao oráculo é limitada por $$\,\text{poly}(|x|)$$.

Como vimos $$\,\text{NP}\,$$e $$\,\text{P}\,$$ designam as situações em que o oráculo é o conjunto vazio $$\,\emptyset\,$$.


> Sejam $$\,\mathcal{L},\mathcal{K}\,$$duas linguagens na classe $$\,\text{NP}\,$$. Diz-se $$\,\mathcal{K}\,$$ é **redutível** a $$\mathcal{L}\,$$ , e escreve-se  $$\,\mathcal{K}\;\leq\; \mathcal{L}\,$$,
> quando $$\,\mathcal{K}\,\in\, \mathcal{L}\!\!-\!\!P$$.
> Isto é, consultando soluções de $$\,\mathcal{L}\,$$um número de vezes polinomial com $$|x|$$ , pode-se decidir se $$\,x\,$$é uma solução de $$\,\mathcal{K}\,$$.
> Quando $$\,\mathcal{K}\,$$e $$\,\mathcal{L}\,$$são mutuamente redutíveis então os problemas dizem-se **equivalentes**.


| A versão noção de redução aqui usada é designada por **redução de Turing**. Na literatura aparecem frequentemente versões mais fracas de redução. Por exemplo a redução $$\,\mathcal{K}\leq_p \mathcal{L}\,$$ocorre quando existe uma função $$\,f\,$$ , computável e  de complexidade polinomial, tal que $$x\in \mathcal{K}\,$$se e só se $$\,f(x)\in \mathcal{L}$$. |

É importante comentar que nem todos os problemas da classe $$\text{NP}\,$$são difíceis. Nomeadamente $$\,\text{NP}$$ contém $$\text{P}$$ e muitos problemas desta classe claramente que não são difíceis.

Por outro lado é natural que existam problemas difíceis em classes de ordem superior da hierarquia da aritmética: classe $$\,\Sigma_o^A\,$$ com $$o > 1$$. Se tais problemas existirem eles não serão aqui estudados: todos os eventuais problemas difíceis referidos neste estudo pertencem a uma das classes $$\,A\!\!-\!\!\text{NP}\,$$para algum oráculo $$A$$.

Por isso é necessário concretizar melhor quais são as sub-classe da classe $$\,A\text{-NP}\,$$ que descrevem os problemas  considerados “difíceis”. Um possível candidato é a classe dos problemas $$\,A\text{-NP-Hard}\,$$  ou $$\,A\text{-NP-Completo}\,$$.


> Um problema $$\mathcal{L}$$ é $$A\text{-NP-Hard}$$  quando todo o problema $$\,\mathcal{K}\,$$ da classe $$\,A\text{-NP}\,$$é redutível a $$\mathcal{L}$$.
> O problema $$\,\mathcal{L}\,$$ é $$\,A\text{-NP-Completo}\,$$ quando é $$\,A\text{-NP-Hard}\,$$ e pertence à classe $$\,A\text{-NP}\,$$.

Como limitamos o nosso estudo a problema $$\,A\text{-NP}\,$$, os dois conceitos são equivalentes.


| **Exemplo: fatorização de inteiros**<br>Este é um dos problemas mais importantes em criptografia. Visto como um problema de decisão,<br><br>> dado $$N$$ decidir se esse inteiro tem um fator num intervalo $$\,I\,$$, com $$I \subseteq (1,N)\,$$<br><br>pode ser descrito por uma linguagem $$\,\mathcal{F}(I)\,$$ , definida por <br><br>                                              $$\mathcal{F}(I) \;\equiv\;\{N \;|\; \exists\,p\in I\,\centerdot\, \text{mdc}(p,N) > 1\} \,$$<br>                                              <br>A análise do algoritmo de Euclides, usado para determinar   $$\text{mdc}(p,N)$$   mostra que o algoritmo termina num número de passos que é linear com o tamanho de $$N$$. Por outro lado, como $$p<N$$ tem-se $$|p|\leq |N|$$. Portanto cada uma das linguagens $$\,\mathcal{F}(I)\,$$ está em $$\text{NP}$$.   <br>Se o problema é $$\,\text{NP-Hard}\,$$ é uma questão que ainda está em aberto. Muito provavelmente não é $$\,\text{NP-Hard}\,$$. No entanto, ainda assim, é considerado difícil pelo menos no modelo de computação clássica. |



## Redução e Imunidade a Ataques

As observações anteriores parecem sugerir que, como primeira caracterização dos problemas difíceis, pode-se considerar os problemas $$\,\text{NP-Hard}\,$$mas que também existem problemas que não são $$\,\text{NP-Hard}\,$$e que, ainda assim, podem-se considerar difíceis.

Considere-se, como referência, o problema da **decisão Diffie-Hellman** num corpo primo $$\,\mathbb{F}_p\,$$.

A linguagem que determina o problema da decisão Diffie-Hellman pode-se definir como

$$\text{DDH}(p)\;\equiv\; \{(a, b,c,d)\in (\mathbb{F}^\ast_p)^4\;|\; \exists\,s < p-1\,|\, c = a^s \;\wedge\; d = b^s\,\}$$

Os elementos $$\,(a, b,c,d)\,$$nesta linguagem (i.e. soluções deste problema) designam-se por **tuplos Diffie-Hellman**. 

É bem sabido que existe um algoritmo de exponenciação eficiente que calcula $$\,a^s\,$$ e $$\,b^s\,$$num número de passos polinomial com $$\,|s|\leq |p| \leq |(a, b, c, d)|\,$$. Portanto o problema está na classe $$\text{NP}\,$$. Se é ou não $$\,\text{NP-Hard}\,$$, tal como o problema da fatorização com que está relacionado, provavelmente a resposta é “não”. No entanto, ainda assim, assume-se que é um problema difícil pelo menos no modelo de computação clássica.

**Uma prova de segurança de um esquema PKE**
Vamos usar $$\,\text{DDH}(p)\,$$ para construir uma prova de segurança  IND-CPA da cifra *El Gamal*.
A prova tem a forma de uma redução em dois passos, no contexto desta cifra, do problema $$\,\text{DDH}(p)$$ ao execução com sucesso de um ataque arbitrário IND-CPA.


1. O primeiro passo da prova é a identificação do problema que um ataque IND-CPA com sucesso resolve; seja $$\,\mathcal{A}\,$$ esse problema.
2. O segundo passo é a construção, no contexto da cifra, de uma redução do problema $$\text{DDH}(p)$$ ao problema  $$\,\mathcal{A}\,$$.


| **El Gamal**<br>Qualquer PKE é determinado por três algoritmos: geração de chaves, cifra e decifra. No contexto de ataques IND-CPA apenas os dois primeiros são relevantes e apenas a chave pública  relevante.<br><br>$$\text{Keys}(p)$$<br><br>    - assume-se que o parâmetro $$p$$ é tal que o grupo $$\,\mathbb{F}_p^\ast\,$$ tem um sub-grupo de ordem prima elevada e que é conhecido um gerador $$g$$ desse sub-grupo<br>    - gera-se $$s\neq 0 < \text{ord}(g)$$ ,  calcula-se  $$\,\beta \gets  g^s\quad$$e revela-se   a chave pública é  $$\,\mathbf{pk} \equiv (g,\beta)$$<br><br>$$\text{Enc}(\mathbf{pk},m)$$<br><br>    - a mensagem $$m$$ é um elemento de $$\mathbb{F}_p^\ast$$ .<br>    - gera-se $$\,\omega\neq 0 < \text{ord}(g)$$ e calcula-se  $$\,\gamma \gets g^\omega\;$$ e $$\,\kappa \gets \beta^\omega\,$$.<br>    - calcula-se o criptograma $$\,\mathbf{c}\gets (\,\gamma\,,\, m\times\kappa\,)\,$$<br><br>Note-se que se verifica $$\,\kappa = \gamma^s\,$$. |

| **Problema** $$\,\mathcal{A}\,$$<br><br>$$\,\mathcal{A}(\mathbf{pk},\mathbf{c},\mathbf{m}_0,\mathbf{m}_1) \;\equiv\; \{b \in\{0,1\}\;|\; \exists \omega\,\centerdot\, \mathbf{c} = \text{Enc}'(\mathbf{pk},\mathbf{m}_b,\omega)\}$$<br><br>em que $$\,\text{}$$$$\,\text{Enc}'$$ é o núcleo determinístico  de  $$\,\text{Enc}$$ ; i.e. é o algoritmo determinístico que verifica<br><br>      $$\text{}$$$$\,\text{Enc}(\mathbf{pk},m)\,\equiv\, \vartheta\,\omega < \text{ord}(g) \,\centerdot\, \text{Enc}'(\mathbf{pk},m,\omega)$$<br>      <br>Neste caso será simplesmente<br><br>$$\,\text{Enc}'(\mathbf{pk},m,\omega) \;\equiv\; \vartheta (g,\beta) \gets \mathbf{pk}\,\centerdot\,(g^\omega,m\times \beta^\omega)$$ |

| **Redução IND-CPA**<br>Recorde-se  que sumariamente o ataque IND-CPA é um protocolo entre um ‘adversário’ e um ‘challenger’ em que:<br><br>    - Um “trusted agent” corre $$\text{Key}(p)$$ e divulgar chave pública  $$\mathbf{pk} \equiv (g,\beta)$$ <br>    - o adversário escolhe $$\,$$duas mensagens $$\mathbf{m}_0,\mathbf{m}_1\in \mathbb{F}_p^\ast$$ , e revela-as<br>    - o ‘challenger’ gera aleatoriamente um bit $$b$$ , calcula $$\,\mathbf{c}\gets \text{Enc}(\mathbf{pk},\mathbf{m}_b)\,$$ e revela-o<br>    - o atacante determina uma solução $$b$$ do problema $$\,\mathcal{A}(\mathbf{pk},\mathbf{c},\mathbf{m}_0,\mathbf{m}_1)\,$$, e com essa solução calcula $$\mathbf{m}_b$$; após o que<br>        - recupera $$\,(\gamma, \mathbf{m}_b\times \gamma^s) \gets \mathbf{c}\,$$  e  $$\,\gamma^s \gets (\mathbf{m}_b\times \gamma^s)\times \mathbf{m}_b^{-1}\,$$<br>        - recupera $$(g, g^s) \gets \mathbf{pk}$$<br>        - constrói um DH tuplo $$(g,\gamma,g^s,\gamma^s)$$ solução de $$\text{DDH}(p)$$ |


Este exemplo ilustra a estratégia mais comum para construir provas de segurança derivadas de problemas difíceis. Esta estratégia, dita de **redução**, tem três passos essenciais:


1. Identificar o problema difícil $$\,\mathcal{L}\,$$relevante à estrutura criptográfica em questão.
2. Identificar o critério de segurança e converte-lo num ataque. No contexto da estrutura criptográfica identificar o problema $$\,\mathcal{A}\,$$ que o ataque resolve.
3. Verificar a redução  $$\,\mathcal{L} \leq \mathcal{A}\,$$

Tomamos como parâmetro de segurança o tamanho $$\,|x|\,$$ da solução de $$\,\mathcal{L}$$ e represente-se esse tamanho por $$\,\lambda\,$$. O grau de confiança que se tem numa prova assim construída depende crucialmente da complexidade computacional da redução; ou seja, do número de vezes que é necessário consultar o oráculo $$\,\mathcal{A}\,$$ para obter $$\,x\in \mathcal{L}$$ . Seja $$\,\text{red}_\mathcal{A}(\lambda)$$ essa complexidade.

Sabemos que $$\,\text{red}(\lambda) \leq \text{poly}(\lambda)\,$$. Porém isso não impede que seja um número muito grande.

Se tal acontecer esta “prova” fornece poucas garantias de confiança uma vez que confirmar a redução é quase tão complicado como resolver o problema difícil inicial.

Para existir confiança na prova a redução tem de ser muito mais eficiente do que resolver o problema difícil. Se tal acontecer a redução diz-se **tight**.

O critério mais usado para classificar uma redução como “tight” é considerar $$\,\text{red}_\mathcal{A}(\lambda)$$ limitado linearmente com  $$\,\lambda\,$$.  Isto depende da técnica criptográfica e do problema difícil. Por vezes só se considera “tight” uma redução onde aa complexidade é limitada linearmente com o número de bits de $$\lambda$$.$$\,$$


# Fatorização, Teorema Chinês dos Restos

[Notebooks aqui](https://www.dropbox.com/sh/j8m0e6ym3uxhk3p/AAAE3IUwUU-zWUYVRB4hdalBa?dl=0)

# Fatorização.

Recorde-se, da sessão anterior,  a noção de PID (*“principal ideal domain”*): um domínio integral (i.e. um anel comutativo onde não existem divisores de zero) onde todo o ideal não nulo é principal. 

Recorde-se que são PID’s  o anel $$\,\mathbb{Z}\,$$ , qualquer corpo $$\,K\,$$ e qualquer anel de polinómios univariáveis $$\,K[w]\,$$ com coeficientes num corpo. Nas aplicações criptográficas, para além do paradigma $$\,\mathbb{Z}\,$$,  são úteis os seguintes PID’s

    - Os racionais $$\,\mathbb{Q}\,$$e os corpos de números $$\,\mathbb{Q}(\beta)\,$$: i.e. os corpos de característica $$0$$.
    - Os corpos de característica prima $$\,\mathbb{F}_q\,$$: sendo $$q=p^d$$ uma potência de um primo. 
    - Os anéis de polinómios univariados sobre corpos finitos, representados como $$\,\mathcal{R}_q \equiv \mathbb{F}_q[w]\,$$


Num   PID  existem as noções, herdadas dos inteiros  $$\,\mathbb{Z}\,$$, derivadas da noção de divisor. Existe a noção de **elemento irredutível** ou **primo,** i.e. ****o ****que não tem qualquer divisor ****para além de ****$$1$$ e do próprio, e de **factorização única por elementos irredutíveis.**


| **Exemplo1**<br>Considere-se o anel $$\,\mathcal{R}_q$$, sendo $$q$$ primo, e  os polinómios<br>                                    $$f_n \equiv w^n - 1\,$$  e $$\;t_n \equiv f_n/(w-1)\,=\,\sum_{j=0}^{n-1}\,w^j$$<br>para algumas combinações típicas dos parâmetros $$\,q\,$$ e $$\,n\,$$. <br><br>Note-se que as raízes de $$\,f_n\,$$são as raízes da unidade de ordem $$\,n\,$$em $$\,\mathbb{F}_q\,$$e por isso $$\,f_n\,$$é sempre divisível pelo monómio $$\,(w-1)\,$$. Pretende-se averiguar se $$\,t_n\,$$é factorizável e, se for, quais são os seus factores.<br><br><br>    - $$n$$ é um primo e $$\,q=2\,$$. <br>        Usando *Sagemath* pode verificar que o polinómio $$\,t_n\,$$ ou é irredutível (ex: $$n=5,11,13,19,29,\cdots$$) ou então factoriza em polinómios irredutíveis com o mesmo tamanho $$d$$.<br>        Por exemplo $$\,t_{127}\,$$factoriza em 18 polinómios irredutíveis de grau 7,  $$\,t_{131}\,$$é irredutível  enquanto que $$\,t_{257}\,$$ factoriza em 16 polinómios irredutíveis de grau 16.<br>    -  $$\,n\,$$é primo e $$\,n < q\,$$. <br>        Esta é uma combinação muito comum em criptoesquemas da família NTRU. <br>        Neste caso existem vários arranjos $$(n,q)$$ com interesse criptográfico que conduzem a polinómios $$\,t_n\,$$irredutíveis. Por exemplo $$\,q=257\,$$ e $$\,n=127,131,\cdots,233,251$$.  Para $$\,q=521\,$$ temos $$\,n=131,\cdots,257,\cdots,509$$. Mesmo quando não é irredutível existem vários valores de $$n$$ onde $$\,t_n\,$$tem factores grandes; por exemplo $$\,t_{503}$$ factoriza em dois factores de grau $$\,251\,$$. |

| **Exemplo2**<br>Outro caso importante para o anel $$\,\mathcal{R}_q$$  ocorre quando<br><br>        -   $$\,q\,$$ é primo  e $$\,n\,$$é uma potência de $$2$$   que divide  $$\,(q-1)/2\,$$ <br>        -   $$\,g_n \equiv (w^n + 1)\,$$<br><br>O anel $$\,\mathcal{R}_q/g_n\mathcal{R}_q$$ aparece frequentemente em criptoesquemas da família RLWE. Os polinómios$$\,g_n$$ são frequentemente usados como módulos porque permitem formas eficientes de aritmética.<br><br>Para esta combinação de parâmetros prova-se que o corpo $$\,\mathbb{F}_q\,$$contém todas as raízes da unidade de ordem $$\,2n\,$$. Como  $$\,(w^{2n}-1) \,\equiv\,(w^n+1)\,(w^n-1)\,$$, metade dessas raízes são raízes  de $$g_n$$. <br>Desta forma $$\,g_n\,$$ factoriza em $$\,n\,$$ monómios $$\,(w-r_i)\,$$ em que todos os $$\,r_i$$ são raízes de ordem $$\,2n\,$$ de $$1$$.<br><br>De facto se tomarmos uma qualquer destas raízes, por exemplo $$r_0$$,  então $$\,s\,$$ todas as outras raízes têm a forma $$\;r_i \equiv r_0\times (r_0)^{2j}\,$$ com $$j=0,\cdots,n-1$$. |



# Máximo Divisor Comum

É bem conhecido o conceito de máximo divisor comum de dois números $$\,a,b\in\mathbb{N}_+$$. Sabemos que existe o **algoritmo de Euclides** que calcula $$\,\text{mdc}(a, b)\,$$em tempo semelhante ao da multiplicação.

 Já nos inteiros $$\,\mathbb{Z}$$, nos corpos $$\,\mathbb{F}_q\,$$e nos anéis de polinómios $$\,\mathbb{R}_q\,$$a noção é mais complexa e, normalmente, não existe um equivalente ao algoritmo de Euclides. A diferença é que o algoritmo de Euclides recorre ao facto de que nos naturais existe uma *ordem bem fundada:* a **ordem $$\,a\prec b\,$$ sse $$a\neq b\,$$ e $$a$$ divide $$b$$ (representado por $$\,a|b\,$$).   O máximo divisor comum  $$\,\text{mdc}(a, b)\,$$ é por isso o  *meet*  $$\,a \land b\,$$ nesta ordem parcial.

![$$\text{mdc}(a, b)$$](https://paper-attachments.dropbox.com/s_93C1592772A6DA8CDE9AC33EC1FC5761FA16C550811B1CE76722294E0A25294B_1585247519662_Documento+do+Scannable+em+26-03-2020+18_28_11.png)


 
É simples alterar o algoritmo de Euclides para lidar com inteiros negativos mas não é simples fazer algo semelhante nos restantes casos. Num corpo, qualquer $$a\neq 0$$ é divisor de qualquer $$b$$; por isso a noção de $$\text{mdc}(a, b)\,$$é trivial: é sempre $$1$$.

Já no anel $$\mathbb{R}_q$$ é simples definir $$\,\text{mdc}(f,g)\,$$de dois polinómios mónicos (i.e. o coeficiente do monómio de maior grau é $$1$$): basta factorizar ambos os polinómios em polinómios irredutíveis mónicos e agregar num só polinómio todos os factores comuns.

Os PID’s onde existe um algoritmo específico, determinístico, para calcular o máximo divisor comum, designa-se por **domínio Euclidiano**. Os inteiros $$\mathbb{Z}$$ e os polinómios $$\mathbb{R}_q$$ são domínios Euclidianos, mas os corpos $$\mathbb{F}_q$$ não são.
 
O resultados fundamental no estudo do máximo divisor comum é a chamada **lema de Bézout,** que se verifica em qualquer PID $$\,\mathcal{R}\,$$e é uma consequência direta de em $$\,\mathcal{R}\,$$todo o ideal ser principal.


> Para todos $$\,a,b\in \mathcal{R}\,$$,  não nulos, existem  únicos $$\;\mu,\lambda\;$$ tais que $$\,\mu \in \langle a \rangle \;,\;\lambda\in \langle b \rangle\,$$ e $$\, \mu +  \lambda = \text{mdc}(a,b)$$. Os valores $$\,\mu,\lambda$$  são determinados com o algoritmo de Euclides.
# Teorema Chinês dos Restos

#crt
O **teorema chinês dos restos**, ou **CRT** (“chinese remainders theorem”), é conhecido desde o século XIII, em versão publicada,  mas existem referências (sem prova) desde o século IV. É um dos resultados mais antigos da Matemática, rivalizando com o próprio algoritmo de Euclides com o qual tem uma ligação estreita.

O CRT é também um dos resultados mais flexíveis da Teoria dos Números com inúmeras aplicações na criptografia “number theoretic”.  Porém, talvez o aspeto mais interessante resulta de ser extensível a qualquer PID, nomeadamente aos anéis $$$$$$\,\mathbb{R}_q\,$$, o que o torna útil mesmo na PQC.

O CRT  num PID $$\,\mathcal{R}\,$$ é definido por um conjunto de **módulos** $$\,\{q_1,q_2,\cdots,q_\kappa\}\,$$ coprimos dois a dois, que geram o módulo $$\,n \equiv q_1\times \cdots\times q_\kappa\,$$.  

Para ilustrar a construção vamos considerar apenas dois módulos coprimos  $$\,p,q\in \mathcal{R}\,$$;  neste exemplo $$\,n = p\times q$$. Por facilidade de notação representamos $$\langle n\rangle\,$$o ideal $$\,n\mathcal{R}\,$$e o mesmo ocorre para $$\,\langle p\rangle\,$$e $$\,\langle q\rangle\,$$.

O CRT estabelece um isomorfismo de anéis   $$\, \mathcal{R}/\langle n\rangle \,\simeq\, {\mathcal{R}/\langle p\rangle}\times {\mathcal{R}/\langle q\rangle}$$ definido pelo par de  isomorfismos 

    - $$\text{Mod}\,\colon\,\mathcal{R}/\langle n\rangle \,\to\, \mathcal{R}/\langle p\rangle \times \mathcal{R}/\langle q\rangle$$   
        é o morfismo que mapeia    $$\, x$$   no par  $$\,(x \bmod p\,,\, x \bmod q)$$
    
    - $$\text{CRT}\,\colon\,\mathcal{R}/\langle p\rangle \times \mathcal{R}/\langle q\rangle\,\to\,\mathcal{R}/\langle n\rangle \,$$
         é o morfismo que mapeia  o par $$\,(x_p \,,\, x_q)\,$$ no elemento  $$\,x \equiv (\mu\,x_p + \lambda\, x_q) \bmod n\,$$ 
         em que $$\,\mu,\lambda \in \mathcal{R}\,$$  são únicamente definidos pelas relações
                  $$\,\mu \in \langle q\rangle \quad,\quad \lambda \in \langle p \rangle \quad,\quad \mu + \lambda = 1$$
         A razão porque este par $$(\mu,\lambda)$$ existe e é bem determinado deriva do lema de Bézout e da             hipótese  $$\,\text{mdc}(p,q) = 1$$.

É fácil  verificar que ambas as aplicações mapeiam somas em somas e multiplicações em multiplicações e, como são inversa uma da outra, são isomorfismos.

Também é fácil generalizar esta construção de 2 módulos $$p,q$$ para $$\kappa$$ módulos $$\,q_1,\cdots,q_\kappa$$.  Num algoritmo iterativo, basta fazer  $$\,p \gets q_1\,$$ e $$\,q \gets  q_2\times\cdots\,q_\kappa$$ e proceder como no caso de 2 módulos. No passo seguinte, se $$\,\kappa \geq 2\,$$, decompõe-se $$\,q\,$$ em dois módulos ($$p\gets q_2\,,\,q \gets q/q_2)\,$$, decrementa-se $$\kappa$$ e  procede-se do mesmo modo. Termina quando $$\,\kappa = 1$$.

Para $$\kappa \geq 2\,$$ módulos e sendo $$$$ $$\,n\equiv q_1\times \cdots \times q_\kappa\,$$ $$\, \,$$, define-se $$\,p_i \equiv n/q_i\,$$; o algoritmo de Euclides permite calcular um único vetor  $$\,\mu  \equiv (\mu_1,\cdots,\mu_\kappa)\,$$ tal que $$\,\mu_i\in \langle p_i\rangle\,$$, para  todo $$i$$,  e $$\,\mu_1 + \mu_2 + \cdots + \mu_\kappa \,=\, 1$$. O vetor $$\,\mu\,$$ chama-se a **base CRT** para os módulos $$\,q_1,\cdots,q_\kappa$$.

A base $$\mu$$ determina completamente a função $$\,\text{CRT}_\mu\,$$; dado um vetor de resíduos $$\, (x_1,\cdots,x_\kappa)\,$$, o valor de  $$\,\text{CRT}_\mu(x_1,\cdots,x_\kappa)$$ é construído como $$\,(\sum_i\,x_i\times \mu_i) \bmod n\,$$.

| **Exemplo:** Um general chinês tinha dificuldades em calcular o número de soldados que tinha em parada.  <br><br>Estimou que não seriam mais do que 2500 e, por isso escolhe os números $$\,5,7,8,9\,$$ que multiplicados produzem $$\,2520$$; um valor superior ao estimado. Em seguida manda alinhar os soldados, sucessivamente, em filas de $$\,5,7,8\,$$e $$9$$ elementos tomando nota, em cada caso,  de quantos ocupam a última fila.<br><br>Sendo $$\,x < 2520\,$$o número  de soldados, então os que ocupam a última fila são sucessivamente $$\,x\bmod 5\,$$, $$\,x\bmod 7\,$$, $$\,x\bmod 8\,$$e $$\,x \bmod 9$$. O general executa o algoritmo CRT acima esboçado e determina $$\,x\,$$.<br><br> Em alternativa pode esperar até ao século XX e invocar  a função `crt` do Sagemath. |


Outros exemplos de aplicações do CRT são analisadas nas duas seções seguintes.


# Aplicações do CRT

Técnicas como “Residue Number Systems” e “Number Theoretic Transforms” têm vindo a adquirir um papel fundamental na criptografia contemporânea. Ambas as técnicas são aplicações do CRT para melhorar a eficiência de operações básicas em anéis: somas, multiplicações, exponenciações, cálculo de resíduos e, eventualmente, divisões.

## RNS (“Residue Number Systems”)

#rns
A multiplicação e a exponenciação de inteiros são as operações mais frequentes na criptografia NT: os esquemas RSA, DSA e outros da mesma família usam constantemente estas operações.

Tomando a multiplicação como referência, e tendo em atenção que ela é executada sobre inteiros representados por strings com alguns milhares de bits, a procura de algoritmos de multiplicação eficientes foi sempre um requisito essencial das aplicações criptográficas.

Ultimamente tem existido uma atenção especial por técnicas derivadas do CRT que definem o que é designado por “Residue Number Systems” (ou RNS’s). Para detalhes e  uma análise mais detalhada consultar o artigo [*Pratical Evaluation of Protected Residue Number  System Scalar Multiplication*](https://www.dropbox.com/s/iub3wh752zqsk09/7341-Article%20Text-2469-1-10-20181109.pdf?dl=0).

Os RNS’s são usados em criptografia com dois tipos de objetivos:

1. Melhorar a eficiência da multiplicação executando concorrentemente as operações elementares que contribuem para o resultado.
    Para isso os RNS’s decompõe um inteiro  grande em inteiros mais pequenos que podem ser  operados em paralelo.
2. Melhorar a imunidade em relação a “*side channel attacks*" (SCA’s).
    Os SCA’s exploram fugas de informação, do dispositivo que executa as operações, sobre os argumentos dessas operações. Essas fugas podem vir do tempo de execução das operações, do consumo de energia, radiação eletromagnética e de outras formas de interação do dispositivo com o seu meio ambiente.
    A representação binária dos inteiros é muito vulnerável a fugas e por isso são necessárias medidas para que o dispositivo mostre ao meio ambiente sempre o mesmo perfil (de tempo, consumo, radiação, etc.) quaisquer que sejam os argumentos das operações. Todas essas medidas implicam perdas de eficiência e os RNS´s permitem minimizar essas perdas.

O RNS mais óbvio usa diretamente o CRT.

    - Escolhe-se uma **base de módulos primos**  $$\,\mathcal{Q}\equiv \{q_1,\cdots,q_\kappa\}\,$$,  e define-se $$\,n \equiv q_1\times\cdots\times q_\kappa\,$$.  
    - Um tal sistema permite representar inteiros positivos $$\,x < n$$ através do seu vetor de resíduos: $$\,\bar{x}\equiv (\bar{x}_1,\cdots,\bar{x}_\kappa)\,$$ com $$\,\bar{x}_i < q_i\,$$ e $$\,\bar{x}_i \equiv x \bmod q_i$$.
    - A multiplicação $$\,x\times y\,$$ é efetuada
        -  calculando o vetor de resíduos $$\,\overline{x\times y}$$ é determinado pelas suas componentes $$\,(\overline{x\times y})_i < q_i$$ tais que  $$\,(\overline{x\times y})_i \equiv  \bar{x}_i\times \bar{y}_i \bmod q_i$$
        - calculando a base CRT $$\,\mu\,$$ definida pelos $$\,q_i$$’s e recuperando $$\,(x\times y) \gets \text{CRT}_\mu(\overline{x\times y})$$.

Note-se que:

    - Todas as operações neste algoritmo são executadas nos inteiros positivos.
    - As componentes $$\,(\overline{x\times y})_i\,$$podem ser calculadas em paralelo desde que existam recursos computacionais que suportem paralelismo. Adicionalmente envolvem argumentos muito mais pequenos que os originais $$\,x,y$$. Como a complexidade temporal da multiplicação ordinária de inteiros é quadrática com o número de bits, esta decomposição (mesmo sem paralelismo) tem ganhos de eficiência significativos.
    - Se a multiplicação $$\,x\times y\,$$ fizer parte de um processo mais complexo envolvendo várias somas e multiplicações, então toda esta representação é optimizada  através de:
        - a base $$\mu$$ só é calculada uma vez e serve para todas as operações
        - as somas e multiplicações intermédias podem ser todas executadas ao nível dos vetores de resíduos com os ganhos de eficiência referidos antes.
        - o cálculo inicial dos resíduos só se efectua nos *inputs* do processo e o cálculo do $$\text{CRT}_\mu$$ só se efectua no *output* do processo.
    - Padrões na representação binária dos inteiros (e.g. muitos ou poucos bits $$1$$’s) são diluídos  com a representação em resíduos; basta o cálculo dos resíduos para distribuir os bits de forma mais uniforme; isto torna as fugas de informação mais fáceis de controlar.

Este sistema de representação está longe de ser o melhor RNS´s mas serve de base a melhores sistemas que usam várias bases de primos $$\,\mathcal{Q}\equiv\{q_i\}\,$$ para poderem ser usados não só nas operações básicas (somas e multiplicações) mas  também em operações mais complexas (i.e. divisões). Para detalhes ver o artigo atrás referido.

## NTT-CRT

#ntt #crt
Um segundo exemplo ocorre no anel de polinómios $$\,\mathcal{R}_q\equiv \mathbb{F}_q[w]\,$$. Aqui a operação mais complexa é a multiplicação de polinómios   $$\,f \ast g\,$$ que está na base de muitas técnicas criptográficas. 

Esta multiplicação, representa polinómios pela sequência dos seus coeficientes; isto é, tem-se $$\,f\equiv f_0 + f_1\,w + \cdots + f_i\,w^{i-1} + \cdots$$ e análogamente para $$g$$.  A multiplicação, com esta representação, designa-se por **convulsão** e ****verifica

                                    $$(f\ast g)_k \,=\, \sum_i\,\sum_{j\leq k}\,f_i\,g_{k-j}$$

A execução direta desta definição implica que a convulsão de dois polinómios com $$\,\ell\,$$ coeficientes envolve executar $$\,O(\ell^3)\,$$ operações básicas de $$\,\mathbb{F}_q$$ (somas e multiplicações).


A  interpretação mais genérica de NTT é equivalente à transformada discreta de Fourier sobre um qualquer corpo finito $$\,\mathbb{F}_q\,$$. 

Aqui vamos antes apresentar uma versão particular de NTT que deriva das propriedades do CRT e só se aplica a corpos primos em que o primo $$q$$ tem uma forma particular. 
Também não se aplica a qualquer elemento de $$\,\mathcal{R}_q$$ mas apenas aos conjunto de polinómios de graus inferior a um certo limite $$\,N\,$$ da forma de uma potência de $$2$$. Genericamente vamos representar por $$\,\mathcal{R}_{q,N}\,$$ o subconjunto de $$\,\mathcal{R}_{q}\,$$ formado pelos polinómios que podem ser descritos por um vetor de $$N$$ coeficientes.

O primeiro passo é a escolha de um $$N$$ da forma $$2^d$$  e um primo $$\,q\,$$ que  verifique $$\,q \equiv 1 \bmod 2N\,$$.

| É óbvio que a multiplicação de dois elementos de $$\,\mathcal{R}_{q,N}\,$$ produz um resultado que  pode não pertencer a este domínio.  Por isso $$N$$ tem de ser escolhido sufientemente grande para que $$\,\mathcal{R}_{q,N}\,$$ contenha  todos os polinómios que, previsivelmente, são relevantes à aplicação desta tecnica. |

Vimos anteriormente que, nestas circunstâncias, 


- o corpo $$\,\mathbb{F}_q\,$$ contém todas as raízes do polinómio $$\,\phi \equiv w^N + 1$$.  Seja $$\xi$$ uma qualquer destas raízes; então todas as raízes têm a forma $$\,\xi^{2\,i+1}$$ , com $$\;i=0,\cdots,N-1$$.


- definindo $$\,\omega \equiv  \xi^2\,$$, pode-se escrever o conjunto de raízes como  $$\,\mathcal{S}\,\equiv\,\{\sqrt{\omega}\times \omega^{i}\,|\, i \in \mathbb{Z}_N\}\,$$. Com estas raízes, o polinómio $$\,\phi(w)\,$$ factoriza nos monómios  por elas definidos
                                $$\phi(w)\;=\; \prod_{s\in \mathcal{S}}\,(w-s)$$
                                
- para  qualquer   $$\,f \in \mathbb{R}_q\,$$  e todo o monómio  $$\,(w-s)\,$$, tem-se $$\,f(s) \equiv f(w) \bmod (w-s)\,$$.

Estas observações sugerem a seguinte estratégia


1. Define-se como módulos CRT os monómios $$\,q_i \equiv w- s_i\,$$ em que $$s_i \equiv  \sqrt{\omega}\times \omega^i\,$$ é a raíz  de ordem $$\,i\,$$ de $$\phi$$. Note-se que $$\,-s_i\,$$é também raíz e coincide com $$\,s_{(i + N/2)\bmod N}$$.
2. Para cada $$\,f\in\mathcal{R}_{q,N}\,$$ o resíduo $$\,\bar{f}_i \equiv f \bmod q_i\,$$ calcula-se como $$\,f(s_i)\,$$. O  vetor $$\,\bar{f}\,$$ de componentes $$\,\bar{f}_i = f(s_i)$$ é designado por **transformada NT** de $$f$$.
3. As operações básicas (soma e multiplicação) do anel $$\mathcal{R}_q\,$$podem agora ser executadas ao nível das componentes. 
                                $$(\overline{f + h})_i \,=\, \bar{f}_i + \bar{h}_i\quad$$e $$\quad (\overline{f \times h})_i \,=\, \bar{f}_i \times \bar{h}_i$$
    portanto com complexidade $$\,O(N)\,$$.
4. Para reconstruir $$f$$ a partir da sua transformada $$\bar{f}$$ usa-se o algoritmo CRT. Essencialmente isto passa pelo cálculo da base  $$\,\mu\,$$ em que todos os $$\,\mu_i\,$$ têm grau inferior a $$N$$; como a base depende apenas dos parâmetros $$N$$ e $$q$$, só necessita de ser calculada uma vez. A reconstrução tem a forma  $$\,f \,=\, \sum_i\,\bar{f}_i\times \mu_i\,$$. 


| No ponto 4.   o CRT impõe  realmente $$\,f \,=\, (\sum_{i<N}\,\bar{f}_i\times \mu_i) \bmod \phi\;$$$$\,$$; o  somatório realiza-se em tempo $$\,O(N)\,$$mas o  cálculo do módulo final $$\,{}\bmod \phi\,$$é uma operação mais complicada: no caso geral, tem uma complexidade próxima da multiplicação. Se realmente fosse efectuada eliminaria em grande medida os ganhos em eficiência de todo este processo.<br>A solução passa por garantir que todos os $$\,\mu_i\,$$têm grau inferior a $$N$$ e, dado que os $$\,\bar{f}_i\,$$ são constantes, o somatório tem grau inferior a $$N$$.<br>Evidentemente que a dificuldade está em assegurar $$\,\text{deg}(\mu_i)<N\,$$ para todo $$i< N\,$$. Mas isso é feito na construção da base e portanto só é feito uma vez. |

| **Transformada NT** <br>Existe uma forma de calcular o vetor $$\,\bar{f}\,$$ , de componentes $$\,\bar{f}_i\equiv f(s_i)$$, em tempo  $$O(N\log(N))\,$$.<br><br>O algoritmo baseia-se na decomposição de um polinómio $$\,f\,$$ com $$N$$ coeficientes em dois polinómios $$\,f^+,f^-$$ com $$N/2$$ coeficientes cada de tal forma que $$\,f(w) = f^+(w^2) + w\,f^-(w^2)\,$$. Para isso basta  agrupar em $$f^+$$ os coeficientes de $$\,f\,$$ de índice par e em $$\,f^-\,$$ os coeficientes de índice ímpar.<br><br>Por exemplo: seja $$\,f(w) = 1 + w -2w^2 - w^3\,$$.  Então  $$\,f(w) \, = \, (1-2w^2)+ w\,(1-w^2)$$  o que significa que $$\,f^+(w) =1 -2\,w\,$$ e  $$\,f^-(w) = 1 - w\,$$.<br><br>Da relação $$\,s_i = -s_{j}\,$$ , com $$\,j \equiv (i+N/2)\bmod N\,$$, vemos que o par $$\,(\bar{f}_i,\bar{f}_j)$$ pode ser calculado com apenas uma invocação de $$\,f^+\,$$e de $$f^-$$; tem-se $$\bar{f}_i = f^+(s_i^2) + s_i\,f^-(s_i^2)\,$$ e $$\bar{f}_j = f^+(s_i^2) - s_i\,f^-(s_i^2)$$. Neste nível é preciso calcular $$N/2$$ valores de $$f^+(s_i^2) , f^-(s_i^2)$$ e fazer, para cada par, uma multiplicação, uma soma e uma subtração. Recursivamente aplica-se a mesma transformação às funções $$\,f^+\,$$ e $$\,f^-\,$$; para cada uma existem $$N/2$$ pontos mas só preciso calcular metade: i.e. $$N/4$$. <br>É simples verificar que o número total multiplicações é  $$\,$$da ordem  $$O(N\,\log(N))\,$$.<br><br>O algoritmo recursivo para calcular  o vetor $$\bar{f}$$ pode ser escrito como<br><br>$$\text{NTT}(\xi,N,f)$$<br>         $$\mathbf{if}\;\;N=1\;\;\mathbf{then}$$<br>                   $$\mathbf{return}\;\;(f_0)$$<br>         $$f^+,f^- \gets \text{split}(f)$$<br>         $$\bar{f}^+ \gets \text{NTT}(\xi^2,N/2,f^+) \;;\; \bar{f}^- \gets \text{NTT}(\xi^2,N/2,f^-)$$<br>         $$s \gets \xi$$<br>         $$\mathbf{for}\;\; i\in \{0,\cdots,N/2-1\} \;\; \mathbf{do}$$<br>                  $$\bar{f}_i \,\gets\, \bar{f}^+_i + s \times \bar{f}^-_i\;\;;\;\; \bar{f}_{i+N/2}\,\gets\, \bar{f}^+_i - s\times \bar{f}^-_i$$<br>                  $$s \,\gets\, s\times \xi^2$$<br>         $$\mathbf{return} \;\; (\bar{f}_0,\bar{f}_1,\cdots,\bar{f}_{N-1})$$ |

##  Equivalência de Problemas Difíceis via CRT

Outro tipo de aplicações do CRT são a prova  de equivalência entre alguns “problemas difíceis”; por exemplo o problema da factorização de inteiros e o problema da raíz quadrada modular ou ainda os problemas do grupos cíclicos que iremos ver na próxima secção.

Apenas como ilustração vamos comparar, de forma informal, o problema da factorização de um inteiro composto  $$\,N\,$$  com o problema do cálculo da raíz quadrada em $$\,\mathbb{Z}_N$$.

De uma forma geral, o **problema da raíz quadrada** módulo um inteiro $$\,N\,$$, na forma decisional,  consiste em saber, dado um qualquer $$\,x < N\,$$não nulo, se  $$\,\exists y< N\,\centerdot\, y^2\equiv x \bmod N\,$$.

| **redução da raíz quadrada à factorização**<br><br>Quando $$\,N\,$$ é primo, metade dos elementos de $$\,\mathbb{Z}^\ast_N\,$$tem  duas raízes quadradas e a outra metade não tem nenhuma. Os $$x$$’s que têm raiz quadrada são os que verificam $$\,x^{(N-1)/2}\equiv 1 \bmod N\,$$enquanto que  os restantes verificam $$\,x^{(N-1)/2}\equiv -1 \bmod N$$. Adicionalmente, quando existe raíz quadrada, existe um algoritmo eficiente para a calcular; por exemplo, se $$\,N \equiv 3\bmod 4$$ e $$x\,$$tem raízes quadradas, então uma das raízes quadradas é $$\,x^{(N+1)/4} \bmod N$$.<br><br>Se $$\,N\,$$ é o produto de dois primos e se for conhecida uma factorização $$\,N = p\times q\,$$ então, para qualquer $$\,x\in \mathbb{Z}^\ast\,$$ pode-se tentar resolver os problemas $$\,\exists u< p \centerdot \, u^2 \equiv x \bmod p\,$$ e  $$\,\exists v < q \centerdot \, v^2 \equiv x \bmod q\,$$. Isto é tentamos extrair a raíz quadrada de $$x$$ módulo $$p$$ e módulo $$q$$. <br><br>Como $$p$$ e $$q$$ são primos é simples verificar se existem essas raízes quadradas: basta verificar $$\,x^{(p-1)/2}\equiv 1 \bmod p\,$$ e $$\,x^{(q-1)/2}\equiv 1\bmod q\,$$. Se ambas as condições se verificarem existe 4 pares $$\,(u,v)\,$$ formados por uma raíz  $$u$$ múdulo $$p$$ e uma raíz $$v\,$$módulo $$q$$ já que existem 2 valores possíveis de $$u$$ e dois valores possíveis de $$v$$,<br><br>Usando o CRT determina-se $$y< N$$ que verifica $$\,y\equiv u \bmod p\,$$e $$\,y \equiv v \bmod q\,$$.  Como $$y^2 \equiv u^2 \equiv x \bmod q\,$$e $$\,y^2 \equiv v^2\equiv x \bmod q$$, também se tem $$\,y^2 \equiv x \bmod p\times q\,$$e por isso $$y\,$$ é raíz quadrada módulo $$N$$ de $$x$$. Como existem quatro pares $$(u,v)$$ existe também quatro raízes quadradas de $$x$$ módulo $$N$$. |

| **redução da factorização à raíz quadrada**<br><br>A factorização da raíz quadrada à factorização é conhecida por  **factorização de Fermat.** É dado um $$N>0$$ que é produto de dois primos desconhecidos e pretende-se determinar um fator de $$N$$. O problema é determinar se é válido<br>                                                 $$\,\exists\,p< N \,\centerdot\,\text{mdc}(p,N) \neq 1\,$$<br>usando um oráculo que resolve o problema da raíz quadrada módulo $$N$$.<br><br>Gera-se inteiros $$\,x < N\,$$ tais que $$\,x^2\,$$ tenha uma raíz quadrada $$\,y\,$$ distinta de $$\,$$$$\,x\,$$ e $$\,-x$$. Para isso usa-se o oráculo atrás referido.  Portanto $$\,x^2 \equiv y^2 \bmod N\,$$, o que implica $$(x-y)\times (x+y) \equiv 0 \bmod N\,$$; uma vez que, por construção, se verifica $$\,(x - y)\neq 0\,$$ e $$(x+y)\neq 0\,$$, então um dos valores  $$\,p \equiv \text{mdc}(x-y,N)\,$$ou $$\,p' \equiv \text{mdc}(x+y,N)\,$$ é diferente de $$1$$; esse  valor um dos fatores primos de $$N$$. |



