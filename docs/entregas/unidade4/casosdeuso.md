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


## 4. Acessar serviços de saúde
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



## Histórico de versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
|**07/07/25**|0.1|Adiciona esqueleto |Sophia|
|**07/07/25**|0.2|Adicionando o Caso de Uso número 6 |Pedro|
