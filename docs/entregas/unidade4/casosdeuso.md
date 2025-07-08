# Estudo de caso: ConnectCare

Em uma comunidade remota chamada Vila Esperança, onde o acesso a serviços de saúde é limitado, um grupo de desenvolvedores e ativistas sociais se reuniu para criar o "ConnectCare". A plataforma foi projetada para superar barreiras, como a falta de transporte e informações, facilitando o acesso dos moradores a cuidados médicos. O objetivo principal é garantir que comunidades vulneráveis tenham acesso facilitado e eficiente a serviços de saúde, promovendo bem-estar social e impacto positivo por meio da tecnologia.

Para facilitar o entendimento do produto, foi utilizado Diagrama de Casos de Uso, que pode ser visualizado a seguir.
<div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://lucid.app/documents/embedded/0d6cf692-ced8-43f7-ba5d-cdf58f6ce4ab" id="-FXvrC83u1Cn"></iframe></div>

## Atores

- *Administrador*: Administrador do sistema, responsável pela manutenção e funcionamento do sistema.
- *Paciente*: Público-alvo do sistema, pode localizar e acessar serviços de saúde essenciais.
- *Profissional da saúde*: Gerencia os atendimentos e acessam informações de saúde dos pacientes.
- *Agente comunitário*: Gerencia visitas domiciliares e relatórios de saúde das comunidades.
- *Parceiro*: Gerencia campanhas de saúde e seus indicadores de desempenho.

## Mapeamento de Casos de Uso

1. Administrador


2. Paciente


3. Profissional da saúde


4. Agente Comunitário


5. Parceiros


# Especificação dos Casos de Uso

## 1. Monitorar sistema

### Breve Descrição
Este caso de uso permite que o administrador do sistema acompanhe, em tempo real ou em intervalos definidos, os indicadores de desempenho da plataforma ConnectCare.  
Os dados analisados incluem número de usuários ativos, agendamentos realizados, taxa de satisfação, falhas técnicas e avaliações de usuários.  
O objetivo é garantir a qualidade do serviço, identificar anomalias e orientar decisões estratégicas.


### Atores
- **Administrador do sistema**

### Fluxo de Eventos

**Fluxo Principal**
1. O administrador acessa a funcionalidade “Monitoramento do Sistema” no painel principal.
2. O sistema exibe um dashboard com métricas atualizadas:
   - usuários ativos,
   - número de agendamentos,
   - taxa de satisfação,
   - falhas registradas.
3. O administrador seleciona uma métrica específica para análise detalhada.
4. O sistema exibe gráficos, estatísticas e filtros por data, região ou tipo de serviço.
5. O administrador identifica irregularidades ou pontos de melhoria.
6. O administrador pode registrar ações internas ou abrir solicitações técnicas.
7. O caso de uso se encerra.


**Fluxos Alternativos**

**FA01 – Visualizar feedbacks dos usuários**
- O administrador seleciona a aba “Avaliações”.
- O sistema exibe os comentários e avaliações mais recentes dos usuários.
- O administrador filtra por tipo de serviço, período ou região.

 **FA02 – Exportar relatório de desempenho**
- O administrador seleciona a opção “Exportar”.
- O sistema apresenta os formatos disponíveis (PDF, CSV).
- O administrador escolhe o formato e clica em “Gerar”.
- O sistema gera o relatório e disponibiliza para download.


**Fluxos de Exceção**

**FE01 – Falha no carregamento de dados**
- O sistema exibe a mensagem:  
  **“Erro ao carregar dados do painel. Tente novamente mais tarde.”**
- O sistema retorna ao passo 2 com dados parciais ou sugere nova tentativa.

**FE02 – Falha na exportação**
- O sistema exibe a mensagem:  
  **“Erro ao exportar o relatório. Tente novamente.”**
- O sistema retorna ao FA02.


### Regras de Negócio (RN)
- **RN01 – Acesso restrito**: Apenas administradores autenticados têm acesso ao painel de monitoramento.
- **RN02 – Atualização periódica**: As métricas devem ser atualizadas automaticamente a cada 15 minutos ou sob demanda.
- **RN03 – Conformidade com a LGPD**: Os dados devem ser anonimizados e armazenados de forma segura.


### Pontos de Extensão

**PE01 – Integração com alertas automatizados**
- **Local**: Após o passo 4 do fluxo principal.  
- **Descrição**: Se determinada métrica ultrapassar limites críticos (ex: falha > 10%), o sistema envia notificações automáticas para o administrador.

