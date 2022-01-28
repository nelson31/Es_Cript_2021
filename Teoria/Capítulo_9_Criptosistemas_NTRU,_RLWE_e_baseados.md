# Capítulo 9: Criptosistemas NTRU,  RLWE e baseados em Códigos.

Criptosistemas baseados em “Hard Lattices” (HL’s) têm segurança máxima quando as matrizes que determinam as HL’s são aleatoriamente geradas. Formalmente, só nesses casos e com apropriados valores dos restantes parâmetros, é possível garantir que a complexidade de problemas como o $$\mathbf{SIS}_\beta\,$$ ou $$\,\mathbf{LWE}_\alpha\,$$tem características de segurança ótimas; 
nomeadamente 

> no caso médio (em relação às matrizes usadas) e em modelos de computação quântica, a complexidade iguala ou supera o pior caso de problemas standard em reticulados.

Por este motivo as condições de segurança das HL’s,  exigem que os criptosistemas usem matrizes que, além de serem grandes, têm de ser **densas:** cada um dos seus elementos é gerado independentemente dos restantes e, por isso, exige uma descrição explícita. 
Como estas matrizes fazem parte da chave pública, da chave privada ou de ambas, um tal criptosistema tem chaves enormes, por vezes da ordem dos Mbytes.

Uma primeira justificação para usar descrições implícitas dos reticulados, deriva da necessidade de compactar a representação dos criptosistemas. 

Um criptosistema, oferecendo imunidade a ataques quânticos mas exigindo chaves de Mbytes de tamanho, não tem muita viabilidade prática, nomeadamente porque não pode ser implementado  em pequenos dispositivos (“smart cards”, telemóveis, …); quanto muito pode ser usado em situações de nicho quando não existem limites aos recursos computacionais usados.
Porém,  se o tamanho  das chaves for reduzido para alguns Kbytes, eventualmente já poderá ser implementado nesses dispositivos tornado-se uma alternativa realista às técnicas clássicas.

Outra justificação prende-se com a flexibilidade algébrica dos reticulados quando são usados em técnicas criptográficas concretas. 
Formalmente um reticulado é “apenas” um grupo: tem uma única operação algébrica, tipicamente uma soma,  e é regido pelas propriedades do grupo. As aplicações dos reticulados tornam-se mais ricas e flexíveis se existirem mais operações, multiplicações por exemplo,  e mais propriedades. 

Sem perder a estrutura de grupo abeliano, é interessante que um reticulado  $$\,\mathcal{L}\,$$ esteja imerso num anel  $$\,\mathcal{R}\,$$ comutativo  que funciona como o seu “span”.   

O grupo aditivo de $$\,\mathcal{R}\,$$ é sempre um $$\,\mathbb{Z}$$-módulo e qualquer subgrupo desse grupo aditivo é também um $$\,\mathbb{Z}$$-módulo. 
Em particular um **ideal** $$\,\mathcal{I}\subseteq \mathcal{R}\,$$ é  um subgrupo do grupo aditivo de $$\,\mathcal{R}\,$$que satisfaz a propriedade de *ser fechado* por multiplicação com qualquer  elemento do anel: $$\,\forall\,x\in\mathcal{R}\,\centerdot\, x\,\mathcal{I}\subseteq \mathcal{I}\,$$.
Esta propriedade faz com que, de entre os vários possíveis subgrupos aditivos de $$\,\mathcal{R}\,$$ , os ideais sejam uma boa hipótese para ser reticulados.

Porém nem todos os ideias podem ser reticulados; de facto, um reticulado é um subgrupo de um $$\,\mathbb{Z}$$-módulo que é finitamente gerado e nem todos o ideais o são.


## Reticulados sobre ideais de $$\mathbb{Z}[w]$$ e $$\mathbb{Z}_q[w]$$

Tomemos o anel dos polinómios de coeficientes inteiros e uma só variável

                                                           $$\mathcal{R}\;\equiv\,\mathbb{Z}[w]$$

Considere-se um primo  $$\,q\,$$ e seja  

                                                          $$\mathcal{R}_q \,\equiv\,\mathbb{F}_q[w]$$

Como é usual  cada  $$\,f\in \mathcal{R}_q$$ é representado por um polinómio de coeficientes  inteiros   $$\,f'\in\mathbb{Z}_q[w]\,$$.  Os coeficientes de $$\,f'\,$$ são  inteiros de $$\,\mathbb{Z}_q\,$$em uma de duas interpretações:

    - $$\mathbb{Z}_q\,\equiv\,\{x\in\mathbb{Z}\,|\, 0\leq x < q\}\,$$ com a norma $$\,\|x\|\equiv \min\{x,q-x\}$$
    - $$\mathbb{Z}_q\,\equiv\,\{x\in\mathbb{Z}\,|\, | x| \leq \lfloor q/2\rfloor\}\,$$ com a norma  $$\,\|x\| \equiv |x|\,$$.

Adicionalmente, em qualquer das interpretações,

    - Dado $$\,z\in\mathbb{Z}\,$$ representamos por $$\,\lceil z\rfloor_q\,$$ o único  $$\,z'\in\mathbb{Z}_q\,$$ que verifica $$\,z \equiv z' \bmod q\,$$.
    - A distância  $$\,\mathbf{d}(x,y)$$ entre  $$\,x,y\in \mathbb{Z}_q\,$$ é dada por $$\|\lceil x-y\rfloor_q\|$$.

Neste documento os símbolos $$\,\mathcal{R}\,$$ e $$\,\mathcal{R}_q\,$$denotam sempre os anéis de polinómios acima definidos.
Em qualquer dos anéis  $$\,\deg f\,$$ denota o grau do polinómio $$\,f\,$$.   

O máximo divisor comum de dois elementos $$\,g,f\in\mathcal{R}\,$$ é representado por $$\,\gcd(g,f)\,$$; no anel $$\,\mathcal{R}_q$$  o máximo divisor comum é representado por $$\,\gcd_q(g,f)$$. Como cada um dos  polinómios $$\,g,f\,$$ tem (muito provavelmente) fatorizações diferentes em $$\,$$$$\,\mathcal{R}\,$$ e $$\,\mathcal{R}_q\,$$, os polinómios $$\,\gcd(g,f)\,$$ e $$\,\gcd_q(g,f)\,$$ são quase sempre distintos.

**Ideais Principais**
Fixo um qualquer $$\,g\in\mathcal{R}\,$$ o conjunto de todos os múltiplos de $$\,g\,$$ é uma forma particular de ideal designado por **ideal principal** com gerador $$\,g\,$$. Esse ideal é representado  por $$\,\langle g \rangle\,$$ ou por $$\,g\,\mathcal{R}\,$$. Por razões que serão óbvias em breve preferimos a designação $$\,\mathbf{ip}(g)\,$$ e a definição


                                $$\,\mathbf{ip}(g)\,\equiv\,\{ y \in \mathcal{R}\,|\,\exists\,z\in \mathcal{R}\,\centerdot\,y = z\ast g\}$$
                                

Este subgrupo é um ideal mas não é finitamente gerado. Isto porque é possível definir uma base infinita formada pelos polinómios    $$\{\,g\,,\,w\,g\,,\,w^2\,g, \cdots, w^\kappa\,g\,,\,\cdots\}$$  e qualquer   $$\,z\ast g \in \mathbf{ip}(g)\,$$  pode ser escrito como uma combinação  linear inteira dessa base: 

$$\,z\ast g \,\equiv z_0\,g + z_1\,(w\,g) + \cdots + z_\kappa\,(w^\kappa\,g)$$       sendo  $$\,\kappa = \deg z$$   e    $$z_i \in \mathbb{Z}$$   para todo $$i\geq 0$$

        

Como não existe limite a $$\,\deg z\,$$ , também não existe limite ao número de elementos da base que são usados nessa combinação linear.

Porém é possível transformar um ideal principal num reticulado; para isso basta adicionar um módulo $$\,f\in \mathcal{R}$$  e modificar a definição de $$\,\mathbf{ip}\,$$ para


                        $$\,\mathbf{ip}(g,f)\,\equiv\,\{\, y \in \mathcal{R}\;|\;\exists\,z\in \mathcal{R}\,\centerdot\,y \equiv  z\ast g \mod f\,\}$$

A dimensão deste reticulado é determinada pelo seguinte resultado


> Se for $$\,n \equiv \deg f\,$$  e $$\,\ell \equiv \deg \gcd(g,f)\,$$ então o ideal $$\,\mathbf{ip}(g,f)\,$$ tem dimensão $$\,\kappa \equiv n - \ell\,$$;

Como exemplo de uma base tem-se a 

                                     $$\,\mathcal{B}\,\equiv\,\{\,g\,,\,w\,g\,,\cdots,\,w^{\kappa-1}\,g\,\}$$
