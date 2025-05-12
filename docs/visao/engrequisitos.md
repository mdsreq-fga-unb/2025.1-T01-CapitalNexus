# Engenharia de Requisitos

*A partir das informações apresentadas na seção 3, deste documento, devem ser estabelecidas as atividades da Engenharia de Requisitos (ER), suas práticas e técnicas em alinhamento ao processo de ESW informado.  Inicialmente, cada uma das 6 atividades da ER deve ser associadas as técnicas que serão utilizadas no projeto em desenvolvimento durante a disciplina.* 


### Elicitação e Descoberta

- **Entrevista**: Na fase de Elicitação e Descoberta de requisitos, a técnica de entrevistas tem como principal objetivo não apenas **coletar requisitos**, mas também **compreender as expectativas** do cliente em relação à solução em desenvolvimento e **compreensão do problema**. Além disso, essa técnica é fundamental para **alinhar a equipe de desenvolvimento** com a visão do cliente (CRT), garantindo que todos compartilhem do mesmo entendimento sobre o projeto. Serão utilizadas primordialmente *entrevistas fechadas*.

### Análise e Consenso

- **Entrevista** : Na fase de Análise e Consenso, a técnica de entrevistas tem como principal objetivo analisar e refinar os requisitos obtidos na etapa de Elicitação e Descoberta. Durante a análise, busca-se **eliminar ambiguidades**, **resolver contradições** e **complementar informações ausentes** nos requisitos. Já no consenso, o foco é **alinhar as diferentes perspectivas** levantadas na elicitação, **priorizando requisitos** e **mediando conflitos** entre necessidades divergentes.

### Declaração de Requisitos

- **User Stories**: Na fase de Declaração de Requisitos será utilizada a técnica de narrativas de usuários (*user stories*), que **descrevem funcionalidades** sob a perspectiva do usuário. O objetivo dessa técnica é garantir o **foco em entregas de valor**.

### Representação de Requisitos

- **Prototipação**: A técnica de representação informal de prototipação será utilizada com objetivo de permitir a CRT **fornecer feedback** rapidamente sobre o que será desenvolvido, por meio de protótipos interativos de alta fidelidade.

### Verificação e Validação de Requisitos

- **Definition of Ready (DoR)**: A técnica de DoR delimita quando um **requisito está preparado para ser trabalhado**. Para que seja considerado como *Ready*, serão levadas em consideração se:
1. O requisito está represntado por uma história de usuário?
1. O requisito possui critérios de aceitação orientados por *Behavior Driven Development* (BDD)?
1. As dependências do requisitos estão mapeadas (se houver)?
1. O requisito está consoante com a granularidade dos demais?
- **Definition of Done (DoD)**: A técnica de DoD demonstra **qualidade do requisito produzido**. Para que seja considerado como *Done*, deve atender ao seguinte:
1. Esse requisito entrega um incremento do produto?
1. Contempla critérios de aceite estabelecidos?
1. Está documentado para uso?
1. Segue os padrões [estabelecidos de codificação](../../CONTRIBUTING.md)?

### Organização e Atualização de Requisitos

- **Kanban**: será utilizado em conjunto com a plataforma [GitHub Projects](https://docs.github.com/pt/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) para organização visual das fases de cada um dos requisitos do backlog. Os requisitos serão divididos nas seguintes fases:
    |Todo | In Progress | Review | Done |
    |---- | ----------- | ------ | ---- |
    | Prontos para serem desenvolvidos: [*Ready*](#verificação-e-validação-de-requisitos) | Em desenvolvimento | Esperando por review: [*Done*](#verificação-e-validação-de-requisitos) | Revisados e finalizados |
    
- **MoSCoW**: será utilizada a técnica de priorização de requisitos *MoSCoW* (*Must Have, Should Have, Could Have, Won't Have*), com objetivo de gerar o Produto Mínimo Viável (*MVP*).
- **Fedback**: será utilizada a técnica de feedback para manter um backlog de produto organizado e atualizado conforme necessidades do projeto

## Engenharia de Requisitos e o AUP

*Aqui, as atividades da ER, suas práticas e técnicas devem ser mapeadas, a partir das fases (etapas) do processo estabelecido pela equipe, para a condução do projeto. Essas informações devem ser apresentadas em uma tabela conforme indicado, a seguir (exemplo).* 


|**Fases do AUP** |**Atividades ER** |**Prática** |**Técnica** |**Resultado Esperado** |
| - | - | - | - | - |
|**Concepção** |*Elicitação e Descoberta* |*Conversas e reuniões com a CRT* |*Entrevistas* |*Compreender e coletar requisitos* |
||*Análise e Consenso* |*Conversas e reuniões com a CRT* |*Entrevistas* |*Eliminar ambiguidades e preencher lacunas nos requisitos* |
||*Declaração* | *User Story* | *Narrativas de Usuário* |*Descrição das funcionalidades que entregam valor de negócio* |
||*Organização e Atualização* |*Priorização de Requisitos* |*MoSCoW* |*Mínimo Produto Viável (MVP)* |
|**Elaboração** |*Verificação e Validação* | *Validação de Requisitos* |*Aplicação da DoD* |*Lista de US prontas pasra serem revisadas — Review* |
|||*Verificação de Requisitos*|*Aplicação da DoR*| *Lista de US prontas para serem desenvolvidas — Todo*
||*Representação* |*Prototipação* |*Prototipação Intertativa* |*Garantir entrega alinhada às expectativas do cliente* |
||*Organização e Atualização* |*Organização de Backlog* |*Kanban* |*Organização do Backlog* |
|||*Organização de Backlog* |*Feedbacl* |*Organização do Backlog* |
|**Construção** |*Representação* |*<Prática 6>* |*<Técnica 6>* |*<Resultado esperado 6>* |
||*Elicitação e Descoberta* |*<Prática 7>* |*<Técnica 7>* |*<Resultado esperado 7>* |
||*Organização e Atualização* |*<Prática 8>* |*<Técnica 8>* |*<Resultado esperado 8>* |
|**Transição** |*Representação* |*<Prática 6>* |*<Técnica 6>* |*<Resultado esperado 6>* |
||*Elicitação e Descoberta* |*<Prática 7>* |*<Técnica 7>* |*<Resultado esperado 7>* |
||*Organização e Atualização* |*<Prática 8>* |*<Técnica 8>* |*<Resultado esperado 8>* |

## Histórico de versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
| 12/05/2025 | 0.1 | Descrição das técnicas utilizadas | Wanjo Christopher |
|||||
|||||