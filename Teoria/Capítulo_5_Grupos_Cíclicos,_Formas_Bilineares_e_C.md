# Capítulo 5: Grupos Cíclicos, Formas Bilineares e Curvas Elípticas.

# Grupos Cíclicos

Vimos  na aula anterior que um grupo abeliano $$\,\mathcal{G}\equiv (G,\square,e)$$ define sempre uma **multiplicação escalar,**
                                                           ****$$\,\mathbb{Z}\times G \,\to\, G\,$$
tal que, para qualquer inteiro $$\,\ell\,$$ e qualquer $$\,a\in G\,$$, se tem
              $$\,\ell\,a \,=\,\left\{\begin{array}{lcr} e &\;\text{se}\;& \ell=0 \\ a \mathbin{\square} \cdots \mathbin{\square} a\quad (\ell\,\text{vezes}) &\;\text{se}\;& \ell > 0 \\ ((-\ell)\,a)' &\;\text{se}\;& \ell < 0  \end{array}\right.$$              

| Quando o grupo é multiplicativo a multiplicação escalar representa-se como uma exponenciação $$\,a^\ell$$. |

Definimos **grupo de torção** como um grupo onde cada elemento tem uma **ordem** finita, e definimos **grupo cíclico** como um  grupo de torção gerado por um único elemento $$g$$; isto é, todo $$\,a\in  G\,$$ pode ser escrito como $$\,a = \ell\,g\,$$ para algum inteiro $$\ell$$.

Inversamente, qualquer $$\,a\in G\,$$de ordem $$\,\kappa\,$$determina um grupo cíclico $$\,\lbrack a \rbrack\,$$, designado como **órbita** de $$\,a\,$$ , tal que  $$\,\lbrack a \rbrack \;\equiv\; \{\ell\,a \,|\,0 \leq \ell < \kappa\}$$.

O **teorema fundamental dos grupos abelianos** diz-nos que qualquer grupo abeliano finito é expresso como uma soma direta de grupos cíclicos; isto é, existem geradores $$g_1,g_2,\cdots, g_m\,$$linearmente independentes  tais que

                                $$\mathcal{G}\;\simeq\; [g_1]\oplus [g_2]\oplus \cdots \oplus [g_m]\,$$


## Problemas Standard: Exponenciação e Logaritmo Discreto

Seja  $$\,\mathcal{G}\equiv (G,\square,e)\,$$ um qualquer grupo cíclico de ordem $$\,n \equiv \#G\,$$ e seja $$\,g\,$$ um seu gerador .

 Em  $$\,\mathcal{G}\,\simeq\, [g]\,$$ são definidos problemas que são recorrentes nas aplicações criptográficas deste tipo de estruturas; nomeadamente


1. O problema da **exponenciação** pode ser definido, na forma decisional, pela  $$\mathsf{P}$$-linguagem
                 $$\,\text{Exp}\;\equiv\; \{ (\ell,a, b) \,|\, b = \ell\,a \}\,$$         com $$\ell\in \mathbb{Z}_n\,$$ e  $$\,a, b \in G$$
    A linguagem está na classe $$\,\mathsf{P}\,$$ por existe um algoritmo eficiente de calcular a multiplicação escalar sem ter de executar a operação de grupo $$\ell$$ vezes  mas apenas $$\,|\ell|\,$$ vezes.


| **Exponenciação rápida**<br><br><br>1. Seja $$\,\kappa \equiv | n |\,$$ o tamanho, em bits, da ordem do grupo. Constrói-se um dicionário $$\,i \mapsto d_i \,$$ com $$\,d_i\equiv 2^ia\,$$ para $$i\in \mathbb{Z}_\kappa\,$$. Como $$\,d_0=a\,$$, $$\,d_{i+1} = d_i\mathbin{\square} d_i\,$$  , a construção do dicionário requer  $$\kappa-1$$ duplicações.<br>2. Calcula-se a representação binária de $$\ell$$ ; isto é $$\,\ell = \ell_0 + 2\ell_1 + \cdots\,2^{\kappa-1}\ell_{\kappa-1}\,$$.<br>3. Então $$\;\ell\,a \,=\, \square_{\ell_i\neq 0}\,d_i\,$$ . No pior caso são necessárias $$\kappa$$ execuções da operação de grupo. |



2. O problemas do logaritmo discreto (DLP) é definido pela linguagem
                    $$\text{DLP}\;\equiv\; \{ (a, b) \,|\, \exists\,\ell < n\,\centerdot\, b = \ell\,a \}$$       com   $$\,a, b \in G$$
    Este é um problema $$\mathsf{NP}$$ que provávelmente não é $$\,\mathsf{NP}$$-completo mas, ainda assim e 
    em muitos grupos cíclicos, é considerado difícil .

Em relação ao problema $$\,\text{DLP}\,$$ é relevante falar de mais uma aplicação do CRT designada por  **factorização de Pohlig-Hellman** que ilustra casos em que o problema pode deixar  de ser difícil.


| **Pohlig-Hellman**<br><br>Seja $$\,q\,$$ o maior fator primo de $$\,n = \#G\,$$ e seja $$\,m\equiv n/q\,$$ o seu co-fator. Vamos considerar o caso em que $$\,$$$$\,q\,$$ tem multiplicidade $$1$$ e, por isso,  $$\,\text{mdc}(q,m) = 1\,$$.  Não é difícil generalizar para o caso em que a multiplicidade de $$\,q\,$$ é maior do que 1; aqui porém vamos limitar-nos ao caso mais simples de $$\,q\,$$ primo.<br><br>Usando o CRT é possivel determinar $$\,\mu \in \langle m \rangle\,$$ e $$\,\lambda \in \langle q \rangle\,$$ tais que $$\,\mu + \lambda = 1\,$$, a base determinada pelos módulos $$\,q\,\text{e}\,m\,$$, de tal modo  que qualquer índice se pode escrever $$\,\ell = \ell_q\,\mu + \ell_m\,\lambda\,$$ . <br><br>Então  $$\,b = \ell\,a \,=\, \ell_q\,(\mu\,a) \mathbin{\square} \ell_m\,(\lambda\,a)\,$$ e  portanto  $$\, m\,b \,=\,\ell_q\,(m\,\mu\,a) \mathbin{\square} \ell_m\,(m\lambda\,a)\,$$. Como $$\,\lambda\,$$é múltiplo de $$\,q\,$$, então $$\,m\lambda\;$$ é múltiplo da orden $$\,n\,$$do grupo e consequentemente $$\,(m\,\lambda)\,a = e$$.  <br><br>Somos conduzidos à relação  $$\,b' \,=\, \ell_q\,a'\,$$ em que   $$\,b'\equiv m\,b\,$$ e $$\,a' \equiv m\mu\,a\,$$. Determinar $$\,\ell_q\,$$a partir desta relação é novamente um problema DLP mas agora num grupo de ordem $$\,q\,$$. Procedendo da mesma forma para $$\,\ell_m\,$$ constrói-se um outro problema DLP  $$\,b'' = \ell_m\,a''$$  em que $$\,b'' \equiv q\,b\,$$ e $$\,a''\equiv q\lambda\,a\,$$.<br><br>Se $$q$$ for sufientemente pequeno pode-se pensar em determinar $$\ell_q$$ por algum método trivial. <br><br>Para determinar $$\,\ell_m\,$$ aplica-se esta mesma factorização PH mas agora à ordem $$m$$; se o primeiro problema for simples de resolver , o segundo também o será porque os fatores de $$\,m\,$$ são menores do que  $$q$$.<br><br>Esta fatorização é por isso a base do **algoritmo Pohlig-Hellman** para resolver o DLP. O algoritmo só é viável se o primo $$q$$ é suficiente pequeno que o DLP num subgrupo com esta ordem tenha solução trivial. |

Como consequência do algoritmo de Pohlig-Hellman pode-se afirmar que o problema DLP no grupo $$\,\mathcal{G}\,$$ só é seguro quando existe um subgrupo $$\,\mathcal{G}'\subseteq \mathcal{G}\,$$ de ordem prima $$\,q\,$$ onde a resolução do DLP é difícil.

# Hidden Number Problem (HNP)

 O HNP foi introduzido como uma forma relaxada para os principais problemas em grupos cíclicos; nomeadamente o DDH e o DLP.
 
 O interesse do HNP deriva do fato de relacionar um problema supostamente difícil  em grupos cíclicos, na versão relaxada, com um problema que eventualmente pode ser resolvido usando reticulados.
 
 Vamos considerar o problema definido num grupo multiplicativo cíclico $$\,\mathbb{F}_q^\ast\,$$ com $$q$$ primo.
 O problema, na sua versão computacional, pode-se definir informalmente da seguinte forma:

    - Existe um *segredo*  $$\,s\in \mathbb{F}_q^\ast\,$$
    - Existe uma função $$\,\text{msb}_k\,\colon\, \mathbb{F}_q \,\to\, \mathbb{N}\;$$ que extrai, sob a forma de um inteiro positivo,  os $$\,k\,$$ bits mais significativos do argumento. Se $$x\in \mathbb{F}_q\,$$  for representado por um inteiro positivo $$< q\,$$, então $$\,\text{msb}_k(x)\,$$ é o maior $$\,u\,$$que verifica. $$\, x\geq u\times 2^k\,$$.
    -  São conhecidos $$N$$ pares $$\,(x_i,u_i)\,$$  em que os $$\,x_i\in\mathbb{F}_q\,$$  são aleatoriamente gerados e os $$u_i\in \mathbb{N}\;$$ verificam
                                $$\,u_i\;=\; \text{msb}_k(s\times x_i)\,$$
    - Pretende-se construir um algoritmo que, com  acesso ao oráculo
                                $$\mathcal{H}\;\equiv\;\{(x_i,u_i)\}_{i<N}$$
        seja capaz de calcular  o segredo $$\,s\,$$.

 
 Para determinados valores dos parâmetros $$\,(N,q,k)\,$$ o problema tem solução. Trivialmente, se $$k> |q|\,$$ e  tanto $$x\,$$  como $$\,u\,=\, \text{msb}_k(s\times x)\,$$ forem conhecidos, então $$\,u = s\times x\,$$ e  $$s=u\times x^{-1}$$
 
 Por  isso o problema só tem interesse  quando $$\,k/|q| < \beta\,$$, para  algum $$\,\beta < 1\,$$ e $$\,N\,$$ não é excessivamente grande. Veremos no próximo capítulo que, mesmo nestas circunstâncias, existe uma solução eficiente do problema para valores de $$\beta$$ relativamente baixos.
 
 Vamos usar a solução do HNP como “trapdoor” para atacar o DDH na sua versão computacional.
 
 Problema difícil DDH define-se pela linguagem 

>  $$\text{DDH}(q)\,\equiv\;\{(a,b,c,d)\in\mathbb{F}_q^\ast \;|\; \exists \,s < n\, \centerdot \, c = a^s \,\land\, d = b^s\}$$

 
 O problema  $$\,\text{CDH}(q)\,$$ é a versão computacional do $$\text{DDH}(q)\,$$ e define-se como

> Dados  $$\,a,b,c \in \mathbb{F}_q^\ast\,$$ calcular, se existir,  $$\,d\in \mathbb{F}_q^\ast$$  t  al que $$\,(a, b, c, d)\in \text{DDH}(q)$$

O problema decisional $$\,\text{DDH}(q)\,$$ tem uma versão relaxada,  $$\,\text{xDDH}(q,k)$$ , definido pela linguagem 

                            $$\mathcal{L}\;\equiv\; \{(a,b,c,u)\,|\,\exists\,s\,\centerdot\, c = a^s \,\land\, u = \text{msb}_k(b^s)\}$$
                            

Por seu lado este problema tem uma versão computacional   $$\,\text{xCDH}(q,k)\,$$ definido como

> Dados $$\,a, b,c\in \mathbb{F}_q^\ast\,$$ determinar, se existir,  $$u$$ tal que $$(a,b,c,u) \in \text{xDDH}(q,k)$$.

e que funciona como versão relaxada do $$\,\text{CDH}(q)$$.

Vamos agora construir um ataque, que usa a solução do HNP como “trapdoor”, para reduzir o $$\,\text{CDH}(q)\,$$ à sua versão relaxada $$\,\text{xCDH}(q,k)$$. Isto é, vamos provar que se tivermos acesso a soluções do problema relaxado então, com a ajuda da “trapdoor”   HN P, constrói-se uma solução do  problema $$\,$$sem relaxamento.

Essencialmente isto prova que o problema relaxado é tão difícil que o problema não-relaxado.

**Ataque** $$\,\text{CDH}(q) \mathbin{\;\mathbf{<_T}\;} \text{xCDH}(q,k)$$

1. A partir dos parâmetros $$\,$$$$(a, b, c)\,$$ o atacante gera aleatoriamente $$\,N\,$$ valores de $$\,c_i\equiv c\times a^i = a^{s + i}\,$$ e submete-os ao oráculo $$\text{xCDH}(q,k)\,$$ .
2. Recolhendo  $$u_i$$’s que verificam $$\,u_i = \text{msb}_k(b^{s+i})\;=\; \text{msb}_k(b^s\times b^i)\,$$.
3. Com $$\,x_i\equiv b^i\,$$ o atacante submete os $$N$$ pares $$(x_i,u_i)\,$$ ao oráculo HNP e recolhe $$b^s$$ construindo deste modo um duplo $$(a, b, a^s, b^s)$$ solução do $$\,\text{DDH}(q)$$.


Este exemplo ilustra aspetos importantes na construção de ataques a problemas difíceis:


- O ataque parte de uma versão *relaxada* do problema inicial : isto é, um problema que é mais simples de resolver  porque impõe menos restrições que o problema inicial.
- O ataque mostra que, se for possível resolver o problema mais simples, também é possível resolver o problema inicial.
- No processo usa-se um terceiro problema, a **trapdoor**, que em princípio tem uma solução eficiente. É essa solução que que fornece a informação adicional que permite reduzir o problema difícil à sua versão relaxada.


| A palavra **”trapdoor”** tem muitos significados que, muitas vezes, não são completamente similares.<br><br>A forma mais usual de “**trapdoor”** é a de um mecanismo privado que fornece a **chave secreta**  com a qual  é possível  resolver o problema difícil . <br><br>No exemplo acima,  a “trapdoor” é um algoritmo público ; porém exige que a resolução do problema difícil consulte o oráculo que resolve a versão relaxada do mesmo problema.<br><br>Outro exemplo de “trapdoor” são as **”hidden trapdoors”**  que se baseiam também num problema aritmético, embebido na estrutura algébrica do problema “difícil”, e que permite resolvê-lo mais facilmente: um “segundo caminho” para a solução. |



# Estruturas Bilineares

Na sua forma mais geral uma **estrutura bilinear** é uma função

                                $$f \,\colon \mathcal{G}_0 \times \mathcal{G}_1 \;\to\; \mathcal{U}$$

em que

    - $$\,\mathcal{G}_0,\mathcal{G}_1,\mathcal{U}\,$$ são grupos abelianos que, individualmente, tanto podem ser aditivos como multiplicativos. Sem perda de generalidade vamos considerar que os dois primeiros  têm a forma semelhante $$\,(G_0,\square,e)\,$$ e $$\,(G_1,\square,e)\,$$ enquanto  $$\mathcal{U}$$  tanto pode ser aditivo como multiplicativo.
    - Para cada $$\,a\in G_0\,$$a aplicação $$\,{}\mathcal{G}_1\,\to\,\mathcal{U}$$ definida por  $$\,x\mapsto\,f(a,x)\,$$ é um homomorfismo de grupos. Simetricamente para cada $$\,b\in G_1\,$$ a aplicação $$\,x \mapsto f(x,b)\,$$é também um homomorfismo de grupos.

Desta definição é simples verificar que, para todo $$\,(x,y)\in G_0\times G_1\,$$, se tem $$f(x,e) = f(e,y) = 0$$, supondo $$\mathcal{U}$$ aditivo.

A estrutura bilinear $$f$$ é **não-trivial** quando estes são os unicos casos em que se tem funções constantes, Isto é:

        - Para todo $$\,x\in G_0\,$$existe $$y\in G_1\,$$ tal que $$\,f(x,y) \neq 0$$,
        - Para todo $$y\in G_1\,$$existe $$x\in G_0\,$$ tal que $$\,f(x,y) \neq 0$$.

Duas classes de estruturas bilineares ocorrem em criptografia: **formas bilineares** e **emparelhamentos** .


## Formas Bilineares

São estruturas bilineares  $$\,f\colon X \times Y \,\to\, K\,$$ em que  $$\,K\,$$ é um corpo,  e  $$\,X\simeq K^n\,$$ e $$\,Y\simeq K^m\,$$ são isomórficos  com espaços vetoriais sobre esse corpo.


| Pode-se generalizar a  definição de estruturas bilinear  considerando funções $$\,f \colon X \times Y \to \mathcal{R}$$ em que  $$\,\mathcal{R}\,$$ é um anel (em vez de um corpo) e $$X,Y\,$$ são $$\mathcal{R}$$-módulos finitamente gerados. |

 O caso mais simples de formas bilineares são os **produtos internos** definidos sobre espaços vetoriais $$\,X\;\text{e}\; Y\,$$ com a mesma dimensões $$n$$ e $$m$$. O produto interno $$\,\langle \cdot,\cdot\rangle\,$$ define-se associado a um morfismo de grupos $$\,\tau : X \to Y\,$$ (i.e. função linear) via

                         $$\langle x,y\rangle\,\equiv\,\sum_{ i =1}^m\,\tau(x)_i\times y_i$$

O caso mais simples ocorre quando $$\,X\equiv Y\,$$e $$\,\tau\,$$é a identidade. 

Sendo $$\tau$$ um morfismo  de grupos, existe uma matriz  $$\,A\in K^{n\times m}\,$$ que o representa através da relação $$\,\tau(x) \equiv x \times A\,$$. Aqui $$\times\,$$denota o produto de um vetor linha por uma matriz. Pode-se provar que, neste caso, a $$\tau$$ tem um *morfismo*  *transposto*  $$\,\tau^\top\,$$tal que 

                         $$\langle x,y\rangle\,=\,\sum_{ i =1}^n\,x_i\times \tau^\top(y)_i$$


## Função traço e produtos internos

Uma outra forma de definir um produto interno aplica-se a corpos finitos $$\,$$$$\,\mathbb{F}_q\,$$ de característica $$\,p\,$$e dimensão $$n$$; sabemos que tem de ser $$\,q = p^n\,$$ e, nesse caso, $$\,\mathbb{F}_q\,$$ é isomórfico com $$\,(\mathbb{F}_p)^n\,$$.

No corpo $$\,\mathbb{F}_{p^n}\,$$ define-se uma função que mapeia cada elemento desse corpo num elemento do corpo primo $$\,\mathbb{F}_p\,$$ e que preserva somas (i.e. é linear); tal função é designada por **função traço** e define-se como

                                $$\,\mathbf{tr}(x) \,\equiv\, \sum_{i=0}^{n-1}\,x^{p^i}$$

Por exemplo, num corpo de dimensão $$\,n=4\,$$ e $$p=2$$ tem-se $$\,\mathbf{tr}(x) \equiv x + x^2 + x^4 + x^8\,$$.

Considere-se dois corpos $$\,\mathbb{F}_{p^n},\mathbb{F}_{p^m}\,$$ com a mesma característica $$p$$ mas eventualmente com dimensões diferentes; considere-se um função linear $$\,\tau \,\colon\, \mathbb{F}_{p^n}\,\to\,\mathbb{F}_{p^m}\,$$. O produto interno $$\,\mathbb{F}_{p^n} \times\mathbb{F}_{p^m}\,\to\,\mathbb{F}_p\,$$determinado por $$\tau\,$$  define-se como 

                                $$\langle x,y\rangle_\tau \;\equiv\; \mathbf{tr}(\tau(x)\times y)\,$$
## Emparelhamentos

São estruturas bilineares não trivias  $$\,\mathbf{e}\,\colon\, \mathcal{G}_0\times \mathcal{G}_1 \,\to\,\mathcal{U}\,$$ em que todos os grupos são cíclicos e têm a mesma ordem.

O problema $$\,\text{DDH}(\mathcal{G})\,$$é definido pela linguagem  $$\,\mathcal{L} \,\equiv\,\{(a, b, c, d) \;|\;\exists \ell\,\centerdot\, c = \ell\,a \,\land\, d = \ell \, b\}$$.
Se existir um emparelhamento  $$\,\mathbf{e}\,\colon\,\mathcal{G}\times \mathcal{G}\,\to\,\mathcal{U}\,$$, e se ele for implementado eficientemente, existe um algorimo eficiente para decidir se um tuplo $$\,(a,b,c,d)$$ pertence ou não à linguagem.

Basta comparar $$\,\mathbf{e}(a, d)$$ com $$\,\mathbf{e}(c,b)\,$$; se $$\,\mathcal{U}\,$$for multiplicativo, ambos os valores coincidem com $$\,\mathbf{e}(a,b)^\ell$$. Mesmo sem conhecer o valor de $$\ell$$ podemos decidir se os valores são iguais ou não.

Quando estudarmos Curvas Elípticas analisaremos em mais detalhe a noção de emparelhamento e as suas aplicações criptográficas. 



## Produtos internos com ruído.

A noção de “trapdoor” que esboçamos quando falamos do Hidden Number Problem, aparece na criptografia pós-quântica aliada a funções lineares ou bilineares às quais é adicionado **ruído.**

**Protocolo Hopper-Blum.**
Como paradigma vamos descrever o **protocolo Hopper-Blum :** uma prova de conhecimento não interativa que corre com sucesso quandom  o “prover”  $$\,\mathcal{P}\,$$ como o “verifier” $$\,\mathcal{V}\,$$ conhecem um mesmo segredo $$\,s\,$$. O protocolo é de conhecimento-zero porque, perante as mensagens públicas, nenhuma terceira parte consegue obter informação sobre o segredo $$s$$.

O protocolo funciona exclusivamente com bits, strings de bits e operação XOR. As operações fundamentais são:

    - Dados $$\,s,a\in\{0,1\}^n\,$$ define-se o produto interno $$\,s\cdot a\,$$ como $$\,\bigoplus_{s_i=1}\,a_i\,$$
    - Existe um gerador $$\,\mathcal{H}_n\,$$ que gera aleatoriamente vetores $$\,a\in \{0,1\}^n\,$$. O gerador $$\,\mathcal{H}_n\,$$ pode ser implementado por um *hash* seguro de tamanho $$n$$.
    - Existe um gerador de Bernoulli $$\,\mathcal{B}(\epsilon)\,$$ parametrizado por um “bias” $$\,\epsilon > 0$$ ; isto é, um gerador de bits que gera $$\,0\,$$ com probabilidade $$\,(1/ 2 + \epsilon)\,$$. 
        Este gerador pode ser construído a partir do *hash* $$\,\mathcal{H}_n\,$$ da seguinte forma
                        $$\vartheta\,a \gets \mathcal{H}_n \,\centerdot\, \mathbf{if}\;\|a\|/n > 1 / 2 + \epsilon\; \mathbf{then}\;1\;\mathbf{else}\; 0$$ 
        em que $$\,\|a\|\,$$denota o número de $$1$$’s em $$a$$ (o seu **peso de Hamming**).
    - Os valores de $$\,n,\epsilon\,$$ e de um inteiro $$m$$ (ainda não foi apresentado) são parâmetros públicos do protocolo.


            

O protocolo HB funciona da seguinte forma:

| O “prover” conhece um segredo $$\,s\in\{0,1\}^n\,$$ e o “verifier” conhece um segredo $$\,\upsilon \in \{0,1\}^n\,$$. O objetivo do protocolo é verificar se  $$\,s = \upsilon\,$$ sem revelar qualquer um desses segredos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| São definidos dois geradores:<br><br>            $$\mathcal{P}(s)\;\equiv\; \vartheta\,a\gets \mathcal{H}_n \,\centerdot\,\vartheta\,e\gets \mathcal{B}(\epsilon)\,\centerdot\, (a, e \oplus (s\centerdot a))$$<br>            $$\mathcal{V}(\upsilon,a, b) \;\equiv\; b \oplus (\upsilon\cdot a))$$<br><br>**Prover**: <br><br>        Com o segredo $$s$$ constrói $$m$$ amostras   $$\,(a_i,b_i) \gets \mathcal{P}(s)\,$$ e publicita-as<br>        <br><br>**Verifier**:<br><br>        - Com o segredo $$\,\upsilon\,$$e as $$m$$ amostras, constrói o vetor de erro $$\,r\in \{0,1\}^m\,$$ , via   $$\,r_i \gets \mathcal{V}(\upsilon,a_i,b_i)$$ <br>        - Em seguida decide se os $$\,r_i$$’s são aleatoriamente gerados ou seguem o gerador $$\,\mathcal{B}(\epsilon)$$. Para isso calcula $$\,\|r\|/m \,$$ e verifica se é nitidamente inferior a $$1/ 2$$. <br>            Com elevada probabilidade, o teste  tem sucesso se e só se  $$\,s=\upsilon\,$$.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Correção**<br>Tem-se $$$$$$r_i \,=\, b_i \oplus (\upsilon\cdot a_i) \,=\, e_i \oplus (s\cdot a_i) \oplus (\upsilon\cdot a_i)\,=\,e_i \oplus ((s\oplus \upsilon)\cdot a_i)$$<br><br>        - Se $$\,s\oplus \upsilon \neq 0\,$$ , dado que os $$a_i$$’s são aleatoriamente gerados, os  $$\,r_i\,$$ também são aleatoriamente gerados . Portanto deve ser  $$\,\|r\|/m \approx 1/ 2\,$$ .<br>        - Se $$\,s\oplus \upsilon = 0\,$$ , verifica-se   $$(s\oplus \upsilon)\cdot a_i = 0\,$$ para todo $$i$$ ; por isso os $$\,r_i\,$$ distribuiem  como os $$\,e_i\,$$;  ou seja de acordo com o gerador “biased”  $$\,\mathcal{B}(\epsilon)$$. Portanto deve-se ser  $$\,\|r\|/m \ll 1/ 2\,$$.<br><br>**Segurança**<br>A segurança e correção do protocolo estão diretamente dependentes do valor do”bias”  :<br><br>        - Se o “bias” for muito pequeno, nomeadamente se for $$\,\epsilon = 0\,$$, então a geração dos $$\,r_i\,$$ é sempre “unbiased” quer  seja $$\,s=\upsilon\,$$ou $$\,s\neq\upsilon\,$$ .<br>            O protocolo é incorreto porque não consegue distinguir as duas situações.<br>        - Se o “bias” for muito grande, nomeadamente $$\,\epsilon = 1/ 2\,$$ que  implica $$\,e_i=0\,$$ para todo $$i$$,  então o gerador $$\,\mathcal{P}(s)\,$$ produz pares $$\,(a_i, b_i)\,$$ em que  $$\,b_i = s\cdot a_i\,$$. Recolhendo $$n$$ valores de $$\,a_i\,$$ linearmente independentes , o atacante constrói um sistema de $$n$$ equações  linearmente independentes ; usando álgebra linear, determina $$\,s\,$$. <br>            O protocolo é inseguro porque deixa escapar o segredo.<br>    <br><br>Portanto, para aliar correção com segurança, é necessário usar um “bias” intermédio entre $$\,0\,$$ (incorreto) e $$\,1 / 2\,$$ (inseguro). |