| **Localizações**<br><br>Considere-se $$\,n\,$$ inteiros distintos  $$\,\{\,x_1\,,\,x_2\,,\cdots,\,x_n\,\}$$ que, neste contexto vamos designar por *localizações*. Cada um destes inteiros define um monómio $$\,m_i(w) \equiv w - x_i\,$$.  Obviamente $$\,\gcd(m_i,m_j)=1\,$$ se $$\,i\neq j$$.<br><br>Vamos definir uma situação CRT com os módulos $$\,m_i\,$$. O módulo CRT será  $$\,f \equiv \prod_{i=1}^n\,m_i(w)\,$$. <br>Sejam $$\,\mu_i(w)\,$$ os polinómios que formam a base CRT. Recorde-se que se verifica $$\,\mu_i(w) \equiv 1 \bmod m_i(w)\,$$, $$\,\mu_i(w) \equiv 0 \bmod m_j(w)\;,\;\text{se}\,i\neq j\,$$.<br>A propriedade fundamental das bases CRT é poder verificar, em  qualquer polinómio $$\,h\in\mathcal{R}\,$$,<br>                                                $$h\,\equiv\,\sum_i\,h(x_i)\,\mu_i(w)\mod f$$  $$\,$$<br>                                                <br>Considere-se agora um qualquer polinómio $$\,g\in \mathcal{R}\,$$ ,  de grau $$\,t < n\,$$, que verifica $$\,\gcd(g,f) = 1\,$$ou,  o que é equivalente,  $$g(x_i)\neq 0\,$$ para todo $$i$$.  Então, pelo resultado atrás,  a dimensão do reticulado  $$\,\mathbf{ip}(g,f)\,$$ é $$n$$.<br><br>Um qualquer $$\,y=z\ast g\,$$ elemento desse reticulado verifica<br>                                $$\,y \,\equiv\, \sum_{i=1}^n\,z(x_i)\,g(x_i)\,\mu(w) \mod f$$<br>Isto implica que os $$\,n\,$$ polinómios <br>                                                                  $$\{\,g(x_i)\,\mu_i(w)\,\}_{i=1}^n$$<br>definem uma base do reticulado $$\,\mathbf{ip}(g,f)$$.<br>$$\,$$ |

Os reticulados $$\,\mathbf{ip}(g,f)\,$$ podem ser descritos por polinómio $$\,g\,$$ em que $$\,\deg g \leq \deg f\,$$.  No entanto cada coeficiente de $$\,g\,$$ é um inteiros arbitrário e precisa de ser explicitamente descrito.
Daqui resulta que a descrição do reticulado não é finita.

O uso prático desses reticulados exige descrições finitas. Daí a necessidade de usar, para coeficientes de $$\,g\,$$ , inteiros num intervalo limitado; nomeadamente é necessário substituir $$\,\mathbb{Z}\,$$ por $$\,\mathbb{Z}_q\,$$ nos coeficientes dos polinómios. 

Desta forma temos de refazer a definição de reticulado ideal principal entrando em conta com $$q\,$$ como módulo adicional. Assim, dados  $$\,g,f\in \mathcal{R}_q$$ (mais exatamente $$\mathbb{Z}_q[w]\,$$)


                        $$\,\mathbf{ip}(g,f,q)\,\equiv\,\{\, y \in \mathcal{R}\;|\;\exists\,z\in \mathcal{R}\,\centerdot\,y \equiv  z\ast g \mod f \bmod q\,\}$$

A definição é semelhante à anterior mas há um detalhe diferente que é muito importante: quando se define a dimensão $$\,\kappa\,$$ do reticulado o máximo divisor comum é calculado em $$\,\mathcal{R}_q\,$$ e não em $$\,\mathcal{R}$$.

                                                         $$\,\kappa = \deg f - \deg \gcd_q(g,f)$$


**Ideais “kernel”**
Ideais principais modulares não são a única forma de construir reticulados a partir de ideais em $$\,\mathcal{R}\,$$.  Vamos considerar um  outro tipo de reticulados/ideais.

Dados polinómios   $$\,h,f\in \mathcal{R}_q\,$$  definimos o **kernel modular**


                        $$\,\mathbf{krn}(h,f,q)\,\equiv\,\{\,y\in\mathcal{R}\;|\; y\ast h \equiv 0 \mod f\bmod q\,\}$$

Para se determinar a ordem deste reticulado usamos um outro resultado


> Dados  $$\,h,f\in \mathcal{R}_q\,$$, existe um único  (módulo $$f,q$$)   $$\,g\in\mathcal{R}_q\,$$ tal que $$\,\gcd_q(g,h) = 1$$   e
>                                                             $$\,g\ast h \,\equiv\, 0 \mod f\bmod q$$

O polinómio  $$g$$  é dado por  $$\,g \equiv f/\gcd_q(h,f)\,$$ e designa-se por **co-factor de** $$\,h\,$$ módulo $$f,q$$. 

É simples verificar, pela simetria da definição,  que para quaisquer $$\,f,g,h\in \mathcal{R}_q\,$$,  $$g$$ é  co-factor  de $$h$$ módulo $$f,q$$  se e só se $$\,h\,$$ é co-factor  de $$\, g\,$$ módulo $$\,f,q\,$$ .

Nessas circunstâncias temos o nosso principal resultado


> Se $$g$$ e $$h$$ são co-fatores mútuos módulo $$\,f,q\,$$  então
>                                                   $$\mathbf{ip}(g,f,q)\;\equiv\; \mathbf{krn}(h,f,q)$$

Da relação $$\,f \equiv h\ast\gcd_q(g,f)\,$$ concluímos $$\,\deg h = \deg f - \deg\gcd_q(g,f)\,=\, n - \ell = \kappa$$  ; portanto a ordem deste reticulado coincide com o grau do polinómio $$h$$.

**Reticulados NTRU**
O criptosistema NTRU introduz um terceiro tipo de reticulados,  definido por ideais modulares em $$\,\mathcal{R}\,$$  **,** que essencialmente generaliza  os reticulados “kernel”.      ****

Os polinómios    $$\,h,f \in \mathcal{R}_q\,$$  definem os seguinte reticulado em $$\,\mathcal{R}\times \mathcal{R}$$,


            $$\mathbf{ntru}(h,f,q) \;\equiv\; \{\,(y,x)\in \mathcal{R}\times \mathcal{R}\;|\; y\ast h \equiv x \mod f\bmod q\,\}$$

Neste reticulado $$\,\mathcal{R}\times \mathcal{R}\,$$ tem a estrutura de um grupo abeliano aditivo somando pares de polinómios componente a componente.   ****Note-se que $$\,\mathbf{krn}(h,f,q)\,$$ se identifica com o sub-grupo de $$\,\mathbf{ntru}(h,f,q)\,$$ definido pelos pares da forma $$(y,0)\,$$.


## Reticulados e problemas difíceis em NTRU e RLWE

Nesta seção vamos simplificar a notação considerando implícitos os módulos  $$f$$ e $$q$$ e designar os reticulados  simplesmente por $$\,\mathbf{ip}(g)\,,\,\mathbf{krn}(h)\;\text{e}\;\mathbf{ntru}(h)\,$$.

No criptosistema NTRU, mais básico,  o módulo $$\,f\,$$ tem a forma  $$\,f \equiv w^n - 1\,$$  send $$\,n\,$$ um primo tal que  $$\,\tau_n(w) \equiv (w^n-1)/(w-1)\,$$ é irredutível em $$\,\mathcal{R}_q$$. 

| A principal vantagem deste tipo de módulo reside na possibilidade de representar a multiplicação por um polinómio  $$h$$ módulo $$f$$, a operação  $$\,g \mapsto g\ast h \bmod f\,$$, pela  multiplicação do vetor dos coeficientes $$\,\bar{g}$$ por uma matriz circulante   $$\,\mathbf{rot}(h)\,$$: a operação   $$\,\bar{g} \mapsto \bar{g}\times \mathbf{rot}(h)\,$$. |

Para chave privada o NTRU usa um par $$\,(y,x)\,$$ de pequenos polinómios e para chave pública usa um polinómio $$\,h\,$$ que verifica $$\,x \equiv h\ast y \mod f \bmod q$$.

Assim, a inversão da chave pública NTRU é equivalente a encontrar um “pequeno vetor”  $$\,(y,x)\,$$ no reticulado  $$\,\mathbf{ntru}(h)\,$$.

Para uma mensagem $$\,m\,$$ representada por um “pequeno polinómio”, o criptograma $$\,e\,$$ verifica

                               $$(e + m) \equiv r\ast h \mod f \bmod q$$

para um “pequeno polinómio”  $$\,r\,$$. Portanto o par   $$\,(r,e+m)\,$$ é um vetor do reticulado $$\,\mathbf{ntru}(h)\,$$.
Escrevendo

                                      $$(r\,,\,e+m) \,=\, (0,e) + (r,m)$$

e atendendo que $$\,(r,m)\,$$ pode ser visto como um “erro” (já que é formado por pequenos vetores) então  inverter o criptograma $$\,e\,$$ é equivalente a determinar o vetor do reticulado $$\,\mathbf{ntru}(h)\,$$ que está mais próximo do “target”  $$\,(0,e)\,$$. Se for encontrado esse ponto do reticulado  $$\,(r,e+m)\,$$, a segunda componente desse par determina a mensagem como $$\,m = (e+m) - e\,$$.

Assim, no NTRU, inverter a chave pública é equivalente a resolver, no reticulado $$\,\mathbf{ntru}\,$$, um  problema de vetor mais curto, enquanto que inverter o criptograma é equivalente a resolver um problema de vetor mais próximo.



O RLWE usa outro tipo de reticulados e recorre a vários problemas difíceis para assegura a impossibilidade de inverter a chave pública e inverter o criptograma.

Recorde-se que no RLWE a informação privada é um par $$\,(s,e)\,$$, ambos pequenos polinómios , com $$\,s\,$$ gerado aleatoriamente e $$\,e\,$$ gerado numa distribuição gaussiana discreta $$\,\chi\,$$. A chave pública é o par $$\,(a,b)\,$$ que verifica   $$\;b \equiv a\ast s + e \mod f \bmod q\,$$.