**PE02 – Geração automática de relatório semanal**
- **Local**: Após o passo 7 do fluxo principal.  
- **Descrição**: O sistema pode gerar relatórios periódicos com base nos dados monitorados e enviá-los automaticamente por e-mail institucional.


## 2. Gerenciar serviços de saúde
### Breve descrição


### Atores


### Fluxo de eventos
*Fluxo principal*
1. 
2. 

*Fluxos de exceção*
- *FE01 Nome da exceção*: 

### Requisitos especiais


### Regras de negócio


## 3. Visualizar serviços de saúde
### Breve descrição


### Atores


### Fluxo de eventos
*Fluxo principal*
1. 
2. 

*Fluxo alternativo 1*
No passo ...
1. 
2.

*Fluxos de exceção*
- *FE01 Nome da exceção*: 

### Requisitos especiais


### Regras de negócio


## 4. Gerenciar Campanhas 
### Breve descrição
Este caso de uso permite que os Parceiros criem, modifiquem, visualizem e removam campanhas de saúde no sistema ConnectCare, visando promover ações de prevenção, conscientização e promoção da saúde para as comunidades.

### Atores
- Parceiros.

### Fluxo de eventos
**Fluxo principal**
1. O caso de uso inicia quando o Parceiro acessa a funcionalidade "Gerenciar Campanhas de Saúde" no sistema ConnectCare.

2. O sistema exibe uma lista de campanhas de saúde existentes (se houver) e as seguintes opções:

- Criar Nova Campanha

- Editar Campanha

- Visualizar Detalhes

- Remover Campanha

3. O Parceiro seleciona a opção "Visualizar Detalhes" para uma campanha existente.

4. O sistema exibe todas as informações da campanha selecionada em um formato de somente leitura (ex: nome, descrição, público-alvo, período de início e fim, objetivos, recursos, status).

5. O caso de uso é encerrado.


**Fluxos alternativos**
FA01 - Criar Nova Campanha

1. No passo 2 do fluxo básico, o Parceiro seleciona a opção "Criar Nova Campanha".

2. O sistema apresenta um formulário para entrada de dados da nova campanha, solicitando:

- Nome da Campanha

- Descrição

- Público-alvo

- Período de Início

- Período de Fim

- Objetivos

- Recursos Necessários

- Status (ex: Rascunho, Ativa, Finalizada)

3. O Parceiro preenche os dados e clica em "Salvar" [FE01].

4. O sistema valida os dados [RN01] [RN02] e registra a nova campanha no banco de dados.

5. O sistema exibe a mensagem de sucesso: "Campanha criada com sucesso!".

6. O caso de uso é encerrado.

FA02 - Editar Campanha

1. No passo 2 do fluxo básico, o Parceiro seleciona uma campanha da lista e escolhe a opção "Editar Campanha".

2. O sistema carrega os dados da campanha selecionada em um formulário pré-preenchido.

3. O Parceiro modifica os dados conforme necessário e clica em "Salvar" [FE01].

4. O sistema valida os dados [RN01] [RN02] e atualiza as informações da campanha no banco de dados.

5. O sistema exibe a mensagem de sucesso: "Campanha atualizada com sucesso!".

6. O caso de uso é encerrado.

FA03 - Remover Campanha

1. No passo 2 do fluxo básico, o Parceiro seleciona uma campanha da lista e escolhe a opção "Remover Campanha".

2. O sistema solicita uma confirmação da remoção com uma janela de diálogo (modal) com o aviso "Atenção! Você tem certeza que deseja remover esta campanha? Esta ação é permanente."

3. Se o Parceiro confirmar a remoção, o sistema remove a campanha do banco de dados [RN03].

4. O sistema exibe a mensagem de sucesso: "Campanha removida com sucesso!".

5. O caso de uso é encerrado.


**Fluxos de exceção**
FE01: Dados Inválidos (FA01 passo 3, FA02 passo 3): Se os dados submetidos pelo Parceiro forem inválidos (ex: campos obrigatórios vazios, formato incorreto de data), o sistema não salva as informações, exibe mensagens de erro indicando qual(is) campo(s) precisa(m) ser corrigido(s) e permanece no formulário para correção.

FE02: Nenhuma Campanha Cadastrada (Fluxo Principal passo 2): Se não houver campanhas cadastradas no sistema, o sistema informará ao Parceiro que "Não há campanhas cadastradas no momento." e pode sugerir a criação de uma nova.