#LPN
O problema de extrair $$\,s\,$$ de amostras do gerador $$\,\mathcal{P}(s)\,$$designa-se por **“Learning Parity with Noise” (LPN)** e faz parte de uma família de problemas derivados da Teoria da Aprendizagem (“learning theory”) que estão nos fundamentos de uma parte substancial dos novos problemas difíceis em criptografia pós-quântica. 

Acredita-se que, com uma apropriada escolha de parâmetros, LPN é $$\,\text{NP}$$-completo. Em particular existem algoritmos eficientes para reduzir ao LPN a maioria dos problemas difíceis clássicos, como a fatorização de inteiros e o logaritmo discreto.

Analisando o protocolo de Hooper-Blum vê-se algumas das características  que ocorrem também em outros problemas de aprendizagem. Em todos


1. Existe uma informação privada $$\,s\,$$ que é transformada por uma aplicação bilinear  com informação aleatoriamente gerada, ao qual é adicionado um ruído.  Algo da forma
                          $$\text{Gen}(s)\;\equiv\quad\vartheta\, a \gets \mathcal{S} \,\centerdot\,\vartheta\, e\gets \chi \,\centerdot\, (a\,,\, s \ast a + e)$$
2. Os geradores  $$\,\mathcal{S}\,$$e $$\,\chi\,$$, para além da estrutura algébrica que define os operadores $$\,+\,$$e $$\,\ast\,$$, determinam o problema.
3. As amostras $$\, (a, b) \gets \text{Gen}(s)\,$$ são públicas. 
    O problema “difícil” é a **aprendizagem do segredo** $$\,s\,$$  a partir das amostras públicas.  