Aqui são relevantes três reticulados todos gerados por $$\,a\,$$que sugerem “ataques” ao RLWE

    - o  ideal principal  $$\,\mathcal{L}_0\, \equiv\, \mathbf{ip}(a,f,q)\,$$
    - o seu dual            $$\,\mathcal{L}_1 \,\equiv\, \mathbf{krn}(a,f,q)$$ 
    - a versão **ntru**        $$\mathcal{L}_2\,\equiv\,\mathbf{ntru}(a,f,q)$$


1. Para *inversão da chave pública* $$\,(a,b)\,$$ pode-se considerar que um vetor $$\,y\,$$ que verifique  $$\,y \equiv s\ast a \mod f \bmod q\,$$ é um ponto do reticulado  $$\,\mathcal{L}_0$$. A definição da chave pública diz-nos que   $$\, y = b - e\,$$. Por isso determinar  $$\,(y,e)\,$$ é resolver, no reticulado $$\,\mathcal{L}_0\,$$ o problema do vetor mais próximo ao “target”  $$b$$.


2. Ainda para *inverter a chave pública* pode-se seguir uma outra abordagem: vamos tentar resolver um problema do vetor mais curto no reticulado $$\,\mathcal{L}_1\,$$. Seja $$\,\tau\in\mathcal{L}_1\,$$ um vetor curto determinado resolvendo uma qualquer forma de SVP.
    Como $$\,\tau\,$$ pertence ao “kernel” de $$\,a\,$$, verifica-se $$\,\tau\ast a \equiv 0 \mod f \bmod q\,$$.  Dada a relação que define $$\,b\,$$ tem-se 
            $$\,\tau\ast b \,\equiv \tau\ast a\ast s + \tau\ast e \,\equiv \, \tau\ast e \mod f \bmod q$$.
    Designemos por $$\,z \equiv \tau\ast b\,$$ o **sindroma** de $$b$$ com $$\tau$$. Este polinómio calcula-se a partir da informação disponível. Ficamos com uma equação na incógnita $$e$$
                                           $$\,z \equiv \tau\ast e \mod f \bmod q$$
    Determinar um “pequeno”  $$e$$ que seja solução desta equação é conhecido como o **problema da descodificação**. Como veremos no próximo capítulo este é um problema que em média tem complexidade muito elevada. 
    No entanto, aqui, temos um caso especial. Porque $$\,\tau\,$$ é supostamente pequeno, existe um algoritmo, designado por **bit-flip**,  que resolve este problema em tempo polinomial.


3. Para *inverter o criptograma* vamos usar o reticulado  $$\,\mathcal{L}_2\equiv \mathbf{ntru}(a)\,$$.
    Para cifrar uma mensagem $$\,m\,$$ que se destaca dos erros gaussianos $$\,e\gets \chi\,$$ o esquema LPR usado na maioria das implementações RLWE usa dois polinómios:
        - $$u \equiv a\ast r + e_u\,$$                       com pequenos polinómios $$\,r,e_u \gets \chi$$
        - $$\upsilon\equiv b\ast r + e_\upsilon + m\,$$              com pequeno polinómio  $$\,$$$$\,e_\upsilon \gets \chi$$
    e forma o criptograma  $$\,e \equiv (u,\upsilon)\,$$.
    Pode-se escrever 
                        $$u - e_u \,\equiv a\ast r \mod f \bmod q$$
    e, por isso, o par  $$\,(r,u-e_u)\,$$ é um elemento do reticulado  $$\,\mathbf{ntru}(a)\,$$.  Também
                       $$(r,u-e_u)\,=\,(0,u) + (r,-e_u)$$
    Assim, porque $$\,(r,-e_u)\in\mathcal{R}^2\,$$ é um pequeno “erro”, determinar  $$\,(r,u-e_u)\,$$ é determinar o ponto do reticulado  $$\,\mathbf{ntru}(a)\,$$mais próximo do “target”  $$(0,u)\,$$.
    
    Resolvido este problema passa-se a conhecer $$\,r\,$$  e pode-se escrever
                                             $$\,m \,=\,-e_\upsilon + (\upsilon - b\ast r)$$
    O polinómio $$\,\upsilon - b \ast r\,$$ pode ser determinado.  Como $$\,-e_\upsilon\,$$ é pequeno e provém do gerador gaussiano $$\,\chi\,$$ e como a mensagem $$\,m\,$$ se destaca das amostras desse gerador, descodificar $$\,(\upsilon - b\ast r)\,$$ permite recuperar $$\,m\,$$.


## Complexidade dos problemas “hard” em reticulados sobre ideais.

No início deste capítulo referimos aos problemas $$\,\mathbf{SIS}_\beta\,$$ e $$\,\mathbf{LWE}_\alpha\,$$ como fornecendo complexidade “hard” no caso médio desde que as matrizes que os definem sejam aleatoriamente geradas. 
Nos reticulados sobre ideais, a sua versão HL apresenta matrizes com uma forma específica (ligada à multiplicação de polinómios)  que, por isso, não podem ser vistas como aleatoriamente geradas. 
Por isso faz sentido analisar em que medida a complexidade destes problemas standard é afectada pelo facto de as descrições matriciais se cingirem a esta forma específica. 

A análise em profundidade desta questão está longe de estar completa e não cabe no âmbito deste estudo introdutório. 

No entanto crê-se que, se as restantes condições de segurança se cumprirem nomeadamente na escolha apropriada dos geradores de erros, as descrições dos  reticulados sobre ideais não diminui significativamente a complexidade dos problemas standard em relação à dos mesmos problemas em descrições aleatoriamente geradas.

Essa é uma **crença** que é partilhada por quase todas as candidaturas PQC que são “lattice based”; nessa classe incluem-se não só as das famílias NTRU e RLWE com também as designadas “code-based”.


# Criptografia Baseada em Códigos

De entre as estruturas criptográficas ditas pós-quânticas existe um número significativo que vai buscar à **Teoria dos Códigos** as estruturas algébricas, os problemas difíceis e, sobretudo, os paradigmas de processamento da informação.

Alguns dos criptosistemas destas classe são contemporâneos dos clássicos RSA e Diffie-Hellman. Questões de eficiência fizeram com que, na altura, que não tivessem o mesmo tipo de sucesso. Porém, ao reconhecer-se que a Teoria de Códigos oferece problemas difíceis  com muitas possibilidades de serem imunes a ataques quânticos, passou a existir um interesse renovado nessas técnicas.

A Teoria dos Códigos nasceu com objetivos muito distintos da Criptografia. Essencialmente surgiu da necessidade de corrigir os erros que são adicionados a uma mensagem durante a sua transmissão  através de “meios ruidosos”.


