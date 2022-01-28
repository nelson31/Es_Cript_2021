# Capítulo 6: Provas de Conhecimento e Assinatura Digital

# Introdução

Técnicas criptográficas associadas a objetivos de *autenticação* e *confiança* (em agentes, documentos, atos, etc.) lidam essencialmente com **provas de conhecimento verificáveis** .
O que é **conhecimento**, o que é **prova** e como se **verificam** tais provas é o objetivo desta sessão de estudo.

Em matemática  (e criptografia) a noção de conhecimento está associada à **capacidade de construir a solução de um problema**. 
Um **problema** pode ser interpretado como uma **linguagem**: formalmente um conjunto $$\mathcal{L}$$ de naturais $$\mathbb{N}$$ ou de *strings* de bits $$\{0,1\}^\ast$$. Uma **solução** do problema é um elemento $$x\in\mathcal{L}$$.

----------

**Exemplos**

1. $$\mathbf{SAT}(\varphi)$$ é o problema definido por uma fórmula proposicional  $$\varphi(x_1,\cdots,x_n)$$ com $$n$$ varíáveis.

As soluções do problema são vetores $$\upsilon \in \{0,1\}^n$$  representando alocações de valores de verdade às variáveis de forma a tornar a fórmula válida:.

$$\mathbf{SAT}(\varphi) \,\equiv\, \{ \upsilon \in \{0,1\}^n\,|\,\varphi\lbrack x \gets \upsilon \rbrack = 1 \}$$


2. Um problema análogo é o da **valorização** de um circuito booleano $$C$$ com $$n$$  *inputs*.
> Dado $$C$$ , a **valorização** de ****$$C$$ é a linguagem $$\mathcal{V}_C \equiv \{\upsilon \in \{0,1\}^n \,|\,C(\upsilon) = 1\}$$. 


----------

Em criptografia coloca-se a ênfase na “capacidade de construção”. Por isso conhecimento é não só **informação** estática, como a solução de um problema, mas também a capacidade para computar essa informação. Aqui inclui-se não só os algoritmos que, a partir da descrição do problema, geram a sua solução mas também os recursos computacionais exigidos por esses algoritmos.
Retomando o problema $$\,\mathbf{SAT}(\varphi)\,$$ sabemos que existe um algoritmo trivial que gera uma sua solução: basta enumerar  todos os vetores $$\,\upsilon\in \{0,1\}^n\,$$até encontrar um que verifique $$\,\varphi(\upsilon) = 1\,$$. No entanto  tal algoritmo pode não representar  conhecimento da solução porque a complexidade computacional de tal algoritmo torna-o impraticável se $$\,n\,$$ for suficientemente grande. 

## Provas Verificáveis

Para definir provas verificáveis temos de recordar a noção de **computação com oráculo** e a noção de **hierarquia aritmética**.


> Seja $$X$$ um oráculo (conjunto, sequência de bits, função, etc.). 
> A linguagem $$\mathcal{L}$$ pertence à classe $$\,\Sigma^X_0\,$$ quando existe uma decisão determinística $$D$$ tal que  $$x\in \mathcal{L}$$  se e só tal que $$\,D^X(x)$$ tem sucesso.
> A linguagem $$\mathcal{L}$$ pertence à classe $$\,\Sigma^X_1\,$$ quando existe uma decisão determinística $$D$$ tal que  $$x\in \mathcal{L}$$  se e só se existe uma string $$w\in\{0,1\}^\ast$$ tal que $$\,D^X(x,w)$$ tem sucesso.

Para linguagens em  $$\,\Sigma_1^X\,$$ a *string*  $$w$$ designa-se por **witness** ( *testemunha*  ou *certificado* ) de $$x$$ e pode-se identificar com a **prova, com ajuda**  de $$X$$, da solução $$x\in\mathcal{L}$$. A decisão $$\,D(x,w)\,$$ é a **verificação**  da prova  $$(x,w)$$.


## Classes de Complexidade $$X\!$$-NP e $$X\!$$-P

A classe $$\Sigma^X_1$$ é um modelo para os problemas com provas verificáveis. No entanto esta classe é excessivamente permissiva porque não entra em conta com a complexidade da prova nem a complexidade de verificação da prova.

A **complexidade da prova** mede-se pelo comprimento $$|w|$$ dessa prova. 

A **complexidade da decisão**  $$D^X(x,w)$$ mede-se pelo número de consultas ao oráculo $$X$$. Quando não existe um oráculo explícito (na decisão escrita como $$D(x,w)$$ ) considera-se implícito um oráculo vazio $$\emptyset$$; isto é  $$D\,\equiv\,D^\emptyset$$.

Assim


> A classe $$X\!$$-**NP** é formada por todas as as linguagens $$\mathcal{L}\in \Sigma_1^X$$  em que qualquer $$x\in\mathcal{L}\,$$ tem um certificado $$w$$ com $$|w| \leq \text{\textbf{poly}}(|x|)$$ e, na decisão $$\,D(x,w)\,$$ , o número de consultas ao oráculo $$X$$ é limitado por $$\text{\textbf{poly}}(|x|)$$.
> 
> A classe $$X\!$$-**P**  é formada por todas as as linguagens $$\mathcal{L}\in \Sigma_1^X$$  onde qualquer $$x\in\mathcal{L}\,$$ é verificável por uma  decisão $$\,D(x)\,$$ , em que o número de consultas ao oráculo $$X$$ é limitado por $$\text{\textbf{poly}}(|x|)$$.



## Sigma - protocolos como provas de conhecimento

Um **sigma-protocolo** para um problema $$\mathcal{L}\,\in\,\text{NP}$$ é uma prova de conhecimento para um **candidato a solução**  $$\,x\,$$. Provar que $$\,x\in\mathcal{L}\,$$ equivale a apresentar o certificado $$w$$ para esse candidato ou, pelo menos, uma prova de que se consegue construir esse certificado.

Nesse contexto, no par $$\,(x,w)\,$$, o candidato $$\,x\,$$ é **informação pública** enquando o certificado $$\,w\,$$é **informação privada**.

No protocolo intervêm dois agentes: 

1. O **Prover** que, caso reconheça $$\,x\,$$como solução do problema $$\,\mathcal{L}\,$$,  é capaz de provar que conhece o certificado $$\,w\,$$ respetivo, e
2.  O **Verifier** que, sem conhecer $$w$$, é ainda assim capaz de computar a decisão $$\,D^X(x,w)\,$$.