Se o ruído $$\,e\,$$ for sempre nulo, existe um processo eficiente de recuperar o segredo $$\,s\,$$a partir das amostras : tipicamente, tal como no LPN, resolvendo um sistema de equações lineares. É a presença do ruído que  torna o problema difícil.

A dificuldade do problema manifesta-se na incapacidade que um atacante tem em distinguir os *outputs* de $$\,\text{Gen}(s)\,$$ dos *outputs* de um *hash* aleatório com o mesmo tamanho. 

O uso do problema numa técnica criptográfica concreta exige uma “trapdoor” :  um agente privilegiado,  que seja capaz de fazer essa distinção, tem de ter acesso a essa “trapdoor”.

Este formato provém inicialmente no âmbito da Teoria dos Códigos e é apropriadamente designado por **descodificação de um código linear .** A **** “trapdoor” ****referida antes é precisamente o algoritmo designado como **algoritmo de descodificação**.
 
 **Um protocolo de acordo de chaves** **baseado em aprendizagem**

Um protocolo KEX (“key exchange”) do tipo Diffie-Hellman que, em vez de grupos cíclicos, usa o anel $$\,\mathcal{R}_q\,$$ de polinómios com coeficientes no corpo primo $$\,\mathbb{F}_q$$. 
Assume-se que os elementos do corpo são representados por inteiros no intervalo $$\,\{-\delta , \cdots, \delta\}\,$$ sendo $$\,\delta\equiv (q-1)/2\,$$.

