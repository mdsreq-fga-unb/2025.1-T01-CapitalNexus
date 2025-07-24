# Mapeamento de Requisitos por Área

Este documento organiza as Histórias de Usuário (US) do sistema por módulos funcionais, **mapeando cada funcionalidade** às suas **respectivas regras de negócio** (RN). Permitindo visualizar rapidamente as capacidades do sistema e suas dependências regulatórias.

## 📂 Página de Gestão de Núcleos
*Gerenciamento dos centros de responsabilidade da equipe*

| História de Usuário       | Descrição                              | Regras Associadas |
|-------------------|----------------------------------------|------------------|
| **US02**          | Editar informações de núcleo existente | RN02, RN06       |

---

## 👥 Página de Gestão de Membros e Perfis
*Gerenciamento de cadastro, permissões e informações dos membros*

| História de Usuário       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US04**          | Cadastrar novos membros                        | RN01             |
| **US05**          | Atualizar informações de membros      | RN02, RN06       |
| **US06**          | Excluir membro           | RN02, RN06       |

---

## 📅 Página de Gestão de Reuniões e Frequência
*Agendamento e controle de presenças/justificativas*

| História de Usuário       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US08**          | Cadastrar nova reunião                         | RN04             |
| **US09**          | Atualizar reunião agendada                     | RN04             |
| **US10**          | Realizar lista de presença                     | RN03, RN05       |
| **US11**          | Justificar falta em reunião                    | -                |
| **US12**          | Avaliar justificativas (aprovar/reprovar)      | RN03             |

---


## 🌐 Páginas Públicas e Gestão de Conteúdo (Marketing)
*Conteúdo visível ao público externo*

| História de Usuário       | Descrição                                      | Regras Associadas |
|-------------------|------------------------------------------------|------------------|
| **US15**          | Formulário de contato para parcerias           | -                |
| **US18**          | Excluir conteúdo publicado                     | -                |

---

## 📦 Página de Gestão de Estoques e Materiais
*Controle de materiais da equipe*

| História de Usuário       | Descrição                                      | Regras Associadas |
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
|**15/07/25**| 1.0 | Construindo documento de mapeamento de requisitos e interface | Victor Câmara e Wanjo Christopher |
|**23/07/25**| 1.1 | Corrige nomenclatura e remove US's que estavam fora do MVP | Wanjo Christopher |