FE03: Falha na Conexão/Processamento: Em qualquer ponto onde o sistema tenta acessar o banco de dados ou processar informações (FA01 passo 4, FA02 passo 4, FA03 passo 3), se houver uma falha na conexão ou no processamento de dados, o sistema exibe uma mensagem de erro genérica (ex: "Erro ao processar a solicitação. Tente novamente mais tarde.") e o caso de uso é abortado.

### Requisitos especiais

A interface deve ser intuitiva e fácil de usar.

Todos os campos de entrada devem ser validados para garantir a integridade dos dados.

Somente Parceiros autenticados e autorizados devem ter acesso a esta funcionalidade.

Capacidade de filtrar e ordenar a lista de campanhas.


### Regras de negócio

RN01 - Nome Único: Cada campanha deve ter um nome único no sistema.

RN02 - Validação de Período: A "Período de Início" de uma campanha não pode ser posterior ao "Período de Fim".

RN03 - Restrição de Remoção: Campanhas que já foram ativas ou que possuem dados de impacto registrados (e que seriam usados em "Monitorar Indicadores de Impacto de Campanhas") não podem ser removidas diretamente, apenas arquivadas ou desativadas (ou necessitam de permissão especial do administrador).


## 5. Gerenciar conta de profissional da saúde
### Breve descrição
Este caso de uso permite que profissionais visualizem, editem, troquem de senha e excluam seu próprio perfil na ConnectCare

### Atores
- Profissional da saúde

### Fluxo de eventos
**Fluxo principal**

O caso de uso inicia quando o profissional da saúde clica no ícone "Meu Perfil"

1. O sistema apresenta as seguintes opções:

- Visualizar

- Editar

- Trocar de senha

- Excluir

2 - O profissional seleciona a opção "Visualizar"

3 - O sistema redireciona o profissional para a sua página de perfil, exibindo as informações

- Foto de perfil

- Nome

- E-mail de contato

- Especialidade

- Número de registro no conselho profissional

- Horários de atendimento

4 - O caso de uso é encerrado

**Fluxos alternativos**

FA01 - Editar

No passo 2 do fluxo básico, o profissional seleciona a opção "Editar"

1. O sistema exibe um formulário com as informações do usuário que podem ser editadas:
  
2. O profissiona edita os detalhes registrados no seu perfil [RN02] [RN03] [RN04] [FE01]
  
3. O sistema valida as informações, salva e exibe a mensagem de sucesso: "Seu perfil foi atualizado com sucesso!"
  
4. O caso de uso é encerrado


FA02- Trocar de Senha

No passo 2 do fluxo básico, o profissional seleciona a opção "Trocar de senha"

1. O sistema exibe um formulário específico para alteração de senha, solicitando:

- Senha Atual

- Nova Senha

- Confirmar Nova Senha

2. O profissional preenche os campos e clica em "Salvar".

3. O sistema valida se a "Senha Atual" informada está correta e salva as alterações. [FE02]

4. O sistema exibe a mensagem de sucesso: "Senha alterada com sucesso!.

5. O sistema desloga o profissional e redireciona para a página de login.

6. O caso de uso é encerrado.

FA03 - Excluir

No passo 2 do fluxo básico, o profissional seleciona a opção "Excluir"

1. O sistema exibe uma janela de diálogo (modal) com o aviso "Atenção! Você tem certeza que deseja excluir sua conta? Esta ação é permanente e não pode ser desfeita. Os atendimentos realizados ainda poderão ser acessados pelos pacientes atendidos e pelo administrador do sistema." e solicita que o profissional digite sua senha atual no campo correspondente. 

2. O profissional digita a senha e clica no botão de confirmação final, com "Excluir minha conta permanentemente".

3. O sistema valida se a "Senha Atual" informada está correta e executa a rotina de exclusão da conta. [FE02] [RN01]

4. O sistema desloga o profissional e o redireciona para a página inicial pública do ConnectCare.

5. O caso de uso é encerrado.

**Fluxos de exceção**

FE01: Dados Inválidos (FA01): No passo 3 do FA01, se os dados forem inválidos, o sistema não salva as informações, exibe uma mensagem de erro indicando o(s) campo(s) problemático(s) e permanece no formulário de edição para correção.