Essenciais ao protocolos são os geradores:

    - $$\,\chi_{n}\,$$ gera aleatoriamente “pequenos polinómios” de tamanho $$\,n\,$$ , aqui definidos como polinómios cujos vetores de coeficientes pertencem a $$\,\{-1,0,1\}^n\,$$ .
    - $$\,\mathcal{S}_n\,$$gera aleatoriamente “grandes polinómios” ; por exemplo, polinómios da forma $$\,(\delta\, f)\,$$ com $$f$$ um pequeno polinómio.

**SetUp**  $$s\gets \chi_n\,$$é chave privada do agente **A** ; $$\,\upsilon \gets \chi_n\,$$é chave privada do agente  **B** ;  ****$$a\gets \mathcal{S}_n\;$$é um parâmetro público. 
É definida a *função de descodificação*  $$\,\mathsf{decode}\,$$ que, aplicada a um elemento de $$\mathcal{R}_q$$ , seleciona os bits mais significativos de cada um dos seus coeficientes.


1. 
    **Agente A**  calcula $$\,b \gets \,(\vartheta\,e \gets \chi_n\,\centerdot\, a*s + e)\;$$ e publica este valor
    **Agente B**  calcula $$\,c \gets \,(\vartheta\,r \gets \chi_n\,\centerdot\, a*\upsilon + r)\;$$e publica este valor
