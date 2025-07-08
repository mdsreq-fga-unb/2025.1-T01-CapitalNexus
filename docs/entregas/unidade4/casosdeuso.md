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

## 6. Gerenciar Dados Médicos
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
- RN04: Toda a manipulação e exibição de dados deve estar em conformidade com as regulamentações de proteção de dados.
- RN05: Certos campos de um registro médico (ex: descrição do diagnóstico) são de preenchimento obrigatório para garantir um atendimento "preciso e eficiente".
- RN06: Todas as adições e alterações no prontuário de um paciente devem ser registradas com a identificação do profissional e a data/hora da alteração para garantir um ambiente "seguro e confiável".
- RN07: O Paciente só pode gerenciar suas informações básicas e "condições de saúde preexistentes", não podendo inserir registros clínicos como "diagnósticos, prescrições e orientações".
- RN08: Profissionais de Saúde e Agentes Comunitários só podem gerenciar dados de pacientes e comunidades dentro de sua área de atuação designada.

## Histórico de versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
|**07/07/25**|0.1| Adiciona esqueleto |Sophia|
|**07/07/25**|0.2| Adiciona UC de Gerenciar Dados Médicos |Wanjo Chriustopher|
