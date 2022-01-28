# Capítulo 10:  Esquemas de Assinatura Digital  “PQC-High-Algebra”.


## Referências úteis

[CRYSTALS](https://pq-crystals.org). esquemas da família LWE:   assinaturas [Dilithium](https://www.dropbox.com/sh/p3axecn23v650rs/AADrftMrxTeZFuDw0SrgRRo9a?dl=0) e KEM Kyber.
[qTESLA](https://www.dropbox.com/sh/2vr43y9dk7mf08e/AABeUWtwI7h4Ix9_D-ervJvJa?dl=0). [esquema de assinatura digital](https://qtesla.org) LWE
[PICNIC](https://www.dropbox.com/sh/tjjc5bcoor2z4qw/AAAj9vMhTIjjRMW7dtdzjDWIa?dl=0). [esquema de assinatura digital derivado de provas de conhecimento zero](https://microsoft.github.io/Picnic/)
[SPHINCS+](https://www.dropbox.com/sh/0udnx9r3hx46jf6/AABy-9ciwzsVIU97n2_ideUBa?dl=0). [esquema de assinatura digital derivado de funções de hash.](https://sphincs.org)


# Provas de Conhecimento

Na [+Sessão 1](https://paper.dropbox.com/doc/Sessao-1-hLb9hJVPeGF0t3mmHe1A9)  falámos de **provas verificáveis de conhecimento** e como esta noção conduz os a **esquemas de assinatura digital**. Vamos aqui recordar rapidamente as noções aí referidas e adapta-las não só a formalização de dos esquemas de assinatura mas também à definição da sua segurança.

O ponto de partida foi a identificação

                        *conhecimento* $$\;\equiv\;$$ *solução para um problema* 

e a de *prova de conhecimento* com um *mecanismo de confirmação*  que decide se um eventual candidato a solução resolve realmente o problema.

Recorde-se que um problema se identifica com o conjunto das suas soluções. Um problema da classe NP é definido por um conjunto

                                   $$\mathcal{L}\;\equiv\;\{\,x\;|\; \exists\,w\,\centerdot\,D(x,w)\}$$
                                

A string $$\,w\,$$ que verifica $$\,D(x,w)\,$$ é o **certificado** da solução $$\,x\,$$ e o seu  comprimento $$\,|w|\,$$ é limitado polinomialmente com $$\,|x|\,$$;  a **decisão de confirmação** $$\,D(x,w)\,$$tem complexidade polinomial com o tamanho $$\,|(x,w)|\,$$.


----------
> No contexto das provas de conhecimento, a solução (ou candidato a solução) $$\,x\,$$ é visto como **informação pública** ,  enquanto que o certificado $$\,w\,$$ é visto como **informação privada**.

Um **protocolo de** **prova não-interativa de conhecimento verificável**  para um parâmetro de segurança $$\,\lambda\,$$, é definido por um par de algoritmos, um **prover** e um **verifyer,**  $$\,$$$$\;\langle\,\mathcal{P}\,,\,\mathcal{V}\,\rangle$$ tais que:


    - O **prover**  $$\;\mathcal{P}\;$$ é um **** algoritmo não determinístico da forma 
                       $$\mathcal{P}(x,w)\;\equiv\; \vartheta\,c \gets \mathcal{C}\,\centerdot\,\mathcal{S}(x,w,c)$$
        em que o núcleo  $$\;\mathcal{S}\;$$ tem complexidade polinomial com o tamanho do  input.
    
        - A fonte de aleatoriedade $$\,c\,$$ é o **desafio** (*challenge*) ; o domínio $$\,\mathcal{C}\,$$ designa-se por “*challenge space*"   e o seu **tamanho** é  $$\,\lambda\,\equiv\,\lceil \log_2 (\#\mathcal{C})\rceil$$. Sem perda de generalidade pode-se considerar sempre  $$\,\mathcal{C}\,\equiv\,\{0,1\}^\lambda\,$$.


        - O “output”  $$\,\pi \,\gets\,\mathcal{P}(x,w)\,$$  é a **prova**  de conhecimento para o par $$\,(x,w)\,$$


    - O **verifyer**  $$\;\mathcal{V}\;$$ é uma decisão determinística.  $$\,\mathcal{V}(x,\pi)\,$$,  de complexidade polinomial com o tamanho do seu input, e que é **completo:**  para todo $$\,(x,w)\,$$, se $$\; D(x,w)\;$$sucede então verifica-se
                                                 $$\mathbb{P}[\,\vartheta\,\pi \,\gets\,\mathcal{P}(x,w)\,\centerdot\,\mathcal{V}(x,\pi)\,]\;\simeq\;1$$.


| A probabilidade <br><br>                                                       $$\mathbb{P}[\,\vartheta\,\pi \,\gets\,\mathcal{P}(x,w)\,\centerdot\,\mathcal{V}(x,\pi)\,]$$<br><br>é sumariamente representada por<br>                                                                       $$\mathbb{P}[\,\langle\mathcal{P}(x,w)\,,\,\mathcal{V}(x)\rangle\,]$$ |

----------
## Fiabilidade

Se um agente submete $$\,\pi\,$$, como eventual prova de conhecimento, e se $$\,\mathcal{V}(x,\pi)\,$$ falha, então o facto de o protocolo ser completo assegura que esse agente não conhece o segredo $$\,w\,$$;  $$\,\pi\,$$ não é uma prova de conhecimento.

Porém pode acontecer que o agente, mesmo sem conhecer $$\,w\,$$, possa submeter várias propostas de provas $$\,\pi_1,\cdots\,\pi_\kappa\,$$ e em todas elas a decisão  $$\,\mathcal{V}(x,\pi_i)\,$$ tem sucesso. Esses $$\,\pi_i$$’s são designados por **falsos positivos**.
A **fiabilidade** do protocolo afirma que, se $$\kappa$$ for suficientemente longo, a probabilidade de se gerar uma sequência de falsos positivos e comprimento $$\,\kappa\,$$é negligenciáveis com $$\lambda$$ e $$\,\kappa\,$$.

Formalmente, o protocolo é **fiável**  quando, se um agente consegue construir um gerador $$\,\mathcal{G}\,$$ de falsos positivos, isto é um gerador que verifique
                                                    $$\mathbb{P}[\,\vartheta\,\pi \,\gets\,\mathcal{G}\,\centerdot\,\mathcal{V}(x,\pi)\,]\;\simeq\;1\;$$, 
então esse agente também consegue computar $$\,w\,$$  tal que $$\; D(x,w)\;$$  sucede. 


----------
## Conhecimento Zero

Adicionalmente o protocolo deve ser de **#conhecimento-zero.** Isto é um agente que conhece $$\,x\,$$, conhece um desafio $$\,c\,$$ , e que constrói um oráculo que usa estes parâmetros para construir provas verificáveis ,  não consegue obter o resultado de qualquer decisão que não conseguisse também obter sem conhecer o oráculo.

Para formalizar esta ideia defina-se, para quaisquer  $$\,x,c,r\geq 0\,$$,  o oráculo
                          $$\,\mathcal{O}(x,c,r)\;\equiv\; \vartheta\,w\gets B_r \,\centerdot\,\vartheta\,\pi\gets \mathcal{S}(x,w,c)\,\centerdot\,\pi\;\,\mathsf{if}\;\,\mathcal{V}(x,\pi)\,\;\mathsf{else}\;\,\bot$$
sendo $$\,B_r \equiv\,\{w\,|\,|w|\leq r\}\;$$.

| O oráculo $$\,\mathcal{O}(x,c,r)\,$$ começa por gerar aletoriamente um “candidato a testemunha” $$\,w\,$$ de tamanho  limitado a $$\,r\,$$; calcula em seguida uma prova $$\,\pi\,$$ como se $$w$$ fosse realmente um certificado para $$x$$ e finalmente testa se $$\,\pi\,$$ é uma prova real; se for gera $$\,\pi\,$$ como “output”; senão, falha. |


O protocolo será de conhecimento zero se, para todo $$x,c\,$$ e para $$\,r  = \text{poly}(|x|)\,$$, o oráculo $$\,\mathcal{O}(x,c,r)\,$$é $$K$$-trivial.

Em alternativa pode-se colocar uma condição mais fraca que é uma consequência da anterior. Diz-se que o protocolo é de conhecimento zero quando é possível construir um algoritmo PPT, um **simulador**   $$\,\text{Sim}(x,c)\,$$ , computacionalmente indistinguível de $$\,\mathcal{O}(x,c,r)\,$$ para todo $$\,x,c\,$$e $$r$$ suficientemente grande.


----------
## Provas com comprometimento.

A maioria dos protocolos de prova verificável de conhecimento envolve, na definição do “prover”  $$\,\mathcal{P}\,$$, o uso de um esquema de comprometimento. Recorde-se que

| Um **esquema de comprometimento** de um segredo $$\,s\,$$é formado por:<br><br>    - um algoritmo probabilístico  $$\,\text{Com}(s)$$ que produz um par $$(a , d)$$, commit-disclose; o “commit” $$\,a\,$$ é público e o “disclose”  $$\,d\,$$ é privado.<br>    - um algoritmo deterministico $$\,\text{Open}(a , d)\,$$  que “abre” o commit e reproduz o segredo $$\,s\,$$<br><br>O esquema é *correcto* quando, para todo $$s\,$$,<br>                                       $$\,\mathbb{P}[\,\vartheta (a , d) \gets \text{Com}(s) \;\centerdot\; \text{Open}(a , d)= s\,] \simeq 1$$.<br><br>O esquema *esconde*  $$\,s\,$$ (“hides”) quando, para todos $$\,s\neq s'\,$$, os geradores $$\;\text{Com}(s)\;$$ e $$\;\text{Com}(s')\;$$  são computacionalmente indistinguíveis; isto é, para toda a decisão $$\,D\,$$ “eficiente” verifica-se<br>                                    $$\,\mathbb{P}[\vartheta\,x\, \gets\, \text{Com}(s)\,\centerdot\, D(x)] \;\simeq\; \mathbb{P}[\vartheta\, y \,\gets\, \text{Com}(s')\,\centerdot\, D(y)]$$<br><br>O esquema *compromete*  $$\,a\,$$ (“bindes”) se não fôr possível  encontrar $$\,d,d'$$ tais que $$\text{Open}(a, d)\,$$ e $$\,\text{Open}(a, d')$$ terminam ambos com sucesso mas com resultados distintos.<br>Add a note |


Neste caso o “prover”  $$\,\mathcal{P}(x,w)\;\equiv\;\vartheta\,c\gets \mathcal{C}\,\centerdot\,\mathcal{S}(x,w,c)\;$$ decompõe  $$\,\mathcal{S}\,$$ em dois algoritmos: 


    - um “commit” do segredo $$\text{Com}(x,w)$$, que produz um par “commit-disclose”  $$\,(a,d)\,$$: o elemento $$\,a\,$$é público e $$\,d\,$$é uma chave privada usada no algoritmo seguinte,
    
    - um resposta   $$\,\mathcal{R}(d,c)\;$$que usa $$\,d\,$$ com chave privada, o desafio $$\,e\,$$ como argumento e gera a “resposta”  pública $$\,r\,$$. $$\,$$
    

 A  prova é o triplo das entidades públicas  $$\,\pi \,\equiv\,(a,e,r)\,$$

O núcleo $$\,\mathcal{S}\,$$ formado pela decomposição “commit-reply”  será então

                          $$\,\mathcal{S}(x,w,e)\;\equiv\; \vartheta\,(a,d)\gets \text{Com}(x,w)\,\centerdot\,\vartheta\,r\gets \mathcal{R}(d,e)\,\centerdot\,(a,e,r)$$
                                   
  e, globalmente, um “prover”    será                            
                                  

               $$\mathcal{P}(x,w) \;\equiv\;\vartheta\,(a,d)\,\gets\,\text{Com}(x,w)\,\centerdot\,\vartheta\,e \gets \mathcal{C}\,\centerdot\,\vartheta\,r \,\gets\,\mathcal{R}(d,e)\,\centerdot\, (a,e,r)\;$$
----------
![$$\Sigma$$-protocolo](https://paper-attachments.dropbox.com/s_9A989A297B238753AFAAB98CCB2A401E7EE4686D96206283F58F57C226439ECE_1621929607499_sigma-protocol.png)

----------
## Esquemas de assinatura digital e sigma-protocolos

Quando o protocolo $$\;\langle\mathcal{P},\mathcal{V}\rangle\,$$ é completo, fiável e de conhecimento zero esta construção produz dois tipos de protocolos criptográficos seguros:


1. Um **esquema de assinaturas Fiat-Shamir** $$\;\langle\text{KeyGen},\text{Sign},\text{Verify}\rangle\;$$em que


    1. $$\,\text{KeyGen}(\lambda)\,$$ 
        estabelece o tamanho do desafio e o  problema difícil do qual conhece uma solução $$\,x\,$$, a chave pública, e uma testemunha $$\,w\,$$, a chave privada.
        
    2. $$\text{Sign}(x,w,m)\,$$ , em que $$\,m\,$$ é a mensagem a assinar, é definido como
                     $$\text{Sign}(x,w,m)\;\equiv\;\vartheta\, c\gets\mathcal{H}(m)\,\centerdot\,\mathcal{S}(x,w,c)$$
        sendo $$\,\mathcal{H}\,$$ um “hash” aleatório de tamanho $$\,\lambda\,$$. 
        
        A assinatura é o triplo $$\,\pi \equiv (a,c,r)\,$$ das entidades públicas geradas por $$\,\mathcal{S}\,$$; neste esquema de assinaturas a própria assinatura carrega o “hash” da mensagem.
        
    3. $$\text{Verify}(x,\pi,m)\,$$ é construída como
                    $$\text{Verify}(x,\pi,m)\;\equiv\;\mathsf{if}\; c = \mathcal{H}(m)\;\mathsf{then}\;\mathcal{V}(x,\pi)\;\mathsf{else}\;\mathtt{falha}$$


2. Um **sigma-protocolo** formado  pelo agente “Prover”  $$\langle\text{Com},\mathcal{R}\rangle\,$$, um “Challenger” definido por um gerador aleatório no domínio $$\,\mathcal{C}\,$$ e um “Verifyer” $$\,\mathcal{V}$$.

  
      O gerador $$\,\mathcal{P}\,$$ acima fornece as provas “honestas” deste protocolo.

        


----------
## Repetições

É relativamente simples construir um problema $$\,\mathcal{L}\,$$ do qual resulte um protocolo de provas de conhecimento que seja completo. O mesmo não se pode afirmar em relação às propriedades restantes: é muito difícil definir um problema e um protocolo que seja simultaneamente fiável e de conhecimento zero.

Na maioria das provas de conhecimento onde se coloca a ênfase no “conhecimento zero”,  a probabilidade de surgirem falsos positivos é um valor $$\,\eta < 1\,$$   que não é negligenciável .

A solução para esta questão passa pela repetição, um número $$\,\kappa\,$$ de vezes, do “prover” $$\,\mathcal{P}(x,w)$$.

Para um qualquer gerador $$\,\mathcal{G}\,$$ representamos por $$\,\mathcal{G}^\kappa\,$$ o gerador que repete $$\,\kappa\,$$ vezes  $$\,\mathcal{G}\,$$ e recolhe todos os valores gerados.  Formalmente tem-se

                                         $$\mathcal{G}^\kappa\;\equiv\;\vartheta\,x_1 \gets \mathcal{G}\,\centerdot\,\cdots\,\centerdot\,\vartheta\,x_\kappa\gets \mathcal{G},\centerdot\;\,x_1\|\,\cdots\,\|x_\kappa$$

Aplicando esta construção ao “prover”  $$\,\mathcal{P}(x,w)\,$$ obtém-se uma prova
                                                              $$\pi\;\equiv\; \pi_1\|\cdots\|\pi_\kappa \;\gets\; \mathcal{P}(x,w)^\kappa$$
A verificação de $$(x,\pi)$$  é a decisão
                                                  $$\mathcal{V}^\kappa(x,\pi) \;\equiv\; \bigwedge_{i=1}^\kappa\, \mathcal{V}(x,\pi_i)$$
Nestas circunstâncias a probabilidade de existir um falso positivo baixa para $$\,\eta^\kappa\,$$  mas, em contrapartida, o tamanho da prova aumenta $$\,\kappa\,$$ vezes.


----------
## Provas com rejeição

Lyubasheshevky introduziu a noção de [“proofs with aborts”](https://www.dropbox.com/s/6gt0v7s732c4ab4/Lyubashevsky.pdf?dl=0)  em que se explora a possibilidade de um gerador falhar (tal como  o oráculo $$\,\mathcal{O}(x,c,r)\,$$ em #conhecimento-zero) para construir sigma-protocolos e esquemas de assinatura de uma forma particularmente eficiente.

Considere-se, como exemplo, um sigma protocolo numa construção semelhante ao esquema Diffie-Hellman mas construído sobre os inteiros $$\,\mathbb{Z}\,$$ em vez do usual corpo finito primo $$\,\mathbb{F}_p$$.

**Problema**
Como parâmetros são escolhidos domínios finitos de inteiros $$D_s,D_c,D_y,D_z\subset \mathbb{Z}$$; são também escolhidos  dois inteiros $$N,g$$.
O problema NP é definido pela linguagem

                              $$\,\mathcal{L}\;\equiv\;\{x\,|\,\exists\,w\in D_s\,\centerdot\, x \equiv g^w\bmod N\}$$.

**KeyGen**
A chave privada é   $$\,s\gets D_s\,$$ e a chave pública é  um inteiro $$S$$ que verifica  $$\,S\equiv g^s\bmod N$$.

**Commit**  
$$\qquad\text{Com}(S,s) \;\equiv\; \vartheta\,y \gets D_y\,\centerdot\,\vartheta\, a \gets g^y \bmod  N \,\centerdot\,(a,d)$$                  sendo  $$d\,\equiv\,(y,s)$$
**Challenge**
$$\qquad c \gets D_c$$
**Reply**
$$\qquad \mathcal{R}(d,c)\;\equiv\; \vartheta\,z \gets y + s\,c\,\centerdot\, \mathsf{if}\,\;z\in D_z\,\;\mathsf{then}\,\;z\,\;\mathsf{else}\,\;\bot$$

A prova é   $$\,\pi \equiv (a,c,z)\,$$ , se for  $$\,z\neq\bot\,$$, ou então é  $$\,\pi = \bot\,$$ quando $$\,z=\bot$$.  É por isso um exemplo de uma prova com “abort”.

**Verify**
$$\qquad \mathcal{V}(S,\pi) \; \equiv\,(\pi \neq \bot)\,\land\,g^z \equiv a\,S^c\mod N$$

     
As propriedades de  completude, conhecimento zero e fiabilidade  deste protocolo dependem crucialmente da relação entre os vários domínios $$\,D_s,D_c,D_y,D_z$$.  

| Como habitualmente, para um domínio finito $$D$$, o seu tamanho em bits é  dado por  $$\,|D|\,\equiv\,\lceil \log_2(\#D)\rceil$$. |

Note-se que:

1. A propriedade de  “conhecimento zero”  está diretamente relacionada com o valor
                                              $$\,z = y + s\,c\,$$
    calculado na resposta  $$\,\mathcal{R}(d,c)\,$$. Como $$\,z\,$$e $$\,c\,$$ são públicos (fazem parte da prova), se $$\,y\,$$ fosse nulo ou, genericamente, igual a uma constante, seria simples determinar o segredo $$\,s\,$$.


2. Genericamente  $$y$$ tem de ser aleatoriamente gerado, dentro de um domínio $$D_y\,$$, de forma a “ofuscar” o produto  $$\,s\,c\,$$. Para isso $$D_y$$ deve ser escolhido de tal modo, para $$\,c\in D_c\,$$ conhecido e quaisquer  segredos $$\,s\neq s'\in D_s$$ ,   sejam indistinguíveis  os geradores
                                           $$\,\vartheta\,y\gets D_y\,\centerdot\,y + s\,c\,$$       e           $$\,\vartheta\,y\gets D_y\centerdot\,y + s'\,c\,$$
        
3. As várias multiplicações $$\,s\,c\,$$ , com $$\,s\in D_s\,$$ e $$\,c\in D_c\,$$, formam um domínio que designamos por $$\,D_{sc}\,$$ cujo tamanho é $$\,\approx |D_s|+|D_c|\,$$.  
    Se o valor gerado $$\,y\gets D_y\,$$ for tal que $$\,z \equiv y + s\,c\,$$ não pertence a $$\,D_{sc}\,$$, então esse valor não pode passar nenhuma informação sobre o inteiro  $$\,s\,c\,$$ e, portanto, sobre $$s$$.
    Por isso deve ser um dos objetivos da prova garantir que a condição $$\,z\in D_{sc}\,$$ não se verifica.


4. Uma opção seria escolher um superconjunto $$\,D_y \supseteq  D_{sc}\,$$ com tamanho  muito superior.  Por exemplo, escolhendo $$\,D_y$$ de tal forma que $$\,|D_y| \approx M + |D_{sc}|\,$$ , com $$\,M \geq  |D_{sc}|\,$$.
    Como $$D_y$$  é $$\,2^M\,$$ vezes superior a  $$\,D_{sc}$$,  a probabilidade de $$\,z\equiv\,y+s\,c\,$$ ser um elemento de $$\,D_{sc}\,$$ é ínfima.  Por isso, com elevada probabilidade, não se verifica  $$\,$$$$\,z\in D_{sc}$$.


5. Sendo assim, pode-se  escolher $$\,D_z \,\equiv\, D_y\!\setminus\! D_{sc}\,$$. Neste caso  o algoritmo “reply”  tem uma baixa probabilidade de falhar e as respostas  que fornece ofuscam o segredo $$s$$.
    Como a probabilidade de falhar é muito pequena, este esquema pode ser visto como um sigma-protocolo sem falhas.
    
6. Porém, esta solução é impraticável por que iria conduzir a respostas $$\,z\,$$ e provas $$\,\pi\,$$ muito  longas. Nomeadamente se este protocolo for usado, com a transformação de Fiat Shamir, num esquema de assinatura digital onde a assinatura coincide com a prova $$\,\pi\,$$, o tamanho em bits das assinaturas seria superior a $$\,M+|D_{sc}|$$.


6. A alternativa será escolher também $$\,D_y \supseteq D_{sc}\,$$, de tamanho  $$\,M + |D_{sc}|\,$$,  mas sendo $$\,M\,$$  um valor bastante menor do que o usado em (4.) ; de facto escolhe-se$$\,M=1\,$$ ou $$\,M=2\,$$.
    Fazendo  $$\,D_z \equiv D_y\!\setminus\!D_{sc}\,$$, o mecanismo de falha continua a dar garantias de que $$\,z\,$$ esconde $$\,s\,c\,$$. Porém a probabilidade de falha é  $$\approx 2^{-M}\,$$ e portanto não é desprezável.

A vantagem essencial deste mecanismo de rejeição é o de fazer com que as provas $$\,\pi\,$$ sejam muito mais curtas: apenas $$1$$ ou $$2$$ bits acima do limite mínimo definido por $$\,|D_{sc}|$$.


----------
## Fiat-Shamir With Aborts (FSWA)

Uma construção semelhante a $$\,\mathcal{G}^\kappa\,$$ , designada por **iteração de** $$\,\mathcal{G}\,$$ e representado  por $$\,\mathcal{G}^\ast\,$$, descreve a situação em que se testa amostras sucessivas do gerador $$\,\mathcal{G}\,$$ , um número indeterminado de vezes, rejeitando todos as amostras até que uma determinada condição se verifique.  Este gerador  pode-se definir recursivamente como
                                               $$\mathcal{G}^\ast \;\equiv\; \vartheta\,z \gets \mathcal{G}\,\centerdot\, \mathsf{if}\; z \neq \bot \;\mathsf{then}\;\,z\;\,\mathsf{else}\;\,\mathcal{G}^\ast$$
designando por $$\,\bot\,$$  a amostra a rejeitar.

Com esta construção pode-se definir um esquema de assinatura digital baseado no  mecanismo de prova com rejeição.

O mecanismo é análogo à transformação de Fiat-Samir anteriormente apresentado,  com a diferença de na geração  de assinaturas , 


                     $$\text{Sign}(x,w,m)\;\equiv\;\vartheta\, c\gets\mathcal{H}(m)\,\centerdot\,\mathcal{S}(x,w,c)$$
                    

se passa a usar um “kernel” $$\,\mathcal{S}\,$$  onde o “reply”  $$\,\mathcal{R}(d,c)\,$$ é  substituído pela iteração  $$\,\mathcal{R}(d,c)^\ast$$

                             $$\,\mathcal{S}(x,w,c)\;\equiv\; \vartheta\,(a,d)\gets \text{Com}(x,w)\,\centerdot\,\vartheta\,z\gets \mathcal{R}(d,c)^\ast\,\centerdot\,(a,c,z)$$

# Esquemas LWE


## Objetivo

O sigma protocolo que acabámos de descrever usa o grupo aditivo dos inteiros e um grupo multiplicativo abeliano dos inteiro módulo $$N$$.  Define também um homomorfismo entre estes dois grupos,   $$\,h(s) \,\equiv\, g^s \bmod N\,$$, que é a fonte não só do problema difícil como também do algoritmo de verificação. De facto esse algoritmo explora a relação
                                                       $$h(y + s\,c) \,=\, h(y) \times h(s)^c\,$$

Este mecanismo pode ser estendida para outros pares de grupos associados a outros problemas difíceis; nomeadamente tem-se em vista os problemas das famílias LWE, M-LWE e similares.

Construindo um sigma-protocolo análogo ao apresentado para os inteiros, o mecanismo do “**Fiat-Samir With Aborts**” vai permitir construir esquemas de assinaturas.


## “Rejection Sampling”

Na implementação de técnicas criptográficas da família LWE é essencial ser capaz de construir um gerador $$\,f\,$$ , com uma função  distribuição $$\,\chi_f\,$$ complexa, a partir de um outro gerador $$\,g\,$$ de implementação conhecida e com uma função distribuição $$\,\chi_g$$. 
Um algoritmo simples para construir $$\,f\,$$ designa-se por **amostragem com rejeição** e está diretamente ligado aos geradores com “aborts” que temos estado a usar.

Vamos apresentar uma versão simplificada do algoritmo onde se assume

1. $$\,f,g\,$$ são “hashs” com o mesmo domínio finito $$\,{X}\,$$ tais que $$\,\chi_f(x) > 0\,$$ e $$\,\chi_g(x)> 0\,$$ para todo $$\,x\in{X}\,$$.
2. as funções distribuição  $$\,\chi_f\,$$ e $$\,\chi_g\,$$ são conhecidas e é possível calcular a função “likelyhood” 
                                                  $$\mathcal{L}(x)\;\equiv\; \chi_f(x)/\chi_g(x)\,$$

     o seu valor máximo
                                                            $$M \;\equiv\, \max\,\{\,\mathcal{L}(x)\;|\;x\in X\,\}$$     

    e o seu valor relativo 
                                                       $$\,\ell(x) \,\equiv\, \mathcal{L}(x)/M$$                                          
3. $$\;\overline{\ell(x)}\;$$ é o gerador de Bernoulli que produz  $$1$$’s  com probabilidade $$\,\ell(x)\;$$.


    A forma mais direta de implementar um gerador de Bernoulli  $$\,\overline{\varepsilon}$$ ,  com $$\,0< \varepsilon \leq 1$$ e com a precisão de $$\,n\,$$ bits, é o algoritmo.

                                             $$\overline{\varepsilon} \;\equiv\;\vartheta \,w\gets \{0,1\}^n\,\centerdot\,\mathsf{if}\,\;\hat{w}\leq \varepsilon\;\,\mathsf{then}\,\;1\;\,\mathsf{else}\,\;0$$
      

    > Aqui, e no que se segue, $$\,\hat{w} \equiv \sum_{i=1}^n\,2^{-i}\,w_i\,$$   é o designado racional de Lebesgue  determinado pela string de bits $$\,w\,$$.  
    > Em muitos CPU’s ,  $$\,\hat{w}\,$$ pode ser calculado em tempo constante ; por isso, este é um processo usual para gerar uniformemente racionais no intervalo $$\,[0\,,\,1]$$.

   Nestas circunstâncias o gerador $$\,f\,$$ pode ser implementado como    $$f \,\equiv\, F^\ast$$   em que


                       $$F \;\equiv\; \vartheta\,x \gets g \,\centerdot\,\vartheta\,b \gets \overline{\ell(x)}\,\centerdot\, \mathsf{if}\;\,b \,\;\mathsf{then}\;\,x\,\;\mathsf{else}\,\;\bot$$


| **Exemplo**<br>Vamos ilustrar como construir um gerador com uma função distribuição gaussiana a partir de um gerador uniforme ambos definidos no intervalo de inteiros $$\,X \equiv \left[-2^{t-1}\,,\,2^{t-1}\right]$$ representáveis com $$t$$ bits.<br><br>A distribuição gaussiana $$\,\chi_f(x)\,$$ , de variância $$\,\sigma\,$$,  é dada por $$\,$$$$\,(e^{-x^2/\sigma})/c\,$$  em que $$\,c\,$$ é uma constante de normalização. A distribuição uniforme tem o valor  $$\,\chi_g(x)\,=\,2^{-t}\,$$. Fazendo os cálculos conclui-se que <br>                                                                      $$\ell(x)\,=\,e^{-x^2/\sigma}$$<br>Portanto o gerador gaussiano pode ser implementado pelo algoritmo  $$\,f \equiv F^\ast\,$$ em que <br><br>                                $$F \,\equiv\,\vartheta\,x \gets g\,\centerdot\, \vartheta\, w \gets \{0,1\}^n\,\centerdot\, \mathsf{if}\;\,\hat{w} \leq e^{-x^2/\sigma}\;\,\mathsf{then}\,\;x\;\,\mathsf{else}\;\,\bot$$ |

Este gerador requer operações nos reais complicadas e, só por isso, não é muito conveniente. Adicionalmente não corre em tempo constante: para valores de $$\,x\,$$longe de zero (o que implIca $$\ell(x)$$  baixo) o número de strings $$w$$ que é preciso gerar para   $$x$$ ser aceite, é muito maior dos que são precisos  quando $$\,x\approx 0\,$$.  
Neste caso o tempo de execução do algoritmo dá informação sobre o valor absoluto de $$x$$.   Se $$\,x\,$$ for uma chave ou um outro tipo de segredo, esta implementação será muito insegura.

Isto dá-nos uma ideia de como uma implementação correta e segura de geradores gaussianos é algo muito complexo. Problemas difíceis  como o LWE exigem geradores gaussianos para poderem ser considerados “verdadeiramente seguros” ; frequentemente porém a perda de segurança, que ocorre quando se substitui um gerador gaussiano por outro tipo de geradores, é compensada por implementações mais seguras desses geradores alternativos.


| **Exemplo**<br>O criptosistema KEM/PKE  NewHope  usa um gerador simples que aproxima a distribuição gaussiana por uma distribuição calculada como uma distribuição binomial. <br>A ideia básica consiste em gerar aleatoriamente duas strings $$\,u,\upsilon\in \{0,1\}^n\,$$, calcular os respetivos pesos de Hamming  $$\,|u|\,,\,|\upsilon|\,$$  e gerar $$\,|u|-|\upsilon|\,$$ como “output”.<br><br>                                                           $$g \;\equiv \;\vartheta\,(u\,,\,\upsilon) \gets \{0,1\}^{n}\times\{0,1\}^n\,\centerdot\, |u| - |\upsilon|\,$$<br>                                                           <br>É simples verificar que, para $$x\geq 0$$, a  probabilidade   $$\,\chi_g(x) \equiv \mathbb{P}[z=x \,|\,z \gets g]\;$$ é dada por<br><br>                                            $$2^{-2\,n}\,\sum_{y=0}^{n - x}\,\binom{n}{y+x}\,\binom{n}{y}\;$$  $$\,=\,$$  $$\,2^{-2n}\,\binom{2n}{n+x}$$      <br>                                                 <br>e que $$\,\chi_g(-x) = \chi_g(x)\,$$.   <br><br>Esta função distribuição tem desvio padrão $$\,\sigma = \sqrt{n/2}\,$$  e é uma muito boa aproximação da distribuição gaussiana com o mesmo desvio padrão.<br><br>Se se pretender realmente uma distribuição gaussiana basta agora aplicar o algoritmo de “rejection sampling” a partir desta aproximação  $$\,g\,$$. |



## Algoritmo básico.

O esquema básica que foi proposto por Lyubashevsky , e que referimos atrás num contexto de inteiros, pode ser adaptado ao problema LWE da seguinte forma:

**Parâmetros**

1. Inteiros $$\,n,m$$ com $$\,m\approx 2n\,$$, um primo $$q$$ com $$\,|q| \approx 30\,$$ e um limite $$\,B\approx \sqrt{\frac{q-1}2}$$ .
2. Um gerador $$\,\chi\,$$ gaussiano (ou quase) com desvio padrão $$\,\sigma > 2\sqrt{n}$$ e centrado em $$0$$.
3. O domínio de inteiros $$\,\mathbb{Z}_q\,$$ identifica-se com o intervalo $$\,\left[-\frac{q-1}2\,,\,\frac{q-1}2\right]\,$$.   
4. É fixado um número de bits $$\,d < |B|\,$$  e,  para cada $$\,a \in \mathbb{Z}_q\,$$,  determina-se inteiros positivos  $$\,[a]_H \equiv \, \lfloor a/2^d\rfloor\,$$ e  $$\,[a]_L \equiv a - [a]_H\,2^d\,$$ .  Estes inteiros designam-se respetivamente por **“high bits”** e **“low bits”**  de  $$\,a\,$$. 
5. Definem-se também domínios inteiros  $$\;D_y \equiv \left[-B,B\right]\;$$ e $$\;D_z \equiv \left[-B+\varepsilon,B-\varepsilon\right]\;$$ sendo $$\varepsilon\,$$ um pequeno inteiro. 
6. Define-se o domínio de “hash”  $$\,D_c\equiv \{0,1\}^\ell\,\simeq\,\left[-2^{\ell-1},2^{\ell-1}-1\right]$$ e uma função de “hash” que produz resultados nesse domínio de inteiros.
7. É gerada pseudo-aleatoriamente  uma matriz  $$\,\mathbf{A}\in \mathbb{Z}_q^{n\times m}\,$$.
| Normalmente a matriz  $$\,\mathbf{A}\,$$ é construída por um XOF, do tipo $$\,\mathsf{shake\_128}\,$$  ou $$\,\mathsf{shake\_256}\,$$ , a partir de um $$\mathit{seed}\,$$ aleatoriamente gerado.<br>O único parâmetro aleatoriamente gerado é precisamente o argumento do XOF; por isso a complexidade descritiva da matriz  $$\,\mathbf{A}\,$$ coincide  com o comprimento  do $$\textit{seed}$$. |



**Problemas**
Determinados por este conjunto de parâmetros define-se o problema difícil
                                  $$\text{LWE}\,\equiv\,\{\,t\in \mathbb{Z}^m\;|\; \exists\, (s,e)\in \chi^{n+m}\,\centerdot\,t \equiv s\,\mathbf{A}+e \mod q \}$$

**Prova de conhecimento**
Numa abordagem “proof with aborts” define-se uma prova de conhecimento para o problema $$\,\mathcal{L}\,$$, usando a chave pública  $$\,\mathsf{pk}\equiv t\,$$  e a chave privada $$\,\mathsf{sk}\equiv (s,e)\,$$.


- **Commit** 
    $$\text{Com}(\mathsf{pk},\mathsf{sk})\;\equiv\;\vartheta\,y\gets D_y \,\centerdot\,\vartheta\,a\gets [y\mathbf{A}]_H\,\centerdot\,\vartheta\,d \gets (y,\mathsf{sk})\,\centerdot\,(a,d)$$
- **Challenge** 
    $$\text{Ch}(a) \;\equiv\; \vartheta\,m \gets \{0,1\}^\ell \,\centerdot\, \text{Hash}(m\,\|\,a)$$
- **Reply** 
    $$\mathcal{R}(d,c)\;\equiv\;\vartheta\,(y,s,e) \gets d\,\centerdot\, \vartheta\,z \gets y + c\,s\,\centerdot\,\mathsf{if}\;\,z \in D_z^m \;\,\mathsf{and}\,\;[y\,\mathbf{A}-c\,e]_L\in D_z^n\;\,\mathsf{then}\;\,z\;\,\mathsf{else}\;\,\bot$$

Como é usual numa “prova com rejeição” , se a prova tem sucesso então será  $$\,\pi \equiv (a,c,z)$$


- **Verify** 
        $$\mathcal{V}(\mathsf{pk},\pi)\;\equiv\;\vartheta\,(t,a,c,z) \gets \mathsf{pk},\pi\, \centerdot\,\mathsf{if}\;\, a =[z\mathbf{A}-c\,t]_H\, \;\,\mathsf{and}\;\,z\in D_z\;\,\mathsf{then}\;\,\mathtt{sucesso}\;\,\mathsf{else}\;\,\mathtt{falha}$$
    

A justificação da completude da prova deriva do facto de, se os parâmetros $$B,\varepsilon,d,\ell\,$$  forem bem escolhidos, então verifica-se
                                                                         $$[y\mathbf{A}]_H\;=\;[y\mathbf{A}-c\,e]_H$$
Isto é, a parcela $$\,c\,{e}\,$$  não afecta os “high bits”  de $$\,y\,\mathbf{A}$$. Nesse caso, verifica-se
                                              $$\,z\,\mathbf{A}- c\,t \;=\;(y + c\,s)\mathbf{A} - c\,(s\,\mathbf{A} + e)\;=\;y\,\mathbf{A}-c\,e$$ 
e por isso

                                         $$[z\,\mathbf{A} - c\, t]_H \,=\, [y\,\mathbf{A}]_H\,=a$$
## Esquema de Assinatura Digital

A conversão deste esquema de prova num esquema de assinatura digital segue, em traços gerais, o mecanismo de “Fiat-Shamir With Aborts”. No caso geral esta transformação está organizada em três passos:

1. Substituição da geração aleatória de um “callenge”  $$\,c \gets \{0,1\}^\ell\,$$  por um “hash” da mensagem a assinar $$\,c \gets \text{Hash}(m)$$.
2. Substituição do “reply with abort”  $$\,\mathcal{R}(d,c)\,$$ pela sua iteração $$\,\mathcal{R}(d,c)^\ast\,$$. Essencialmente executar repetidamente $$\,\mathcal{R}(d,c)\,$$ até que o resultado não seja $$\,\bot\,$$.
3. Toma-se a prova $$\,\pi = (a,c,z)\,$$ como a assinatura $$\mathsf{sign}\,$$ e usa-se a verificação da prova  $$\,\mathcal{V}(\mathsf{pk},\pi)\,$$ como verificação da assinatura.

                     $$\,\text{Verify}(\mathsf{pk},\pi,m)\;\equiv\;\mathsf{if}\;\, c = \text{Hash}(m) \;\,\mathsf{then}\;\,\mathcal{V}(\mathsf{pk},\pi)\,\;\mathsf{else}\;\,\mathtt{falha}$$

Para esta prova em particular vamos fazer algumas pequenas modificações nos passos 1. e 3. com o objetivo de  tornar mais eficiente o esquema de assinaturas.


1. A prova usa uma geração aleatória do “challenge” da forma $$\,$$$$\,\vartheta\,m\gets\{0,1\}^\ell\,\centerdot\, \text{Hash}(m\|a)\,$$. 

      No esquema de assinaturas vai-se usar o núcleo determinístico deste gerador; isto é

                                           $$\,\text{Cha}(m,a) \;\equiv\; \text{Hash}(m\|a)$$
2. $$\cdots$$
3. Como $$c$$ já contém informação sobre o “commit” $$\,a\,$$ , a assinatura não precisa de conter toda a prova. Desta forma a assinatura será apenas

                                                            $$\mathsf{sign}\;\equiv\,(c,z)$$

    que é substancialmente mais curta do que a prova; isto é importante porque “esquema práticos” procuram minimizar o tamanho da assinatura.
    
    A verificação da assinatura tem de ser modificada porque $$a$$ não é passado na assinatura mas tem de ser calculado .
    
        $$\begin{array}{ll}\text{Verify}(\mathsf{pk},\mathsf{sign},m)\;\equiv\; & \vartheta\,(t,c,z) \gets \mathsf{pk},\mathsf{sign}\, \centerdot\,\vartheta\,a \gets [z\mathbf{A}-c\,t]_H\,\centerdot\, \\ & \mathsf{if}\;\, c = \text{Hash}(m\|a) \;\,\mathsf{and}\;\,z\in D_z\;\,\mathsf{then}\;\,\mathtt{sucesso}\;\,\mathsf{else}\;\,\mathtt{falha} \end{array}$$



# Esquemas RLWE

Dois esquemas de assinatura digital presentes no concurso NIST PQC usam o esquema LWE básico como ponto de partida: o  [esquema Dilithium](https://pq-crystals.org/dilithium/index.shtml)  e o esquema [qTesla](https://qtesla.org). 
Em ambos os reticulados são ideais no habitual anel 

                                         $$\mathcal{R}_q \, \equiv\, \mathbb{F}_q[w]/\langle w^n+1\rangle$$

definido por um $$\,n\,$$ que é potência de $$\,2\,$$ e por um primo  $$\,q\,$$ que verifica $$\,q \equiv 1 \bmod 2n$$.

Como vimos anteriormente esta escolha de parâmetros permite que as operações soma e multiplicação no anel $$\,\mathcal{R}_q\,$$ sejam efectuadas de forma eficiente usando  $$\mathsf{NTT}$$ (“number theoretic transform”) .
No **Dilithium** , nas suas diferentes implementações, o valor de $$\,n\,$$ é sempre $$\,256\,$$ e o valor de $$\,q-1\,$$ é sempre $$\,2^{23}-2^{13} \,=\,16368\times (2n)\,$$.
No  **qTesla** existem duas implementações, com $$\,n=1024\,$$ $$\,n=2048\,$$, e os respetivos valores de $$\,q-1\,$$ são, respetivamente, $$\,167762\times(2n)\,$$ e $$\,209020\times(2n)\,$$.


Alguns parâmetros comuns:

1. Os elementos de $$\,\mathbb{F}_q\,$$ são representados por inteiros no domínio $$\,\mathbb{Z}_q\,\equiv\,[-\lfloor q/2\rfloor,\lfloor q/2\rfloor]$$ equipado com a norma $$\,\|x\|\equiv |x|$$ e o arredondamento  $$\,\lfloor\cdot\rceil_q\,\colon \mathbb{Z}\to \mathbb{Z}_q$$. 
2. O anel  $$\, \mathcal{R}_q\,$$ está equipado com as normas $$\,\|f\|_\infty\equiv \max_{i=1..n}\,|f_i|\,$$   e  $$\,\|f\|_1\equiv \sum_{i=1..n}\,|f_i|$$ sendo  $$f_i\,$$ o representante do $$i$$-ésimo coeficiente de $$f$$.
3. São definidos parâmetros  $$B,h$$ e os domínios 

              $$\,\mathcal{R}_{[B]}\equiv \{f\in \mathcal{R}_q\,|\, \|f\|_\infty\leq B\}\,$$          e         $$\mathbb{H}_h\equiv \{f \in \mathcal{R}_q\,|\,\|f\|_\infty = 1\;\text{e}\;\|f\|_1=h\,\}\,$$.

4. É definido um parâmetro positivo $$\,d\,$$ tal que  $$\,2^d < \sqrt{q}\,$$  e as funções “low bits” e “hight bits”   definidas nos inteiros  $$\,x\in\mathbb{Z}_q\,$$ por
                                    $$[x]_L\,\equiv\,\lfloor x \rceil_{2^d}\qquad$$ e $$\qquad [x]_H\,\equiv\,(x - [x]_L)/2^d$$   
    Esta definição estende-se para polinómios $$f\in\mathcal{R}_q$$  e define-se $$\,[f]_L\;\text{e}\;[f]_H\,$$ aplicando o operador coeficiente a coeficiente e concatenando esses valores.


De forma resumida e omitindo muitos dos principais aspetos de optimização, as principais características deste dois esquemas são


## qTesla

**Parâmetros e notação** 


1. É definido um “hash” $$\,\mathsf{H}\,$$ de tamanho $$\,\ell\,$$ e uma função de codificação $$\,\mathsf{Enc}\colon \,\{0,1\}^\ell \to \mathbb{H}_h$$ que transforma o “output” do “hash” num “pequeno polinómio”.
2. O gerador $$\,\mathcal{D}_\sigma\,$$ é  gaussiano discreto em $$\,\mathbb{Z}_q\,$$ centrado na origem e variância $$\sigma\,$$ . O gerador $$\,\mathcal{D}_\sigma^n\,$$  produz vetores in $$\,\mathbb{Z}_q^n\,$$ com componentes independentemente geradas por $$\,D_\sigma\,$$; esses vetores são também interpretados em $$\mathcal{R}_q$$ .
3. Aqui a matriz $$\,\mathbf{A}\,$$ do algoritmo básico, é substituída por $$\,\kappa\,$$ polinómios $$\,\mathbf{a}_1,\mathbf{a}_2,\cdots,\mathbf{a}_\kappa \in \mathcal{R}_q\,$$ pseudo-aleatoriamente gerados por um XOF $$\,\mathbf{Gen_a}\,$$ a partir de uma $$\,\mathit{seed}_a\,$$.
4. Existe um gerador pseudo-aleatório  $$\,\mathbf{Gen_y}\,$$que, sob input de uma $$\,\textit{seed}_y\,$$e de uma string $$\,\textit{r} \gets \{0,1\}^\ell\,$$, produz um polinómio $$\, \mathbf{y}\in \mathcal{R}_{[B]}\,$$.
5. Existe um gerador pseudo-aleatório $$\,\mathbf{GenG}\,$$ que, sob input de $$\,\textit{seed}_{se}$$ , simula o gerador aleatório $$\,s,e_1,e_2,\cdots,e_\kappa \gets \mathcal{D}_\sigma^n\,$$.
6. Existem parâmetros de rejeição $$\, L_e,L_s< B$$ e parâmetros  $$E,S$$ tais  que $$\,L_e < E < 2L_e\;$$ e $$L_s < S < 2L_s$$.

**KeyGen**

1. Gerar $$\,\textit{seed}_a,\textit{seed}_y\gets\{0,1\}^\ell\,$$   
2. Repetir
        i. Gerar $$\,\textit{seed}_{se}\gets \{0,1\}^\ell\,$$
        ii. Gerar$$$$$$\,s,e_1,e_2,\cdots,e_\kappa \gets \mathbf{GenG}(\textit{seed}_{se})\,$$  
    até que $$$$$$\,\|s\|_\infty \leq L_s\,$$ e $$\,\|e_i\|\leq L_e\,$$  para todo $$i=1,\cdots\,\kappa$$.
    A chave privada é $$\,\mathbf{sk}\equiv\,\langle \textit{seed}_a\,,\, \textit{seed}_y\,,\,\textit{seed}_{se}\rangle$$.
4. Gerar $$\mathbf{a}_1,\cdots,\mathbf{a}_\kappa \gets \mathbf{Gen_a}(\textit{seed}_a)\;$$ e calcular $$\;t_i \gets \mathbf{a}_i\ast s + e_i\;$$, para todo  $$i=1,\cdots,\kappa\,$$. 
    A chave pública é $$\;\mathbf{pk}\equiv \langle\textit{seed}_a,t_1,t_2,\cdots,t_\kappa\rangle$$.
| A chave privada é relativamente curta porque é formada por 3 “seeds”. A chave pública é bastante maior porque, para além de um “seed” tem $$\kappa$$ polinómios grandes. |

**Sign**
Dada a chave privada    $$\,\mathbf{sk}\equiv\,\langle \textit{seed}_a\,,\, \textit{seed}_y\,,\,\textit{seed}_{se}\rangle$$ e uma mensagem $$\,m \in \{0,1\}^\ast\,$$.
*Commit* 

1. Gerar $$\,\mu\gets \{0,1\}^\ell\,$$   e calcular   $$\;y \gets \mathbf{Gen_y}(\textit{seed}_y\,,\, \mathsf{H}(m\,\|\,\mu))$$
2. Gerar  $$\;\mathbf{a}_1,\cdots,\mathbf{a}_\kappa \gets \mathbf{Gen_a}(\textit{seed}_a)\;$$  e   calcular  $$\,\upsilon_i \gets  \lfloor\mathbf{a}_i\ast y\rceil_q\;$$ para todo $$i=1,\cdots,\kappa$$ . 
3.  O “commit”  é dado pelos  “high bits” dos $$\,\upsilon_i$$’s :      $$\,a \gets [\upsilon_1]_H\,\|\cdots\|\,[\upsilon_\kappa]_H$$

*Challenge* 

4. $$\textit{ch} \gets \mathsf{H}(m\,\|\,a)$$
5. Codificar o desafio num polinómio  $$\;$$$$\,c \gets \textsf{Enc}(\textit{ch})$$

*Reply*  

6. Calcular  $$\;s,e_1,\cdots,e_\kappa \gets \mathbf{GenG}(\textit{seed}_{se})$$ 
7. Calcular $$\;z \gets y + s*c$$

*Confirmation* — “rejection sampling”

8. Se $$\;z \in \mathcal{R}_{[B-S]}\;$$  $$\;\texttt{aceitar}\;$$ a resposta $$z\;$$, senão $$\,\texttt{rejeitar}\;$$ $$\,z\,$$ e repetir a partir de   $$\texttt{1.}$$
9. Calcular $$\,$$$$\;w_i \gets \lfloor \upsilon_i - e_i\ast c\rceil_q\;$$ para todo $$i$$ . 
    Se existir algum $$i=1,\cdots,\kappa\;$$ tal que 
                                      $$\,\;E + \|[w_i]_L\|_\infty\geq 2^{d-1}\;\,$$     ou        $$\;\;E + \|w_i\|_\infty \geq \lfloor q/2\rfloor\;$$
    então $$\;\texttt{rejeitar}\;$$ $$\,z\;$$   e repetir a partir de  $$\,\texttt{1.}$$

A assinatura é o par $$\,(\textit{ch}\,,\,z)$$.

| A correção da confirmação deriva do facto de $$\;E,S\;$$, para além de $$\,s,e_i,c\,$$ , serem gerados de forma a que se verifique, para todo $$i$$,     $$\|e_i\ast c\|_\infty \leq E\,$$    e    $$\,\|s\ast c\|_\infty \leq S$$. |


**Verify**
Dada a mensagem $$\,m\,$$, a chave pública   $$\;\mathbf{pk}\equiv \langle\textit{seed}_a,t_1,t_2,\cdots,t_\kappa\rangle$$   e a assinatura $$\;(\textit{ch},z)\;$$.

1. Calcular  $$c \gets \mathsf{Enc}(\textit{ch})$$  , 
2. Gerar  $$\mathbf{a}_1,\cdots,\mathbf{a}_\kappa \gets \mathbf{Gen_a}(\textit{seed}_a)\;$$  e  calcular  $$\,$$$$\;w_i \gets \lfloor \mathbf{a}_i*z - t_i\ast c\rceil_q\;$$ para todo $$i$$ .
3. Reconstruir o “commit”  $$\,a' \,\gets \,[w_1]_H\,\|\cdots\|\,[w_\kappa]_H\,$$        com  os “hight bits” dos $$\,w_i$$.
4. Se  $$\;\textit{ch} = \mathsf{H}(m\,\|\,a')\;\;$$   e   $$\;z \in \mathcal{R}_{[B-S]}\;\;$$então $$\;\;\texttt{aceitar}\;$$   senão $$\;\texttt{rejeitar}$$. 


| $$\upsilon_i = \mathbf{a}_i\ast y = \mathbf{a}_i*z - \mathbf{a}_i*s*c \;$$.  <br>Como $$t_i = \mathbf{a}_i*s + e_i\,$$, tem-se $$\,\mathbf{a}_i*s*c \,=\, t_i*c - e_i*c$$   e, por isso,   <br>                                           $$\;\upsilon_i \,=\, \mathbf{a_i}*z - t_i*c + e_i*c \,=\, w_i + e_i*c\;$$<br>Os parâmetros são escolhidos de forma a se verificar<br>                                                                     $$\,[\upsilon_i]_H\,=\,[w_i]_H$$<br>Tal obtém-se garantindo que o produto $$\,e_i*c\,$$ não contribui para os “high bits”  de $$\;w_i\;$$. |



## Dilithium

A construção do esquema Dilithium é semelhante à do qTesla mas tem algumas diferenças importantes quer ao nível da estrutura algébrica quer ao nível da forma de compressão e da codificação da informação  pública (a chave pública e a assinatura).

Tal como o qTesla segue o algoritmo básico de Lyubashevsky que vimos anteriormente na versão RLWE. No entanto, ao nível da estrutura algébrica refere-se

1. O Dilithium segue uma abordagem de *Modular LWE*.
    1. A matrix $$\,\mathbf{A}\,$$ que, no algoritmo básico é um elemento de $$\,\mathbb{Z}_q^{n\times m}$$ com $$n,m$$ “grandes”, no Dilithium é uma matriz de polinómios de “pequenas” dimensões. Tem-se
                                       $$\,\mathbf{A}\,\in\,\mathcal{R}_q^{\kappa\times(\kappa-1)}$$            com  $$\,\kappa\in\{3,4,5,6\}$$
        Os valores de $$\,\kappa\,$$ determinam as 4 configurações  submetidas ao concurso PQC NIST.
    2. Os diferentes vetores  $$\,\,s,e,y,z,t\,$$  são vetores de polinómios; são elementos de $$\,\mathcal{R}_q^\kappa\,$$ ou de $$\,\mathcal{R}_q^{\kappa-1}\,$$.
    Como consequência o tamanho de $$q$$ e a dimensão $$n$$ de $$\,\mathcal{R}_q\,$$ é bastante inferior aos valores usados no qTesla.  Tem-se, para todas as configurações, $$n=256\,$$ e $$\,q=2^{23}-2^{13} + 1$$. 
2. O Dilithium não usa geradores gaussianos discretos. Antes implementa geradores uniformes $$\,\mathcal{S}_\eta\,\equiv\,\{e\in\mathcal{R}_q\,|\,\|e\|_\infty \leq \eta\}$$  .

A estratégia de compressão e implementação tem também alguma diferenças.

1. Vimos no qTesla que a chave pública continha $$\kappa$$ polinómios $$\,t_i\,$$ todos eles com um número considerável de coeficientes. Esta é a principal fonte de complexidade. No Dilithium existe um vector $$t$$  com  $$\,\kappa-1\,$$ polinómios; o número total de polinómios é semelhante mas o  número de coeficientes de cada polinómio é bastante menor no Dilithium. 
2. Adicionalmente no Dilithium apenas os “high bits” de $$\,t\,$$ fazem parte da chave pública; os “low bits” são passados na chave privada. Isto implica que o mecanismo de verificação da assinatura tem de ser modificado para poder executar apenas com os “high bits” de $$t$$.
3. Uma outra característica do Dilithium é o uso intensivo da $$\,\mathsf{NTT}\,$$. Dado que são executadas muitas multiplicações polinomiais a matriz $$\,\mathbf{A}\,$$ é gerada, armazenada e operada no domínio das transformadas NTT
4. Tal como no qTesla, a transformada $$\;\mathbf{\hat{A}}\;$$é gerada, a partir de uma “seed” $$\,\textit{seed}_a\,$$. Porém $$(s,e)\,$$ é gerado na forma polinomial diretamente dos gerador unifirme $$\,\mathcal{S}_\eta^\kappa\times \mathcal{S}_\eta^{\kappa-1}$$ sendo necessário, por isso, calcular as suas transformadas $$\,(\hat{s},\hat{e})\gets \mathsf{NTT}((s,e))\,$$.
5. O vetor $$\,t\,$$ é determinado na forma transformada  $$\,\hat{t} \gets \hat{s}\,\mathbf{\hat{A}} + \hat{e}\,$$ , em que  todas as multiplicações e somas são calculadas componente a componente.
6. Existe ainda uma diferença fundamental: assinatura no qTesla é sempre não-determinística  mas no Dilithium pode ser uma assinatura determinística.
    Recorde-se que no qTesla, no passo 1. do algoritmo de assinatura,  gera-se aleatoriamente uma string $$\,\mu\,$$ como $$\ell\,$$ bits que é a fonte do não determinismo na operação “commit”; a partir deste parâmetro tudo o resto é calculado deterministicamente.
    No Dilithium existe um parâmetro $$\,\rho\,$$ que tem o mesmo papel. No entanto $$\,\rho\,$$ entanto tem duas implementações possíveis. Uma delas é, como no qTesla,  a geração aleatória de uma string de bits . Tem também uma segunda opção em que $$\,\rho\,$$ é calculado como um “hash” da mensagem $$\,m\,$$  e de um parâmetro fixo que faz parte da chave privada.
    A primeira opção designa-se, na candidatura, por “randomized signing”. A segunda opção tem sido objecto de muitas críticas e não parece recomendável. 
    

Todo o esquema segue agora o algoritmo básico e é muito semelhante ao qTesla. Não vamos aqui entrar nos pormenores de implementação que podem ser consultados na documentação da candidatura.



# “Multivariate Public Key Cryptography” (MPKC) 
| Estas notas são fortemente baseadas na documentação da candidatura RAINBOW ao concurso NIST-PQC |


MPKC denota uma família de técnicas criptográficas baseadas em polinómios, com múltiplas variáveis, definidos sobre um corpo finito $$\,\mathbb{F}_q\,$$. 

No caso mais geral a classe  $$\,\mathsf{MQ}_{m,n,q}$$ denota os criptosistemas cuja chave pública é um vetor  de $$\,m\,$$ polinómio quadráricos a $$\,n\,$$ variáveis sobre um corpo finito de dimensão $$\,q\,$$ 


                                 $$\mathcal{P}\;\equiv\;\{\,\rho_1(x),\rho_2(x),\cdots\,\rho_m(x)\,\}$$,
                

Sendo  $$\,x = (x_1,x_2,\cdots,x_n)\,$$ o vetor de variáveis então tem-se para todo $$\,i=1...m\,$$


                               $$\rho_i(x)\;\equiv\; x\,{A}_i\,x^\top + x\,B_i^\top + C_i$$
                            

em que $$\,A_i\in \mathbb{F}_q^{n\times n}$$ é a matriz simétrica de coeficientes dos termos quadráticos, $$\,B_i\in \mathbb{F}_q^n\,$$ é  o vetor dos coeficientes dos termos lineares  e  $$\,C_i\in \mathbb{F}_q$$ é um coeficiente constante. 

Desta forma conclui-se que  $$\,\mathcal{P}\,$$ é determinado por $$\,(m/2)\,(n+1)\,(n+2)\,$$coeficientes em $$\,\mathbb{F}_q$$.

                    

Um polinómio pode ser visto também como uma função; neste caso cada $$\,\rho_i\,$$ pode ser interpretado como uma aplicação

                                                $$\,\rho_i\,\colon\,\mathbb{F}_q^n \,\to\,\mathbb{F}_q$$ . 

Globalmente  $$\,\mathcal{P}\,$$ define uma aplicação      $$\mathcal{P}\,\colon \,\mathbb{F}_q^n\,\to\,\mathcal{F}_q^m\,$$  que mapeia  $$\,\mathbf{x}\in\mathbb{F}_q^n\,$$ no  vetor

                                $$\,\mathbf{y}\,\equiv\,(\rho_1(\mathbf{x}),\rho_2(\mathbf{x}),\cdots,\rho_m(\mathbf{x}))\,\in\,\mathbb{F}_q^m$$

Num criptosistema de chave pública da classe  $$\,\mathsf{MQ}_{m,n,q}$$  as operações públicas , como  cifrar  num PKE,  encapsular num KEM  ou a verificar num esquema de assinaturas, são implementadas calculando  um valor   $$\,\mathbf{y}\,\gets\,\mathcal{P}(\mathbf{x})\,$$.

As operações privadas, como decifrar um criptograma ou assinar uma mensagem,  são implementadas resolvendo um sistema de equações 
                                                          $$\mathcal{P}(x)\,=\,\mathbf{y}$$
ou, equivalentemente, determinando o conjunto

                                   $$\mathcal{P}^{-1}(\mathbf{y})\;\equiv\;\{\,\mathbf{x}\in\mathbb{F}_q^n\;|\;\mathcal{P}(\mathbf{x})\,=\,\mathbf{y}\,\}$$

Resolver o sistema de equações acima ou calcular $$\,\mathcal{P}^{-1}(\centerdot)\,$$,  designa-se por “**multivariate quadratic problem**” ou **MQP**$$(m,n,q)\,$$.

É simples verificar que, para qualquer $$\,q\,$$, o problema  $$\,\text{MQP}(m,n,q)\,$$  é NP-hard. As instâncias mais  complexas do problema ocorrem quando $$\,m,n\,$$  são da mesma ordem de grandeza. Adicionalmente, através de evidência experimental,  constata-se que os melhores algoritmos para resolver o MQP têm complexidade que no pior caso é muito semelhante à complexidade no caso médio.

Esta observação é ainda válida de considerar-mos algoritmos quânticos. De momento não existe qualquer algoritmo quântico cuja complexidade melhore a complexidade dos melhores algoritmos clássicos. Por outro lado, dado que MQP é NP-hard não se prevê que essa situação se modifique no futuro.

No entanto têm de existir algumas instâncias do problema MQP que têm uma solução eficiente. São essas instâncias que permitem construir “trapdoors” secretas que permitem construir as chaves privadas nos criptosistemas   $$\,\mathsf{MQ}_{m,n,q}$$.  Na terminologia da classe   $$\,\mathsf{MQ}_{m,n,q}$$, as instâncias $$\,\mathcal{F}\,$$ para as quais o problema MQP tem uma solução calculada por um algoritmo PPT  designam-se por **central maps** .


## Criptosistemas $$\,\mathsf{MQ}_{m,n,q}$$ : forma geral.

Um aspeto fundamental à aplicação criptográfica das instâncias   $$\,\mathcal{P}\in\mathsf{MQ}_{m,n,q}$$  é saber quanto elementos tem o conjunto $$\,\mathcal{P}^{-1}(\mathbf{y})\,$$. A cardinalidade desse conjunto depende de $$\,\mathbf{y}\,$$ mas também depende da relação entre os parâmetros  $$\,m\,$$ e $$\,n\,$$. 

Nomeadamente pode-se provar

> Quando $$\,m >  n\,$$ , para todo $$\,\mathbf{y}\in\mathbb{F}_q^m\,$$,  o conjunto $$\,\mathcal{P}^{-1}(\mathbf{y})\,$$ tem cardinalidade $$\,\leq 1\,$$.

**KeyGen**
 A forma geral de um criptosistema de chave pública na classe $$\,\mathsf{MQ}_{m,n,q}$$  gerar um par de chaves $$\,(\mathsf{pk},\mathsf{sk})\,$$ segue os seguintes passos

    - Em função do parâmetro de segurança $$\,\lambda\,$$ e do tipo de criptosistema , são escolhidos parâmetros $$\,m,n,q\,$$
    - Gera-se um “central map”  $$\,\mathcal{F}\in\text{MQ}_{m,n,q}\,$$ . Gera-se um par de transformações afins e invertíveis  $$\,\mathcal{S}\,\colon\, \mathbb{F}_q^m\to\mathbb{F}_q^m\,$$ e   $$\,\mathcal{T}\,\colon\, \mathbb{F}_q^n\to\mathbb{F}_q^n\,$$ .  O triplo $$\,(\mathcal{F},\mathcal{S},\mathcal{T})\,$$ é a chave privada $$\,\mathsf{sk}\,$$.
    - A transformação $$\,\mathcal{P}\,\equiv\,\mathcal{S}^{-1}\circ\mathcal{F}\circ\mathcal{T}^{-1} \,$$ é a chave pública $$\,\mathsf{pk}\,$$.

**PKE** $$\,(m > n)\,$$
Uma cifra de chave pública $$\,\mathsf{MQ}_{m,n,q}$$  exige uma instância desta classe em que  $$\,m > n\,$$.


1. Para **cifrar** uma mensagem $$\,\mathbf{x}\in\mathbb{F}_q^n\,$$com a chave pública $$\,\mathcal{P}$$,  calcula-se  o criptograma $$\,\mathbf{y} \equiv \mathcal{P}(\mathbf{x})\,$$.


    Note-se que, porque $$\,m>n\,$$, o conjunto $$\,\mathcal{P}^{-1}(\mathbf{y})\,$$ não contém nenhum outro elemento para além de $$\,\mathbf{x}\,$$. Porém esse conjunto não pode ser calculado eficientemente dado que, no caso médio,  o problema MQP$$_{m,n,q}\,$$ é NP-Hard.  Assim
    
2. Para **decifrar** o criptograma $$\,\mathbf{y}\,$$ com a chave privada $$\,(\mathcal{F},\mathcal{S},\mathcal{T})\,$$, calcula-se  $$\mathbf{y}'\,\gets\,\mathcal{S}(\mathbf{y})$$ e
    1. Calcula-se $$\,\mathcal{F}^{-1}(\mathbf{y'})\,$$; porque $$\,\mathcal{F}\,$$ é um “central map” este conjunto pode ser determinado eficientemente. 
    2. Dado que $$\,m>n\,$$, do resultado acima  conclui-se que $$\,\mathcal{F}^{-1}(\mathbf{y'})\,$$ tem exatamente um elemento; seja $$\,\mathbf{x}'\,$$ esse elemento. Recupera-se $$\,\mathbf{x}\gets \mathcal{T}(\mathbf{x}')$$ .

**DSS** $$\;(m < n)$$ ****
Uma esquema de assinatura digital $$\,\mathsf{MQ}_{m,n,q}$$  exige uma instância da classe onde seja $$\,n > m\,$$.
Para além das chaves pública e privada, exige-se uma função de “hash” $$\,\mathcal{H}\colon\{0,1\}^\ast\to\mathbb{F}_q^m\,$$ para mapear mensagens arbitrárias em “hashed messages”, elementos de $$\,\mathbb{F}^m_q$$.
Neste esquema o espaço das assinaturas é $$\,\mathbb{F}_q^n\,$$. Portanto a **incerteza** na geração de assinaturas, o número de assinaturas possíveis para cada “hashed message”, será $$\,q^{n-m}\,$$.


1. Para **assinar** uma mensagem $$\,M\in\{0,1\}^\ast\,$$ com a chave privada $$\,(\mathcal{F},\mathcal{S},\mathcal{T})\,$$, 
    1. calcula-se a “hashed message”  $$\,\mathbf{y} \gets \mathcal{H}(M)\;$$ e a sua imagem  $$\,\mathbf{y}'\gets \mathcal{S}(\mathbf{y})$$ ,
    2. usando o facto de que $$\,\mathcal{F}\,$$ é um “central map”, determina-se o gerador  $$\,$$$$\,\mathcal{F}^{-1}(\mathbf{y}')\,$$
    3. gera-se aleatoriamente $$\,\mathbf{x}'\gets \mathcal{F}^{-1}(\mathbf{y}')\;$$ ; calcula-se, como assinatura de $$\,M\,$$,  $$\,\mathbf{x}\gets\mathcal{T}(\mathbf{x}')\,$$.

Note-se que a cardinalidade de  $$\,\mathcal{F}^{-1}(\mathbf{y}')\,$$ é  a incerteza na geração de $$\,\mathbf{x}'\,$$, e na geração da assinatura $$\,\mathbf{x}\,$$; como vimos é  $$\,|q|\times (n-m)\,$$ bits.


2. Para **verificar**, com a chave pública $$\,\mathcal{P}\,$$,  se $$\,\mathbf{x}\,\in\mathbb{F}_q^n\,$$ é assinatura válida para $$\,M\in\{0,1\}^\ast\,$$, calcula-se a “hashed message”  $$\,\mathbf{y}\gets \mathcal{H}(M)\,$$ e aceita-se a assinatura se e só se $$\,\mathbf{y} = \mathcal{P}(\mathbf{x})\,$$.



## Esquemas de assinaturas “Oil and Vinager” (OV).

Os diferentes esquemas de assinaturas que usam a classe MQ$$_{m,n,q}\,$$ distinguem-se pela forma como são definidos os “central maps” $$\,\mathcal{F}\,$$ , como são determinado os geradores $$\,\mathcal{F}^{-1}(\mathbf{y})\;$$ (a *inversão* de ****$$\,\mathcal{F}\,$$) e na forma como é comprimida a chave pública $$\,\mathcal{P}\,$$. **

Uma abordagem simples a todas estas questões é vulgarmente designada por “*oil and vinegar*"  consiste em 

    - Não oferecer nenhuma forma de compressão da chave pública $$\,\mathcal{P}\,$$
    - Dividir o conjunto  $$\,\mathcal{I}_n\equiv \{1,\cdots,n\}\,$$ , índices das variáveis nos polinómios $$\,\rho_i(x)\,$$, em dois conjuntos disjuntos $$\,{V}\equiv \{1,\cdots,\upsilon\}\,$$ , com $$\,\upsilon < n\,$$, e $$\,\mathcal{O}\equiv\{\upsilon+1,\cdots,n\}$$ ; 
| Os conjuntos $$\,V\,$$ (“vinegar”) e $$\,\mathcal{O}\,$$(“oil”)  não precisam de ser exatmente estes; pode-se escolher um qualquer subconjunto $$\,V \subset \mathcal{I}_n\,$$ , com $$\,\upsilon\,$$ elementos,  e calcular $$\,\mathcal{O} = \mathcal{I}_n\setminus V\;$$. |

    - Restringir o conjunto de polinómios $$\,\mathcal{F} \equiv \{\,\rho_1(x),\cdots,\rho_m(x)\,\}\,$$ às condições
        - o número de polinómios $$\,m\,$$ coincide com $$\, n - \upsilon\,$$
        - nenhum dos polinómios contém um termo quadrático que só tenha variáveis “oil”; isto é, todo o  monómio quadrático $$\,a_{i,k,j}\,x_k\,x_j\,$$ verifica  $$\,a_{i,k,j}=0\,$$ ou então pelo menos um dos índices $$\,k,j\,$$pertence a $$\,V\,$$.
        
        Não existe qualquer restrição aos monómios lineares ou constantes. Note-se que é muito simples construir  $$\,\mathcal{F}\,$$ que verifique estadas condições: basta gerar $$\,\mathcal{F}\,$$aleatoriamente e, em seguida, percorrer as matrizes $$\,A_i\,$$ (dos coeficients de monómios quadráticos) substituindo por zero todas as entradas $$\,a_{i,k,j}\,$$ em que ambos os índices $$\,k,j\,$$ são elementos de $$\,\mathcal{O}\,$$.

Vamos supor que o vetor de variáveis $$\,x = (x_1,\cdots,x_n)\,$$ se decompões num par de vetores de variáveis $$\,(x_\upsilon , x_o)\,$$ em que $$\,x_\upsilon\,$$ é formado pelas variáveis com índices $$\,i\in V\,$$ e $$\,x_o\,$$é formado pelas variáveis com índices em $$\,\mathcal{F}\,$$. 

Então cada polinómio $$\,\rho\,\in\,\mathbb{F}_q[x]\,$$ pode ser escrito como um polinómio nas variáveis $$\,x_o\,$$cujos coeficientes são polinómios nas variáveis $$\,x_\upsilon\,$$. Tem-se

                                      $$\,\mathbb{F}[x]\;\simeq\;\mathbb{F}_q[x_\upsilon][x_0]$$

Nomeadamente cada  $$\,\rho(x)\,$$ pode-se escrever como $$\,\rho(x_\upsilon)(x_o)\,$$. A condição “vinager-oil” é equivalente à afirmação

> Para cada polinómio $$\,\rho\in \mathcal{F}$$  e para cada vetor $$\,r\in \mathbb{F}_q^\upsilon\,$$ que substitua as variáveis $$\,x_\upsilon\,$$ , o polinómio nas variáveis $$\,x_o\,$$ calculado como $$\,\rho(r)(x_o)\,$$não tem termos quadráticos.


O algoritmo para inverter um “central map”  $$\,\mathcal{F}\,$$ baseia-se fortemente nesta propriedade

**Inverter um “central” map”**  **“vinegar-oil”** 

***Objectivo***: dado o “central map”  $$\,\mathcal{F} \in \mathsf{MQ}_{m,n,q}\,$$ , com $$\,n >  m\,$$, gerar aleatóriamente uma solução da equação  $$\,\mathcal{F}(x) = 0\,$$.


1. Decompõe-se o vetor de variáveis  $$\,x = (x_1,\cdots,x_n)\,$$ em dois vetores  $$\,(x_\upsilon,x_o)\,$$ das variáveis “vinager” e das variáveis “oil” respetivamente. Temos $$\,o = m\,$$  e $$\,\upsilon = n - m$$.
    Reescreve-se cada polinómio $$\,\rho(x) \in \mathcal{F}\,$$ como $$\,\rho(x_\upsilon)(x_o)\,$$.
2. Gera-se aleatoriamente $$\,r \gets \mathbb{F}_q^{\upsilon}\,$$ e calcula-se, para todos  $$\,\rho_i\in \mathcal{F}\,$$  , os polinómios afins $$\,\rho(r)(x_o)\,$$ .  O sistema de equações

                                                    $$\{\,\rho_i(r)(x_o) \,= \, 0\quad\text{com}\quad i=1...m\,\}$$

    é linear e pode ser resolvido, caso a solução exista, por eliminação Gaussiana simples.
3. Se existir uma solução $$\,\mathbf{z}\in \mathbb{F}_q^m\,$$ desse sistema, então o algoritmo devolve o vetor 
                                           $$(\,r\,,\,\mathbf{z})$$
    Se a solução do sistema não existir  então regressa ao passo 2 e, com um novo $$\,r\,$$aleatoriamente gerado , repete o processo. 



## O criptosistema Rainbow

O criptosistema Rainbow segue de perto o esquema de assinatura digital que vimos atrás introduzindo pequenas alterações motivadas por questões de eficiência.

Em primeiro lugar, a gama de variáveis $$\{1,\cdots\,n\}\,$$  é dividido em 3 faixas: uma faixa “vinager”  $$V \equiv \{1,\cdots,\upsilon_1\,\}$$ e duas faixas “oil” : $$\,\mathcal{O}_1\,\equiv\,\{\upsilon_1+1,\cdots,\upsilon_2\}\,$$ e $$\,\mathcal{O}_2\,\equiv\,\{\upsilon_2+1,\cdots,n\}\,$$.

Em seguida, as regras de exclusão de termos quadráticos não se aplicam uniformemente para todos os polinómios  $$\,\rho_i(x)\,$$.  Tem-se


1. Dado que a gama de índice de polinómios é $$\,i\in\{1,\cdots,m\}\,$$ e é isomófica com a união $$\,\mathcal{O}_1\,\cup\,\mathcal{O}_2\,$$ ,   pode-se dividir  também em duas faixas: $$\,\mathcal{U}_1\equiv\{1,\cdots,\upsilon_2-\upsilon_1\}\,$$ e $$\,\mathcal{U}_2\,\equiv\,\{\upsilon_2-\upsilon_1 + 1,\cdots,m\}\,$$,  isomórficas respetivamente a $$\,\mathcal{O}_1\,$$ e $$\,\mathcal{O}_2\,$$.


![](https://paper-attachments.dropbox.com/s_9A989A297B238753AFAAB98CCB2A401E7EE4686D96206283F58F57C226439ECE_1621596364303_rainbow.png)

2. A regras de exclusão de termos quadráticos em “central maps” $$\,\mathcal{F}\,$$ é
>             Para $$\,\ell \in \{1,2\}\,$$, se $$\,i\in \mathcal{U}_\ell\,$$ e  $$\,k,j\in \mathcal{O}_\ell\,$$ , então será $$\,a_{i,k,j} = 0\,$$.

Com esta regra o algoritmo de inversão de $$\,\mathcal{F}\,$$ torna-se bastante mais eficiente.