2.   
    **Agente A** calcula $$\,\kappa_A \gets \mathsf{decode}(s*c)$$
    **Agente B** calcula $$\,\kappa_B \gets \mathsf{decode}(\upsilon*b)$$

**Correção** 
Deve-se verificar $$\,\kappa_A\,=\,\kappa_B\,$$ .

**Justificação**
O protocolo é correto porque 

                     $$\,s*c - \upsilon * b\,=\, s*a*\upsilon + s*r - \upsilon*a*s - \upsilon * r\,=\,s*r - \upsilon*e$$ 

Como todos  $$\,s,\upsilon,e,r\,$$ são  pequenos polinómios, a diferença $$\,(s*c-\upsilon*b)\,$$ é eliminada pela função de descodificação.

**Comentário**  

Um número importante de candidaturas ao concurso NIST-PQC na categoria  PKE, KEX e KEM,  segue este modelo. As principais melhorias em relação ao que aqui é apresentado  incidem na função de descodificação (muito melhor do que a aqui esboçada) e nos geradores de “pequenos polinómios”. Também variam na forma como  implementam as operações soma e multiplicação no anel de polinómios (usam normalmente uma transformação do tipo NTT) o que implica algum discernimento na escolha desse anel. $$$$



# Curvas Elípticas

[+Capítulo 5a: Curvas Elípticas](https://paper.dropbox.com/doc/Capitulo-5a-Curvas-Elipticas-NcOecWcwpZJtJXXvlKTvy) 

