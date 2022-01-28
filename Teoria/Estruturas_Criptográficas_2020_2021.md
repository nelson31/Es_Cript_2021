# Estruturas Criptográficas: 2020/2021


## Objetivos e Programa

Nesta unidade curricular pretende-se estudar a segurança, correção e eficiência das técnicas criptográficas usadas na Tecnologia da Informação, quer as que fazem das atuais aplicações quer ainda as que no futuro serão cruciais a essas aplicações.

Qualquer destes aspectos depende fundamentalmente das estruturas usadas para modelar a informação tanto na forma como é descrita como na forma como é operada.
Essencialmente as estruturas da informação vão-se traduzir nas  **estruturas algébricas** que caracterizam as propriedades das diversas técnicas criptográficas. 

No entanto a designação “estrutura criptográfica” vai além desta componente meramente algébricas; em criptografia interessa também a complexidade dos algoritmos que implementam as operações algébricas porque, em grande medida, a segurança das estruturas criptográficas depende dessa complexidade.

Nomeadamente interessa avaliar as situações nas quais essa complexidade torna inviável executar os algoritmos com recursos computacionais “razoáveis”. Tais situações conduzem à noção de problema difícil que é crucial a muitas formalizações da segurança.

Os fundamentos desta análise de complexidade são apresentados, sumariamente, no capítulo introdutório

[+Prólogo  1: Introdução à Complexidade Aritmética](Prólogo_1_Introdução_à_Complexidade_Aritmética.md) 

Criptografia lida fundamentalmente com as relações que se estabelecem entre agentes e “items” de informação. Por exemplo uma cifra criptográfica é uma técnica usada para controlar a **posse** de um agente sobre uma determinada quantidade de informação.

Por isso é necessário ter conceitos que permitam caracterizar os objectos que concretizam informação: i. e. os **dados**. É necessário quantificar a quantidade de informação em a cada  objeto, o seu grau de desorganização interna  e em que medida essa informação é previsível a partir de outros objectos. 

Os conceitos essenciais a essa caracterização são a **complexidade descritiva** de objetos finitos (e.g. “strings” de bits) e a **aleatoriedade** de entidades infinitas (e.g. “streams” de bits, conjuntos ou  funções) . Estas noções são apresentadas no capítulo

[+Prólogo 2:  Complexidade Descritiva e Aleatoriedade.](Prólogo_2_Complexidade_Descritiva_e_Aleatoriedad.md) 

As noções de aleatorieade assumem forma criptográfica através de um conjunto de noções “ideais” que abstraem os detalhes das técnicas criprográficas concretas. Nomeadamente são importantes os **hashs aleatórios** que são as funções de “hash” ideais, os **geradores pseudo-aleatórios** (PRG’s) que simulam “streams” verdadeiramente aleatórias e, de uma forma genérica, os **geradores aleatórios** que agregam as construções essenciais dos algoritmos constituintes dessas técnicas.
Estas noções são descritas no capítulo

[+Prólogo 3: Hashs, Pseudo Aleatoriedade e Geradores](Prólogo_3_Hashs,_Pseudo_Aleatoriedade_e_Geradores.md) 

De um modo geral as técnicas criprográficas designam-se por

    - **primitivas** quando envolvem um único algoritmo, 
    - **esquemas** quando agregam várias primitivas e eventualmente vários agentes actuando em regime assíncrono, e
    - **protocolos** quando agregam vários esquemas e vários agentes actuando sincronamente.

Primitivas são componentes básicas de todas as técnica criptográfica;  vamos iniciar o nosso estudo de primitivas  com o documento seguinte

[+Capítulo 1: Primitivas Criptográficas Básicas](Capítulo_1_Primitivas_Criptográficas_Básicas.md) 

No próximo capítulo continuamos a falar de cifras , discutindo critérios de segurança e a construção de algumas cifras simétricas e assimétricas.

[+Capítulo 2: Esquemas de Cifra, Segurança e Construção.](Capítulo_2_Esquemas_de_Cifra,_Segurança_e_Constru.md) 

[+Capítulo 3:  Introdução à Álgebra Abstracta](Capítulo_3_Introdução_à_Álgebra_Abstracta.md) 

[+Capítulo 4:  Fatorização e Teorema Chinês dos Restos.](Capítulo_4_Fatorização_e_Teorema_Chinês_dos_Rest.md) 

[+Capítulo 5: Grupos Cíclicos, Formas Bilineares e Curvas Elípticas.](Capítulo_5_Grupos_Cíclicos,_Formas_Bilineares_e_C.md) 

[+Capítulo 5a: Curvas Elípticas](Capítulo_5a_Curvas_Elípticas.md) 

[+Capítulo 6: Provas de Conhecimento](Capítulo_6_Provas_de_Conhecimento_e_Assinatura_Di.md) 

[+Capítulo 7:  Anéis e Corpos de Polinómios](Capítulo_7_Anéis_e_Corpos_de_Polinómios.md) 

[+Capítulo 8: Reticulados. Problemas “Standard” . Redução Linear.](Capítulo_8_Reticulados_Problemas_“Standard”_Re.md) 

[+Capítulo 9: Criptosistemas NTRU,  RLWE e baseados em Códigos.](Capítulo_9_Criptosistemas_NTRU,_RLWE_e_baseados.md) 

[+Capítulo 10:  Esquemas de Assinatura Digital  “PQC-High-Algebra”.](Capítulo_10_Esquemas_de_Assinatura_Digital_“PQC.md) 

[+Capítulo  11: Esquemas de Assinatura Digital “PQC-Low-Algebra”.](Capítulo_11_Esquemas_de_Assinatura_Digital_“PQC-.md) 




 