![](https://paper-attachments.dropbox.com/s_3116C3C8734601EDA5CF47D8C58847BF6F6A366B159BEA712A204D8DD613F618_1588534580488_codigo.png)


Com este propósito a Teoria dos Códigos desenvolveu o paradigma que, sumariamente, está representado no diagrama acima.

# Introdução à Teoria dos Códigos
## Terminologia

Um **código** $$\,\mathcal{C}\,$$ é uma linguagem; isto é, um conjunto de “palavras finitas” com elementos num **alfabeto** finito  $$\,\mathcal{A}$$. Quando não existir ambiguidade na terminologia, os elementos da própria linguagem são também designados por “códigos”.

Como paradigma vamos apresentar a terminologia dos chamados **códigos sistemáticos.**

1. O ponto de partida é uma **mensagem** $$\,m\,$$ que se pretende transmitir .
2. Para prevenir os efeitos dos erros, a mensagem é estendida acrescentado-lhe  **redundância**  $$\,r = \rho(m)\,$$; o resultado é uma **“palavra código”;** a função que gera a palavra-código designa-se  por $$\,\mathbf{encode}(m)\,$$ e, nos códigos sistemáticos, produz

                                                     $$\,m \,\|\, r\;\gets \; \text{encode}(m)\quad$$com $$\quad r \gets \rho(m)$$ 

3. O espaço das mensagens é sempre isomórfico com o espaço das palavras código:  cada mensagem $$\,m\,$$ tem uma e só uma palavra-código que a representa e, da mesma forma, cada palavra código representa uma e só uma  mensagem.
4. O meio ruidoso modifica não só a componente de mensagem $$\,m\,$$ como também a componente da redundância $$\,r\,$$. O resultado será algo da forma $$\;m'\,\|\,r'\;$$ que assume o nome genérico de **sinal** ou **código corrupto** ou, simplesmente, **código.**
5. Numa descrição algébrica apropriada pode-se afirmar que
                                      $$\,m' \,=\,m + e_m\quad$$   e   $$\quad r' \,=\,r + e_r$$
    em que    $$\,e\,\equiv\ e_m\,\|\,e_r\,$$ se designa por **erro de transmissão .**
6. O ponto crucial neste processo é o algoritmo $$\,\text{decode}(m'\,\|\,r')\,$$ que recebe o código corrupto e consegue reconstruir a palavra código $$\,m\,\|\,r\,$$ “mais próxima” desse sinal. Equivalentemente  consegue reconstruir o erro $$\,e\,\equiv\, (m\,\|\,r) - (m'\,\|\,r')$$, que seja “mais curto”.
7. Note-se que qualquer algoritmo $$\text{decode}\,$$ verifica
        1. vários sinais podem ser descodificáveis numa única mensagem;  
        2. uma palavra código descodifica sempre na mensagem que a originou;
        3. nem todos os sinais são descodificáveis: nesses casos o algoritmo  termina em erro.
    

Toda a definição do código tem um objetivo essencial: facilitar o algoritmo de descodificação. Este modelo pode ser restrito ou estendido de várias formas:$$\,$$

Pode ser restrito definindo um modelo algébrico concreto para o alfabeto, para as palavras código e para as mensagens. 

    1. Frequentemente os **símbolos** do alfabeto são elementos de um corpo finito $$\,\mathbb{F}_q\,$$ em que:
        1. $$q\,$$ é um pequeno primo;  num **código binário** tem-se $$\,q=2\,$$ , com símbolos $$\,\{0,1\}\,$$; num **código ternário** tem-se $$\,q=3\,$$ com símbolos  $$\,\{-1,0,1\}\,$$,
        2. ou então $$q\,$$ é da forma $$\,p^m\,$$ sendo $$\,p\,$$ um pequeno primo ($$2$$ ou $$3$$) e $$\,m\,$$ uma dimensão também pequena; é frequente que $$m$$ seja tal que qualquer elemento de $$\,\mathbb{F}_q\,$$ possa ser descrito por uma palavra básica do processador (“byte” ou duplo “byte”); por exemplo 8 símbolos binários ou 5 símbolos ternários cabem num “byte”.
    2. As palavras da mensagem têm todas o mesmo tamanho e da mesma forma também as palavras código têm todas o mesmo tamanho. 
        Para algum $$\kappa> 0\,$$ e  $$n > \kappa$$, 
        1. O **espaço das mensagens** identifica-se com um espaço vetorial $$\,\mathbb{F}_q^\kappa\,$$; se $$\,q = p^m\,$$ (com $$p\in\{2,3\}\,$$) então o código diz-se binário/ternário de **dimensão** $$\,\kappa\times m\,$$.
        2. O **espaço dos códigos/sinais**  identifica-se com o espaço vetorial  $$\,$$$$\,\mathbb{F}_q^m\,$$; se $$\,q=p^m\,$$ o código é binário/ternário de **tamanho**  $$\,n\times m\,$$
    3. Finalmente os espaços vetoriais  das mensagens e  dos códigos estão equipadas a mesma norma: o **peso de Hamming**. Recorde-se que essa norma se define como
                                                            $$\,\|y\| \;\equiv\; \#\{\,i\;|\; y_i \neq 0 \,\}$$
        A **distância de Hammin**g entre dois sinais $$\,y,x\in\mathbb{F}_q^n\,$$  será  $$\,\|x-y\|\,=\,\#\{\,i\;|\; x_i\neq y_i\,\}$$.


----------
## Códigos Lineares

Quando o espaço das palavras código se identifica com um sub-espaço linear do espaço de códigos, o código diz-se **linear.**   Nesse caso como o espaço das mensagens é sempre isomórfico com o espaço de códigos , vai existir uma função linear injetiva $$\,\varphi \,\colon\, \mathbb{F}_q^\kappa\, \to \, \mathbb{F}_q^n$$ que mapeia qualquer mensagem  $$\,m\,$$ na respetiva palavra-código  $$\,\varphi(m)\,$$. A constante $$\,\kappa\,$$ é a dimensão do espaço das palavras-código em  $$\,\mathbb{F}_q^n\,$$.

A função $$\,\varphi\,$$ é a **função geradora do código**  $$\,\mathcal{C}_q[n,\kappa]\,$$.

Num código  sistemático a função tem a forma $$\,\varphi(m) = m \,\|\, \rho(m)\,$$ com $$\,\rho \colon \mathbb{F}_q^\kappa \,\to\,\mathbb{F}_q^{n-\kappa}$$.  Num código linear a função $$\,\varphi\,$$ é representada por uma **matriz geradora**
                                                    $$\,G\in \mathbb{F}_q^{\kappa\times n}\,$$ 
de “rank” completo; isto é, as linhas da matriz são linearmente independentes. 

Neste modelo

                                                            $$\,y \,\equiv\, m\,G\,$$

é a palavra código determinada pela mensagem $$\,m\,$$.  Alternativamente, se $$\,g_i\in \mathcal{C}_q[n,k]\,$$  for a palavra-código que forma a $$i$$-ésima linha da matriz $$\,G\,$$, temos

                                                         $$y\;=\; \sum_{i=1}^k\;m_i\ast g_i$$


| Aparentemente existe uma grande analogia entre a noção de **código linear**  $$\,\mathcal{C}_q[n,\kappa]\,$$ e a de **reticulado**; ambos são gerados por combinações lineares de uma base finita; ambos têm matrizes geradoras e, como veremos adiante, matrizes de paridades.<br>Existe porém uma diferença essencial que faz com que sejam objetos diferentes: <br><br>1. um reticulado é formado pelas combinações lineares inteiras dos elementos da base<br>2.  um código linear é formado por combinações lineares em que os coeficientes são elementos do corpo $$\,\mathbb{F}_q$$. |

Por simples eliminação gaussiana é sempre possível determinar uma matriz  invertível $$\,S\in\mathbb{F}_q^{\kappa\times \kappa}\,$$  tal que, para alguma matriz $$\quad P \in \mathbb{F}_q^{\kappa\times(n-\kappa)}\,$$
                                               $$G'\,\equiv\, S^{-1}\,G = \, \begin{bmatrix} \mathbf{1}_\kappa  &\!|\!& P \end{bmatrix}$$
Note-se que $$\,G'\,$$ é uma matriz geradora de um código sistemático e tem-se
                                                  $$\,y \,=\,m\,G \; = \; (m\,S)\,G'\;$$
Por isso, com uma simples permutação da mensagem $$\,m\mapsto m\,S\,$$  consegue-se usar sempre um código sistemático equivalente ao código gerado por $$\,G\,$$.

Construa-se agora uma matriz
                                                              $$\,H\;\equiv \; U\,\begin{bmatrix} -P^\top &\!|\!& \mathbf{1}_{\ell}\end{bmatrix}$$
com $$\,\ell\equiv n-\kappa\,$$ e $$\,U\in\,\mathbb{F}_q^{\ell \times \ell}\,$$ , uma qualquer matriz invertível. 
Verifica-se imediatamente que
                                                 $$\,G\,H^\top\;\equiv\, \mathbf{0}$$
A matriz $$\,H\,$$ é a matriz geradora do código dual de $$\,\mathcal{C}\,$$; isto é, o código formado por todas as palavras que são ortogonais a qualquer palavra-código em $$\,\mathcal{C}\,$$. Esta matriz designa-se por **matriz de paridades** e o código pode ser igualmente determinado como

                                                  $$\mathcal{C}_q[n,\kappa]\;\equiv\; \{\,y\in \mathbb{F}_q^n\;|\; y\,H^\top \,=\,0\,\}$$ 


----------


## Distância mínima

Os erros  $$\,e \in \mathbb{F}_q^n\,$$ são interpretados de forma aditiva; por isso, o código corrupto identifica-se com um sinal da forma

                                                        $$y' \,\equiv\, y + e\,$$
                                

Como referimos o sinal $$\,y'\,$$  é recuperável quando não existe ambiguidade em localizar a palavra-código $$\,y\,$$ que está “mais próximo”  de $$\,y'\,$$. 
Para ajudar a formalizar esta ideia, ao código $$\,\mathcal{C}_q[n,\kappa]$$  associa-se um parâmetro  $$\,d\,$$ designado por **distância mínima**  que se define como

                                         $$d\,\equiv\;\min\,\{\|x-y\|\;|\; x,y\in\mathcal{C}_q[n,\kappa]\;\land\; x\neq y\,\}$$

Pela definição acima, a distância mínima $$d$$ também coincide com o mínimo tamanho das palavras-código não nula. Este parâmetro $$d\,$$ completa o trio de parâmetros fundamentais de um código linear no alfabeto $$\,\mathbb{F}_q\,$$que genericamente, passa a ser representado por

                                                                     $$\mathcal{C}_q[n,\kappa,d]$$

Obviamente só não existe ambiguidade na descodificação de $$\,y'\,$$ quando a sua distância mínima ao código é inferior a $$\,d/2\,$$. A distância mínima de um sinal a um  código $$\,\mathcal{C}\,$$ é definida como

                    $$\text{dist}(y',\mathcal{C})\, \equiv \,\min_y\,\{\,\|y'-y\|\;|\; y\in \mathcal{C}\, \}$$

Portanto só é possível descodificar  $$\,y'\equiv y + e\,$$  quando  $$\,\text{dist}(y',\mathcal{C}) \,< d/2\,$$ , o que é equivalente a dizer que $$\,y'\,$$ só são recuperáveis sinais se o   $$\,e\equiv y'-y\,$$ verifica $$\,\|e\| \,<\,d/2$$. 


