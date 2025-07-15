# Mapeamento de Requisitos por Área

Este documento organiza os casos de uso (US) do sistema por módulos funcionais, **mapeando cada funcionalidade** às suas **respectivas regras de negócio** (RN). A estrutura permite visualizar rapidamente as capacidades do sistema e suas dependências regulatórias.

## 📂 Página de Gestão de Núcleos
*Gerenciamento dos centros de responsabilidade da equipe*

| Caso de Uso       | Descrição                              | Regras Associadas |
|-------------------|----------------------------------------|------------------|
| **US01**          | Cadastrar novo núcleo                  | RN02, RN06       |
| **US02**          | Editar informações de núcleo existente | RN02, RN06       |
| **US03**          | Excluir núcleo dissolvido              | RN02, RN06       |

---

## 👥 Página de Gestão de Membros e Perfis
*Gerenciamento de cadastro, permissões e informações dos membros*

| Caso de Uso       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US04**          | Cadastrar novos membros                        | RN01             |
| **US05**          | Atualizar informações/alocação de membros      | RN02, RN06       |
| **US06**          | Excluir membro (manter apenas ativos)          | RN02, RN06       |
| **US07**          | Consultar lista de membros e responsabilidades | RN02             |

---

## 📅 Página de Gestão de Reuniões e Frequência
*Agendamento e controle de presenças/justificativas*

| Caso de Uso       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US08**          | Cadastrar nova reunião                         | RN04             |
| **US09**          | Atualizar reunião agendada                     | RN04             |
| **US10**          | Realizar lista de presença                     | RN03, RN05       |
| **US11**          | Justificar falta em reunião                    | -                |
| **US12**          | Avaliar justificativas (aprovar/reprovar)      | RN03             |

---

## 📊 Área de Relatórios de Desempenho
*Geração de relatórios analíticos*

| Caso de Uso       | Descrição                              | Regras Associadas |
|-------------------|----------------------------------------|------------------|
| **US13**          | Relatório de desempenho dos membros    | RN03             |
| **US14**          | Relatório de situação dos núcleos      | -                |

---

## 🌐 Páginas Públicas e Gestão de Conteúdo (Marketing)
*Conteúdo visível ao público externo*

| Caso de Uso       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US15**          | Formulário de contato para parcerias           | -                |
| **US16**          | Publicar conteúdo na área pública              | -                |
| **US17**          | Editar conteúdo da área pública                | -                |
| **US18**          | Excluir conteúdo publicado                     | -                |

---

## 📦 Página de Gestão de Estoques e Materiais
*Controle de materiais da equipe*

| Caso de Uso       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US19**          | Adicionar materiais ao núcleo                 | -                |
| **US20**          | Modificar material (atualizar estoque)         | -                |
| **US21**          | Visualizar listas de materiais                 | -                |
| **US22**          | Reservar material disponível                   | -                |
| **US23**          | Solicitar compra de novos materiais            | -                |
| **US24**          | Relatório de materiais em falta/solicitações   | -                |

## 📜 Histórico de Versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
|**15/07/25**| 0.1 | Construindo documento de mapeamento de requisitos e interface | Victor Câmara e Wanjo Christopher |