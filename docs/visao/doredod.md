# DoR e DoD

Esta seção apresenta os conceitos de Definition of Ready (DoR) e Definition of Done (DoD), que auxiliam a garantir que o trabalho seja bem definido previamente. Enquanto o DoR estabelece critérios claros para garantir que um item do backlog esteja pronto para ser iniciado — com definição, valor, tempo e critérios bem definidos —, o DoD define os padrões de qualidade que determinam quando um incremento está verdadeiramente concluído e pronto para entrega.


*Boas práticas e Direcionamentos utilizados para definição dos critérios*
|DoD |DoR|
|----|----|
|1. Actionable immediately by the team<br>2. Negotiable, open to modification<br>3. Valuable <br>4. Time estimate<br>5. Testable <br>6. Size proper for the team<br>| 1. Code review <br>2. Integrated <br>3. Tests <br>4. Commit standard <br>|


## Definition of Ready (DoR)
O DoR delimita quando um **requisito está preparado para ser trabalhado**. Permitindo a equipe que avalie o trabalho que será feito antes de começar a desenvolver. Para que seja considerado como *Ready*, serão levadas em consideração se:

1. O requisito está representado por uma história de usuário?
1. O requisito possui critérios de aceitação orientados por *Behavior Driven Development* (BDD) e testes?
1. O requisito está consoante com a granularidade dos demais?
1. O requisito foi estimado?
1. O requisito agrega valor e está associado à algum dos objetivos específicos da solução?
1. As dependências do requisitos estão mapeadas (se houver)?

## Definition of Done (DoD)

O DoD define os critérios que precisam ser cumpridos para que uma funcionalidade seja considerada completa, demonstrando **qualidade do requisito produzido**. Para que seja considerado como *Done*, deve atender ao seguinte:
1. Esse requisito entrega um incremento do produto?
1. Contempla critérios de aceite estabelecidos?
1. Está documentado para uso?
1. Foi revisado por outro desenvolvedor?
1. Segue os padrões [estabelecidos de codificação](../../CONTRIBUTING.md)?
1. Foi testado?

## Histórico de versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
| 13/05/2025 | 0.1 | Definindo DoR, DoD e critérios de aceite | Wanjo Christopher |