FE02: Senha Atual Incorreta (FA02 passo 3, FA03 passo 3): Se a senha atual informada para troca ou exclusão estiver incorreta, o sistema exibe a mensagem "Senha atual incorreta. Tente novamente." e não prossegue com a ação.

FE03: Novas Senhas não Coincidem (FA02): Se no passo 2 a nova senha e sua confirmação não forem idênticas, o sistema exibe a mensagem "As novas senhas não coincidem." e limpa os campos para nova digitação.

### Requisitos especiais

Esse caso de uso deve ser acessível por dispositivo móvel.

### Regras de negócio

RN01 - Resolução CFM nº 1.821/2007:  O sistema deve seguir a resolução CFM nº 1.821/2007 que aprova as normas técnicas concernentes à digitalização e uso dos sistemas informatizados para a guarda e manuseio dos documentos dos prontuários dos pacientes, autorizando a eliminação do papel e a troca de informação identificada em saúde.

RN02 - Número de registro no conselho profissional: O sistema deve integrar-se com os serviços públicos dos conselhos profissionais para verificar se o registro é válido e se o profissional está com o status "Ativo". Se a verificação falhar, o perfil não pode ser publicado.

RN03 - Horários de atendimento: Os horários de atendimento não podem ultrapassar 8h diárias.

RN04 - Foto de perfil: A foto deve ser uma imagem nítida do rosto do profissional e ter no máximo 5mb. É proibido o uso de logotipos, avatares, paisagens, personagens ou qualquer imagem que não seja do próprio profissional.


## 6. Gerenciar Relatórios de Comunidade

### Breve descrição
Este caso de uso permite que um agente comunitário registre e visualize relatórios sobre o estado de saúde da comunidade atendida por meio da plataforma ConnectCare.  
Os relatórios incluem dados coletados em visitas domiciliares, campanhas de saúde e observações gerais sobre fatores ambientais, sociais e epidemiológicos.  
O objetivo é fornecer uma visão consolidada para apoiar decisões estratégicas em saúde pública.

### Atores
- Agente comunitário  
- Administrador do sistema

### Fluxo de eventos

**Fluxo principal**
1. O agente acessa a opção “Relatórios da Comunidade” no menu principal.  
2. O sistema apresenta as opções:  
   - Criar novo relatório  
   - Visualizar relatórios anteriores  
   - Exportar relatório  
3. O agente seleciona “Criar novo relatório”.  
4. O sistema apresenta um formulário com os campos:
   - Período da coleta  
   - Áreas visitadas  
   - Problemas de saúde mais recorrentes  
   - Número de atendimentos realizados  
   - Observações adicionais  
5. O agente preenche todos os campos obrigatórios.
6. O agente confirma o envio do relatório.  
7. O sistema valida os dados, armazena o relatório e disponibiliza uma visualização resumida.  
8. O agente recebe uma notificação de confirmação.  
9. O caso de uso se encerra.

**Fluxo alternativo 1 – Visualizar relatórios anteriores**
No passo 2, o agente seleciona a opção “Visualizar relatórios anteriores”.
1. O sistema exibe uma lista filtrável por data, área e tipo de relatório.  
2. O agente seleciona um relatório e o sistema exibe o conteúdo completo.  

**Fluxo alternativo 2 – Exportar relatório**
No passo 2, o agente seleciona um relatório disponível.  
1. O sistema oferece opções de exportação (PDF, CSV).  
2. O agente escolhe o formato desejado.  
3. O sistema gera o arquivo e disponibiliza o download.

**Fluxos de exceção**
- *FE01 – Campos obrigatórios não preenchidos*:  
  “Todos os campos obrigatórios devem ser preenchidos antes de salvar o relatório.”  
  O sistema retorna ao passo 5 do fluxo principal.  

- *FE02 – Falha na exportação*:  
  “Erro ao exportar o relatório. Tente novamente mais tarde.”  
  O sistema retorna ao fluxo alternativo de exportação.

### Requisitos especiais
- Os relatórios devem estar disponíveis para visualização offline, se necessário.
- O sistema deve permitir exportação em formatos PDF e CSV.
- O caso de uso deve ser acessível por dispositivos móveis de baixa performance.

### Regras de negócio

- **RN01 – Preenchimento obrigatório**  
  O sistema não permite salvar o relatório se campos obrigatórios estiverem vazios.

- **RN02 – Acesso restrito**  
  Apenas agentes autenticados podem criar relatórios. Apenas administradores podem visualizar relatórios consolidados de várias regiões.