![](https://paper-attachments.dropbox.com/s_3116C3C8734601EDA5CF47D8C58847BF6F6A366B159BEA712A204D8DD613F618_1590346860846_codigo0.png)

----------


## Taxa de codificação e taxa de erros.

Verificamos que se o sinal corrompido  $$y'$$ é recuperável,  então a sua distância a $$\,\mathcal{C}[n,\kappa,d]\,$$ é sempre inferior a  $$d/2$$. 

O inverso não é necessariamente verdade: pode acontecer que exista algum $$\,y'\,$$ cuja distância ao código seja inferior a $$\,d/2\,$$ e que não seja recuperável. 

Por isso faz sentido definir um limite superior para a distância ao código $$\,\mathcal{C}[n,\kappa,d]\,$$ dos sinais recuperáveis;

                                            $$t\;\equiv\;\max_y\;\{\text{dist}(y,\mathcal{C})\;|\;y\;\text{é recuperável}\}$$

Vimos que $$\,t< d/2\,$$ o que é equivalente à condição  $$\,d \geq 1+2\,t\,$$ . 

O parâmetro $$\,t\,$$ é a principal medida de “qualidade” do algoritmo de descodificação: determina o maior número de erros que a descodificação consegue recuperar.  Desta  forma, quando se verifica a igualdade $$\,d = 1 + 2\,t\,$$,  o código diz-se **perfeito**.

Frequentemente os limites $$\,\kappa\,$$ e $$\,t\,$$ ao tamanho das mensagens e ao tamanho dos erros, respetivamente, são expressos relativos ao tamanho $$\,n\,$$ dos códigos. Assim define-se o racional $$\,\kappa/n\,$$ , designado como **taxa de codificação** (“**code rate**”), e o racional $$\,t/n\,$$ , designado como  **taxa de erro** (**“error rate”).**

Um “limite teórico” para o melhor taxa de erro  é estipulado pela relação

                                                    $$\,t/n \leq 1 -\sqrt{\kappa/n}$$

Este é o limite alcançado por os melhores códigos algébricos usados em Criptografia: os códigos de Goppa e Reed-Solomon. No entanto estes códigos exigem algoritmos de descodificação demasiado complexos para serem  usados em  aplicações com recursos computacionais limitados. Por isso são frequentes códigos com menor conteúdo algébrico, com taxas de erro muito inferiores ao limite teórico, mas com algoritmos de descodificação mais simples.


# Problema da Descodificação

A descodificação é a operação crítica em qualquer código e, de certo modo, todo o código é construído de forma a optimizar os algoritmos de descodificação.

O problema da descodificação pode-se definir por uma linguagem na classe NP através de duas formas diferentes: via a matriz geradora $$\,G\,$$ ou via a matriz de paridades $$\,H\,$$.
Qualquer uma destas versões usa como parâmetro um domínio de “pequenos erros” $$\,\mathcal{S}\,$$; a versão via matriz geradora usa também  um espaço de mensagens $$\,\mathcal{M}\,$$.


    - $$\text{Decode}(\mathcal{S},\mathcal{M},G)\;\equiv\;\{\,y\;|\; \exists\,(e,x)\in \mathcal{S}\times\mathcal{M}\,\centerdot\, y = x\,G + e\,\}$$
    - $$\text{Decode}'(\mathcal{S},H)\;\equiv\; \{\,y\;|\; \exists\,e\in \mathcal{S}\,\centerdot\,e\,H =y\,H\,\}$$

Em função dos domínios $$\,\mathcal{S},\mathcal{M}\,$$ e das matrizes $$\,G,H\,$$ coloca-se a questão de saber classificar estes problemas: se são NP-Hard, NP-completos, simplesmente P ou pertencem a uma  qualquer classe de complexidade intermédia.

Numa perspetiva do objetivo principal da Teoria dos Códigos (recuperar mensagens que passam por uma transmissão ruidosa) é desejável que os problemas estejam na classe P: pretende-se descodificar um qualquer sinal corrupto da forma tão eficiente quanto possível.

Já nas aplicações criptográficas a situação é mais complexa porque descodificar implica, normalmente, revelar um segredo. Aqui é preciso controlar a complexidade do problema; a descodificação deve ser simples (na classe P) ou difícil (na classe NP-hard)  consoante o algoritmo  tem ou não acesso a uma “trapdoor” apropriada.

Como a complexidade da descodificação depende criticamente dos seus parâmetros é importante ver separadamente algumas situações que são relevantes ao uso de códigos em criptografia.


## Códigos Lineares Aleatoriamente Gerados (“random codes”)

Um código linear com alfabeto $$\,\mathbb{F}_q\,$$ e parâmetros $$\,[n,\kappa]\,$$ é completamente descrito por uma “string” de bits de tamanho limitado. De facto a matriz geradora $$\,G\in \mathbb{F}_q^{\kappa\times n}\,$$ exige, na pior das hipóteses,  $$\,|G|_{\max}\,\equiv\,\kappa\times n\times |q|\,$$ bits; do mesmo modo a matriz de paridades exige, na pior das hipóteses  $$\,|H|_{\max}\,\equiv\,(n-\kappa)\times n \times |q|\,$$ bits.


| Uma das matrizes $$G$$ ou $$H$$ faz parte da informação pública de qualquer estrutura criptográfica baseada em códigos. Uma implementação de um código binário (i.e. $$|q|=1$$) no nível de segurança de 128 bits, pode usar valores  $$\,n \approx 20\,000\,$$e $$\,\kappa\approx 10\,000$$, o que equivale a $$\,$$um tamanho da ordem de $$\,200$$ Mbits. |

Na maior parte das aplicações criptográficas essas descrições podem (e devem) ser comprimidas. De facto só são consideradas “práticas”  as descrições com tamanhos $$O(n)$$ ou inferiores.

Quando não for possível comprimir a descrição de $$G$$ ou de $$H$$ para além dos limites máximos, então temos um código aleatoriamente gerado. Um tal código pode ser visto como o “output” de um hash aleatório com o tamanho $$\,|G|_{\max}\,$$ ou $$\,|H|_{\max}\,$$.

Geralmente crê-se que o problema da descodificação de um “random code” é NP-hard e provavelmente NP-completo. Isto porque se sabe que todos os problemas conhecidos  considerados “difíceis”  são, diretamente ou indiretamente, redutíveis a esta descodificação.

Assim, se o que se pretende é escolher um problema verdadeiramente difícil para uma estrutura criptográfica quântico-imune, não é necessário ir além da descodificação de um “random code”.

No entanto não basta um problema difícil para se poder construir uma estrutura criptográfica que seja segura e, adicionalmente,  eficiente tanto em tempo como, principalmente, em espaço.

De facto, um código cuja descrição é aleatoriamente gerada, tem duas dificuldades principais:

    - não é compressível e, por isso, não produz um criptosistema “prático”.
    - não permite “trapdoors” e, portanto, o problema da descodificação não é “útil”.

Concretamente, um problema difícil só é criptograficamente útil se existir um mecanismo “privado” que permita a sua resolução: a “trapdoor”. Algo que seja gerado de forma realmente aleatória não pode possuir um tal mecanismo.

Para compatibilizar estes dois requisitos as técnicas criptográficas “code-based” usam duas descrições do mesmo código: uma **descrição pública** que “aparenta” ser aleatoriamente gerada, e a partir da qual não é possível descodificar, e uma **descrição privad**a a partir da qual é possível construir um algoritmo de descodificação eficiente.

Vamos concretizar estes princípios em algumas classes de códigos.


## Códigos LDPC (“low density parity check”)

Os códigos LDPC estão numa situação intermédia entre os códigos ditos “algébricos” e os códigos aleatoriamente gerados.

Tal como os códigos algébricos os códigos LDPC possuem um algoritmo de descodificação eficiente; de facto o algoritmo é simples de tal forma que pode ser implementado em *”hardware”*. Por outro lado não tem a capacidade de recuperação de erros que é típica dos bons códigos algébricos.

Os códigos LDPC binários são determinados completamente por matrizes de paridade

                                       $$\,H\,\in\, \{0,1\}^{\ell\times n}$$   com $$\, n \geq 2\,\ell$$

geradas de forma “pseudo-aleatória” e sujeitas às seguintes restrições:

    - A matriz é de “rank” completo: o conjunto das suas linhas forma uma base em $$\{0,1\}^n$$,
    - As várias colunas $$\,h_j\in\{0,1\}^\ell\,$$ são vetores em que o peso de Hamming $$\,|h_j|\,$$ é muito inferior ao tamanho $$\,\ell\,$$ desses vetores. Esta é a razão porque os códigos são designados por “low density parity check”.
| Uma geração pseudo-aleatória de $$\,H\,$$ define um valor $$\,w \,\ll\,\ell\,$$ e gera   independentemente $$\,n\,$$  vetores  $$\,h_j\,$$ forçando a condição  $$\,|h_j| = w\,$$ para todos os $$j$$’s. <br>No final verifica-se se eles são linearmente independentes; se não forem repete-se este processo. <br> <br>Na maioria dos casos, porém, as matrizes $$\,H\,$$ são definidas por blocos de matrizes cíclicas. Nesse caso, como adiante se vê, os $$\,h_j\,$$ são vetores de coeficientes de polinómios. <br>Partindo de um polinómio “disperso”, com apenas $$\,w\,$$coeficientes não-nulos, os diversos $$\,h_j\,$$ são rotações desse polinómio. Por isso têm o mesmo número de coeficientes não-nulos e são linearmente independentes. |

Neste modelo o síndroma $$\,s\,\equiv \, y\,H^\top\,$$ , de um sinal  $$\,y\in \{0,1\}^n\,$$, calcula-se simplesmente como
                                                    $$\,s \,=\,\sum_{y_j\neq 0}\,h_j$$
                                                    
Note-se que uma palavra código $$\,y\in \mathcal{C}\,$$ verifica   $$\,y\,H^\top\,=\,0\,$$ o que é equivalente a escrever
                                                           $$\sum_{j=1}^n\,y_i\,h_{j,i}\,=\,0\;$$   para todo  $$i=1..\ell$$
                                                           
Pode-se interpretar esta relação com um sistema de $$\,\ell\,$$ equações em $$\,n\,$$ variáveis $$\,y_j\,$$. Estas equações designam-se **equações de paridade.**
Quando ****$$\,y\,$$ é uma palavra código todas as equações são verificadas.

Quando $$\,y\,$$ não é uma palavra código  e se tem um síndroma não-nulo $$\,s \equiv y\,H^\top\,$$ então as posições $$i$$ onde $$\,s_i\neq 0\,$$ identificam as equações de paridade que  não são verificadas. 
Genericamente  um vetor $$\,s\in \{0,1\}^\ell\,$$ pode-se interpretar também como um conjunto   de posições $$\,s \subseteq \{1..\ell\}\,$$ ; neste exemplo, $$\,s\,$$ denota o conjunto das paridades não verificadas.

Do mesmo modo, vendo cada coluna $$\,h_j\,$$  como um conjunto de potencias paridades, a interseção  $$\,s \cap h_j\,$$ denota o conjunto das paridades não verificadas onde $$\,h_j\,$$intervém. Obviamente $$\,|s\cap h_j|\,$$denota o número de essas equações não verificadas.

A definição do síndroma pode-se escrever
                                                  $$\,s\,=\, \sum_{y_j\neq 0}\,s\cap h_j$$
                                                  
Esta é a relação básica que permite definir um algoritmo iterativo onde passo a passo se vai alterando os bits  $$y_j$$ e atualizando o valor de $$\,s\,$$ até que no final a única solução possível da equação acima é $$\,s = 0\,$$. 

O algoritmo que obedece a este princípio designa-se por **bit-flip** e conceptualmente é muito simples.    

Como “inputs” o algoritmo recebe 

1. o conjunto de $$n$$ vetores $$\,{h_j}\,$$, que  formam a matriz de paridades $$H$$
2. um código $$\,y\,$$ e o seu síndroma $$\,s\equiv y\,H^\top\,$$

O “output” é a palavra código $$\,x\,$$ recuperada do código corrupto $$y$$.

| $$\mathbf{BitFlip}(\,\{h_j\}\,,\,y\,,\,s\,)$$<br>       $$x \gets y$$                                                  — nova *palavra código* <br>       $$z \gets s$$                                                  — *novo síndroma* <br>       $$\mathbf{while}\;z\neq 0\;\colon$$<br>              $$\mathbf{for}\;j\in\{1..n\}\;\colon$$<br>                    $$\mathbf{if}\,|z\cap h_j|\;\text{é grande}\;\colon$$<br>                          $$x_j\gets \neg\;x_j\;$$                       — *o bit flip* : *atualização da palavra código*<br>                          $$z\; \gets z + h_j$$                     — *atualização do síndroma*                    <br>      $$\mathbf{return}\;x$$ |

Se os vetores $$\,h_j\,$$ têm muito poucas componentes não nulas e os erros de codificação forem baixos, então este algoritmo converge. Devido à sua simplicidade o algoritmo “bit flip” é muitas vezes implementado em *hardware*.

O algoritmo é objeto de muitas optimizações. Nomeadamente a operação crítica é a que implementa o critério  “ $$\,|z\cap h_j|\;\text{é grande}\;$$” porque é ela que determina a sua convergência.

Também é crítica a estratégia para armazenar os vetores $$\,\{h_j\}\,$$: normalmente não é possível armazenar explicitamente todas as componentes destes vetores (o que aliás é inútil porque a maioria são zeros), A importância deste ponto é óbvia quando o código lida com valores da ordem de  $$\,n\approx 20\,000\,$$,  $$\,\ell\approx 10\,000\,$$ e, em cada vetor $$\,h_j\,$$, poucas componentes ($$\approx 70\,$$) são não nulas. Por isso é mais eficiente armazenar apenas as posições ****onde aparecem esses bits $$1$$.

Um outros aspeto é o facto de (quase sempre) as matrizes de paridade  $$\,H\,$$ são **quasi-cíclicas** : isto é, são matrizes por blocos em que todos os blocos não-nulos são matrizes cíclicas.
Como sabemos uma matriz cíclica é completamente determinada pela primeira linha; portanto cada bloco não nulo é descrito pela sua primeira linha e pela sua posição na matriz  $$\,H\,$$.
Quando $$H\,$$ é formada por muitos blocos cíclicos pequenos, a primeira linha de cada bloco é descrita explicitamente por um vetor com a dimensão do bloco. Ao invés, quando $$\,H\,$$tem  poucos blocos cíclicos mas  grandes, a primeira linha de cada um é descrita pelas posições dos seus bits $$1$$, relativas à posição do bloco em $$\,H\,$$.



## Um exemplo: o criptosistema BIKE

O criptosistema BIKE é um KEM que aparece como um dos candidatos na concurso PQC-NIST.

É baseado num código LDPC em que a matriz de paridade $$\,H\in \mathbb{F}_2^{\ell\times n}$$, com $$\,\ell\,$$ primo e $$\,n = 2\,\ell$$.


                                              $$H^\top\,=\,\begin{pmatrix} \mathbf{rot}(h_0)\\ \text{---}\text{---}\text{---}\\ \mathbf{rot}(h_1) \end{pmatrix}$$

A “trapdoor” aqui deriva do facto de, sendo $$(h_0\,,\,h_1)\,$$ polinómios dispersos (com muito pouco coeficientes não-nulos), é possível usar o algoritmo Bit-Flip para descodificar um código associado a pequenos erros.  Se $$\,H\,$$ não tiver esta forma ou os polinómios $$\,(h_0,h_1)\,$$ não forem dispersos, não é viável efectuar qualquer descodificação.

A estrutura algébrica básica é o anel de polinómios  $$\,\mathcal{R}\,\equiv\, \mathbb{F}_2[w]/(w^\ell +1)\,$$ .
Os polinómios  $$h_0,h_1\in \mathcal{R}\,$$ são mónicos, são  “dispersos” (têm poucos coeficientes não-nulos) e são invertíveis em $$\mathcal{R}$$. Estes dois polinómios determinam completamente a matriz de paridade.

Sejam $$\,|h_0|, |h_1|\,$$ os pesos de Hamming dos vetores de coeficientes de cada um dos polinómios. As condição de geração exigem que se verifique  $$\,|h_0| = |h_1| \ll \ell\,$$. Típicamente $$\,\ell\,$$ é da ordem das dezenas de milhar enquanto que $$\,|h_0|=|h_1|\,$$ é da ordem da dezena.

A matriz geradora do código é definida também por duas matrizes cíclicas geradas por polinómios invertíveis $$\,g_0,g_1\in \mathcal{R}\,$$
                                               $$G\,=\, \begin{pmatrix} \mathbf{rot}(g_0) &\!\!|\!\!&\mathbf{rot}(g_1) \end{pmatrix}\,$$
calculados de forma a que se verifique a relação fundamental  $$\,G\,H^\top = \mathbf{0}$$.
                                          $$\,G\,H^\top \;\equiv\; \mathbf{rot}(g_0*h_0 + g_1*h_1)$$
Por isso, pode-se descrever a matriz de paridade $$\,H\,$$ pelo par de polinómios   $$\,\mathcal{H}\,\equiv\,(h_0\,,\,h_1)\,$$ e descrever a matriz geradora $$\,G\,$$ pelo par $$\,\mathcal{G}\,\equiv\,(g_0\,,\,g_1)\,$$. 
O produto $$\,G\,H^\top\,$$ é o produto interno dos dois vetores $$\,\mathcal{G}\cdot\mathcal{H}\,$$; por isso a relação fundamental escreve-se    $$g_0\ast h_0 \,+\,g_1\ast h_1 \,=\, 0$$ o que é equivalente a afirmar

                                $$g_1 \,=\,g_0\ast h_0\ast h_1^{-1}$$

**KeyGen** 
Uma vez gerado $$\,(h_0\,,\,h_1)\,$$ existem várias hipóteses para definir $$\,(g_0\,,\,g_1)\,$$. Sendo  $$\,\mu\in\mathcal{R}\,$$ um polinómio denso ($$\,|\mu| \approx \ell/2\,$$) , invertível e aleatoriamente gerado, pode-se definir:

    - $$\,g_0 \equiv\, \mu\ast h_1\,$$           e    $$g_1 \,\equiv \,g_0\ast h_0\ast h_1^{-1}\,=\,\mu\ast h_0$$
    -  $$g_0 \equiv 1$$                     e    $$g_1 \,\equiv \,g_0\ast h_0\ast h_1^{-1}\,=\, h_0\ast h_1^{-1}$$

A chave privada é  $$\,\mathbf{sk}\,\equiv\,(h_0\,,\,h_1)\,$$ e a chave pública é o par $$\,\mathbf{pk}\,\equiv\,(g_0,g_1)\,$$
Note-se que

        1.  Em nenhum dos casos é possível recuperar $$(h_0,h_1)\,$$ a partir de $$(g_0,g_1)$$.
        2. Enquanto que $$\,(h_0,h_1)\,$$ é dispersa, $$\,(g_0,g_1)\,$$ é densa e não é viável computar uma matriz de paridade dispersa para esta matriz geradora.

**Encaps** : abordagem McEliece para um KEM-CPA
Usa a chave pública $$(g_9,g_1)$$

        i. Gerar aleatoriamente pequenos erros $$\,e_0,e_1 \in \mathcal{R}$$. A chave encapsulada é o “hash” 
                                                    $$\,\text{key} \,\gets\, \text{Hash}(e_0,e_1)$$
        ii. Gerar aleatoriamente $$\,r \gets \mathcal{R}\,$$ denso. O encapsulamento da chave é o código
                                          $$\,(y_0,y_1)\,\gets\,(r*g_0+e_0\,,\,r*g_1+e_1)$$

**Decaps**
Usa a chave privada $$(h_0\,,\,h_1)\,$$ e o encapsulamento $$\,(y_0\,,\,y_1)$$. 

        1. Calcula a matriz dispersa $$\,H\,$$ a partir do par de matrizes  cíclicas $$\,\mathbf{rot}(h_0)\,,\,\mathbf{rot}(h_1)\,$$e comprime-a de forma a ser manipulada eficientemente pelo algoritmo Bit-Flip. Para isso determina-se, para cada linha $$h_j$$ de $$H$$,  as posições das suas componentes não nulas.
        2. Descodifica-se $$\,(y_0,y_1)\,$$ com a ajuda do síndroma  $$\,s \equiv h_0\ast y_0 + h_1\ast y_1\,$$  ;  obtém-se assim os erros $$\,(e_0,e_1)\,$$ a partir dos quais se recupera  $$\,\text{key} = \text{Hash}(e_0,e_1)$$.

Este é um KEM-CPA. Para se obter um KEM-CCA2 usa-se, como é usual, a transformação de Fujisaki-Okamoto (ou uma sua variante) sobre este esquema CPA.



# Códigos Algébricos


## Motivação 

O problema que limita o uso dos códigos “Low Density” é a baixa eficiência do algoritmo de descodificação Bit-Flip: este algoritmo só consegue recuperar erros com um peso $$\,|e\,|$$ muito mais pequeno do que o comprimento do código: a taxa de erros é tipicamente inferior a $$1\%$$.
Dado $$|e|$$ é fundamentalmente determinado pelo nível de segurança criptográfica, isto implica que o código tem de ser muito longo para poder alcançar essa segurança.
Daqui deriva a necessidade de recorrer a técnicas de descrição implícita (“sparse matrices”) dos vários elementos do código; nomeadamente as matrizes geradoras e de paridade. Por isso se recorre com frequência a matrizes cíclicas onde a matriz é completamente descrita por um polinómio.

Os **códigos algébricos** , derivados de anéis de polinómios, são muito mais eficientes. Num código $$\,[n,\kappa,d]\,$$ perfeito, pode obter-se taxas de de erros $$\,t/n\,$$não superiores a  $$\,1 -\sqrt{\kappa/n}$$ .
Em contrapartida, a sua estrutura algébrica uma forma de matrizes geradoras ou de paridade que não é compatível com uma estrutura cíclica; essas matrizes têm de ser explicitamente descritas e daqui  resultam grandes chaves públicas.

Dado um código algébrico $$\,\mathcal{C}\,$$existem dois modelos fundamentais para a criação de um PKE: o modelo de McEliece e o modelo de Niederreiter.
Em ambos os modelos, o algoritmo de descodificação é um problema difícil mas com *trapdoor.* 

**Modelo McEliece.**

    1. **KeyGen**
        A trapdoor é uma matriz $$\,G\,$$ geradora do código com uma forma particular que permite resolver o problema da descodificação.
        A chave pública é uma outra matriz geradora $$\,G'\,$$ do mesmo código que resulta da “ofuscação aleatória” da matriz $$G$$.  Define-se 
                                                              $$\,G' \,\equiv\, S^{-1}\; G \; P^{-1}\,$$
        em que $$\,S\,$$ é uma permutação do espaço das mensagens, e $$P$$ uma permutação das posições dos símbolos do código, ambas aleatoriamente geradas. A chave privada é o triplo $$\,(G,S,P)\,$$. 
    2. **Encrypt** 
        Para cifrar uma mensagem $$\,m\,$$ com a chave pública $$\,G'\,$$, gera-se um erro $$\,e\,$$ com peso de Hamming limitado a $$\,t\,$$ e calcula-se o criptograma  $$\,y \equiv m\,G' + e\,$$.
    3. **Decrypt** 
        Para decifrar o criptograma $$\,y\,$$ com a chave privada $$\,(G,S,P)\,$$
        1. Calcula-se $$\,e' \,\equiv\, e\,P\,$$  e $$\,y'\equiv\,y\,P\,$$.  Estas dois códigos verificam a relação
                                                        $$y'\,=\,(m\,S^{-1})\,G + e'$$ 
        2. Como $$\,P\,$$ apenas permuta as posições dos símbolos o código $$\,e'\,$$ tem o mesmo peso do que $$\,e\,$$. Usando a matriz $$\,G\,$$, parte da chave privada, e o algoritmo de descodificação consegue-se descodificar  $$\,y'\,$$ e recuperar uma mensagem  $$\,m'\equiv m\,S^{-1}$$.
        3. Recupera-se $$\,m\,$$  como   $$\,m = m'\,S$$ .

**Modelo Niederreiter**

    1. **KeyGen** 
        A trapdoor é uma matriz de paridade $$\,H\,$$ com uma forma particular que permite resolver o problema da descodificação do síndroma
        A chave pública é uma outra matriz de paridades $$\,H'\,$$, para o mesmo código, que resulta da “ofuscação aleatória” da matriz $$\,H\,$$.  Define-se 
                                                              $$\,H' \,\equiv\, P^{-1}\; H \; S^{-1}\,$$
        sendo $$\,S\,$$ é uma permutação do espaço dos síndromas, e $$P$$ uma permutação das posições de símbolos do código, ambas aleatoriamente geradas. A chave privada é $$\,(H,S,P)\,$$. 
    2. **Encrypt** 
        Para cifrar $$\,m\,$$identifica-se esta informação com um código com um peso de Hamming limitado a $$\,t\,$$. O criptograma é o sindroma $$\,s \equiv m\,H'\,$$.
    3. **Decrypt** 
        Para decifrar $$\,s\,$$, com a chave privada  $$\,(H,S,P)\,$$
        1. Calcula-se $$\,s' \equiv s\,S\,=\,(m\,P^{-1})\,H$$.
        2. Com o algoritmo da descodificação e a *trapdoor* $$\,H\,$$ determina-se o código $$\,m' \equiv m\,P^{-1}\,$$.
        3. Recupera-se  $$\,m\,=\,m'\,P\,$$.

Tal como no modelo McEliece, em cada um dos  três passos do algoritmo de decifrar, intervém um dos elementos da chave privada. A chave  pública tem um único passo e um único elemento.


## Códigos de Goppa

Os códigos de Goppa formam a classe dos códigos algébricos mais usados nestes tipos de aplicações criptográficas. Não sendo os únicos são os mais frequentes porque, apesar de serem usados há mais de 40 anos, até ao momento nunca a combinação Goppa+McEliece sofreu um ataque com sucesso. 

Vou basear esta secção a duas das candidaturas ao concurso NIST-PQC [nesta diretoria](https://www.dropbox.com/sh/ziskln06b98wedu/AABnVRx5TqdTLb_BNW4SO3LHa?dl=0): o **Classical McEliece** e  o **NTS-KEM**.

Um código de Goppa binário ($$\,\text{BGC}\,$$)  usa o corpo de bits $$\,\mathbb{F}_2\,$$  e a sua extensão $$\,\mathbb{F}_{q}\,$$  , com $$\,q=2^m\,$$.  Usa também  os anéis de polinómios  $$\,\mathcal{R}\,\equiv\,\mathbb{F}_2[w]\;\;\text{e}\;\;\mathcal{R}_q\,\equiv\,\mathbb{F}_q[w]$$.  

| Formalmente é conveniente referir também o fecho algébrico  $$\,\overline{\mathbb{F}_{2}}\,\simeq\, \bigcup_{m\geq 0}\,\mathbb{F}_{2^m}$$: isto é, o corpo formado por todas as raízes de todos os elementos de $$\,\mathcal{R}\,$$. O anel $$\,\overline{\mathcal{R}}\,$$ é formado  pelos polinómios com coeficientes nesse fecho algébrico.<br><br>Nestes anéis de polinómios, a derivada $$\,f'\,$$ é o polinómio  que se define recursivamente pelas regras:  $$f' = 0\,$$ se $$\,\deg  f = 0\,$$; $$\;(f+g)' = f' + g'\;$$ e  $$\;(f\ast g)' = f'\ast g + f\ast g'$$.<br><br>Quando se pretende especificar que um polinómio $$\,h\in \mathcal{R}_q\,$$ não tem raízes múltiplas, basta dizer que $$h$$ e a sua derivada não têm raízes comuns. Ou seja<br>                                                                      $$\,\deg\,\gcd(h,h')\,=\,0$$<br>O máximo divisor comum é sempre interpretado como um elemento de $$\,\overline{\mathcal{R}}$$. |

Neste contexto é necessário  identificar representações explícitas dos elementos de $$\,\mathbb{F}_q\,$$. Para tal

    - Define-se um polinómio $$\,\phi\in\mathcal{R}\,$$ mónico, de grau $$\,m\,$$ e irredutível nesse anel,   de tal forma que se pode identificar $$\,\mathbb{F}_q\,\simeq\,\mathcal{R}/\phi\,$$.  
    - Os elementos de $$\,\mathbb{F}_q\,$$ podem-se também identificar como as raízes do polinómio definidor
                                                    $$\,\tau_q(w) \,\equiv\,w^q+w$$

Um $$\text{BGC}$$ é um código  $$\,[n,\kappa,d]$$   sobre   $$\,\mathbb{F}_2\;$$ que verifica as seguintes condições:


1. Os parâmetros $$\,[n,\kappa,d]\,$$ satisfazem
    - $$\,m\,t < n \leq q\quad$$ sendo $$\,t\equiv\,\lfloor \frac{d-1}{2}\rfloor\,\geq\, 2$$
    - $$\,\kappa = n - m\,t$$


2. Existe $$\,f\in\mathcal{R}_q\,$$ mónico, de grau $$\,n\,$$ com $$\,n\,$$ raízes distintas em $$\mathbb{F}_q\,$$. As raízes de $$\,f\,$$ designam-se por **localizações** do código.  Formalmente estas condições são equivalentes a
                         $$\deg\, \gcd(f,\tau_q)\,=\,n\quad$$e $$\quad \deg\,\gcd(f,f')\,=\,0$$
                
3. Existe um **módulo**  $$\,g\in\mathcal{R}_q\,$$ de grau $$\,t\,$$ sem raízes múltiplas e sem raízes comuns a $$\,f\,$$.  Formalmente 
              $$\deg\,\gcd(g,\tau_q)\,=\,t\;$$, $$\quad\deg\,\gcd(g,g')\,=\,0\;$$,  $$\quad\deg\,\gcd(g,h)\,=\,0$$

Os parâmetros $$\,[n,\kappa,d]\,$$ e o par de polinómios $$\,f,g\in \mathcal{R}_q\,$$ determinam completamente o código Goppa e através deles é possível, como veremos, desenvolver um algoritmo de descodificação eficiente.  Assim $$f,g$$ (ou só $$g$$) são a chave privada dos criptosistemas que usam esse código.

| Existem várias variantes dos $$\text{BGC}$$’s  que dependem da escolha do comprimento do código e do polinómio $$\,h\,$$. Por exemplo<br><br><br>1. *Quando* $$\,n < q\,$$ *é primo e verifica*  $$\, q\,\equiv 1  \mod n$$<br>    Neste caso, o corpo $$\,\mathbb{F}_q\,$$ contém todas as raízes da unidade de ordem $$\,n\,$$. O polinómio da localizações é simplesmente  $$\,f(w) \equiv\, w^n+1$$.<br><br>     As $$n$$-raízes da unidade formam um grupo multiplicativo cíclico $$\,\mathcal{L} \equiv \{z^i\}_{i=0}^{n-1}\,$$  sendo $$z\neq 1$$  uma qualquer      dessas raízes. Para definir a sequência de localizações basta especificar esse $$z$$.<br>     Esta é a variante que aqui vai ser desenvolvida.<br>  <br>  <br><br>2. *Quando* $$\,n = q\,$$<br>    Dado que, neste caso, existem $$\,2^m\,$$ localizações distintas em $$\,\mathbb{F}_q\,$$e o corpo tem exatamente este número de elementos, todo o elemento do corpo é uma localização. <br>    O  polinómio das localizações é  $$\,f(w)\,\equiv\,\tau_q(w)\,\equiv\, w^n + w\,$$. A sequência de localizações $$\,\mathcal{L}\,$$ é uma qualquer permutação dos elementos de $$\,\mathbb{F}_q$$ .<br>    Esta é a variante usado no NTS-KEM.<br><br><br>3. *Quando* $$\,n< q\,$$ *e é definido um subconjunto de* $$\,\mathbb{F}_q\,$$ *de cardinalidade* $$n$$*.*<br>    Seja  $$\,\mathcal{L}\,\equiv\,\{z_0,z_1,\cdots,z_{n-1} \}\,\subset\,\mathbb{F}_q\,$$ a sequência das localizações. Então o polinómio $$\,f(w)\,$$é dado por   $$\,f(w)\,\equiv\, \prod_{i=1}^n\,(w + z_i)$$.<br>    Esta é a variante usada no Classical McElice<br><br>Acrescentar uma nota |


**Desenvolvimento**

Seja $$\,\mathcal{L}\,$$ a sequência de localizações. Para cada $$\,z\in \mathcal{L}\,$$ defina-se $$\,h(z)\in\mathcal{R}_q\,$$ como o polinómio de menor grau que verifica  
                                              $$\quad h(z,w)\ast (w+z)\,\equiv\, 1 \bmod g(w)\,$$
O polinómio $$\,h(z)\,$$ existe porque, por hipótese,  $$\,\deg_w \,\gcd(w+z,g(w)) = 0$$. Com um pouco de liberdade de expressão pode-se representar
                                          $$\,h(z,w)\;\equiv\;1/(w+z) \mod g(w)$$

Finalmente, para cada   subconjunto $$\,\mathcal{U}\subseteq \mathcal{L}\;$$ defina-se

               $$\,h_\mathcal{U}(w)\;\equiv\; \sum_{z\in\mathcal{U}}\,h(z,w)\quad$$     e      $$\quad f_\mathcal{U}(w)\;\equiv\; \prod_{z\in\mathcal{U}}\,(w + z)$$
    

É relativamente simples provar 
**Proposição**  

> $$h_\mathcal{U}\,,\,f_\mathcal{U}\,$$  são polinómios de grau $$t$$ e $$\,\#\mathcal{U}\,$$, respetivamente,  que verificam
>                                                            $$\,f'_\mathcal{U} \equiv f_\mathcal{U} \ast h_\mathcal{U} \mod g$$

Para provar este resultado basta calcular o produto $$\,f\ast h\bmod g\,$$ e comparar com a derivada $$f'$$. Note-se que por $$\,h,f\,$$  verificarem a propriedade não significa que sejam únicos. Para termos um resultado semelhante em que se verifica a unicidade  temos de ter algo um pouco diferente.

**Teorema da descodificação dos códigos de Goppa**

> Seja $$\,\mathcal{U}\subset \mathcal{L}\,$$ um qualquer subconjunto desconhecido do conjunto de localizações. Sejam
> $$\,h_\mathcal{U}\,$$ e  $$\;f_\mathcal{U}\;$$ como acima e suponhamos que $$\,$$$$\,h_\mathcal{U}\,$$ é conhecido.
> Então, se $$\,\#\mathcal{U}\, \leq \,t\,$$,  existe um algoritmo eficiente  que determina   $$\,f_{\mathcal{U}}$$  de grau menor ou igual a  $$\,t\,$$, que é a   única solução de
>                                                     $$\,f'_\mathcal{U}\;\equiv\; f_\mathcal{U}\ast h_\mathcal{U}\mod g$$

Note-se que, mesmo que $$\,\mathcal{U}\,$$ seja desconhecido, a proposição anterior assegura que  relação se verifica. A dificuldade está em provar que, quando $$\,h_\mathcal{U}\,$$ é conhecido,  o polinómio $$\,f_\mathcal{U}\,$$ é o único que verifica a equação e pode ser calculado a partir dela.

Note-se também que, a partir de $$\,f_\mathcal{U\,}$$,  se consegue recuperar o conjunto $$\,\mathcal{U}\,$$ como
                                      $$\mathcal{U}\;\equiv\;\{\,z\in\mathcal{L}\;|\; \deg_w\,\gcd(w+z,f_\mathcal{U}(w))\,=\,1\,\}$$

Existem vários algoritmos eficientes que determinam $$\,f_\mathcal{U}\,$$. O mais conhecido é [o algoritmo de Sardinas-Patterson](https://www.dropbox.com/s/bjo60d1qhtmkgu0/salinas-patterson.pdf?dl=0) que pode ser consultado na documentação da disciplina mas, por falta de tempo e espaço, não vamos aqui reproduzir.

**Palavras Código, síndromas e descodificação.** 


1. Os **sinais** no código de Goppa $$\,(f,g)\,$$  são os subconjuntos $$\,\mathcal{U}\subseteq \mathcal{L}\,$$.   
    Como $$\,\mathcal{L}\,$$ tem $$\,n\,$$ elementos, fixando uma enumeração desses elementos, cada sinal pode ser representado por uma palavra de bits   $$\,u\in \mathbb{F}^n_2\,$$  tal que $$\,u_i = 1\,$$ se e só se $$\,z_i\in \mathcal{U}\,$$.


2. O polinómio $$\,h_\mathcal{U}\in \mathcal{R}_q\,$$, de grau menor do que $$\,t\,$$ , é o **síndroma** do sinal $$\,\mathcal{U}$$.


3. As **palavras código** são os sinais $$\,\mathcal{C}\,$$ que verificam $$\,h_\mathcal{C}\,=\,0$$


4. **Descodificar** um sinal  $$\,\mathcal{U}\,$$ é determinar a palavra código $$\,\mathcal{C}\,$$ que se distingue de $$\,\mathcal{U}\,$$ em $$t$$ ou menos posições.


5. Processo de **descodificação** de um sinal $$\,\mathcal{U}$$
    1. Calcular $$\,$$o síndroma  $$\,h_\mathcal{U}\,$$.
    2. Usando o teorema da descodificação de Goppa acima,  determinar um polinómio $$\,f_\mathcal{V}\,$$ de grau menor ou igual a $$t$$ , solução da equação
                                                         $$\,f'_\mathcal{V}\,\equiv\,f_\mathcal{V}\ast h_\mathcal{U}\mod g$$
    3. Factorizando $$\,f_\mathcal{V}\,$$ ou calculando os sucessivos  $$\,\gcd(f_\mathcal{V}(w),w+z)\,$$, para todo $$\,z\in\mathcal{L}\,$$, determina-se o conjunto de erros $$\,\mathcal{V}\,$$
    4. Determina-se a palavra código $$\,\mathcal{C}\,$$  corrigindo em $$\,\mathcal{U}\,$$ todos os valores que ocorrem em $$\,\mathcal{V}\,$$
                           $$\,z\in \mathcal{C}\quad\mathbf{sse}\quad z \in \mathcal{U}\quad\mathbf{xor}\quad z\in\mathcal{V}$$



