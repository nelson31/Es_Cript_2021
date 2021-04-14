# Trabalho Prático 2

## Enunciado

### Criptosistemas pós-quânticos PKE/KEM 

Pretende-se implementar no SageMath protótipos das seguintes candidaturas ao concurso **NIST-PQC**. Algumas sugestões de notebooks auxiliares são apresentadas nas referências indicadas.
Implemente os seguintes esquemas **KEM** em classes *Python/SageMath* apresentando, para cada um, as versões **KEM-IND-CPA** e **PKE-IND-CCA**.

1. [NTRU](https://ntru.org/)
2. [Kyber/Crystalis](https://pq-crystals.org/kyber/)
3. [BIKE](https://bikesuite.org/)



### Rerências recentes de algumas propostas ao concurso NIST-PQC *(documentação adicional)*

**[Ver página da 3ª ronda do concurso NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography/round-3-submissions)**


1. KEMs
    1. [NewHOPE](https://newhopecrypto.org/) — [documentação da candidatura](https://www.dropbox.com/sh/c0lj9t7820dhrk2/AACpW7lbmS63BoNosFmy2Rbha?dl=0)
    2. [NTRU - website](https://ntru.org/)
    3. [BIKE](https://bikesuite.org/)  (web site) e [proposta](https://bikesuite.org/files/BIKE.pdf)
    4. [KYBER](https://pq-crystals.org/kyber/)  (web site)
    5. Classical McElice
2. Digital Sign
    1. [qTESLA](https://www.microsoft.com/en-us/research/project/qtesla/) —  [documentação da candidatura](https://www.dropbox.com/sh/2vr43y9dk7mf08e/AABeUWtwI7h4Ix9_D-ervJvJa?dl=0) e o [website](https://qtesla.org/)
    2. [SPHINCS+](https://sphincs.org/)
    3. [DILITHYM](https://pq-crystals.org/dilithium/) - website
    4. [Rainbow](https://www.pqcrainbow.org/) - website
3. [Notebooks vários](https://www.dropbox.com/sh/hsjcb8gfzrr6usp/AAAz-lekJK75IeeVNC8zYseya?dl=0)
        1. Uma implementação simples do NTRU na versão Silverman 2015
        2. Uma implementação do Number Theoretic Transform (NTT) adequada a protótipos para a família RLWE: por exemplo,  o NewHope ou o qTESLA