![](https://paper-attachments.dropbox.com/s_19832A83A9AC9F5E5D42684FCCD78B838CCCE111FFA37515733DB383AE0114B2_1618946256936_sigma-protocol.png)


**Commit/Open:** $$\quad\text{Comm}(x,w)\,\stackrel{\sim}{\to}\, (a , d)$$
O prover *compromete-se* não só com o candidato $$x$$ mas também com o certificado $$w$$  (caso $$x$$ seja realmente uma solução do problema) que supostamente conhece.  O objetivo é *fixar* o par $$(x,w)$$ e impedir que ele possa ser repudiado em passos futuros.

A computação$$\,\text{Comm}(x,w)\,$$usa um algoritmo probabilístico para  “comprometer” $$(x,w)$$; caso $$\,(x,w)\,$$não seja válido o algoritmo $$\,\text{Comm}\,$$ falha. Se o par for válido a computação fornece *um item público*  $$a$$ (o “commit”), que autentica a integridade do par, e cria um *item privado*  $$d$$ (o “disclose”) que permite reconstruir o certificado.

Como o algoritmo $$\text{Comm}$$ é probabilístico, o mesmo par válido $$(x,w)$$ pode produzir muitos pares $$\,(a , d)\,$$distintos. A reconstrução porém  recorre a um algoritmo determinístico, $$\,\text{Open}\,$$, que verifica  sempre $$\,\text{Open}(a , d) = w$$. 

**Chalenge:** $$\quad\text{Chal}()\,\to\, e$$
Gera aleatoriamente um desafio $$e$$ dentro de um determinado domínio finito de desafios possíveis. 
O tamanho da cardinalidade desse domínio é um parâmetro $$\,\lambda$$ fundamental ao protocolo; isto  porque limita a $$\,2^{-\lambda}\,$$ a probabilidade  de se poder prever o desafio antes do protocolo se iniciar.

**Prove:** $$\quad \text{Repl}(d,e)\,\to\,r$$
É um algoritmo determinístico para criar uma resposta $$\,r\,$$ a partir da informação privada $$\,d\,$$ que representa o par $$\,(x,w)\,$$.

A **prova** $$\,\pi\,$$ , construída pelo protocolo,  é o registo das mensagens públicas trocadas entre os agentes **Prover** e **Verifier** ; isto é,  $$\;\pi\;\equiv\;(a , e , r)$$.

**Verify:**  $$\quad \text{Ver}(x,\pi)$$
A decisão determinística **Verify** complementa o protocolo, aceitando o candidato $$\,x\,$$ (como solução válida do problema) quando o registo das mensagens, $$\,\pi = (a , e , r)\,$$,  foi corretamente construído. 

| Quando o problema $$\,\mathcal{L}\,$$ está numa classe $$\,X\!\!-\!\!\text{NP}\,$$ a verificação consulta o oráculo $$\,X\,$$; tem-se uma verificação $$\,\text{Ver}^X(x,\pi)\,$$. |


Uma execução correta do protocolo pode ser descrita por um gerador de  “provas honestas”  , representado por $$\,\text{HP}\,$$(“honest proof”), e por um verificador dessas provas 

$$\text{HP}(x,w) \;\equiv \vartheta\, (a , d) \gets \text{Comm}(x,w) \centerdot \vartheta\, e\in \{0,1\}^{\lambda} \centerdot \vartheta\, r \gets \text{Repl}(d,e)\centerdot (a,e,r)$$

$$\text{Sig}(x,w)\;\equiv\;\vartheta \,\pi \gets \text{HP}(x,w)\,\centerdot\, \text{Ver}(x, \pi)$$ 

O protocolo é **completo** para o problema $$\,\mathcal{L}\,$$ caracterizado pela relação$$\,D\,$$ quand, para todo o par $$\,(x,w) \in D\,$$ se verifica que a probabilidade de sucesso de   $$\,\text{Sig}(x,w)\,$$é  $$\,1\,$$ a menos de um erro negligenciável.

| Representado como $$\,\mathbb{P}\,\lbrack \text{Sig}(x,w)\rbrack \;\simeq\, 1$$ |

A completude  assegura que, sempre que o registo das mensagens $$\,\pi = (a , e , r)\,$$é corretamente construído, a verificação tem sempre sucesso. Portanto, se a verificação falhar, o agente de verificação tem a certeza que o **Prover** não tem o conhecimento necessário.

Pode também acontecer que um atacante, mesmo sem conhecer qualquer informação privada $$\,w\,$$ou $$\,d\,$$, seja capaz de contruir um triplo de mensagens $$\,(a, e,r)$$ aceite pelo verificador. Tais triplos designam-se por *falsos positivos.*

Para avaliar a possibilidade de falsos positivos e eliminar os seus efeitos usa a propriedade designada por **special soundness** (aqui traduzida para **fiabilidade**).


> O protocolo é $$k$$-fiável quando qualquer atacante que, dados $$x\in \mathcal{L}$$  e o respetivo “commit” $$\,a\,$$, seja capaz de construir $$k$$ registos de mensagens $$\pi_i = (a,e_i,r_i),\; i=1\cdots k\,$$,  tais que$$\,\text{Ver}(x,\pi_i)$$  têm sucesso, é igualmente capaz de abrir o “commit” $$\,a\,$$; ou seja, é capaz de computar $$\,d\,$$ a partir dos vários $$\,\pi_i\,$$, e com esse $$\,d\,$$ constrói   $$\,w \gets \text{Open}(a , d)\,$$.

Quando um protocolo é $$k$$-fiável e  é conhecido $$\lambda$$, o tamanho da cardinalidade dos espaço de desafios, então é fácil de verificar que a probabilidade de um falso positivo é limitada por $$\,2^{-\lambda}\,(k-1)$$.

**Conhecimento Zero**

Para além de ser completo e fiável, para poder ser usado repetidamente com a mesma informação privada, o protocolo não posso deixar escapar, nos vários registos $$\,\pi_i = (a , e_i , r_i)\,$$aceites pelo verificador, informação privada.

A *forma  forte* de descrever a noção de **conhecimento** zero é


> Para todo $$(x,w) \in D$$ o gerador $$\;\text{HP}(x,w)\;$$ é $$\,K$$-trivial.

A *forma fraca* de descrever o mesmo conceito é


> Para todo $$\,x\in \mathcal{L}\,$$, não existe nenhum gerador PPT (“probabilistic polynomial time”) $$\,\text{Sim}(x)\,$$ que seja estatisticamente indistinguível de $$\,\text{HP}(x,w)$$.


| **Esquema de comprometimento**<br><br>Existe alguma semelhança entre um esquema de comprometimento usado num sigma-protocolo e funções de *hash* e por isso quase todos baseiam-se em funções de *hash*. <br><br>Por exemplo, seja $$\,H\,$$uma função de *hash* segura de tamanho $$\,t\,$$. Um esquema simples de comprometimento de um segredo $$\,s\,$$ pode ser definido  pelo seguinte par de geradores:<br><br><br>    - $$\text{Comm}(s)\,\equiv\;\vartheta\,\upsilon\gets \{0,1\}^\lambda \centerdot \vartheta\, d \gets (\upsilon,s) \centerdot \, (H(d) , d)$$<br>    - $$\text{Open}(a , d) \,\equiv\; \vartheta\,(\_,s) \gets d \,\centerdot\, \text{\textbf{if}}\; a = H(d)\;\text{\textbf{then}}\;s\;\text{\textbf{else}}\; \bot$$<br><br>Note-se que $$\,\text{Comm}\,$$ é um algoritmo probabilístico mas $$\,\text{Open}\,$$é sempre  deterninístico.<br><br>Genéricamente um esquema de comprometimento de um segredo $$\,s\,$$é formado por:<br><br>    - um algoritmo probabilístico  $$\,\text{Comm}(s)$$ que produz um par $$(a , d)$$, commit-disclose; o commit é público e o disclose é privado.<br>    - um algoritmo deterministico $$\,\text{Open}(a , d)\,$$que “abre” o commit e reproduz o segredo $$\,s\,$$<br><br>O esquema é *correcto* quando, para todo $$s\,$$, $$\,\mathbb{P}[\vartheta (a , d) \gets \text{Comm}(s) \centerdot s = \text{Open}(a , d)] \simeq 1$$.<br><br>O esquema *escondes*  $$\,s\,$$ (“hides”) quando, para todos $$\,s\neq s'\,$$, os geradores $$\,\text{Comm}(s)\,$$ e $$\,\text{Comm}(s')\,$$são computacionalmente indistinguíveis; isto é, para toda a decisão $$\,D\,$$ “eficiente” verifica-se     $$\,\mathbb{P}[\vartheta\,x \gets \text{Com}(s)\centerdot D(x)] \simeq \mathbb{P}[\vartheta\, y \gets \text{Comm}(s')\centerdot D(y)]$$.<br><br>O esquema *compromete*  $$\,a\,$$ (“bindes”) se não fôr possível  encontrar $$\,d,d'$$ tais que $$\text{Open}(a, d)\,$$ e $$\,\text{Open}(a, d')$$ terminam ambos com sucesso mas com resultados distintos. |



## Transformação de Fiat-Shamir

Sigma-protocolos ocorrem numa grande variedades de técnicas criptográficas desde protocolos de identificação, de computação partilhada e partilha de segredos, “block-chains”, etc.

A aplicação mais importante é, no entanto, a construção de esquemas de assinatura digital através de uma metodologia designada por **transformação de Fiat-Shamir (FST)**.

Um esquemas de assinaturas digitais é fundamentalmente uma forma particular de **prova de conhecimento não-interativa**. A FST é um mecanismo genérico para transformar um sigma protocolo (prova de conhecimento interativa) numa prova de conhecimento não-interativa.

Um sigma-protocolo, com parâmetro $$\lambda$$ para o espaço de desafios, que seja $$k$$-fiável, tem probabilidade de erro (aceitação de um falso positivo) limitada a $$\,2^{-\lambda}\,(k-1)$$. 

Dado que este valor pode ser elevado, a estratégia para a diminuir passa por repetir a execução do protocolo um número $$\,t\,$$ de vezes. Neste caso a probabilidade de erro diminui para $$\,2^{-\lambda\,t}\,(k-1)\,$$ mas, em contrapartida, o tamanho do registo de mensagens aumenta $$\,t\,$$ vezes.

Estes parâmetros são fundamentais quando se constrói um esquema de assinaturas a partir de uma repetição de um sigma-protocolo porque traduz o equilíbrio entre a probabilidade de erro e o tamanho da assinatura.$$\, \,$$

Qualquer esquema de assinaturas é formada por dois geradores probabilísticos e uma decisão determinística: **KeyGen**, que gera as chaves pública e privada, a partir dos parâmetros definidores do esquema; **Sign** que gera a assinatura de uma mensagem $$\,m\,$$ usando a chave privada; **Verify**  uma decisão determinística que verifica a correção da assinatura com a mensagem e a chave pública.

A transformação de Fiat-Shamir constrói estes 3 items a partir de 

1. um problema $$\mathcal{L}$$ da classe $$\,\text{NP}$$
2. um sigma protocolo que construa provas de conhecimento interativas para $$\mathcal{L}$$
3. uma função de *hash* segura $$\,H\,$$


- $$\text{KeyGen}(\mathcal{L},\lambda)$$
    - Escolhe uma solução $$x\in\mathcal{L}$$ e um seu certificado $$w$$.
    - $$x$$ é a chave pública e $$w$$ é a chave privada.


- $$\text{Sign}(x,w,m,t)$$
    - constrói uma execução honesta do protocolo como
    
        $$\text{HP}'(x,w) \;\equiv \vartheta\, (a , d) \gets \text{Comm}(x,w) \centerdot \vartheta\, e\gets H(a , m)\,\centerdot \vartheta\, r \gets \text{Repl}(d,e)\centerdot (a,r)$$

    

| Note-se que<br>        - o desafio $$e$$  não é gerado aleatoriamente mas  via uma função de *hash*:   $$e \gets H(a,m)$$; <br>        - o valor de $$e$$ não ocorre no registo da prova. |

    - Executa $$t$$ vezes a execução honesta: $$\,\sigma_i \gets \text{HP}'(x,w)\,$$ para $$i=1,\cdots, t$$.
    - A assinatura é   $$\,\text{sign}\,\gets\,(\sigma_1,\cdots,\sigma_t)$$.


- $$\text{Verify}(x,m,\text{sign})$$
    - recupera $$\;\sigma_1,\cdots,\sigma_t \,\gets\,\text{sign}$$
    - para $$\,i = 1,\cdots\,t$$ constrói as decisões deterministicas

                     $$V_i(x,m)\,\equiv\,\vartheta\,(a_i,r_i) \gets \sigma_i \centerdot \vartheta\,e_i \gets H(a_i,m)\centerdot \vartheta \,\pi_i \gets (a_i,e_i,r_i) \centerdot \text{Ver}(x,\pi_i)$$
     e verifica se, para todas,   $$\,\mathbb{P}\lbrack \text{V}_i(x,m)\rbrack\;= \; 1.$$



## Partilha de Segredos e Computação Cooperativa

A partilha de segredos, **secret sharing (SS),** e a computação cooperativa, **multi-party computation (MPC),** são áreas da criprografia que frequentemente ocorrem no mesmo protocolo criptográfico. Ambos lidam com partilha ou cooperação entre um número de **agentes** (ou **participantes** ) para executar uma tarefa que, individualmente, nenhum dos agentes consegue completar.

Exemplos típicos são protocolos usados para partilhar chaves privadas usadas, por exemplo, em esquemas de assinatura cooperativa: cada agente conhece uma **cota-parte** (ou **“share”**) da chave, nenhum dos agentes conhece a cota dos restantes nem a chave completa; coletivamente, sem revelar os respetivos segredos, os agentes conseguem construir a assinatura.

Assinaturas digitais ou cifras de chave pública são, tipicamente, operações complexas que envolvem estruturas algébricas sofisticadas. Mas, em grande medida, os problemas SS+MPC podem ser estudados em modelos da computação mais simples; nomeadamente no **cálculo em circuitos**  (ou **circuit evaluation**).

O modelo da computação é o de funções *booleanas*
                                                               $$\,{f}\; \colon\; \{0,1\}^n \;\to\,\{0,1\}$$
que podem ser implementadas por um **circuito** *booleano*  $$\,\mathcal{C}_f\,$$construído a partir de um repertório de operações simples, designadas por **gates** 

Tipicamente usam-se as seguintes *gates booleanas* 

    - a adição e multiplicação por constante:$$\quad x\, \mapsto\,x \oplus c\quad$$ e  $$\quad x \,\mapsto\,x \cdot c\;$$
    - a adição e multiplicação binárias: $$\quad x,y \,\mapsto\, x\oplus y\quad\text{e}\quad x,y\,\mapsto x\cdot y$$

Frequentemente são necessárias operações mais complexas e usam-se *gates aritméticas*  que são análogas às anteriores mas as operações de soma e multiplicação são executadas num corpo finito $$\,\mathbb{F}_q$$.

Para implementar a função *booleana* $$\,f\; \colon\; \{0,1\}^n \;\to\,\{0,1\}$$ é necessário um circuito $$\,\mathcal{C}_f\,$$que aceite *inputs* $$x$$ de tamanho $$n$$. Diz-se que o circuito tem **ordem** $$n$$. 

O **tamanho** do circuito, representado por $$\,|\mathcal{C}_f|\,$$ , é o número de *gates* do circuito.

Neste caso o número máximo de *gates* é da ordem $$O(2^n)$$ e, por isso, no pior caso o problema de verificar  $$\,\mathcal{C}_f(x) = 1\,$$tem complexidade da mesma ordem.

Nas aplicações SS+MPC os circuitos usados têm um número de *gates* bastante inferior ao limite teórico. Por isso pode-se assumir que o problema de *circuit evaluation* tem uma solução razoavelmente eficiente.

De facto, se for possível converter eficientemente o circuito em certas formas normalizadas do cálculo preposicional (CNF’s e BDD’s) o problema tem complexidade polinomial de baixo expoente. Obviamente a conversão de um circuito arbitrário numa destas formas tem complexidade exponencial.

Num *circuito reduzido* (sem *gates* redundantes)  o seu tamanho  $$\,|\mathcal{C}_f|\,$$ é dado pelo número total de *gates*. O circuito diz-se **polinomial** quando o seu tamanho é limitado polinomialmente com o tamanho do *input (i.e. a ordem do* circuito)*.*

O problema da **verificação** ou **aceitação** de um circuito polinomial $$\,\mathcal{C}\,$$de ordem $$n$$ é o de determinar um $$\,x\in \{0,1\}^n\,$$ que seja aceite pelo circuito: i.e.  $$\,\mathcal{C}(x) = 1$$.


> Se $$\,\mathcal{C}\,$$é um circuito polinomial de tamanho. $$\,N\equiv |\mathcal{C}|\,$$ e ordem $$\,n\,$$. Então o problema da verificação de $$\mathcal{C }$$ está na classe $$\text{NP}\,$$:  o candidato a solução é o input aceite $$\,x\in\{0,1\}^n\,$$ ;  o certificado $$\,w\,$$ é o elemento de $$\,\{0,1\}^N\,$$ formado pelos outputs das várias gates do circuito quando o input é $$x$$.

**Exemplo**
Um circuito com 6 inputs e 7 gates. A ordem é $$6$$ e o tamanho é $$7$$.


![](https://paper-attachments.dropbox.com/s_19832A83A9AC9F5E5D42684FCCD78B838CCCE111FFA37515733DB383AE0114B2_1618952248029_curcuito.png)


O vetor $$\,x\equiv (x_0,\cdots,x_5)\,$$é o candidato a solução enquanto que o vetor $$\,w \equiv (w_0,\cdots,w_6)$$ é o respetivo certificado. O candidato $$\,x\,$$ é aceite se e só se $$\,w_6=1$$.

**Cálculo de circuitos com partilha de segredos.**

O cálculo de circuitos parece ser um problema muito mais simples do que o da verificação: se o *input* $$\,x\,$$ for completamente conhecido por um agente, esse agente pode usar as relações que determinam os valores do vários $$w_i$$ até chegar à última *gate*; o esforço computacional é dado por  $$\,|w|\,$$ que, por construção, é polinomial com a ordem $$\,|x|\,$$.

Porém a versão interessante desse problema ocorre quando o conhecimento sobre $$\,x\,$$ está distribuído por vários agentes.  Mais exatamente, quando cada agente conhece cada um dos *inputs* $$x_i$$ e dos ouputs $$w_j$$ a menos de um erro .

Neste caso o cálculo do valor exato do último output só pode ser realizado com a colaboração de todos os agentes. Porém, nessa colaboração, nenhum dos agentes deve revelar aos restantes a sua quota-parte de $$x$$ e $$w$$.

No que se segue vamos sempre considerar

    - $$n$$ é a ordem do circuito; i.e. o número de *inputs*
    - $$m$$ é o tamanho do circuito; i.e. o número de *gates* 
    - $$N>2$$ é o número de *agentes*  participantes na partilha

O índice $$\ell$$ percorre os *inputs*, o índice $$i$$ percorre as *gates* e o índice $$j$$ percorre os participantes.

**Partilha de um segredo** $$s\in \{0,1\}$$ 

O caso mais simples de partilha ocorre quando o segredo $$s$$ tem um único bit.

O segredo $$s$$ está relacionada com as “shares”  $$\,s_j\,$$ por
       $$\,s \;=\; s_0 \oplus s_1 \oplus \cdots \oplus s_{N-1}\,$$
 Um vetor de bits $$\,(s_0, s_1,\cdots, s_{N-1})\,$$ que verificam esta  relação é representado por  $$\,\lbrack s \rbrack\,$$.   
     
As operações básicas de partilha do segredo respondem a duas questões:

- **Sharing:** como deve ser feita a alocação de cotas pelos agentes.
- **Reconstruct**: como é que um participante arbitrário $$j$$ pode determinar o valor do segredo $$\,s\,$$ a partir da sua própria cota $$\,s_j\,$$e da contribuição honesta dos restantes agentes.

Em qualquer das construções deve-se verificar:

    1. Nenhum participante conhece as cotas dos restantes.
    2. Qualquer participante que reconstrua o segredo $$\,s\,$$ pode verificar se algum dos restantes não agiu honestamente.

O protocolo básico, dito **trivial,** é


- $$\text{Share}(s)$$
    - um “Trusted agent” gera aleatoriamente $$N-1$$ bits $$\,s_1,\cdots,s_{N-1}$$ e calcula $$\;s_0 \gets s \oplus s_1 \oplus \cdots s_{N-1}$$.
    - distribui, por canais privados, cada uma das *shares* $$\,s_j\,$$aos respetivos titulares.


- $$\text{Recon}(k)$$
    Para cada $$j$$ sejam $$\quad j^+  \equiv\, (j+1)\bmod N\quad$$e $$\quad j^- \equiv\, (j-1)\bmod N$$
    - O agente $$\,k\,$$ gera aleatoriamente um bit $$\,e\,$$,  calcula $$\,m_{k}\gets e\oplus s_k\,$$ e envia-a a $$k^+$$ por um canal privado.
    - Todos os agentes $$j\neq k$$ calculam $$\,m_j \gets s_j \oplus m_{j^-}$$ e enviam $$\,m_j\,$$ ao agente $$\,j^+$$ por um canal privado.
    - O agente $$\,k\,$$ calcula $$\,s'\gets e \oplus m_{k^-}$$

É trivial verificar que $$\,s = s'$$ desde que todos os agentes ajam honestamente.


![](https://paper-attachments.dropbox.com/s_19832A83A9AC9F5E5D42684FCCD78B838CCCE111FFA37515733DB383AE0114B2_1618953714165_partilha-segredo.png)


É essencial que a comunicação seja feita por um canal privado uma vez que um agente que conheça ambas as mensagens $$\,m_{j^-}\,$$e $$\,m_j\,$$, determina o *share*  $$\,s_j = m_{j^-}\oplus m_j$$. Por isso, para manter privado $$\,s_j$$ ,  nenhum agente pode conhecer ambas as mensagens: conhece, quanto muito, uma delas.

| A insistência em “canais privados” introduz o maior factor de complexidade neste protocolo dado que a execução ou corre no contexto da memória partilhada de um único processo (agentes “virtuais”) ou, se correr em processos independentes (um por cada agente), tem de recorrer a cifras, autenticação, etc.<br>Na primeira hipótese  o protocolo costuma designar-se  por **SS-in-the-head**. |

Um agente pode recusar-se a participar, simplesmente interrompendo a cadeia de mensagens: não fazendo nada. Porém isso é algo que os restantes detectam facilmente e podem penalizar o agente faltoso impedindo-o de participar em futuras instâncias do protocolo.

Por isso se um agente não quer participar e não quer ser detectado, a solução mais simples é mentir: executa a sua parte do protocolo mas com o complemento $$\,\bar{s_j} = s_j \oplus 1\,$$da sua cota.

Se o número de participantes que mentem fôr par, então o valor final reconstruído $$\,s\,$$ não é alterado. Se à partida nenhum dos faltosos souber se vão existir outros faltosos, nunca pode ter a certeza se o valor recuperado é correto ou errado.

Um protocolo SS é **verificável** quando é possível detetar a presença de agentes faltosos; é **fortemente verificável** quando, adicionalmente, é possível  identificar os faltosos.

Tal como foi apresentado o protocolo básico não é verificável. Para introduzir verificação é necessário modificar as operações $$\,\text{Share}(s)\;$$e $$\;\text{Recon}(k)\;$$introduzindo o comprometimento do segredo $$\,s\,$$ distinto para cada um dos participantes.

A nova versão do protocolo usa um *hash* seguro $$\,H\,$$de tamanho $$\,t\,$$ bits.


- $$\,\text{Share}(s)$$
    - o “trusted agent” gera o vetor de cotas $$\,\lbrack s \rbrack\,$$tal como no protocolo básico,
    - gera $$\,N\,$$ “nounces” $$\,\nu_0,\cdots,\nu_{N-1}\,$$, um por cada participante, e calcula os comprometimentos $$\;a_j \gets H(\nu_j)\oplus s\,0^{t-1}$$.
    - envia $$\,(s_j,a_j)\,$$, por canal privado, ao agente $$j$$.
| $$s\,0^{t-1}\;$$é a string de comprimento $$t$$ cujo primeiro bit é $$\,s\,$$ e os $$(t-1)$$ bits finais são zeros. |

- $$\,\text{Recon}(k)$$
    - O agente $$k$$ começa por reconstruir o segredo $$s\,$$tal como no protocolo básico usando a colaboração (faltosa ou não) dos restantes agentes.
    - Para verificar a autenticidade de $$\,s\,$$necessita da colaboração do “trusted agent”. Para isso
        - Pede ao TA que lhe envie o seu *nounce* $$\,\nu_k\,$$e calcula  $$\,\tau_k \equiv a_k \oplus H(\nu_k)$$
        - Verifica se $$\,\tau_k\,$$tem a forma $$\,s\,0^{t-1}\;$$sendo $$\,s\,$$o bit que reconstruiu.


## Secret Sharing Multi-Party Circuit Evaluation

Pretende-se definir um protocolo onde $$\,N\,$$ agentes colaboram para resolver o problema de cálculo de um circuito em que:

    1. a informação de *input* é partilhada e 
    2. o cálculo de *outputs,* que cada agente faz, baseia-se exclusivamente na sua cota do *input*. 

Para simplificar a notação vamos usar a designação genérica de *wire* para representar quer os inputs quer os *outputs* das várias *gates*. O número total de *wires* é $$\,n+m\,$$.

A notação fundamental do protocolo usa índices  $$\alpha,\beta,\gamma\,$$ para identificar os vários *wires*. 

Nomeadamente  $$\,w_\alpha\,$$ é o valor do bit no *wire* $$\,\alpha\,$$. Estes valores são, à priori, desconhecidos dos vários agentes que, só no final da execução, conseguem reconstruir os *outputs* das várias *gates*.

**Fase “setup”**

1. Para todos os *inputs* e todos os *outputs* de gates **multiplicação é definido um bit $$\,\lambda_\alpha\,$$aleatoriamente gerado. As cotas $$\,\lbrack\lambda_\alpha\rbrack\,$$ são distribuídas pelos participantes.
2. Para cada *output* de uma soma $$\,w_\gamma = w_\alpha \oplus w_\beta\;$$, o valor de $$\,\lambda_\gamma\,$$é definido como $$\,\lambda_\alpha \oplus\lambda_\beta\,$$.
    Cada participante $$\,j\,$$ constrói a sua cota de $$\,\lambda_\gamma\,$$como   $$\,\lambda_{\gamma,j}\equiv \lambda_{\alpha,j}\oplus\lambda_{\beta,j}$$.
3. Para todas as  multiplicações $$\, w_\alpha \cdot w_\beta\,$$ são distribuídas pelos participantes as cotas $$\;\lbrack \lambda_\alpha\cdot\lambda_\beta\rbrack\;$$.
4. Para todo *input*  $$\,\alpha\,$$ é distribuído por todos os participantes o valor ofuscado $$\;\hat{w}_\alpha \equiv w_\alpha \oplus \lambda_\alpha$$.
| Mesmo conhecendo $$\,\hat{w}_\alpha\,$$um participante não conhece $$\,w_\alpha\,$$porque, do erro $$\,\lambda_\alpha\,$$, apenas conhece a sua cota. |

**Fase de cálculo intermédio**
Este é o processo em que cada agente, individualmente e colaborativamente, calcula o valor ofuscado $$\,\hat{w}_\alpha \equiv w_\alpha \oplus \lambda_\alpha\,$$ para cada *wire* $$\,\alpha$$.

1. Quando $$\,w_\gamma = w_\alpha \oplus w_\beta\quad$$calcula-se $$\,\hat{w}_\gamma \gets \hat{w}_\alpha \oplus \hat{w}_\beta$$.
2. Quando $$\,w_\gamma = w_\alpha \cdot w_\beta\quad$$calcula-se $$\;\hat{w}_\gamma \gets s \oplus \hat{w}_\alpha \cdot \hat{w}_\beta\;$$em que

   $$\;$$$$\lbrack s\rbrack \,=\, [\lambda_\gamma] \oplus [\lambda_\alpha\cdot\lambda_\beta]\oplus \hat{w}_\alpha\cdot [\lambda_\beta]\oplus\hat{w}_\beta\cdot [\lambda_\alpha]$$

        - Cada agente usa a relação anterior para construir a sua cota de $$\,s\,$$
        - Usando a colaboração dos restantes agentes, reconstrói o valor de $$\,s\,$$e calcula $$\,\hat{w}_\gamma$$
        

**Fase de conclusão**
Seja $$\,w_\text{out}\,$$o *wire* do *output* final do circuito. Note-se que $$\,\hat{w}_\text{out}\,$$já foi calculado na fase anterior por cada um dos agentes.  Assim, cada agente,

1. Reconstrói, usando a colaboração dos restantes agentes, o erro $$\,\lambda_\text{out}\,$$ a partir das cotas $$\,$$$$\,[\lambda_\text{out}]\;$$
2. Calcula. $$\;w_\text{out} \gets \hat{w}_\text{out} \oplus \lambda_\text{out}$$

Observações finais:

    1. O algoritmo precisa de fazer uma reconstrução do bit $$\,s\,$$para cada *gate* de multiplicação. Precisa de fazer uma única reconstrução do erro $$\,\lambda_\text{out}$$.
    2. A complexidade do cálculo é ditada essencialmente pelo número de reconstruções e portanto pelo número de multiplicações. Por isso são desejáveis circuitos com uma baixa percentagem de *gates* multiplicação.
    3. Só é feita uma reconstrução $$\,\lambda_\text{out}\,$$se apenas for a gate final do circuito a única para a qual se pretende conhecer o valor do *output* . Se, por acaso, se pretender conhecer os *outputs* de outras *gates* é necessário fazer uma reconstrução do valor $$\,\lambda_\alpha\,$$em cada uma destas *gates*.



# Segurança de Esquemas de Assinatura Digital

Esquemas de assinatura digital (DSS’s) formam  a principal classe de técnicas criptográficas orientadas para a autenticação de itens de informação e de actos. Neste texto, vamos fixar  um **espaço de mensagens** $$\,\mathcal{M}\equiv \{0,1\}^t\,$$ e um **espaço de assinaturas** $$\,\mathcal{S}\equiv \{0,1\}^s\,$$de dimensão pré-determinada. 

| Apesar desta restrição não ser estritamente necessária, a prática criptográfica mostra como o tamanho das mensagens  e o tamanho das assinaturas são elementos fundamentais na segurança e eficiência de  DSS’s. |


**Definição:** 
Um esquema de assinatura digital (DSS) é um par $$\,\langle\, \Sigma\,,\,\mathsf{Gen}\,\rangle\,$$ constituído por uma enumeração computável  $$\,\Sigma\,\equiv\,\{(\mathsf{Sig}_k,\mathsf{Ver}_k)\}_{k\in\mathbf{N}}\,$$ de pares de algoritmos em que, para todo índice $$\,k\,,$$

    -  $$\mathsf{Sig}_k\,$$ é um algoritmo probabilístico, total e privado que aceita uma *mensagem*  $$\,m\in\mathcal{M}\,$$como ‘input’ e gera uma *assinatura* $$\,\sigma\in \mathcal{S}\,$$,
    - $$\mathsf{Ver}_k\;$$é uma decisão determinística, parcial e pública  tal que
                                    $$\mathsf{Ver}_k(\sigma,m)\simeq 1 \quad\text{sse}\quad\sigma\gets \mathsf{Sig}_k(m)$$
          Um tal par $$\,(\sigma,m)\,$$diz-se $$\,\Sigma$$-**verificável** (ou só **verificável,** quando ****$$\Sigma$$ está implícito).

e por  um algoritmo probabilístico, total e privado $$\,\mathsf{Gen}\,$$ que, sob input de um parâmetro de segurança $$\,\lambda\,$$  gera aleatoriamente uma instância $$\,(\mathsf{Sig},\mathsf{Ver})\in\Sigma\,$$ .


----------

A forma usual de introduzir  privacidade e publicidade em técnicas criptográficas ditas “de chave pública”, assume que esses qualificativos se aplicam exclusivamente a items de informação estática designados por “chaves”. Nomeadamente, nos esquemas de assinatura digital, assume-se usualmente que os algoritmo $$\,\mathsf{Sig}\,$$ e $$\,\mathsf{}$$$$\,\mathsf{Ver}\,$$ recebem uma destas chaves como parte do “input” (respetivamente a chave privada e a chave pública); os algoritmos em si são públicos e é apenas o conhecimento estática das chaves que lhe dá o carácter privado ou público.

Neste texto a noção de conhecimento vai além do acesso a items de informação estática, como “chaves”. Como foi referido no início deste capítulo, 

> conhecimento é a capacidade para construir uma solução de um problema específico.

Esta capacidade inclui o acesso a informação estática mas, principalmente, inclui  a capacidade para realizar determinados atos ou computações.  Nomeadamente inclui uma escolha de modelo de computação (e.g. clássica ou quântica) e os limites superiores à complexidade dos algoritmos que se consegue executar neste modelo.

Por isso faz sentido interpretar o carácter privado e o caráter público como graus na capacidade de realizar atos ou computações. Em particular, é o conjunto de atos e computações que um agente pode realizar que determina a sua identidade.

O carácter “público” aplica-se à execução de um algoritmo cuja descrição é um item de informação pública e cujos argumentos são públicos. Ao invés a segurança de um DSS é aqui explicitada por argumentos públicos de algoritmos privados: $$\,\mathsf{Sig , Gen}$$.


> Um **ataque** a um DSS  $$\,\langle\Sigma,\mathsf{Gen}\rangle\,$$ é um gerador de pares $$\,\Sigma$$-verificáveis $$\,(\sigma,m)\,$$a partir de conhecimento público. A **segurança** desse DSS é a sua imunidade a tais ataques.

A construção, a partir de conhecimento público, de um par verificável $$\,(\sigma,m)\,$$ é vulgarmente designado por “falsificação” de assinatura ou “forgery”. A imunidade a um tal ataque pode ser designado por “autenticidade” mas, neste contexto, usa-se principalmente a designação “unforgeability” (UF).

A falsificação de uma assinatura pode ser analisada em vários aspectos. Nomeadamente é usual estabelecer tipos distintos de *objetivos de ataque:*

    - *Dada uma mensagem arbitrária* $$\,m\,$$*, calcular um par verificável* $$\,(\sigma,m)\,$$ 
        Este objetivo designa-se por **universal forgery** e a imunidade respetiva designa-se por **universal unforgeability** ou UUF.
    - *Produzir um par verificável* $$\,(\sigma,m)\,$$*para um qualquer* $$\,m\,$$ *escolhido pelo atacante*. 
        O objetivo do ataque designa-se por **existential forgery** e a sua imunidade por **existential unforgeability**  ou EUF.

A segunda dimensão na caracterização de um ataque DSS é o tipo de *conhecimento público* usado.

Um ataque tem como referência um par de algoritmos resultado de uma amostragem
                                                  $$\,(\mathsf{Sig},\mathsf{Ver})\gets \mathsf{Gen}(\lambda)\,$$
O momento em que a amostragem é realizada é o momento em que o algoritmo  $$\,\mathsf{Ver}\,$$ passa a fazer parte do conhecimento público. A partir desse momento qualquer agente pode comprovar se o resultado do ataque, o par $$\,(\sigma,m)\,$$, é  um verificável: basta-lhe executar $$\,\mathsf{Ver}(\sigma,m)\,$$. Por esse motivo um tal par $$\,(\sigma,m)\,$$ é aqui designado como ***prova de sucesso do ataque*** *.*

Para além do conhecimento público $$\,\mathsf{Ver}\,$$, o atacante tem capacidade para consultar um oráculo que, dentro de certos limites, é uma enumeração de pares verificáveis por esse algoritmo.

                                        $$\Omega(\mathsf{Ver})\;\equiv\; \{\,(\sigma_k,m_k)\,\}_{k\in\mathbb{N}}$$
                                

Os limites e restrições impostas a $$\,\Omega(\mathsf{Ver})\,$$ vão introduzir uma segunda dimensão na classificação dos ataques. Neste texto vamos considerar quatro tipos principais de oráculos $$\,\Omega\,$$ e algumas variantes.


    1. Quando $$\,\Omega\,\equiv\,\emptyset\,$$ o ataque designa-se por “no message attack” (abreviadamente NMA). 
        A imunidade UUF-NMA — “universal unforgettability with a no-message attack” — é a forma mais fraca de segurança que se pode estabelecer num DSS; é a que impõe as restrições mais fortes à capacidade do atacante: é obrigado a produzir uma prova de sucesso com uma mensagem pré-determinada sem a ajuda de qualquer oráculo.
        
    2. Quando o oráculo é determinado por uma sequência de mensagens aleatoriamente geradas, o ataque designa-se por “random message attack” (ou RMA). 
        O oráculo pode ser escrito como
                              $$\Omega\;\equiv\;\vartheta\,m \gets h\,\centerdot\,\vartheta\,\sigma\gets\mathsf{Sig}\,\centerdot\,(\sigma,m)\,$$
        em que $$\,h\,$$é um “hash” aleatório cujo tamanho coincide com a dimensão $$\,t\,$$do espaço de mensagens. 
        
        Dado que, consultando $$\,\Omega\,$$, o atacante pode simplesmente devolver como prova de sucesso uma amostra ao oráculo, a imunidade a EUF-RMA é impossível de obter. Por isso é necessário impor restrições às provas de sucesso aceitáveis. Veremos adiante essas restrições.
        Já a imunidade UUF-RMA faz mais sentido uma vez que a complexidade computacional de um ataque UF-RMA depende da complexidade computacional de um algoritmo de procura  da mensagem pré-determinada $$\,m\,$$como “output” do “hash” aleatório $$\,h\,$$. 
        No modelo clássico de computação esse complexidade é, quase sempre e no melhor caso,  exponencial com $$\,t\,$$. Se executar um tal algoritmo fizer parte do conhecimento do atacante, o ataque terá sucesso; se não, como quase sempre acontece, não fizer parte desses conhecimento, então o ataque falha.
        
    3. O atacante pode escolher *a priori* um número finito de mensagens $$\,m_1,m_2,\cdots,m_n\,$$e só depois passa a conhecer $$\,\mathsf{Ver}\,$$ e as assinaturas $$\,\sigma_1,\sigma_2,\cdots,\sigma_n\,$$das mensagens escolhidas. Nestas circunstâncias tem-se um “non-adaptative chosen-message attack” (ou naCMA).
         Neste ataque o oráculo $$\,\Omega\,$$ é um conjunto finito $$\,\Omega \equiv \{(\sigma_i,m_i)\}_{i=1}^n\,$$.
    
        As imunidade UUF-naCMA e  EUF-naCMA conseguem-se quando é apresentada uma prova de sucesso $$\,(\sigma,m)\,$$ em que a mensagem $$\,m\,$$ é distinta de qualquer das mensagens $$\,m_i\,$$escolhidas. 
        
        Essencialmente o ataque inclui um ***algoritmo de repúdio*** usado para impedir que o resultado do ataque inclua uma mensagem $$\,m\,$$ contida em $$\Omega$$. O repúdio actua na escolha dos $$\,m_i\,$$ num UUF-naCMA, dado que aqui $$\,m\,$$é pré-determinado, ou  num ataque EUF-naCMA, actua na apresentação da prova de sucesso impedindo que esta contenha um $$\,m = m_i$$.


        Este repúdio pode ser relaxado considerando que a mesma mensagem pode ter muitas assinaturas. Assim pode-se aceitar que $$\,m\,$$ coincida com algum dos $$\,m_i\,$$desde que a assinatura $$\sigma\,$$ na prova de sucesso seja distinta de todas as assinaturas $$\,\sigma_i\,$$referidas no oráculo. Nestes casos as inunidades passam a ter a designação de “strong” e passamos a ter SUUF-naCMA e SEUF-naCMA para designar estas versões de segurança.


    1. A última versão do ataque, e do respetivo oráculo, considera um atacante com capacidade para escolher  adaptativamente as mensagens no oráculo e na prova de sucesso. Cada mensagem $$\,m_i\,$$ é gerada por um algoritmo de escolha que tem como “imputs”  todas as mensagens anteriormente geradas e as respetivas assinaturas. 
        Este ataque designa-se por “adaptative chosen-message attack” ou CMA.


        Num ataque UUF-CMA ou EUF-CMA existe, como no caso anterior, uma prova de sucesso $$\,(\sigma,m)\,$$ onde a mensagem $$\,m\,$$ coincida com algum $$\,m_i\,$$. Esta restrição pode igualmente ser relaxada considerando que só são repudiadas as provas $$\,(\sigma,m)\,$$ que coincidam com alguma das amostras do oráculo.
        
# Provas de segurança

Uma prova de segurança EUF-CMA para um esquema de assinaturas

                              $$\,\Sigma\;\equiv\;\langle\,\mathsf{KGen}\,,\,\mathsf{Sign}\,,\,\mathsf{Vrfy}\,\rangle\,$$

é uma algoritmo que resolve eficientemente um problema difícil 

                               $$\,\mathcal{P}\;\equiv\;\{x\;|\;\exists\,z\,\centerdot\,\mathcal{P}(x,z)\,\}$$

usando o “output” de um eventual  “forger” CMA desse esquema de assinaturas. 

Recorde-se que os elementos $$\,x\,$$ do conjunto $$\,\mathcal{P}\,$$ designam-se por **soluções** do problema, e os elementos $$\,z\,$$ tais que $$\,\mathcal{P}(x,z)\,$$ é válido designam-se por **testemunhas**  da solução $$\,x\,$$.

A prova de segurança EU-CMF é um algoritmo, genericamente designado como $$\,\mathbf{Adversary}$$ , que recebe como “input” um candidato a solução $$\,x\,$$ (o “desafio”) e decide se esse candidato é realmente uma solução, apresentando para isso  uma testemunha $$\,z\,$$; se $$\,x\,$$ não for solução o algoritmo falha.

$$\,\mathbf{Forger}\,$$ denota a classe de algoritmos  que recebem como “inputs” a chave pública $$\,\mathsf{pk}\,$$ e o limite superior $$\,Q\,$$ ao número de  consultas que podem realizar  ao oráculo $$\,\mathsf{Sign}\,$$; após essas consultas o algoritmo genérico dessa classe devolve um par $$\,(M',\sigma')\,$$ verificável com a chave pública $$\,\mathsf{pk}\,$$ ou então falha.

O princípio  que justifica esta prova pode ser sumariado da seguinte forma

> Se a classe $$\,\mathbf{Forger}\,$$ for não vazia, i.e. se existir alguma instância dessa classe, então o algoritmo $$\,\mathbf{}$$$$\,\mathbf{Adversary}(\mathcal{P})\,$$ pode usar essa instância  para construir eficientemente uma solução verificável do problema difícil  $$\,\mathcal{P}\,$$.

O seguinte esquema representa a estrutura genérica de uma tal prova de segurança mostrando a interação entre o $$\mathbf{Advsersary}\,$$e uma qualquer instância da classe  $$\mathbf{Forger}$$ está ilustrado na seguinte figura.  



![](https://paper-attachments.dropbox.com/s_19832A83A9AC9F5E5D42684FCCD78B838CCCE111FFA37515733DB383AE0114B2_1621950553344_eu-cma-proof-1.png)


Concretamente $$\,\mathbf{Adversary}(\mathcal{P})\,$$ é um esquema formado por três algoritmos: 

    - $$\mathsf{Commit}$$ 
        É um algoritmo probabilístico que,  partir do desafio $$\,x\,$$ e de um parâmetro de segurança $$\,\lambda\,$$,   gera aleatoriamente toda a informação necessária à construção e verificação de assinaturas  e cálculo da testemunha $$\,z\,$$ nos algoritmos seguintes. Nomeadamente $$\,\mathsf{Commit}\,$$ calcula e torna pública a chave pública $$\,\mathsf{pk}\,$$ de $$\,\Sigma\,$$ . 
        Os restantes items gerados formam  um estado $$\,\mathsf{St}\,$$ que é informação privada, partilhada apenas  com os outros dois algoritmos deste esquema.
    - $$\,\mathsf{Sign}\,$$
        É um algoritmo parcial determinístico que recebe como “input” a mensagem  $$\,M\,$$ e usa-a conjuntamente com  $$\,\mathsf{St}\,$$ para gerar, se puder, uma assinatura verificável $$\,\sigma\,$$. Se não for capaz de calcular essa assinatura, falha. Este resultado é público.
    - $$\mathsf{Solve}$$
        É um algoritmo determinístico que recebe como “input” um par verificável $$\,(M',\sigma')\,$$ou uma indicação de falha e, conjuntamente com $$\,\mathsf{St}\,$$ e se puder, calcula a testemunha $$\,z\,$$da solução $$\,x\,$$ ou então falha.

Qualquer instância da classe $$\,\mathbf{Forger}\,$$ é um esquema formado por dois algoritmos determinísticos: $$\,\mathsf{AdaptativeChoice}\,$$ e $$\,\mathsf{Reveal}\,$$. 
O estado partilhado por ambos  é formado por $$\,i\,$$, um contador de acessos disponíveis ao oráculo de assinaturas,  e um registo de todas as mensagens trocadas com $$\,\mathbf{Adversary}\,$$.

    - $$\mathsf{AdaptativeChoice}$$
        Em função do estado calcula uma mensagem $$\,M\,$$ e consulta $$\,\mathsf{Sign}\,$$ com ela.
    - $$\,\mathsf{Reveal}$$ 
        Em função do estado decide se é possível revelar a falsificação $$\,(M',\sigma')$$ como um par verificável que não ocorre previamente no estado. Se for possível comunica essa informação ao algoritmo $$\,\mathbf{Adversary}$$. Se não for possível e ainda tiver acessos disponíveis volta ao algoritmo anterior. Se já não tiver acessos disponíveis, falha.
    

Como exemplo de uma esquema de assinaturas digitais que possui uma prova de segurança EUF-CMA vamos estudar um esquema OTS (“one time signature”) que faz parte de um esquema candidato a “standartização” no concurso NIST-PQC: o SPHINCS$$\!+$$.

# Esquemas de *Assinatura Digital Única* (OTS)

“One Time Signatures” (OTS) são esquemas de assinatura digital  com pouca complexidade   algébrica e grande eficiência computacional. 

Quase todos os esquemas de assinaturas, têm alguma álgebra $$\,\mathcal{A}\,$$ em que se baseiam: os principais algoritmos  implementam operações básicas de $$\,\mathcal{A}\,$$, a correção deriva de propriedades algébricas de $$\,\mathcal{A}\,$$ e  a segurança reduz-se à  capacidade de resolver problemas  “hard”  em $$\,\mathcal{A}\,$$.

Ao invés as OTS’s baseiam-se em primitivas criptográficas básicas (funções de “hash” e cifras simétricas) e derivam a sua segurança da incapacidade em resolver alguns problemas considerados “hard” nessas primitivas; por exemplo nas funções de “hash”, a inversão ou a procura de colisões numa tal função.

Em contrapartida a ausência de uma estrutura rica em operadores e propriedades algébricas torna difícil construir os algoritmos de assinar uma mensagem e verificar uma assinatura. Parece óbvio que, se as únicas operações disponíveis são as funções de “hash”  e manipulação  elementar de bits e strings, então vai ser bastante complicado construir e verificar assinaturas a partir de um repertório tão limitado. Não só os algoritmos requerem um grande número de operações elementares como o tamanho dos dados que manipulam (e.g. chaves e assinaturas) é muito superior ao dos algoritmos algébricos.

A necessidade de limitar esta complexidade e produzir um esquema de assinaturas útil,  faz com que se use uma funcionalidade que relaxa algumas das restrições à funcionalidade de um esquema de assinaturas. Por exemplo, um DSS clássica exige que o mesmo par de chaves pública e privada $$\,(\mathsf{pk},\mathsf{sk})\,$$ possa produzir assinaturas para um número não-limitado de mensagens; pelo contrário, como o nome sugere, um par de chaves num “One Time Signature” pode ser usado apenas numa mensagem.

A utilidade de um OTS não é tão limitada como estas observações parecem sugerir. Isto porque, uma OTS pode ser associada a um esquema que permite organizar  número finito mas muito grande de pares de chaves. Os pares de chaves estão organizados em certas árvores binárias (as  **árvores de Merkle**) que permitem autenticar eficientemente um grande número de mensagens.

Os esquemas “hash-based” de assinatura digital candidatos ao concurso NIST-PQC seguem esta abordagem. Porém, nesta secção interessa-nos apenas a componente OTS, nomeadamente uma variante designada por ***Winterniz OTS***   ou WOTS.


## Esquemas WOTS

A abordagem de Winterniz à construção de um OTS baseia-se no conceito de  **iteração de funções de “hash”** ou genericamente de funções unidirecionais (“One Way” ou OW). 

O tamanho do “hash” $$\,n\,$$ (ou o tamanho da cardinalidade da função OW) é o principal parâmetro de segurança. Todos os esquemas OTS produzem assinaturas que são sequências de “outputs” de funções de “hash”. Iremos provar que as condições de “unforgeability” do esquema de assinaturas se reduz a propriedades standard de funções de “hash”: unidirecionalidade e resiltência a colisões . Dado que a segurança de um “hash” depende do  seu tamanho, as condições para “unforgeability” do esquema de assinaturas vão-se  exprimir nesse tamanho. 

**Funções OW iteradas**

Vamos representar por $$\,\mathcal{B}_n\,$$ o domínio $$\,\{0,1\}^n\,$$; como inteiros positivos este domínio pode também ser identificado com $$\,\mathbb{Z}_{2^n}\,$$ . De forma semelhante representamos por $$\,\mathcal{B}_\ast\,$$o domínio das “strings” finitas de bits $$\;\{0,1\}^\ast\;$$; a sua representação como inteiros é $$\,\mathbb{N}\,$$.

Vamos considerar uma qualquer função “one way”  $$\,\mathcal{H}\,\colon\,\mathcal{B}_\ast\,\to\,\mathcal{B}_n$$.  A partir desta função e para cada $$\,u\geq 0\,$$ pode-se definir de várias formas uma **família de funções OW iteradas**

                                          $$\mathcal{F}^u\;\equiv\;\{\,F_{z}^u\,\colon\, \mathcal{B}_\ast \,\to\, \mathcal{B}_n\,\}_{z\in \mathcal{Z}}$$

O  domínio $$\,\mathcal{Z}\,$$ dos **índices** $$\,z\,$$  vai depender da forma da família. Alguns exemplos


1. Toma-se $$\,\mathcal{Z} \equiv \mathcal{B}_n\,$$  e define-se
            $$F_z^u(x)\;\equiv\;\left\{\begin{array}{lcl} x &\quad& \text{se}\; u = 0 \\ \mathcal{H}(z\|x) && \text{se}\;u=1 \\ F_{z'}^{u-1}(x) && \text{se}\;u > 1\;\text{e}\;z'= F_z(x)\end{array}\right.$$
| A função $$\,(z,x)\,\mapsto\,\mathcal{H}(z\|x)\,$$, usada quando $$\,u=1\,$$, pode ser substituída por outra função OW<br>                                                      $$\,f\,\colon\,\mathcal{B}_n\times\mathcal{B}_\ast\,\to\,\mathcal{B}_n\,$$<br>    que assegura uma boa “mistura” dos argumentos. |

    Esta é o tipo de função iterada usada no **esquema WOTS**.
    
2. Toma-se $$\,\mathcal{Z}\,\equiv \,(\mathcal{B}_n)^m\,$$ para algum $$\,m > 0\,$$; as funções iteradas $$\,F_z^u\,$$ definem-se para $$\,0\leq u \leq m$$
                  $$F_z^u(x)\;\equiv\;\left\{\begin{array}{lcl} x &\quad& \text{se}\;u=0 \\ \mathcal{H}(F^{u-1}_z(x) \oplus z_{u-1}) && \text{se}\;0 < u \leq m \end{array}\right.$$


3. Substituindo, na definição anterior, a função $$\,\mathcal{H}\,$$ por uma família  $$\,\{\mathcal{H}_t\,\colon\,\mathcal{B}_\ast\,\to\,\mathcal{B}_n\,\}_{t\in\mathcal{T}}$$ indexada por uma “tweak” $$\,t\,$$ , obtém-se uma família indexada por dois índices
                $$F_{t,z}^u(x)\;\equiv\;\left\{\begin{array}{lcl} x &\quad& \text{se}\;u=0 \\ \mathcal{H}_t(F^{u-1}_{t,z}(x) \oplus z_{u-1}) && \text{se}\;0 < u \leq m \end{array}\right.$$

   
   Esta é a construção usada no **esquema  WOTS**$$+$$ .

**Lei de semi-grupo**

A única propriedade algébrica que pode ser inferida das funções OW iteradas é a que resulta da ordem de composição de funções. Para cada uma das formas atrás descritas, é simples verificar a seguinte propriedade:

1. Nas funções do tipo WOTS tem-se, para todo $$\,z\in\mathcal{B}_n,$$  e todo $$\,x\,$$,

                       $$F^{u+\upsilon}_z(x) \;=\; F^u_{z'}(x)\quad$$com $$\quad z'=F_z^\upsilon(x)$$

2. Nas funções do tipo WOTS$$+$$  tem-se, para todo $$\,z\in\mathcal{B}_n^m$$,  todo $$\,x\,$$ e $$\,u+\upsilon \leq m$$
                 $$F^{u+\upsilon}_z(x) \;=\; F^u_{z'}(F^\upsilon_z(x))\quad$$com $$\quad z'= (z_\upsilon,\cdots,z_m)$$

**Representação das mensagens, chaves e assinaturas**

Para além das funções OW iteradas  $$\,F_z^u\,$$, o outro aspeto essencial dos OTS de Winterniz é a representação das mensagens $$\,M\in \mathcal{B}_\ast\,$$ de uma forma que seja consistente com  as ordens $$\,u\,$$ da iteração. 
Um esquema de Winterniz está sempre associado a um parâmetro inteiro $$\,w>1\,$$ designado por **base de Winterniz**. Uma vez escolhido $$\,w\,$$, 

        1. Cada mensagem $$\,M\,$$ é interpretada, em primeiro lugar, como um inteiros positivo (usando o isomorfismo $$\,\mathcal{B}_\ast\,\simeq\,\mathbb{N}$$ ) e esse inteiro é representado na base $$\,w\,$$ por uma sequência de $$\,d\,$$ dígitos
                                                 $$\,m'\;\equiv\;(m_0,m_1,\cdots\,,m_{d-1})$$
            com $$\,0\leq m_i < w\,$$ e $$\,d = \lceil\,\log_w M\,\rceil$$
        2. É calculado um “checksum”  
                                              $$\;C\;\equiv\;\sum_{i=0}^{d-1}\,(w  - 1 - m_i)\,$$
            Esse inteiro positivo é também representado por uma sequência de $$\,\ell - d\,$$  dígitos 
            na base $$\,w\,$$;     
                                                 $$c\;\equiv\,(m_d\,,\,m_{d+1}\,,\,\cdots\,,m_{\ell-1})$$
            O limite superior ao valor de $$\,C\,$$ é $$\,d\,(w-1)\;$$ ; por isso ,     $$\ell - d\,\leq\, 1 + \lceil\,\log_w d\,\rceil$$ .
        3. Constrói-se a concatenação das duas sequências  de dígitos  $$\,m' \,\|\,c\,$$  e forma-se 
                                       $$\,m\;\equiv\;(m_0\,,\,\cdots\,,\,m_{d-1}\,,\,m_d\,,\,\cdots\,,\,m_{\ell-1})$$
              que define a descrição completa da mensagem $$\,M\,$$ e do seu “checksum”.

Desta forma as mensagens são codificadas em vetores de $$\,\ell\,$$ inteiros $$\,0\leq m_i < w\,$$. 
Como veremos em seguida, a chave privada e a assinatura são vetores de $$\,\ell\,$$ elementos de $$\,\mathcal{B}_n\,$$ enquanto que a chave pública é um vetor de $$\,\ell+1\,$$ elementos de $$\,\mathcal{B}_n$$. Em resumo
                          $$\,m \in \mathbb{Z}_w^\ell \quad,\quad \mathbf{sk}\in \mathcal{B}_n^\ell\quad,\quad \mathbf{pk}\in \mathcal{B}_n\times\mathcal{B}_n^\ell\quad,\quad \sigma\in\mathcal{B}_n^\ell$$

**Geração de Chaves**

Vamos considerar o esquema de assinaturas WOTS , como exemplo, mas a totalidade da análise aplica-se, com poucas modificações no algoritmo de verificação, para o esquema WOTS+.

Os parâmetros principais dos esquemas WOTS são  $$\,n,w,d,\ell\,$$ e a  família de funções OW iteradas  $$\,\{F_z^u\}\,$$ .


1. A chave privada é um vetor $$\,\mathsf{sk}\,\equiv\,(sk_0\,,\,sk_1\,,\,\cdots\,,\,sk_{\ell-1})\,$$ em que os $$\,sk_i\gets \mathcal{B}_n\,$$ são aleatoriamente gerados.
2. A chave pública $$\,\mathsf{pk}\,\equiv\,(x\,,\,pk_0\,,\,\cdots\,,\,pk_{\ell-1})\,$$ é um vetor em que $$\,x\gets \mathcal{B}_n\,$$ é aleatoriamente gerado e, para todo $$\,0\leq i < \ell\,$$, determina-se

                                                          $$pk_i\,\gets\,F_{sk_i}^{w-1}(x)\,$$

**Assinatura:**    $$\,\mathsf{Sign}(\mathsf{sk},M)$$

Dada a mensagem $$\,0\leq M < w^d\,$$, seja $$\,m\in \mathbb{Z}_w^\ell\,$$ a sua codificação como atrás descrita. A sua assinatura é o vetor $$\,\mathbf{\sigma}\,\equiv\,(\sigma_0\,,\,\cdots\,,\,\sigma_{\ell-1})\,$$ em que, para todo $$\,0\leq i < \ell$$,

                                             $$\sigma_i\,\gets\,F_{sk_i}^{m_i}(x)\,$$


**Verificação:** $$\,\mathsf{Vfy}(\mathsf{pk},M,\mathbf{\sigma})$$

Obtém-se $$\,m\in \mathbb{Z}_w^\ell\,$$, a codificação da mensagem $$\,M\,$$. Da chave pública $$\,\mathsf{pk}\,$$ obtém-se $$\,x\,$$ e os elementos $$\,pk_i\,$$. Aceita-se a assinatura $$\,\sigma\,$$ se e só se, para todo $$\,0\leq i < \ell\,$$, se verifica

                                               $$\,F_{\sigma_i}^{w-1-m_i}(x)\,=\,pk_i$$
| O algoritmo de verificação pode ser interpretado como um mecanismo para reconstruir a chave pública $$\,\mathsf{pk}\,$$ a partir de  uma par $$\,(M,\sigma)\,$$ que, á partida, se sabe que é verificável. Por isso, em esquemas que geram assinaturas múltiplas e têm de gerir essas assinaturas, não é necesásrio armazenar a chave pública que é usada para verificar cada assinatura: basta armazenar as assinaturas. |


**Correção**
 
Se $$\,\sigma_i = F_{s_i}^{m_i}(x)\,$$ foi calculado corretamente, então pela lei do semi-grupo tem-se
                                 $$\,F_{\sigma_i}^{w-1-m_i}(x) \,=\, F_{s_i}^{w-1-m_i+m_i}(x)\,=\,F_{s_i}^{w-1}(x)\,=\,pk_i$$
                                 


## Segurança dos esquema WOTS

Mais uma vez vamos considerar o esquema WOTS mas esta análise aplica-se com poucas modificações ao esquema WOTS+.

Antes de apresentar uma prova de segurança convém especificar qual é o problema “difícil” na qual essa prova se baseia.  Dois desses problemas serão


> Dada a família de funções iteradas OW  $$\,F_z^u \colon \mathcal{B}_\ast \to \mathcal{B}_n\,$$usada no esquema WOTS define-se
>         $$\mathcal{P}_1\;\equiv\,\{(x,y)\,|\,\exists\,z\,\centerdot\,y = F_z(x)\,\}\quad$$      e       $$\mathcal{P}_2\;\equiv\,\{(z,y)\,|\,\exists\,x\,\centerdot\,y = F_z(x)\,\}$$

No 1º problema o “desafio”  são pares $$\,(x,y)\in\mathcal{B}_n\times\mathcal{B}_n\,$$ e o “certificado”  são palavras $$\,z\in\mathcal{B}_n\,$$.  No 2º problema comuta-se o papel de $$\,x\,$$ e $$\,z\,$$:  o desafio são pares $$\,(z,y)\,$$ e o certificado  é $$\,x\,$$.

Se  $$\,F_z(x)\,$$ for definida a partir da função de “hash” $$\,\mathcal{H}\,$$ como  $$\,\mathcal{H}(z\,\|\,x)\,$$ , então a complexidade do cálculo  de $$\,z\,$$ tal que $$\,y = F_z(x)\,$$ é limitada superiormente por $$\,2^n\,$$ (a cardinalidade do espaço de procura) mas também é condicionado pelas propriedades de segurança do  “hash” $$\,\mathcal{H}\,$$.  
Porém no problema $$\,\mathcal{P}_2\,$$, a testemunha $$\,x\,$$ não tem um espaço de procura finito; por isso, em princípo, $$\,(z,y)\in \mathcal{P}_2\,$$ pode não  ser decidível.

Num ataque  1EUF-CMA  ao esquema de assinaturas WOTS o atacante escolhe uma mensagem $$\,M\,$$ e obtém um par verificável $$\,(M,\sigma)\,$$ por consulta ao oráculo $$\,\mathsf{Sign}\,$$. Pode-se pensar na viabilidade de um ataque em que o atacante  propõe uma nova mensagem $$\,M'\,$$,  distinta mas “próxima” de $$\,M\,$$, e apresenta uma assinatura $$\,\sigma'\,$$ , válida para $$\,M'\,$$, sem consultar o oráculo.

Por exemplo pode-se considerar o caso em que os dígitos $$\,(m_0,\cdots\,m_{d-1})\,$$ , que representam $$\,M\,$$, coincidem com todos os dígitos $$\,(m'_0,\cdots,m'_{d-1})\,$$, que representam $$\,M'\,$$, excepto em um índice $$\alpha < d\,$$ onde diferem de uma unidade

                Para  $$\,i < d\,$$ escolhe-se  $$m'_i = m_i$$  , se $$\,i\neq \alpha\;$$,  e escolhe-se  $$\,m'_\alpha = m_\alpha + 1\,$$

O “checksum”  $$\,C = \sum_{i<d}\,(w-1-m_i)\,$$ difere do “checksum” $$\,C' = \sum_{i<d}\,(w-1-m'_i)\,$$ em uma unidade  mas em sentido contrário:  $$\,C' = C - 1\,$$. Por isso existe pelo menos um índice $$\,\beta \geq d\,$$ onde $$\,m_\beta = m'_\beta + 1\,$$. 
Para calcular uma assinatura verificável $$\,\sigma'\,$$ o atacante, usando $$\,x\,$$ que consta da chave pública, 

        1. Faz        $$\,\sigma'_i \gets \sigma_i\,$$  se $$i\neq \alpha\,$$ e $$\,i\neq \beta\,$$
        2. Calcula $$\,\sigma'_\alpha \,\gets\,F_{\sigma_\alpha}(x)\,$$
        3. Resolve, em ordem a $$\,z\,$$ ,  a equação $$\,$$ $$\,F_z(x) \,=\,\sigma_\beta\,$$;  o valor de $$\,\sigma'_\beta\,$$ é uma qualquer solução desta equação.

En quanto as duas primeiras tarefas  são simples de realizar, a última exige que se seja verificado $$\,(x,\sigma_\beta) \in \mathcal{P}_1\,$$. A complexidade deste problema torna inviável um tal ataque.

Este resultado não prova a segurança do esquema: apenas prova que este ataque em particular não produz resultados. Para provar segurança temos de considerar um”forre arbitrário e reduzir a um problema difícil à existência desse ataque. 
Considere-se a forma geral do protocolo $$\,\mathbf{Adversary}$$ vs. $$\mathbf{Forger}\,$$ apresentado no início desta seção que aqui se reproduz


![](https://paper-attachments.dropbox.com/s_19832A83A9AC9F5E5D42684FCCD78B838CCCE111FFA37515733DB383AE0114B2_1621950612327_eu-cma-proof1.png)


Neste modelo genérico, a prova de segurança do WOTS é instanciada da seguinte forma:


1. O número máximo $$\,Q\,$$ de consultas ao oráculo $$$$$$\,\mathsf{Sign}\,$$ é $$1$$. Portanto logo que uma das operações falhe todo o protocolo falha.
2. O problema “difícil” $$\,\mathcal{P}\,$$ é o problema $$\,\mathcal{P}_1\,$$atrás especificado. Portanto o “desafio” ao adversário é um par $$\,(x,y)\,$$ e o certificado $$\,z\,$$, produzido por esse adversário, é o índice da função OW iterada $$\,F_z\,$$ que verifica $$\,y = F_z(x)\,$$.

A partir dos parâmetros WOTS, $$\,n\,,\,w\,,\,\ell\,,\,d\,$$,  os algoritmos do adversário são

$$\mathsf{Commit}(x,y)$$

        1. Gera uma chave privads  $$\,\mathsf{sk} = (sk_0\,,\,\cdots\,,\,sk_{\ell-1})\,\gets\,\mathcal{B}_n^\ell\;$$  e  o parâmetro $$\,x\gets \mathcal{B}_n\,$$
        2. Gera aleatoriamente um índice $$\,\alpha\gets\mathbb{Z}_\ell\,$$ e um dígito $$\,r \gets \{1,\cdots,w-1\}$$.
        3. Calcula uma chave pública $$\,\mathsf{pk}\,=\,(x\,,\,pk_0\,,\,\cdots\,,\,pk_{\ell-1})\,$$ em que 
            1.     $${pk}_\alpha \gets F_y^{w-1-r}(x)\quad$$ , e
            2. $$\quad {pk}_i\,\gets\,F_{sk_i}^{w-1}(x)\quad$$para todo $$\,i\neq\alpha$$
                
        A chave pública $$\,\mathsf{pk}\,$$ é passada ao $$\,\mathbf{Forger}\,$$ e o estado $$\,\mathsf{St}\,\equiv\,(\mathsf{sk}\,,\,\alpha\,,\,r)\,$$é passado aos algoritmos $$\,\mathsf{Sign}\;$$e $$\;\mathsf{Solve}\,$$.

$$\mathsf{Sign}(\mathsf{St},M)$$

        1. Calcula a codificação $$\,m \,=\,(m_0,\cdots,m_{\ell-1})\,$$ da mensagem $$\,M\,$$ . 
        2.  Se  $$\,m_\alpha < r\,$$   termina em $$\,\mathtt{falha}\,$$; se não,  calcula $$\,\sigma_\alpha \gets F^{m_\alpha-r}_y(x)$$ 
        3. Calcula  $$\,\sigma_i \gets F_{sk_i}^{m_i}(x)\,$$  para todo $$\,i\neq \alpha$$.  
    
        Envia a assinatura  $$\,\sigma = (\sigma_0,\cdots,\sigma_{\ell-1})\,$$ ao   $$\mathbf{Forger}$$. 

$$\mathsf{Solve}(\mathsf{St},M',\sigma')$$

        1. Calcula a codificação $$\,m'\;=\,(m'_0,\cdots,m'_{\ell-1})\,$$ da mensagem $$\,M'\,$$.  
        2.  Se  $$\,m'_\alpha \geq r\,$$ termina em $$\,\mathtt{falha}\,$$;  se não calcula $$\,z\,\gets\,F^{r-1-m'_\alpha}_{\sigma'_\alpha}(x)\,$$ 
        3. Se $$\,y\neq F_z(x)\,$$ termina em $$\mathtt{falha}\,$$;  se não, devolve $$\,z\,$$ como resultado.


Para demonstrar que $$\,\mathsf{Adversary}(x,y)\,$$ é uma prova de segurança 1EUF-CMA para o WOTS temos de provar os seguintes resultados.

**Proposição 1**

> Se $$\;\sigma \,\gets\,\mathsf{Sign}(\mathsf{St},M)\;$$ termina corretamente, então o par $$\,(M,\sigma)\,$$ é verificável.

**Proposição 2**

> Se $$\;(M',\sigma')\;$$ é verificável e   $$\;z\,\gets\,\mathsf{Solve}(\mathsf{St},M',\sigma')\;$$ termina corretamente, então 
>                                                          $$\,y\,=\,F_z(x)\,$$

**Confirmação**
Para ambas proposições basta verificar o que ocorre no índice $$\,\alpha\,$$, dado que para $$\,i\neq\alpha\,$$ a chave pública e a assinatura são geradas de forma “standard”.

Na proposição 1, temos de calcular $$\,F_{\sigma_\alpha}^{w-1-m_\alpha}(x)\,$$ , atendendo que $$\,\sigma_\alpha = F^{m_\alpha-r}_y(x)\;$$, e comparar esse valor com $$\,pk_\alpha = F^{w-1-r}_y(x)\,$$. De facto, pela lei do semi-grupo, 
                               $$F_{\sigma_\alpha}^{w-1-m_\alpha}(x)\;=\;F_y^{w-1-m_\alpha + m_\alpha - r}(x)\;=\;pk_\alpha$$
                               
Na proposição 2, temos de testar a validade de  $$\,y\,=\,F_z(x)\;$$atendendo que $$\,z \,\equiv\,F_{\sigma'_\alpha}^{r-1-m'_\alpha}(x)\;$$, que $$\,\,pk_\alpha\,\equiv\, F_y^{w-1-r}(x)\;$$ e que, sendo   $$\,(M',\sigma')\,$$ verificável,  se tem $$\,pk_\alpha = F_{\sigma'_\alpha}^{w-1-m'_\alpha}\,$$.

Define-se  um valor $$\,y' \equiv F_z(x)\,$$ e calcula-se uma nova chave pública  usando $$\,y'\,$$ em vez de $$y$$
                                                           $$\,pk'_\alpha \,\equiv\,F_{y'}^{w-1-r}(x)$$
Aplicando a lei do semi-grupo às definições de $$\,z\,$$    e $$\,y'\,$$ tem-se     $$y'\,=\,F_{\sigma'_\alpha}^{r-m'_\alpha}(x)\,$$.  Aplicando a mesma lei a esta iguadade e à definição de $$\,pk'_\alpha\,$$ obtém-se
                                   $$pk'_\alpha = F_{y'}^{w-1-r}(x)\,=\,F_{\sigma'_\alpha}^{w-1-r+r-m'_\alpha}\,$$ $$\;=\; F_{\sigma'_\alpha}^{w-1-m'_\alpha}\,=\,pk_\alpha$$
                    
Portanto a chave pública $$\,pk'_\alpha\,$$  , calculada  a partir de  $$\,y'\,$$ ,  coincide com a chave pública $$\,pk_\alpha\,$$ calculada a partir de $$\,y\,$$. Isto significa que, para efeitos do protocolo, os valores de $$\,y\,$$ e de $$\,y'\,$$ são intermutáveis. Não significa, porém, que os dois valores $$\,y\,$$ e $$\,y'\,$$  tenham de ser iguais.

De facto , fixando os valores de $$\,w,r,x\,$$, pode-se  definir uma função de “hash” que representa a geração da chave pública na posição  $$\,\alpha\,$$ a partir de um $$\,y\,$$ arbitrário

                                            $$G\,\colon\,\,y \,\mapsto\,F_y^{w-1-r}(x)\,$$  

O que acabámos de provar é que, dado qualquer $$\,y\,$$ que ocorra no desafio , consigo calcular $$\,y' \,\gets\, F_z(x)\,$$  tal que   $$\,G(y)\,=\,G(y')\,$$.  Portanto , temos duas hipóteses

    1. Tem-se  $$\,y=y'\,$$  e, nesse caso, conseguimos construir uma solução de problema $$\,\mathcal{P}_1\,$$; isto é calculámos $$\,z\,$$ tal que $$\,F_z(x) = y\,$$,  ou então
    2. Tem-se $$\,y\neq y'\,$$ e, nesse caso , construímos uma colisão para a função de “hash”  $$\,G\,$$ .

Em qualquer dos casos constrói-se uma solução de um problema difícil.