- **RN03 – Armazenamento seguro**  
  Os relatórios devem ser armazenados seguindo normas da LGPD, com acesso controlado por perfil.

- **RN04 – Relatórios como fonte de estatística pública**  
  Os dados podem ser consolidados e utilizados de forma anônima para formulação de políticas públicas.

### Pontos de Extensão

- **PE01 – Integração com dados de campanhas e atendimentos individuais**  
  *Local do Ponto de Extensão:* Após o passo 4  
  *Descrição:* O sistema pode sugerir dados automáticos com base em atendimentos registrados na plataforma.

- **PE02 – Geração de indicadores visuais**  
  *Local do Ponto de Extensão:* Após o passo 7  
  *Descrição:* O sistema pode gerar gráficos e tabelas para visualização rápida dos dados do relatório.
  
## 7. Gerenciar Dados Médicos
### Breve descrição
Permite a criação e atualização de dados de saúde na plataforma, incluindo registros clínicos por profissionais , informações de perfil por pacientes e relatórios de saúde por agentes comunitários.

### Atores
1. Profissional de Saúde
1. Paciente
1. Agente Comunitário

### Fluxo de eventos
*Fluxo Base (F.B)* 
1. O Profissional de Saúde, durante um atendimento, acessa o prontuário digital de um paciente.
1. O ator seleciona a opção para adicionar um novo registro ao prontuário.
1. O ator insere as informações clínicas, como diagnósticos, prescrições, orientações ou solicitações de exames.
1. O sistema valida os dados inseridos para garantir a integridade das informações. [RN05] [FE01]
1. O ator confirma a submissão.
1.O sistema salva as novas informações no prontuário do paciente em tempo real e registra a identificação do profissional e a data/hora da alteração. [RN06] [RN08] [FE02]

*Fluxo alternativo 1 (F.A.01) - Paciente gerencia suas informações de perfil*
No passo 1 do Fluxo Principal, o ator é um Paciente.
1. O Paciente, logado no sistema, acessa a área de seu perfil pessoal.
1. O ator insere ou atualiza suas "informações pessoais, como nome, idade e condições de saúde preexistentes". [RN07]
1. O sistema valida e salva as informações no perfil do paciente.

*Fluxo alternativo 2 (F.A.02) - Agente Comunitário registra visita domiciliar*
No passo 1 do Fluxo Principal, o ator é um Agente Comunitário.
1. O Agente Comunitário, logado na plataforma, seleciona a funcionalidade específica para "registrar visitas domiciliares".
1. O ator preenche o relatório com as informações da visita, incluindo as "condições de saúde nas comunidades atendidas".
1. O sistema salva o relatório, que pode ser usado para a "identificação de áreas prioritárias e na organização de campanhas preventivas".

*Fluxos de exceção*
- *F.E.01 Validação de dados falha*: No passo 4 do Fluxo Principal, se os dados inseridos forem inválidos ou incompletos conforme a RN05, o sistema impede o salvamento e informa ao ator quais campos precisam ser corrigidos.
- *F.E.02 - Falha de conexão durante o salvamento*: No passo 6 do Fluxo Principal, se a conexão com a internet falhar, o sistema deve ser capaz de salvar um rascunho local para sincronização posterior, garantindo que o trabalho não seja perdido, visto que a plataforma é projetada para funcionar em conexões limitadas.


### Requisitos especiais
N/A.

### Regras de negócio
- RN05: Certos campos de um registro médico (ex: descrição do diagnóstico) são de preenchimento obrigatório para garantir um atendimento "preciso e eficiente".
- RN06: Todas as adições e alterações no prontuário de um paciente devem ser registradas com a identificação do profissional e a data/hora da alteração para garantir um ambiente "seguro e confiável".
- RN07: O Paciente só pode gerenciar suas informações básicas e "condições de saúde preexistentes", não podendo inserir registros clínicos como "diagnósticos, prescrições e orientações".
- RN08: Profissionais de Saúde e Agentes Comunitários só podem gerenciar dados de pacientes e comunidades dentro de sua área de atuação designada.


## Histórico de versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
|**07/07/25**|0.1| Adiciona esqueleto |Sophia|
|**07/07/25**|0.2|Adicionando o Caso de Uso número 6 |Pedro|
|**07/07/25**|0.3|Adicionando o Caso de Uso número 1 |Kaio|
