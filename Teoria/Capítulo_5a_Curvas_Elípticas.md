# Capítulo 5a: Curvas Elípticas

## Breve Introdução à Geometria Algébrica

A disciplina da Matemática designada por **Geometria Algébrica** estuda formas geométricas cujos pontos são soluções de equações polinomiais a várias variáveis. 
Nomeadamente a forma mais direta de representar uma **curva**  **plana** é via o conjuntos de raízes, num espaço a duas dimensões, de um polinómio a duas variáveis.

Por exemplo um círculo de raio unitário num plano real  $$\,\mathbb{R}^2\,$$ é definido como o conjunto de pontos $$\,P \equiv (x,y)\,$$ cujas coordenadas verificam a equação

                                        $$\,x^2 + y^2 = 1\,$$. 

Equivalentemente a curva é definida como o conjunto das raízes em $$\,\mathbb{R}^2\,$$ do polinómio
                                                   $$\varphi(x,y)\;\equiv\, x^2 + y^2 - 1$$

| É possível descrever curvas em espaços de maiores dimensões. Por exemplo, no espaço $$\,\mathbb{R}^3\,$$ um polinómio a três variáveis como <br>                                   $$\varphi(x,y,z)\;\equiv\; x^2+y^2 + z^2 - 1$$<br>descreve uma **superfície esférica** e não uma curva.<br>Para descrever um curva temos de acrescentar um segundo polinómio, por exemplo,<br>                                   $$\,\phi(x,y,z)\;\equiv\;x + y + z$$<br>cujas raízes formam um **plano** que passa pela origem. A **interseção** destas duas superfícies forma uma curva.<br><br>Esta curva (que também é um círculo) é agora descrita por um sistema de 2 equações a três variáveis<br>                                     $$\left\{\begin{array}{lcc} x^2+y^2+z^2 &=& 1\\ x + y + z &=&0\end{array}\right.$$<br>Genericamente, num espaço a $$\,n\,$$ dimensões, uma curva é descrita por um sistema de $$(n-1)$$ equações polinomiais a $$\,n\,$$ variáveis. |

Neste curso estamos apenas interessados em curvas planas com coordenadas num corpo genérico $$\,K\,$$ geradas como raízes de polinómios a duas variáveis $$\,\phi\in K[x,y]\,$$.

Tal curva diz-se **irredutível** se, no anel  $$\,K[x,y]\,$$,  o polinómio $$\,\phi\,$$ não tiver outros divisores que não os triviais (i.e. a constante $$\,1\,$$ ou o próprio $$\,\phi\,$$). A curva diz-se **absolutamente irredutível** quando, no anel $$\,\overline{K}[x,y]\,$$,  o polinómio $$\,\phi\,$$ não tem qualquer divisor para além dos triviais.

Se nada for dito em contrário, a designação “curva plana” vais-se aplicar exclusivamente a curvas que, no mínimo, são irredutíveis.
 
Tomando por referência o plano $$\,\mathbb{R}^2\,$$ a geometria das curvas planas usa quase sempre dois tipos de coordenadas: **afins** e **projetivas**.  Esta mesma classificação vai-se também aplicar quando se considera, para um qualquer corpo $$\,K\,$$, o espaço vetorial dos pares  $$\,(x,y)\,$$  com  $$\,x,y\in K\,$$.

Os pontos de um plano definidos por um par de coordenadas $$\,(x,y)\,$$ designam-se por **pontos afins**.  O **espaço afim**, formado por todos  os pontos afins , representa-se  por 
                                                                       $$\mathbb{A}^2\,$$
Genericamente,  se for necessário tornar explícito o corpo $$\,K\,$$ onde as coordenadas $$\,(x,y)\,$$ tomam valores, então  usa-se a notação
                                                                  $$\mathbb{A}^2(K)\,$$

| **Exemplo**<br>No corpo dos reais, todos os pontos do círculo $$\,C:(x^2+y^2-1)\,$$  são afins. <br>Note-se que, explicitarmos o corpo no qual s coordenadas tomam valores, o mesmo polinómio define diferentes curvas contidas em diferentes espaços afins.<br>Nomeadamente<br><br>1.  Se considerarmos apenas as soluções racionais da equação $$\,x^2+y^2 = 1\,$$ definimos uma curva plana no espaço afim $$\,\mathbb{A}^2(\mathbb{Q})\,$$  que representamos por  $$\,C/ \mathbb{Q}:(x^2+y^2-1)\,$$.<br>2. De forma idêntica, considerando soluções reais dessa mesma equação, constrói-se uma curva contida no espaço afim $$\,\mathbb{A}^2(\mathbb{R})\,$$ que contém a anterior |


A maioria das curvas planas, para além dos pontos afins, contêm outros “pontos” designados por **pontos no infinito** ou também  **pontos de fuga**. Cada  ponto de fuga de uma curva $$\,C\,$$ descreve uma  direção assimptótica  dessa curva.

Um ponto de fuga pode ser visto, a duas dimensões, como uma **direção** ******do plano ****onde estará localizado esse “infinito”.  Porém, assim descrito, o ponto de fuga tem uma descrição completamente distinta da de um ponto afim. Para englobar num único sistema de coordenadas, pontos afins e pontos de fuga, necessitamos das chamadas **c*****oordenadas projetivas****.*

Um ponto do plano projetivo sobre um qualquer corpo $$\,K\,$$ é descrito por um triplo de elementos de $$\,K\,$$, escrito como

                                        $$(x\,\colon y\,\colon z)$$

em que pelo menos uma das componentes é não-nula. 
Um ponto projetivo pode ser descrito por vários destes triplos. Dois triplos $$\;(x\,\colon y\,\colon z)\;$$
e $$\;(x'\,\colon y'\,\colon z')\;$$ descrevem o mesmo ponto quando existe algum $$\,\lambda\neq 0\,$$ tal que 

                                        $$x\,=\,\lambda\, x'\;\land\; y\,=\,\lambda\,y'\;\land\; z\,=\,\lambda\,z'$$ 

Um triplo diz-se *normalizado* quando pelo menos uma das suas componentes é $$\,1\,$$. 

O **espaço projetivo** $$\,\mathbb{P}^2(K)\,$$ é formado por todos estes pontos projetivos.

Existe uma relação simples entre o espaço afim $$\,\mathbb{A}^2(K)\,$$ e o espaço projetivo  $$\,\mathbb{P}^2(K)\,$$.


1. O ponto afim genérico $$\,(x,y)\in\mathbb{A}^2(K)\,$$ é descrito, em $$\,\mathbb{P}^2(K)\,$$, pelo triplo normalizado   $$\,(x\,\colon y\,\colon 1)$$.
2. Os pontos de fuga são descritos por triplos em que a última componente é $$\,0\,$$. Nomeadamente 
        1. O ponto $$\,(0\,\colon 1\,\colon 0)\,$$ é aqui representado por $$\,\mathcal{O}\,$$ e descreve uma “direção vertical” para o infinito. Obviamente esta noção de direção só faz sentido quando o corpo $$\,K\,$$ coincide com os reais ou os racionais.
        2. Triplos da forma $$(1\,\colon y\,\colon 0)\,$$ descrevem direções assimptóticas de declive $$\,y\,$$. Nos reais ou racionais , $$\,y\,$$é a tangente do ângulo que a direção para o infinito faz com o eixo dos $$\,x$$’s. Os triplos da forma $$\,(x:1:0)\,$$ descrevem pontos no infinito definidos por direções com declive $$\,1/x\,$$.


![Exemplo de circulo, retas e pontos no infinito](https://paper-attachments.dropbox.com/s_3E3858162728746B0E2D03C7A4A48982BAEC2E3A2F876203D25AE73BFAEFF4F5_1617912576097_circulo.jpg)


As curvas no plano projetivo são definidas por **polinómios homogéneos** nas três variáveis $$\,x,y,z\,$$. 


| Um polinómio  $$\,\varphi(x,y,z)\,$$ de coeficientes no corpo $$\,K\,$$ é homogéneo quando todos os seus monómios têm o mesmo grau.  Exemplos<br><br><br>    - **Cónicas**  são polinómios homogéneos do 2º grau,  como<br>                             $$x^2 + y^2 - z^2\quad$$, $$\quad x\,z + x\,y + y\,z\quad$$, $$\quad x\,z - y^2 + z^2\;$$<br>    - **Retas**  são definidas por polinómios  homogéneos do 1º grau, como  $$\,a\,x + b\,y + c\,z\,$$,  para quaisquer  $$a,b,c \in K$$.<br>    - **Curvas elípticas** são definidas por polinómios homogéneos do 3º grau com uma forma particular<br>                                    $$z\,y^2 + a_1\,x\,y\,z + a_3\,y\,z^2 - x^3 - a_2\,z\,x^2 - a_4\,x\,z^2 - a_6\,z^3$$<br>          em que os coeficientes $$\,a_i\,$$ são elementos de $$\,K\,$$.<br>    <br><br>Polinómios homogéneos cúbicos, como o exemplo acima, dizem-se na **forma de Weierstrass .** <br>É imediato verificar que o ponto  $$\,\mathcal{O}\,=\,(0:1:0)\,$$ é o único ponto de fuga de uma curva descrita por um  polinómio na forma de Weierstrass. |


Algumas propriedades de polinómios homogéneos que são facilmente demonstráveis.
Seja  $$\,\phi(x,y,z)\,$$ um polinómio homogéneo de grau $$\,n\,$$


1. No espaço projetivo  as raízes de $$\,\phi\,$$ definem uma curva. Isto porque, para todo $$\,k\neq 0\,$$, tem-se

                                        $$\phi(k\,x,k\,y,k\,z)\;=\;k^{n}\,\phi(x,y,z)$$
      Portanto, se $$\,(x:y:z)\,$$ é raíz de $$\,\phi\,$$ então também $$\,(k\,x:k\,y:k\,z)\,$$ é raíz de $$\,x\,$$.


2. Para todo $$\,(x : y : z)\,$$ tem-se

                                        $$x\,({\partial \phi}/{\partial x}) \,+\,y\,({\partial \phi}/{\partial y}) \,+\,z\,({\partial \phi}/{\partial z}) \;=\; n\,\phi(x,y,z)$$ 



## Curvas  no espaço $$\mathbb{P}(K)$$

O espaço projetivo $$\mathbb{P}^2(K)$$ é determinado pelo corpo $$\,K\,$$. Uma curva $$\,C/\phi\,$$ é gerada por um polinómio homogéneo não-nulo com coeficientes em $$\,K\,$$ e variáveis $$\,x,y,z\,$$.

A notação $$\,C/\phi\,$$ identifica o conjunto de todas as raizes do polinómio $$\,\phi\,$$ que tenham coordenadas no fecho algébrico $$\,\overline{K}\,$$

                               $$C:\phi \;\equiv\; \{\,(x,y,z)\in \overline{K}\;|\;\phi(x,y,z)=0 \,\}$$

Quando se pretende restringir as raízes a coordenadas em $$\,K\,$$, as chamadas **raízes racionais** usa-se a notação $$\,C/K:\phi$$.

                               $$C/K\colon\phi \;\equiv\; \{\,(x,y,z)\in{K}\;|\;\phi(x,y,z)=0 \,\}$$
                

Nomeadamente uma **reta** em $$\,\mathbb{P}^2(K)\,$$é o conjunto de raízes de um polinómio do 1º grau não-nulo

                                             $$r \;\equiv\; a\,x + b\,y + c\,z$$

Os coeficientes $$\,a,b,c\,$$ determinam a reta e não podem ser simultaneamente nulos.

Uma componente importante de cada curva $$\,\,C/\phi\,$$ é o conjunto das suas retas **tangentes.** 
Uma  ****reta tangente  a $$\,C/\phi\,$$ num ponto $$\,P\,$$ dessa curva, é determinada pelos coeficientes

            $$a_P\,\equiv\,\partial \phi/\partial x(P)\quad$$  , $$\quad b_P\,\equiv\,\partial \phi/\partial y(P)\quad$$,        $$c_P\,\equiv\,\partial \phi/\partial z(P)$$
            

A reta tangente não existe se todos estes coeficientes forem nulos. Os pontos da curva que não têm tangente designam-se por **pontos singulares**.  
Resumidamente, as primeiras derivadas do polinómio gerador $$\,\phi\,$$ caracterizam a tangência e os pontos singulares da curva são soluções $$(x,y,z)\,$$ do sistema de equações polinomiais

                         $$\{\,\phi = 0 \,,\,\partial\phi/\partial x = 0 \,,\,\partial\phi/\partial y = 0 \,,\,\partial\phi/\partial z = 0 \,\}$$
                

As segundas derivadas $$\;\partial^2\phi/\partial^2x\;,\;\partial^2\phi/\partial^2y\;,\;\partial^2\phi/\partial^2x\;$$ têm igualmente um papel importante na caracterização das curvas; genericamente determinam a curvatura da curva. Um ponto singular $$\,P\,$$onde pelo menos uma das segundas derivadas é não-nulo designa-se por **ponto duplo**. Se pelo menos uma das segundas derivadas é nula, o ponto designa-se por **ponto de inflexão**.


----------

**Exemplos**

Vamos considerar alguns polinómios geradores de curvas cúbicas no espaço projetivo $$\,\mathbb{P}^2(K)\,$$ e vamos tentar detetar eventuais pontos singulares e pontos de inflexão dessa curva.


1.   $$\,\phi\,\equiv\,y^2\,z - x^3 - z^3\,$$

O parâmetro crucial para a caracterização da curva é  a característica do corpo $$\,K\,$$uma vez que todas as derivadas dependem dessa característica. O seguinte quadro ilustra as  derivadas parciais de $$\,\phi\,$$ em função de $$\,\mathsf{char}(K)\,$$.

|                              | $$\mathsf{char}(K)\neq 2,\mathsf{char}(K)\neq 3$$ | $$\mathsf{char}(K)=2$$ | $$\mathsf{char}(K)=3$$ |
| ---------------------------- | ------------------------------------------------- | ---------------------- | ---------------------- |
| $$\partial \phi/\partial x$$ | $$-3\,x^2$$                                       | $$\,x^2\,$$            | $$0$$                  |
| $$\partial \phi/\partial y$$ | $$2\,y\,z$$                                       | $$0$$                  | $$2\,y\,z$$            |
| $$\partial \phi/\partial z$$ | $$y^2 - 3\,z^2$$                                  | $$y^2+z^2$$            | $$y^2$$                |

Quando $$\,\mathsf{char}(K)\neq 2\;\text{e}\;\mathsf{char}(K)\neq 3\;$$ nenhum ponto afim (com $$z=1$$) anula todas as derivadas. Apenas o triplo $$\,(0 : 0 : 0)\,$$ as anula mas este não é um ponto da curva. 
Por isso, com este corpo $$\,K\,$$, a curva não tem pontos singulares. Porém tem um ponto de inflexão: o ponto $$\,(0 : 1 : 1)\,$$ pertence à curva e nele anula-se a 2ª derivada $$\,\partial^2/\partial^2 x\,$$.
Quando $$\,\mathsf{char}(K)=2\,$$, o ponto $$\,(0:1:1)\,$$ pertence à curva e anula todas as derivadas. É, por isso, um ponto singular. Quando $$\,\mathsf{char}(K)=3\,$$ o ponto singular é $$\,(1:0:1)\,$$. 
Qualquer que seja a característica de $$\,K\,$$ o ponto no infinito $$(0:1:0)\,$$ pertence à curva e não é singular porque aì $$\,\partial\phi/\partial z\,$$ nunca é nulo.


2. $$\phi\;\equiv\;y^2\,z - x\,(x-z)^2$$

Vamos analisar apenas o caso em que a característica é diferente de $$\,2\,$$ e de $$\,3\,$$. Neste caso as primeiras derivadas são
     $$\partial\phi/\partial x\;=\; -(x-z)\,(3\,x-z)\quad$$, $$\quad\partial\phi/\partial y\;\equiv\; 2\,y\,z\quad$$, $$\quad\partial\phi/\partial z\;=\;y^2 + 2\,x\,(x-z)$$
O ponto $$\,(1:0:1)\,$$ é um ponto afim da curva onde todas as derivadas se anulam. É, por isso, um ponto singular.
A 2ª derivada é $$\,\partial^2\phi/\partial^2 x\,=\,2\,z\;$$; no ponto $$\,(1:0:1)\,$$ é não-nula; por isso o ponto é duplo.


3. $$\phi\;\equiv\;y^2\,z - x^3$$

As primeiras derivadas são
                      $$\partial\phi/\partial x\;=\; -3\,x^2\quad$$, $$\quad\partial\phi/\partial y\;\equiv\; 2\,y\,z\quad$$, $$\quad\partial\phi/\partial z\;=\;y^2$$
O ponto $$\,(0:0:1)\,$$é um ponto afim da curva onde todas estas derivadas se anulam; é um ponto singular. A adicionalmente as segundas derivadas em ordem a $$\,x\,$$e a $$\,z\,$$ nesse ponto são zero e a derivada em ordem a $$\,y\,$$ é não zero.
Por isso $$(0:0:1)\,$$é simultaneamente um ponto de inflexão e um ponto duplo.


![Exemplos de pontos singulares e pontos de inflexão em curvas cúbicas](https://paper-attachments.dropbox.com/s_3E3858162728746B0E2D03C7A4A48982BAEC2E3A2F876203D25AE73BFAEFF4F5_1618226803307_tangentes.jpg)



## Interseção de curvas

Quando duas cirvas $$\,C\,$$ e $$\,S\,$$ se interseptam, a cada ponto $$\,P\,$$ dessa interseção associa-se um inteiro positivo $$\,\mathcal{I}_P\,$$ designado por índice de $$\,P\,$$ em $$\,C\cap S\,$$.
A definição genérica do índice de interseção é algo complexa que envolve detalhes que não são muito importantes neste curso. É mais importante enunciar os resultados dessa definição em algumas situações concretas.
Vamos supor que $$\,C\,$$e $$\,S\,$$ são curvas arbitrárias, que $$\,P\,$$ é um qualquer ponto de $$\,C\,;$$ vamos também supor que $$\,T_P(C)\,$$ é a reta tangente a $$\,C\,$$ em $$\,P\,$$ se tal tangente existir.


1. Se $$\,P\in C \cap S\,$$ não é ponto singular em nenhuma das curvas e as tangentes a $$\,C\,$$e $$\,S\,$$ no ponto de interseção $$\,P\,$$são distintas, então  $$\;\mathcal{I}_P\,=\,1\,$$.
2. Se $$\,P\in C\,$$ não é um ponto singular ou de inflexão em $$\,C\,$$ então,  como ponto da interseção $$\,C\cap T_P(C)\,$$, tem-se   $$\;\mathcal{I}_P\,=\,2\,$$.
3. Se $$\,C\,$$é um cúbica que tem $$\,P\,$$como ponto de inflexão então, como ponto da interseção $$\,C\cap T_P(C)\,$$, tem-se $$\,\mathcal{I}_P\,=\,3$$.
4. Se $$\,C\,$$ tem um ponto duplo $$\,P\,$$, se $$\,P\in C \cap T'\,$$ sendo  $$T'\neq T_P(C)\,$$ um outra reta (distinta da tangente) que passa por $$\,P\,$$, então tem-se $$\,\mathcal{I}_P\,=\,3$$ .

Em quaisquer circunstâncias, o **teorema de Bézout ,** sobre a interseção de curvas, diz


>  Se $$\,C\,\text{e}\,S\,$$ são curvas arbitrárias de graus $$\,n\,$$ e  $$\,m\,$$, se os pontos de interseção das duas curvas são $$\,P_1,\cdots,P_k\,$$, então
                                            $$\mathcal{I}_{P_1}\,+\,\cdots\,+\,\mathcal{I}_{P_k}\;=\;n\times m$$



# Curvas Elípticas e sua Aritmética


## Definição

Seja $$\,K\,\equiv\,\mathbb{F}_q\,$$ um corpo finito ou um corpo de característica zero. Uma curva elíptica definida em $$\,K\,$$, representada como $$\,E/K\,$$,  é uma curva plana cúbica, absolutamente irredutível, sem pontos singulares e com, pelo menos, um ponto  com coordenadas em $$\,K\,$$.

Sem perda de generalidade (a menos de um isomorfismo) toda a curva elíptica tem um único ponto de fuga  $$\,\mathcal{O}\,\equiv\,(0  : 1 : 0)\,$$ e os seus pontos afins são determinados por pares $$\,(x,y)\,$$ no fecho algébrico $$\,\bar{K}\,$$que são raízes do polinómio de  Weierstrass, 

                            $$\mathcal{W}(x,y)\;\equiv\; (y^2 + a_1\,x\,y + a_3\,y)\,-\,(x^3 + a_2\,x^2 + a_4\,x + a_6)$$

Os coeficientes $$\,a_1,a_3,a_2,a_4,a_6\,$$ são elementos de $$\,K\,$$ e designam-se por *coeficientes de Weierstrass.* 

Os **pontos racionais** de $$\,E/K\,$$são os pontos da curva de coordenadas em $$\,K\,$$. O conjunto dos pontos racionais é representado por $$\,E(K)\,$$  e tem-se, pela definição,
                                    $$E(K)\;\equiv\; \{\,\mathcal{O}\,\}\,\cup\,\{\,(x,y)\in \mathbb{A}^2(K)\;|\;\mathcal{W}(x,y)\,=\,0\,\}$$


![Curvas elipticas $$\,E : y^2 = x^3 - a\,x +1\,$$  , no plano afim $$\,\mathbb{A}(\mathbb{Q})\,$$,  com $$\,a=0..4$$.](https://paper-attachments.dropbox.com/s_3E3858162728746B0E2D03C7A4A48982BAEC2E3A2F876203D25AE73BFAEFF4F5_1617967377289_eliticas0.jpg)


Nem todos os os possíveis tuplos $$\,a_1,\cdots,a_6\in K\,$$ determinam um curva elíptica; para forçar a que $$\,E : \mathcal{W}\;$$ seja uma curva elíptica é necessário garantir que $$\,\mathcal{W}(x,y)\,$$ não é divisivel  por um polinómio com coeficientes no fecho algébrico $$\,\bar{K}\,$$, e as derivadas parciais  $$\,\partial\mathcal{W}/\partial x\,,\,\partial\mathcal{W}/\partial y\;$$não se anulam simultaneamente em nenhum ponto dessa curva.

A forma das restrições que necessário impor nos coeficientes $$\,a_1,\cdots\,a_6\,$$depende crucialmente da característica do corpo $$\,K\,$$. Apesar de um vasto estudo que existe sobre a existência e propriedades de curvas elípticas em todo o tipo de corpo $$\,K\,$$, a prática criptográfica limita-se a duas classes de curvas: **curvas primas**, onde o corpo é da forma $$\,K \equiv \mathbb{F}_p\,$$ sendo $$\,p>3\,$$um primo, e **curvas binárias**, onde $$\,K\,\equiv\,\mathbb{F}_{2^m}\,$$, para algum $$\,m\,$$.

Em cada uma destas classes a forma de Weierstrass simplifica-se tornando mais simples formalizar as condições que os os coeficientes têm de verificar para definir realmente uma curva elíptica. O seguinte quadro resume essas formas simplificadas e as condições respetivas.


| **Classe**                       | **Forma simplificada de**  $$\,\mathcal{W}(x,y)$$ | **Condições**                  |
| -------------------------------- | ------------------------------------------------- | ------------------------------ |
| **Curva prima**                  | $$y^2 - (x^3 + a_4\,x + a_6)$$                    | $$4\,a_4^3 + 27\,a_6^2\neq 0$$ |
| **Curva binária ordinária**      | $$y^2 + x\,y + x^3 + a_2\,x^2 + a_6$$             | $$a_6\,\neq\,0$$               |
| **Curva binária super-singular** | $$y^2+a_3\,y + x^3+a_4\,x + a_6$$                 | $$a_3\,\neq\,0$$               |

## Pontos simétricos e cálculo de pontos numa curva $$\,E/K\,$$

Numa curva prima   $$\,E/\mathbb{F}_p\,$$ (com $$p>3$$) , se  $$\,P \equiv (x,y)\,$$ é raíz da forma simplificada, então também $$\,(x,-y)\,$$ pertence à curva; simplesmente porque $$\,y^2 = (-y)^2\,$$.  O ponto de coordenadas $$\,(x,-y)\,$$ é representado por $$\,-P\,$$.

Este é um exemplo de um par de **pontos simétricos** na curva. Essencialmente são um par de pontos $$\,\{\,P\,,\,-P\,\}\,$$  que têm a mesma coordenada $$\,x\,$$.  

Com excepção do ponto no infinito $$\,\mathcal{O}\,$$ e os pontos da forma $$\,(x,0)\,$$, que  coincidem com o próprio simétrico,  todos os restantes pontos da curva são distintos do seu simétrico.  

O problema do **cálculo** **de pontos** define-se como

> Dado um valor arbitrário $$\,z\in \mathbb{Z}_p\,$$,  determinar (se existirem) pontos $$\,P \equiv (x,y)\,$$  onde  $$\,\mathcal{W}(x,y) = 0\,$$  e onde a coordenada $$\,x\,$$ tem o valor $$\,z\,$$

Numa curva prima o problema resolve-se com o seguinte algoritmo

        1. Calcular o inteiro $$\,0\leq c < p\,$$ tal que  $$\,c \equiv z^3 + a_4\,z + a_6\bmod p\,$$.
        2. Verificar se $$\,c\,$$ é um resíduo quadrático módulo $$\,p\,$$.
            Metade dos possíveis valores de $$\,c\neq 0\,$$ são resíduos quadráticos módulo $$p$$; se $$\,c\,$$ não for  um tal resíduo, então não existe qualquer ponto da curva $$\,P=(x,y)\,$$  em que $$\,x=z\,$$.
        3. Se $$\,c\,$$ for resíduo quadrático módulo $$\,p\,$$ usa-se o algoritmo da raíz quadrada modular  para determinar $$\,y\in \mathbb{Z}_p\,$$ tal que   $$\,y^2 \equiv c \bmod p\,$$. 
        

Note-se que em anéis inteiros primos, tanto o teste dos resíduos quadráticos como o cálculo da raíz quadrada modular podem ser efectuados por algoritmos muito eficiente. 


----------

Numa curva binária  ordinária $$\,E/\mathbb{F}_{2^m}\,$$, atendendo à forma simplificada $$\,\mathcal{W}(x,y)\,$$  (ver quadro anterior)  é simples verificar que, se $$\,P\equiv (x,y)\,$$ for uma raíz de $$\,\mathcal{W}(x,y)\,$$, também  $$\,(x,y + x)\,$$ é raíz do mesmo polinómio. Portanto, nas curvas ordinárias tem-se $$$$$$\;-P \equiv (x,y+x)\;$$.

Se a curva for super-singular a forma simplificada $$\,\mathcal{W}(x,y)\,$$ é distinta da anterior. Neste caso o simétrico do ponto $$\,P\equiv (x,y)\,$$ é o ponto  $$\;-P\equiv\,(x,y+a_3)\,$$.

Em qualquer curva elíptica binária o problema de determinar um ponto da curva $$\,(x,y)\,$$ em que a coordenada $$\,x\,$$ coincide com um valor dado e arbitrário $$\,z\in\mathsf{GF}(2^m)\,$$, passa pela resolução do seguinte problema, 


> dado o  parâmetro $$\,c \in \mathsf{GF}(2^m)\;$$, determinar (se existir),  um valor $$\,y\in\mathsf{GF}(2^m)\;$$que verifique
>                                                                       $$y^2\,+\,y \,=\,c$$


| Prova-se facilmente que <br><br><br>    - Existe uma solução $$\,y\,$$ desta equação se e só se $$\,\mathsf{tr}(c) = 1\,$$<br>    - Se $$\,y\,$$ é solução da equação, então também $$\,y+1\,$$é solução da mesma equação.<br>    - Se  $$\,m\,$$é ímpar então uma solução será<br>                                  $$y\;=\;\sum_{i=0}^{(m-3)/2}\,c^{2^{2\,i+1}}$$<br>    - Se $$\,m\,$$é par então uma solução é<br>                                   $$y \;=\;\sum_{i=0}^{m-1}\,\sum_{j=0}^i\,c^{2^j}$$ |

Numa curva binária ordinária, o problema do cálculo de pontos resolve-se como

    1. Dado valor $$\,z\neq 0\,$$ da coordenada $$\,x\,$$, 
        1. calcula-se       $$c \;\equiv\; z + a_2 + (a_6/z^2)$$
        2. usa-se  a metodologia acima para  resolver a equação     $$(y/z)^2 + (y/z) = c$$
    2. Se $$\,z = 0\,$$ então resolve-se  $$\,y^2 = a_6\,$$.

Numa curva binária super-singular para o cálculo de pontos executa-se

        1. Dado $$\,z\,$$ calcula-se      $$c\;\equiv\;(z^3+a_4\,z + a_6)/a_3^2$$
        2. Usa-se a metodologia acima para resolver       $$(y/a_3)^2 + (y/a_3) = c$$ .


## Grupo abeliano aditivo em $$E/K$$

Como uma curva elíptica não tem pontos singulares e tem grau 3, o teorema de Bézout acima referido diz-nos que

> Qualquer reta intersecta uma curva elíptica $$\,E/K\,$$em exatamente três pontos.

Nesta contagem de pontos os pontos de tangência contam duas vezes e tem de se contar com o ponto de fuga $$\,\mathcal{O}\,$$ e os pontos não-racionais (de coordenadas em $$\,\bar{K}\,$$) .


| **Exemplos**<br>No corpo dos racionais $$\,K \equiv\,\mathbb{Q}\,$$ , considere-se a curva gerada por $$E:\mathcal{W}(x,y)\equiv y^2-x^3+x-2\,$$ . Vamos considerar várias retas e a sua interseção com esta curva:<br><br>1. A reta $$y = 0$$ (o eixo dos $$x$$)  intersecta a curva em 3 pontos do fecho algébrico de $$\mathbb{Q}$$ :  soluções da equação cúbica $$\,x^3 - x + 2 = 0\,$$. Existe uma solução real  $$\,\approx -1.5\,$$ e duas soluções complexas $$\,\approx 0.76\pm i\,0.86\,$$.<br>2. A reta vertical tangente à curva  interseta a curva “duas vezes” no ponto $$\,\approx (-1.5,0)\,$$ e no ponto no infinito $$\,\mathcal{O}\,$$. |


Uma outra questão é saber quantos pontos racionais existem na interseção da curva com a reta. Nos exemplos atrás, a primeira reta não tem nenhuma interseção que seja um ponto racional, e a segunda reta tem apenas o ponto no infinito $$\,\mathcal{O}\,$$ como ponto racional.

Obviamente como uma reta em $$\,\mathbb{A}^2(K)\,$$ é gerada por uma equação do 1º grau. Essa equação é

                                $$\,y = \lambda\,x + \mu\,$$                    com  $$\,\lambda,\mu \in K$$

caso a reta não seja vertical, ou então é $$\,x = \mu\,$$ , para retas verticais. Em qualquer caso

> Se a reta passa por dois pontos racionais e o terceiro ponto tem uma coordenada em $$\,K\,$$ esse ponto é racional. 

A partir desse lema prova-se facilmente que


> Se uma reta intersecta uma reta em dois pontos racionais distintos, o terceiro ponto de interseção é racional. Adicionalmente, se a reta é tangente à curva num ponto racional, interseta também a reta num outro ponto racional.  

Estes resultados permitem definir, no conjunto dos pontos racionais $$\,E(K)\,$$, a estrutura de um corpo abeliano aditivo , com soma representada por $$\,\oplus\,$$ , através das seguintes regras:


1. Se $$\,P,Q,R\,$$ são três pontos de interseção de uma reta com a curva $$\,E/K\,$$então
                                       $$P \oplus Q \oplus R\;=\;\mathcal{O}$$
2. O ponto de fuga $$\,\mathcal{O}\,$$ é elemento neutro da soma $$\,\oplus\,$$.

A partir destas duas regras é simples provar os seguintes resultados:

    1. Para qualquer grupo finito $$\,K\equiv \mathbb{F}_q\,$$e para qualquer grupo de característica $$\,0\,$$, o simétrico de um ponto $$\,P\,$$ , definido na secção anterior, verifica
                                         $$\,P \oplus -P \oplus \mathcal{O}\,=\,\mathcal{O}$$
    2. A operação de soma é associativa e comutativa.

Com esta construção conclui-se que  $$\langle\,E(K)\,,\,\oplus\,,\,\mathcal{O}\,\rangle$$  é um grupo abeliano.


## Algoritmos para cálculo da soma $$\,P\oplus Q$$ e duplicação $$\,2\,P\,$$.

 A figura seguinte ilustra como, geometricamente, a soma de dois pontos $$\,P\oplus Q\,$$ numa curva $$\,E/K\,$$ se define a partir da equação $$\,P\oplus Q \oplus R\,=\,\mathcal{O}\,$$.




![Soma de pontos na curva projetiva gerada por $$\;\phi\,\equiv\;y^2\,z - x^3 + x\,z^2 - 2\,z^3$$. $$\;$$](https://paper-attachments.dropbox.com/s_3E3858162728746B0E2D03C7A4A48982BAEC2E3A2F876203D25AE73BFAEFF4F5_1617967424050_elipticas1.jpg)



Em termos algébricos, pretende-se construir as coordenadas do ponto $$\,(P\oplus Q)\,$$ a partir do conhecimento das coordenadas dos pontos  $$\,P\,$$ e $$\,Q\,$$. 

A construção geométrica diz-nos que $$\,P \oplus Q\,=\,-R\,$$. Vimos anteriormente, para  diferentes classes de curvas, como se calcula as coordenadas  de $$\,-R\,$$ a partir das coordenadas de $$\,R\,$$. Por isso o algoritmo que pretendemos tem como objetivo


> Dados  $$\,P = (x_1,y_1)\,$$ e $$\,Q=(x_2,y_2)\,$$ , que são pontos de interseção de uma reta 
>                                                                      $$S : y = \lambda\,x + \mu\,$$
> com a curva elíptica  
>                                                                                $$E/K : \mathcal{W}(x,y)$$
>  determinar  $$\,R = (x_3,y_3)\,$$,  o  3º ponto  dessa interseção.

Este algoritmo decompõe-se em dois sub-problemas:   a soma  $$\,P\oplus Q\,$$ de dois pontos distintos, e a duplicação $$\,2 P\,\equiv\,P \oplus P\,$$ de um ponto. Em qualquer dos casos o algoritmo depende crucialmente da característica do corpo $$\,K\,$$.

**O** **corpo** $$\,K\,$$ **tem característica** $$\,0\,$$ **ou então** $$\,K\equiv\mathbb{F}_p\,$$ **com** $$p > 3\,$$**.**

Neste caso a forma simplificada do polinómio de  Weierstrass é
                                  $$\mathcal{W}(x,y)\;\equiv\; (x^3 + a_4\,x + a_6) - y^2$$ ****

1. $$\,P\equiv(x_1,y_1)\,\neq\, Q \equiv (x_2,y_2)\,$$
    Este problema decompõe-se ainda no caso em que $$\,P = -Q\,$$, onde a soma é trivialmente $$\,\mathcal{O}$$, do caso em que $$\,P\neq - Q\,$$  em que $$\,x_1 \neq x_2\,$$.
    
    Neste segundo caso, os parâmetros da reta, que passa pelos pontos $$\,P\,$$ e $$\,Q\,$$,  são
                       $$\lambda \,=\,(y_2-y_1)/(x_2-x_1)\quad,\quad \mu\,=\,y_1-\lambda\,x_1$$
    Substituindo  $$\,y \mapsto (\lambda\,x + \mu)\,$$ no polinómio  $$\,\mathcal{W}(x,y)\,$$ obtém-se um polinómio em $$\,x\,$$, do 3º grau , cujas raízes são precisamente as coordenadas $$\,x_1,x_2,x_3\,$$ das três raízes $$\,P,Q,R\,$$. 
                  $$(x^3 + a_2\,x+a_6) - (\lambda^2\,x^2 + 2\,\lambda\,\mu\,x +\mu^2) \;=\;(x-x_1)\,(x-x_2)\,(x-x_3)$$

     Igualando os coeficientes em $$\,x^2\,$$ em ambos os lados  da equação  obtém-se

                                     $$\lambda^2 \,=\, x_1 + x_2 + x_3$$ 
    Como $$\,\lambda\,,\,x_1\,,\,x_2\,$$ são conhecidos, desta equação determina-se $$\,x_3\,$$. Da equação da reta  determina-se $$\,y_3 = \lambda\,x_3 + \mu\,$$.


2. $$\,P\equiv (x_1,y_1)\,=\,Q$$
    Neste caso a reta é tangente à curva no ponto $$\,P\,$$.  O seu declive $$\,\lambda\,$$ é dado pela derivada  $$\,dy/dx\,$$ calculada no ponto  $$(x_1,y_1)$$ .   Se $$\,y_1=0\,$$a tangente é vertical e, por isso, tem-se $$\,R \equiv \mathcal{O}\,$$.    Se  $$\,y_1 \neq 0\,$$ tem-se
                        $$\,\lambda \,=\,(3\,x_1^2+a_4)/2\,y_1\quad, \quad \mu \,=\,y_1 -\lambda\,x_1$$
    Aplicando a $$\,\mathcal{W}(x,y)\,$$a substituição $$\,y \mapsto \lambda\,x+\mu\,$$ e aplicando a estratégia usada no caso anterior obtém-se a igualdade 
                                                 $$\,\lambda^2 \,=\,2\,x_1 + x_3$$
    que permite determinar $$\,x_3\,$$ e daí calcular $$\,y_3 = \lambda\,x_3 + \mu$$.

**O corpo** $$\,K\,$$ **tem  característica** $$\,2\,$$ ****

A estratégia é precisamente a mesma que foi usada para a característica $$\,p>3\,$$. Varia apenas a forma do polinómio de Weiertrass
                  $$\mathcal{W}(x,y)\;\equiv\; x^3 + a_2\,x^2 + a_6 + y^2 + x\,y\,\quad$$  nas curvas ordinárias
                  $$\mathcal{W}(x,y)\;\equiv\; x^3 + a_4\,x + a_6 + y^2 + a_3\,y\quad\,$$  nas curvas super-singulares
                  
Nas curvas ordinárias, se $$x_1\neq x_2\,$$, tem-se $$\,\lambda = (y_1+y_2)/(x_1+x_2)\,$$e $$\,\mu=\lambda\,x_1+y_1$$.
Fazendo a substituição do $$\,y\,$$ e igualando os polinómios obtém-se a igualdade 

                                  $$\lambda^2 + \lambda + a_2 \,=\, x_1 + x_2 + x_3$$

o que permite determinar $$\,x_3\,$$ e daí  calcular $$\,y_3 = \lambda\,x_3 + \mu$$.
Para a duplicação de pontos, $$\,x_1 = x_2\,$$, o declive é dado pela tangente no ponto $$\,(x_1,y_1)\,$$
e obtém-se $$\,\lambda = x_1 + (y_1/x_1)\,$$.  Após a substituição usual , dado que $$\,x_1+x_2 = 0\,$$,  obtém-se  $$\,x_3 = \lambda^2 + \lambda + a_2\,$$ e daí  $$\,y_3 = y_1 + \lambda\,(x_3 + x_1)\,$$.

Em curvas super-singulares, quando $$\,x_1\neq x_2\,$$, o declive é $$\,\lambda=(y_2+y_1)/(x_2+x_1)\,$$ e a relação obtida é $$\,\lambda^2 = x_1+x_2+x_3\,$$. Quando $$\,x_1=x_2\,$$ (suplicação de pontos) tem-se $$\,x_3 = \lambda^2\,$$ sendo $$\,\lambda = (x_1^2+a_4)/a_3\,$$ .


## Cardinalidade de $$\,E(K)\,$$

Obviamente é importante analisar as propriedades algébricas deste grupo.  A primeira dessas propriedades é a sua *ordem* : quantos pontos racionais tem a curva $$\,E/K\,$$?

Este é um problema que não é simples. Os algoritmos existentes para a contagem dos pontos racionais têm complexidade polinomial mas não são muito eficientes. 
Nomeadamente, nas aplicações criptográficas, não é viável contar os pontos racionais de uma curva apenas quando ela vai ser imediatamente usada  na geração de uma assinatura ou de um criptograma: é sempre necessário fazer essa contagem “off-line” e usar curvas “standard” onde o número de pontos racionais é conhecido *a priori*.

Existem alguns casos particulares onde a contagem de pontos racionais é simples e, no caso geral, existe um teorema que permite por limites ao número total de tais pontos.

As curvas onde é simples conhecer a ordem do grupo $$\,E(K)\,$$ são precisamente as curvas super-singulares já referidas anteriormente. 

O teorema genérico é o **teorema de Hasse-Weil** que diz

> Para um corpo finito $$\,K\,\equiv\,\mathbb{F}_q\,$$ então  $$\,\#E(K) \,=\,1 + q -t\,$$   para algum inteiro $$\,t\,$$ que verifica $$\,(t/2)^2 \leq q\,$$. 

No caso geral o teorema dá apenas uma aproximação ao número de pontos racionais na curva $$\,E/K\,$$.  No entanto, para algumas formas específicas de curvas, é possível determinar exatamente o valor de $$\,t\,$$e consequentemente o valor de $$\,\#E(K)\,$$.

Nomeadamente, seja $$\,p>3\,$$ um número primo,

    - Uma curva elíptica $$\,E/\mathbb{F}_p\,$$ é super-singular se e só $$\,t = 0\,$$.
    - Para todo inteiro $$\,t$$  que verifique $$\,(t/2)^2 \leq p\,$$ é possível construir  uma curva $$\,E/\mathbb{F}_p\,$$ em que    $$\,\#E(\mathbb{F}_p)\,=\,1 + p - t\,$$ .
    - Para todo  $$\,m\geq 1\,$$,  uma curva elíptica  $$\,E/\mathbb{F}_{p^m}\,$$ é super-singular se e só se  $$\,t \equiv 0 \bmod p\,$$.

Nas curvas binárias uma curva é super-singular se e só se é isomórfica com uma curva gerada por um polinómio  $$\,y^2 + a_3\,y + x^3 + a_4\,x + a_6\,$$, com $$\,a_3\neq 0\,$$. 


## Pontos de Torção

Para definir genericamente a noção de curva super-singular temos de ter em conta a aplicação primária das curvas elípticas em criptografia: nos criptosistemas da família Diffie-Hellman, substituir os grupos multiplicativos $$\,\mathbb{Z}_p^\ast\,$$ por um outro grupo abeliano computacionalmente  mais eficiente onde o problema do logaritmo discreto (e suas variantes) continue a ser “hard”.

A substituição só faz sentido se forem assegurados estes dois aspetos: eficiência e segurança. Assim a aritmética em  $$\,E(K)\,$$deve tão ou mais  eficiente do que em  $$\,\mathbb{Z}_p^\ast\,$$ , tanto em termos  do número de primitivas executadas como em termos de tamanho de chaves, criptogramas e assinaturas digitais. Também, no grupo $$\,E(K)\,$$, a complexidade do DLP ou das suas variantes continua a assegurar a segurança dos criptosistemas.

Porém as curvas elípticas $$\,E/K\,$$ e os seus grupos abelianos $$\,E(K)\,$$ introduzem uma dificuldade que não ocorre num grupo $$\,\mathbb{Z}_p^\ast\,$$:  quando o corpo $$\,K\,$$é finito, o grupo $$\,E(K)\,$$ tem ordem finita mas, geralmente, não só o grupo não é cíclico como a ordem $$\,N \equiv \#E(K)\,$$ não é simples de calcular.

Enquanto que nos criptosistemas DH clássicos o grupo cíclico $$\,\mathbb{Z}_p^\ast\,$$ é  aleatoriamente gerado em cada instância do criptosistema, bastando para isso gerar apropriadamente o primo $$\,p\,$$, o grupo $$\,E(K)\,$$ não pode ser aleatoriamente gerado em cada instância porque o custo do cálculo de uma ordem $$\,N\,$$adequada seria proibitivo.

Por isso os criptosistemas que usam $$\,E/K\,$$ desenvolvem-se sempre em sub-grupos cíclicos de $$\,E(K)\,$$ cuja ordem  $$\,n\,$$ é um  divisor de  $$\,N\,$$; devido ao ataque de Pohlig-Hellman, $$\,n\,$$ deve ser  primo ou uma potência de um primo. 

O grupo cíclico $$\,E(K)\,$$ não é gerado aleatoriamente mas, antes é escolhido dentro de um conjunto de curvas “standard”. No entanto o sub-grupo cíclico de $$\,E(K)\,$$ , onde cada instância é implementada, pode ser aleatoriamente gerado através do seu  elemento gerador.


----------

 
 Um outro ponto de vista passa por fixar  *a* *priori*  uma ordem $$\,n\,$$, que seja um primo ou potência de um primo , e construir um grupo de torção $$\,E[n]\,\subseteq E/K\;$$ com exatamente essa ordem. Como contrapartida, um ponto genérico desse $$\,E[n]\,$$ não é necessariamente um ponto racional  mas um ponto de coordenadas no fecho algébrico $$\,\bar{K}\,$$.
Define-se

                             $$\,E[n]\;\equiv\;\{\,P\in E(\bar{K})\;|\; n\,P\,=\,\mathcal{O}\,\}$$

Em princípio, mesmo que $$\,K\,$$seja um corpo finito, o seu fecho algébrico $$\,\bar{K}\,$$não é finito. Por isso, no caso geral, o grupo abeliano $$\,E(\bar{K})\,$$ não é um grupo de torção. Porém cada $$\,E[n]\,$$ é um sub-grupo de $$\,E(\bar{K})\,$$de ordem finita e, por isso, um grupo de torção.

Um ponto $$\,P\in E[n]\,$$ é um  $$\,n$$-**ponto de torção**. 

A  ordem de um tal $$\,P\,$$ é um divisor $$\,d\,$$ de $$\,n\,$$; como $$\,n\,$$é primo ou uma potência de um primo,  $$\,d\,$$ coincide com $$\,$$$$\,n\,$$ ou também é uma potência de um primo.

A  **órbita**  $$\,[P]\,$$ do ponto $$\,P\,$$, isto é o conjunto de todos os  $$\,k\,P\;\text{com}\; 0\leq k < d\;$$, é um grupo cíclico de ordem $$\,d\,$$ que tem $$\,P\,$$como gerador. Se, adicionalmente,  $$\,P\,$$ for um ponto racional da curva, se  $$\,P\in E(K)\,$$, então todo o  $$\,k\,P\,$$ é também racional. 

Em conclusão, 

> Se $$\,P\in E(K)\,$$ é um $$\,n$$-ponto de torção da curva $$\,E/K\,$$, então a órbita $$\,[P]\,$$ é um sub-grupo cíclico de ordem $$\,d\,|\,n\,$$ do grupo abeliano $$\,E(K)\,$$.

A estrutura genérica do grupo de torção $$\,E[n]\,$$ é  descrita  nos seguintes resultados

**Teorema**
Seja $$\,K\,$$ um corpo de característica $$\,p\,$$ e seja $$\,E/K\,$$ uma curva elíptica 

1. Se $$\,\gcd(p,n) = 1\,$$, então  existe um isomorfismo de grupos 
                                        $$\,E[n]\,\simeq\,\mathbb{Z}_n\times\mathbb{Z}_n$$ 
2. Se $$\,n = p^r\,$$ , para algum $$\,r\geq 1\,$$, então para todo $$\,k\geq 1\,$$ ocorre uma de duas situações
    1. $$E[p^k]\;\equiv\; \{\mathcal{O}\}$$ ;  ou, em alternativa, 
    2. $$E[p^k]\;\simeq\; \mathbb{Z}_{p^k}\;$$.

As curvas $$\,E/K\,$$onde ocorre a situação (a.) dizem-se **super-singulares**. As restante curvas, onde ocorre a situação (b.), dizem-se **ordinárias**. 

Vimos que, para qualquer primo $$\,p>3\,$$ e para qualquer $$\,q = p^m\,$$

    - Uma curva elíptica$$\;E/\mathbb{F}_p\,$$ é super-singular se e só se $$\,\#E(\mathbb{F}_p)\,=\,p + 1\,$$,
    - Uma curva elíptica $$\,E/\mathbb{F}_q\,$$é  super-singular se e só se $$\,\#E(\mathbb{F}_q)\,=\,q + 1 - t\,$$  para algum $$\,t\,$$ tal que   $$\,t \equiv 0\bmod p\,$$ e   $$\,|t|\leq 2\,\sqrt{q}\,$$.



----------

**Exemplos**
Prova-se que, num corpo primo $$\,K \equiv \mathbb{F}_p\,$$ com $$\,p > 3\,$$ , as seguintes curvas elipticas são super-singulares

1.  $$\,E_0:y^2 = x^3 + 1\,$$ é super-singular se e só se  $$\,p + 1\equiv 0 \bmod 3$$
2.  $$\,E_0:y^2 = x^3 + x\,$$ é super-singular se e só se  $$\,p + 1\equiv 0 \bmod 4$$ 

No 1º caso é possível gerar um valor $$\,w \gets \mathsf{GF}(p)\,$$  e calcular $$\,x \gets w^{\frac{p+1}3}\,$$;  verifica-se $$\,x^3\,=\,w^2\,$$.
Resolve-se depois a equação $$\,y = \sqrt{w^2+1}\,$$ ; metade dos valores de $$\,w^2+1\,$$ são resíduos  quadráticos e cada um destes valores tem 2 raízes. Portanto os pares $$\,(x,y)\,$$ assim formados são todos distintos e são $$\,p\,$$ em número . Para todos eles verifica-se $$\,y^2 = w^2 + 1 = x^3 + 1$$ e portanto determinam pontos afins da curva. Juntando o ponto no infinito $$\,\mathcal{O}\,$$ vemos que a curva tem $$\,(p+1)\,$$ pntos e, por isso, é super-singular.

No 2º caso a prova é análoga atendendo que, para todo o $$\,w\,$$ que seja resíduo qadrático, $$\,w^{\frac{p+1}4}\,$$ determina essa raíz.

Quando o corpo é $$\,K\equiv \mathbb{F}_{p^2}\,$$ observa-se o seguinte

    - se $$(p+1)/3\,$$ é inteiro, é possível calcular $$\,\zeta\in \mathbb{F}_{p^2}\,$$, diferente de $$\,1\,$$, que verifica $$\,\zeta^3 = 1\,$$.
    - se $$(p+1)/4\,$$ é inteiro, é possível determinar $$\,j\in\mathbb{F}_{p^2}\,$$ que verifica $$\,j^2 = -1\,$$.

No 1º caso a transformação
                                                        $$(x,y)\; \mapsto\; (\zeta\cdot x\,,\,y)\,$$ 
 define uma isogenia (isto é, um morfismo injetivo)    $$\,E/\mathbb{F}_p \,\to\,E/\mathbb{F}_{p^2}\,$$. 
 
 No 2º caso a isogenia   $$\,E/\mathbb{F}_p \,\to\,E/\mathbb{F}_{p^2}\,$$ é definida pelo morfismo

                                           $$(x,y)\; \mapsto\; (-x\,,\,j\cdot y)\,$$ 

