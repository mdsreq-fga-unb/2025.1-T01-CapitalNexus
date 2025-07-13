# Engenharia de Requisitos

A Engenharia de Requisitos dispõe de diversas **técnicas e práticas**, que devem ser adaptadas conforme o contexto de negócio, necessidades do cliente e o perfil da equipe em questão. A seguir são apresentadas o conjunto de técnicas e práticas da ER a serem utilizadas durante o desenvolvimento da solução para a Capital Rocket Team, visando **garantir clareza e alinhamento do que será feito** e **como será feito**:


### Elicitação e Descoberta
Foca na **identificação e coleta inicial** de requisitos por meio da interação com stakeholders, usuários e outras fontes. O objetivo é descobrir necessidades, expectativas e restrições que o a solução de software deve atender.

- **Entrevista**: Na fase de Elicitação e Descoberta de requisitos, a técnica de entrevistas tem como principal objetivo não apenas **coletar requisitos**, mas também **compreender as expectativas** do cliente em relação à solução em desenvolvimento e **compreensão do problema**. Além disso, essa técnica é fundamental para **alinhar a equipe de desenvolvimento** com a visão do cliente (CRT), garantindo que todos compartilhem do mesmo entendimento sobre o projeto.
- **User Story**: Foi utilizado User Story para que conseguissemos elicitar e descobrir os requisitos a partir do ponto de vista do usuário.
- **Observação**: Um membro da equipe foi responsável por participar do dia a dia com a equipe e descobrir requisitos a partir da Observação.

### Análise e Consenso
Envolve o **refinamento e a consolidação** dos requisitos elicitados. Busca-se eliminar ambiguidades, resolver conflitos, priorizar e garantir que os requisitos sejam completos, consistentes e alinhados com os objetivos do negócio.

- **Entrevista** : A utilização da técnica tem como objetivo **alinhar as diferentes perspectivas** levantadas na elicitação e **mediando conflitos** entre necessidades divergentes.
- **Análise de Domínio de Requisito**: utilizamos análise de domínio de requisito para resolver contradições, eliminar ambiguidades e complementar informações ausentes. 
- **Prompt IA** : O Prompt IA foi utilizado para fazer uma análise dos requisitos, resolver contradições e alinhar as perspectivas, de uma forma mais direta.

### Declaração de Requisitos
É a **documentação formal** dos requisitos analisados, utilizando linguagem clara e estruturada. O foco é especificar "o quê" o sistema deve fazer, garantindo rastreabilidade.

- **Documento de Visão de Produto**: Foi feito o documento de visão para declarar os requisitos e disponibilizar para a equipe e o cliente.
- **User Stories**: Na fase de Declaração de Requisitos será utilizada a técnica de narrativas de usuários (*user stories*), que **descrevem funcionalidades** sob a perspectiva do usuário. O objetivo dessa técnica é garantir o **foco em entregas de valor**.

### Representação de Requisitos
Foca na **modelagem visual ou textual** dos requisitos para facilitar o entendimento e a comunicação.

- **Prototipação**: A técnica de representação informal de prototipação será utilizada com objetivo de permitir a CRT **fornecer feedbacks** intermediarios, afim de validar partes do front inicial.

### Verificação e Validação de Requisitos
**Garante a qualidade** dos requisitos. A **verificação** assegura que os requisitos estão corretamente especificados (ex: completos, não ambíguos), enquanto a **validação** confere se atendem às reais necessidades do cliente.

- **Definition of Ready (DoR)**: A técnica de DoR delimita quando um **requisito está preparado para ser trabalhado**. Para que seja considerado como *Ready*, serão levadas em consideração se:
    1. O requisito está representado por uma história de usuário?
    1. O requisito possui critérios de aceitação orientados por *Behavior Driven Development* (BDD) e testes?
    1. O requisito está consoante com a granularidade dos demais?
    1. O requisito foi estimado?
    1. O requisito agrega valor e está associado à algum dos objetivos específicos da solução?
    1. As dependências do requisitos estão mapeadas (se houver)?
- **Definition of Done (DoD)**: A técnica de DoD demonstra **qualidade do requisito produzido**. Para que seja considerado como *Done*, deve atender ao seguinte:
    1. Esse requisito entrega um incremento do produto?
    1. Contempla critérios de aceite estabelecidos?
    1. Está documentado para uso?
    1. Foi revisado por outro desenvolvedor?
    1. Segue os padrões [estabelecidos de codificação](..\contribuicao)?
    1. Foi testado?
- **Revisão em Pares**: A revisão em pares entre os membros do grupo auxiliará na **verificação dos requisitos**, verificando se estão sendo feitos de maneira correta.
- **Feedback**: Será utilizada a técnica de feedback com a CRT para **manter um backlog de produto verificado** e **validado** de acordo com as necessidades da solução.
- **Análise de Viabilidade**: Será utilizada a técnica de análise de viabilidade para garantir requisitos factíveis.
- **Feedback (cliente/equipe)**: Será utiliza a ténica de feedback para garantir que alinhar diferentes perspectivas, garantindo que os requisitos estejam de acordo entre partes.

