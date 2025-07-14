# DoR e DoD

Esta seção apresenta os conceitos de Definition of Ready (DoR) e Definition of Done (DoD), que auxiliam a garantir que o trabalho seja bem definido previamente. Enquanto o DoR estabelece critérios claros para garantir que um item do backlog esteja pronto para ser iniciado — com definição, valor, tempo e critérios bem definidos —, o DoD define os padrões de qualidade que determinam quando um incremento está verdadeiramente concluído e pronto para entrega.


*Boas práticas e Direcionamentos utilizados para definição dos critérios*

|DoD |DoR|
|----|----|
|1. Actionable immediately by the team<br>2. Negotiable, open to modification<br>3. Valuable <br>4. Time estimate<br>5. Testable <br>6. Size proper for the team<br>| 1. Code review <br>2. Integrated <br>3. Tests <br>4. Commit standard <br>|


## 📋 Definition of Ready (DoR)
O DoR delimita quando um **requisito está preparado para ser trabalhado**. Permitindo a equipe que avalie o trabalho que será feito antes de começar a desenvolver. Para que seja considerado como *Ready*, serão levadas em consideração se:

1. O requisito está representado por uma história de usuário?
1. O requisito possui critérios de aceitação orientados por *Behavior Driven Development* (BDD) e testes?
1. O requisito está consoante com a granularidade dos demais?
1. O requisito foi estimado?
1. O requisito agrega valor e está associado à algum dos objetivos específicos da solução?
1. As dependências do requisitos estão mapeadas (se houver)?

## 🏁 Definition of Done (DoD)

O DoD define os critérios que precisam ser cumpridos para que uma funcionalidade seja considerada completa, demonstrando **qualidade do requisito produzido**. Para que uma tarefa ou User Story seja considerada **concluída ("Done")**, todas as perguntas a seguir devem ser respondidas afirmativamente.

**1. Entrega de Valor**

- O trabalho realizado entrega um incremento funcional e observável ao produto?
- A entrega está claramente rastreada à sua origem? (A descrição do Pull Request ou da tarefa cita a **US**, **RN** ou **O.E.** correspondente?)

**2. Cobertura dos Requisitos**

- Todos os cenários (sucesso, falha e alternativos) descritos nos [**Critérios de Aceite (BDD)**](/backlog/geral/#backlog) foram implementados e são demonstráveis?

**3. Qualidade de Testes**

- Foi criado o teste unitário necessário para a nova funcionalidade?
- Os fluxos principais foram validados **manualmente** em um ambiente de teste, confirmando o comportamento esperado?

**4. Revisão por Pares (Code Review)**

- O **Pull Request (PR)** foi revisado e aprovado por, pelo menos, um outro membro da equipe?
- A revisão de código validou os critérios essenciais?
    - **Conformidade:** O código segue os padrões estabelecidos?
    - **Lógica:** A implementação atende corretamente aos requisitos?
    - **Legibilidade:** O código é claro, bem nomeado e de fácil manutenção?
    - **Segurança:** Não há dados sensíveis (senhas, tokens) expostos no código?

**5. Padrões de Código**

- O código segue os **padrões de codificação** e o guia de estilo definidos pelo projeto?
- As ferramentas de **Linter** e **Formatter** foram executadas e não apontam erros?

**6. Documentação**

- A **documentação técnica** foi devidamente atualizada? (Ex: `README.md`, comentários em lógicas complexas, novas variáveis de ambiente).
- Está documentado para uso com docstrings da biblioteca pydoc, com descrição, argumentos e retorno.

## 📜 Histórico de Versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
| **13/05/2025** | 0.1 | Definindo DoR, DoD e critérios de aceite | Wanjo Christopher |
| **21/05/2025** | 0.2 | Corrige caminho do documento de contribuição | Wanjo Christopher |
| **23/06/2025** | 1.0 | Melhora critérios DoD | Wanjo Christopher |
|**13/07/25**|2.1|Refinando visualmente o documento|Wanjo Christopher|