### Organização e Atualização de Requisitos    
- **MoSCoW**: será utilizada a técnica de priorização de requisitos *MoSCoW* (*Must Have, Should Have, Could Have, Won't Have*), com objetivo de **gerar o Produto Mínimo Viável** (*MVP*).
- **Matriz de priorização**: Foi utilizado a técnica matriz de priorização para definir os requisitos do MVP, considerando esforço técnico e MoSCoW.
- **Feedback**: Conforme o feedback do cliente, os requsiitos foram sendo atualizados, para garantir entregas de valor.

## Engenharia de Requisitos e o AUP

O Processo do AUP (Agiled Unified Process) adota uma **filosofia pragmática e ágil**, concentrando-se numa natureza **colaborativa** e aplicando abordagens **iterativas** e **incrementais** no desenvolvimento de software. Devido à sua natureza flexível, algumas das técnicas se sobrepoem e podem ocorrer em mais de uma das fases do processo:


|**Fases do AUP** |**Atividades ER** |**Prática** |**Técnica** |**Resultado Esperado** |
| - | - | - | - | - |
|**Concepção** |***Elicitação e Descoberta*** |Conversas e reuniões abertas com a CRT |Entrevistas |Compreender e coletar requisitos de alto nível|
||***Análise e Consenso*** |Conversas e reuniões abertas com a CRT |Entrevistas |Eliminar ambiguidades e preencher lacunas nos requisitos |
|||Conversas e reuniões abertas com a CRT |Análise de Domínio de Requisito |Proposta de Solução |
||***Declaração*** | User Story | Narrativas de Usuário |Descrição das funcionalidades que entregam valor de negócio |
||***Verificação/Validação*** | Reuniões abertas com a CRT | Análise de Viabilidade | Garantir requisitos factíveis com a CRT|
||***Organização e Atualização*** |Priorização de Requisitos |MoSCoW |Priorização dos requisitos do ponto de vista do cliente |
|**Elaboração** |***Elicitação e Descoberta*** | Conversas e reuniões abertas com a CRT | Entrevistas |Coletar e específicar requisitos |
||***Análise e Consenso*** | Conversas e reuniões abertas com a CRT |Análise de Domínio de Requisito | Especificações de Requisitos |
||***Representação*** |Prototipação |Prototipação Intertativa |Garantir entrega alinhada às expectativas do cliente |
||***Verificação e Validação*** |Verificação de Requisitos|Aplicação da DoR| Lista de US prontas para serem desenvolvidas — Todo |
| || Validação de Requisitos | Aplicação da DoD |Lista de US prontas para serem revisadas — Review |
||| Validação de Requisitos | Validação em Pares | Requisitos verificados: Done |
||| Verificação e Validação | Feedback | Requisitos alinhados entre perspectivas |
||***Organização e Atualização***|Organização dos requisitos|Matriz de priorização |Mínimo Produto Viável (MVP) |
|**Construção**| ***Verificação e Validação*** | Validação de Requisitos | Validação em Pares |Requisitos verificados: Done |
| || Validação de Requisitos | Aplicação da DoD |Lista de US prontas para serem revisadas — Review |
||***Organização e Atualização***| Organização de Backlog | Feedback |Organização de Backlog |
|**Transição** | ***Verificação e Validação*** | Validação de Requisitos | Validação em Pares |Requisitos verificados: Done |
| || Validação de Requisitos | Aplicação da DoD |Lista de US prontas para serem revisadas — Review |

 ⚠️ Requisitos evoluem iterativamente. O processo de concepção do AUP define **linhas gerais**, focando no MVP.

## Histórico de versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
| **12/05/2025** | 0.1 | Descrição das técnicas utilizadas | Wanjo Christopher |
| **12/05/2025** | 0.2 | Correlação entre técnicas e fases do AUP | Wanjo Christopher|
| **13/05/2025** | 0.3 | Atualizando DoR e DoD | Wanjo Christopher|
| **21/05/2025** | 0.4 | Corrigindo técnicas da engenharia de requisitos | Wanjo Christopher|
| **26/05/2025** | 0.5 | Adiciona técnica de DoD nas fases de Construção e Transição | Wanjo Christopher|
| **23/06/2025** | 1.0 | Adiciona técnicas da ER | Sophia|
| **12/07/2025** | 1.1 | Complementa técnicas de ER, veri/val e elicitação | Wanjo Christopher |
| **12/07/2025** | 2.0 | Adiciona descrições e correlaciona AUP com técnicas | Wanjo Christopher |
