# Estudo de caso: ConnectCare

Em uma comunidade remota chamada Vila Esperança, onde o acesso a serviços de saúde é limitado, um grupo de desenvolvedores e ativistas sociais se reuniu para criar o "ConnectCare". A plataforma foi projetada para superar barreiras, como a falta de transporte e informações, facilitando o acesso dos moradores a cuidados médicos. O objetivo principal é garantir que comunidades vulneráveis tenham acesso facilitado e eficiente a serviços de saúde, promovendo bem-estar social e impacto positivo por meio da tecnologia.

Para facilitar o entendimento do produto, foi utilizado Diagrama de Casos de Uso, que pode ser visualizado a seguir.

<img src="https://raw.githubusercontent.com/mdsreq-fga-unb/2025.1-T01-CapitalNexus/refs/heads/main/docs/entregas/unidade4/diagramauml.png" alt="Diagrama UML">
Figura 1: Diagrama UML ConnectCare

<div style="width: 640px; height: 480px; margin: 10px; position: relative;"><iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://lucid.app/documents/embedded/0d6cf692-ced8-43f7-ba5d-cdf58f6ce4ab" id="-FXvrC83u1Cn"></iframe></div>

## Especificação de Casos de Uso - ConnectCare  
**Versão 1.0**  


## 👥 Atores   
- **Administrador**: Administrador do sistema, responsável pela manutenção e funcionamento do sistema.  
- **Paciente**: Público-alvo do sistema, pode localizar e acessar serviços de saúde essenciais.  
- **Profissional da Saúde**: Gerencia os atendimentos e acessa informações de saúde dos pacientes.  
- **Agente Comunitário**: Gerencia visitas domiciliares e relatórios de saúde das comunidades.  
- **Parceiro**: Gerencia campanhas de saúde e seus indicadores de desempenho.  

---

## 🗺️ Mapeamento de Casos de Uso  

| Ator                   | Casos de Uso                                 |
|------------------------|----------------------------------------------|
| Administrador          | UC01 - Monitorar Sistema                     |
| Paciente               | UC02 - Gerenciar Dados Médicos               |
| Profissional da Saúde  | UC03 - Gerenciar Conta de Profissional da Saúde <br> UC04 - Gerenciar Serviços de Saúde |
| Agente Comunitário     | UC05 - Gerenciar Relatórios de Comunidade    |
| Parceiro               | UC06 - Gerenciar Campanhas                   |

---

## 📑 Especificações dos Casos de Uso  

### UC01 - Monitorar Sistema  
#### 1. Breve Descrição  
Este caso de uso permite que o Administrador do sistema acompanhe, em tempo real ou em intervalos definidos, os indicadores de desempenho da plataforma ConnectCare. Os dados analisados incluem número de usuários ativos, agendamentos realizados, taxa de satisfação, falhas técnicas e avaliações de usuários. O objetivo é garantir a qualidade do serviço, identificar anomalias e orientar decisões estratégicas.  

#### 2. Atores  
- Administrador  

#### 3. Pré-Condições  
- O Administrador deve estar autenticado no sistema com privilégios de acesso ao painel de monitoramento.  

#### 4. Fluxo Básico de Eventos  
1. O caso de uso inicia quando o Administrador acessa a funcionalidade "Monitoramento do Sistema" no painel principal.  
2. O sistema exibe um dashboard com métricas atualizadas em tempo real: usuários ativos, número de agendamentos, taxa de satisfação e falhas registradas.  
3. O Administrador seleciona uma métrica específica para análise detalhada.  
4. O sistema exibe gráficos, estatísticas e filtros por data, região ou tipo de serviço.  
5. O Administrador analisa os dados para identificar irregularidades ou pontos de melhoria.  
6. O Administrador pode registrar ações internas ou abrir solicitações técnicas com base na análise.  
7. O caso de uso se encerra.  

#### 5. Fluxos Alternativos  
**FA01 – Visualizar feedbacks dos usuários**  
1. No passo 2 do fluxo básico, o Administrador seleciona a aba "Avaliações".  
2. O sistema exibe os comentários e avaliações mais recentes dos usuários.  
3. O Administrador pode filtrar os resultados por tipo de serviço, período ou região.  
4. O fluxo retorna ao passo 5 do fluxo básico.  

**FA02 – Exportar relatório de desempenho**  
1. No passo 4 do fluxo básico, o Administrador seleciona a opção "Exportar".  
2. O sistema apresenta os formatos disponíveis (PDF, CSV).  
3. O Administrador escolhe o formato e clica em "Gerar".  
4. O sistema gera o relatório e o disponibiliza para download.  
5. O fluxo retorna ao passo 5 do fluxo básico.  

#### 6. Fluxos de Exceção  
**FE01 – Falha no carregamento de dados**  
- Se o sistema não conseguir carregar os dados no passo 2, ele exibe a mensagem: "Erro ao carregar dados do painel. Tente novamente mais tarde."  
- O sistema pode exibir dados parciais ou retornar ao painel principal.  

**FE02 – Falha na exportação**  
- Se o sistema falhar ao gerar o arquivo no passo 4 do FA02, ele exibe a mensagem: "Erro ao exportar o relatório. Tente novamente."  
- O sistema retorna ao passo 2 do FA02.  

#### 7. Pós-Condições  
- Os dados de monitoramento são visualizados pelo Administrador.  
- Um relatório de desempenho é exportado com sucesso.  

#### 8. Regras de Negócio  
- **RN01 – Acesso restrito**: Apenas administradores autenticados têm acesso ao painel de monitoramento.  
- **RN02 – Atualização periódica**: As métricas devem ser atualizadas automaticamente a cada 15 minutos ou sob demanda.  
- **RN03 – Conformidade com a LGPD**: Os dados de usuários exibidos devem ser anonimizados para garantir a privacidade.  

#### 9. Pontos de Extensão  
**PE01 – Integração com alertas automatizados**  
- **Local**: Após o passo 4 do fluxo básico.  
- **Descrição**: Se determinada métrica ultrapassar limites críticos (ex: taxa de falhas > 10%), o sistema pode enviar notificações automáticas (e-mail, SMS) para a equipe de administradores.  

**PE02 – Geração automática de relatório semanal**  
- **Local**: Independente do fluxo.  
- **Descrição**: O sistema pode ser configurado para gerar relatórios periódicos (diários, semanais, mensais) e enviá-los automaticamente por e-mail para uma lista de destinatários.  

### UC02 - Gerenciar Dados Médicos
#### 1. Breve Descrição
Este caso de uso permite que o Paciente visualize seu histórico de saúde consolidado, anexe documentos pessoais (como exames de laboratórios externos), gerencie as permissões de acesso dos profissionais de saúde e exporte seus dados.

#### 2. Atores
- Paciente

#### 3. Pré-Condições
- O Paciente deve estar autenticado (logado) no sistema ConnectCare.

#### 4. Fluxo Básico de Eventos
1. O caso de uso inicia quando o Paciente clica na opção "Meu Prontuário".
2. O sistema exibe uma interface centralizada com o histórico de saúde do Paciente, contendo as opções: "Visualizar Consultas", "Documentos Anexados", "Gerenciar Permissões" e "Exportar Dados".
3. O Paciente seleciona a opção "Visualizar Consultas".
4. O sistema exibe a lista de consultas que ele realizou através da plataforma, ordenadas da mais recente para a mais antiga.
5. O caso de uso é encerrado.

#### 5. Fluxos Alternativos
**FA01 - Anexar Documento Pessoal**
1. No passo 2 do fluxo básico, o Paciente seleciona a opção "Documentos Anexados".
2. O sistema exibe a lista de documentos já anexados e a opção "Anexar Novo Documento".
3. O Paciente clica em "Anexar Novo Documento".
4. O sistema exibe um formulário solicitando:
   - Título
   - Data
   - Tipo de Documento (Exame, Laudo, Atestado)
   - Campo para upload de arquivo
5. O Paciente preenche as informações, seleciona o arquivo e clica em "Salvar". [FE01]
6. O sistema valida o arquivo, o armazena de forma segura associado ao prontuário do Paciente e exibe a mensagem: "Documento anexado com sucesso!".
7. O fluxo retorna ao passo 2 deste fluxo alternativo.

**FA02 - Gerenciar Permissões de Acesso**
1. No passo 2 do fluxo básico, o Paciente seleciona a opção "Gerenciar Permissões".
2. O sistema exibe uma lista de todos os profissionais de saúde que já interagiram com o Paciente, mostrando o status de acesso atual ("Ativo", "Expirado", "Revogado"). [RN02]
3. O Paciente seleciona um profissional e modifica sua permissão (ex: de "Ativo" para "Revogar Acesso"). [RN03]
4. O sistema solicita confirmação da ação.
5. Após a confirmação, o sistema salva a alteração e exibe a mensagem: "Permissão de acesso atualizada.".
6. O fluxo retorna ao passo 2 deste fluxo alternativo.

**FA03 - Exportar Dados**
1. No passo 2 do fluxo básico, o Paciente seleciona a opção "Exportar Dados".
2. O sistema solicita a seleção do formato ("PDF" ou "CSV") e o intervalo de datas.
3. O Paciente confirma a exportação.
4. O sistema gera um arquivo seguro e protegido por senha, contendo as informações do prontuário, e o disponibiliza para download. [FE02]
5. O caso de uso é encerrado.

#### 6. Fluxos de Exceção
**FE01 - Falha no Upload (FA01)**
- Se o arquivo selecionado for maior que o limite (10MB) ou de um formato não suportado (.exe), o sistema recusa o upload e exibe a mensagem: "Erro: O arquivo é muito grande ou possui um formato inválido. Use apenas PDF, JPG ou PNG.".

**FE02 - Erro na Geração do Relatório (FA03)**
- Se ocorrer um problema técnico durante a compilação dos dados, o sistema exibe a mensagem: "Não foi possível gerar seu relatório no momento. Por favor, tente novamente mais tarde.".

#### 7. Pós-Condições
- O prontuário do Paciente é atualizado com um novo documento.
- As permissões de acesso de um profissional são alteradas.
- Os dados de saúde do Paciente são exportados com sucesso.

#### 8. Requisitos Especiais
- **RE01 - Segurança e Privacidade (LGPD)**: Todos os dados de saúde devem ser criptografados. O sistema deve estar em conformidade com a LGPD.
- **RE02 - Auditoria (Log de Acesso)**: Todas as ações no prontuário devem ser registradas em um log de auditoria acessível ao Paciente.
- **RE03 - Usabilidade e Clareza**: A interface deve ser intuitiva, evitando jargões médicos excessivos.
- **RE04 - Acessibilidade Móvel**: A funcionalidade deve ser completamente funcional em dispositivos móveis.

#### 9. Regras de Negócio
- **RN01 - Paciente como Controlador dos Dados**: O Paciente é o controlador de seus dados. Os profissionais de saúde atuam como operadores.
- **RN02 - Política de Acesso Padrão**: Um profissional ganha acesso temporário ao prontuário (ex: 90 dias) após um atendimento.
- **RN03 - Revogação de Acesso**: Uma vez revogado, o profissional não poderá mais visualizar os dados do prontuário, exceto os registros que ele mesmo realizou.
- **RN04 - Integridade do Registro Clínico**: O Paciente pode adicionar informações, mas não pode alterar ou excluir registros feitos por um profissional de saúde.


### UC03 - Gerenciar Conta de Profissional da Saúde

#### 1. Breve Descrição
Este caso de uso permite que um Profissional da Saúde visualize, edite suas informações de perfil, troque sua senha e exclua sua própria conta na plataforma ConnectCare.

#### 2. Atores
- Profissional da Saúde

#### 3. Pré-Condições
- O Profissional da Saúde deve estar autenticado no sistema.

#### 4. Fluxo Básico de Eventos
1. O caso de uso inicia quando o Profissional da Saúde clica na opção "Meu Perfil".
2. O sistema exibe a página de perfil do profissional com suas informações:
   - Foto
   - Nome
   - E-mail
   - Especialidade
   - Número de registro profissional
   - Horários de atendimento
3. O sistema também apresenta as opções: "Editar Perfil", "Trocar Senha" e "Excluir Conta".
4. O caso de uso se encerra (permanecendo na tela de visualização).

#### 5. Fluxos Alternativos
**FA01 - Editar Perfil**
1. No passo 3 do fluxo básico, o profissional seleciona a opção "Editar Perfil".
2. O sistema exibe um formulário com as informações editáveis do perfil. [RN02] [RN03] [RN04]
3. O profissional edita os dados desejados e clica em "Salvar". [FE01]
4. O sistema valida as informações, salva as alterações e exibe a mensagem: "Seu perfil foi atualizado com sucesso!".
5. O sistema retorna ao passo 2 do fluxo básico, exibindo os dados atualizados.

**FA02 - Trocar Senha**
1. No passo 3 do fluxo básico, o profissional seleciona a opção "Trocar Senha".
2. O sistema exibe um formulário solicitando:
   - Senha Atual
   - Nova Senha
   - Confirmar Nova Senha
3. O profissional preenche os campos e clica em "Salvar".
4. O sistema valida se a "Senha Atual" está correta e se as novas senhas coincidem. [FE02] [FE03]
5. O sistema salva a nova senha, exibe a mensagem "Senha alterada com sucesso!" e desloga o profissional por segurança, redirecionando-o para a página de login.
6. O caso de uso é encerrado.

**FA03 - Excluir Conta**
1. No passo 3 do fluxo básico, o profissional seleciona a opção "Excluir Conta".
2. O sistema exibe uma janela de confirmação com o aviso sobre a permanência dos registros de atendimento e solicita a senha atual para confirmação. [RN01]
3. O profissional digita a senha e clica no botão de confirmação final "Excluir minha conta permanentemente".
4. O sistema valida a senha. [FE02]
5. O sistema executa a rotina de exclusão da conta, desloga o profissional e o redireciona para a página inicial pública do ConnectCare.
6. O caso de uso é encerrado.

#### 6. Fluxos de Exceção
**FE01 - Dados Inválidos (FA01)**
- Se os dados no formulário de edição forem inválidos, o sistema não salva, exibe uma mensagem de erro indicando o campo problemático e permanece no formulário para correção.

**FE02 - Senha Atual Incorreta (FA02, FA03)**
- Se a senha atual informada estiver incorreta, o sistema exibe a mensagem "Senha atual incorreta. Tente novamente." e não prossegue com a ação.

**FE03 - Novas Senhas não Coincidem (FA02)**
- Se a nova senha e sua confirmação não forem idênticas, o sistema exibe a mensagem "As novas senhas não coincidem." e limpa os campos de senha para nova digitação.

#### 7. Pós-Condições
- O perfil do profissional é atualizado com sucesso.
- A senha do profissional é alterada e ele é deslogado.
- A conta do profissional é permanentemente removida.

#### 8. Requisitos Especiais
- **RE01 - Acessibilidade Móvel**: O caso de uso deve ser totalmente funcional em dispositivos móveis.

#### 9. Regras de Negócio
- **RN01 - Resolução CFM nº 1.821/2007**: O sistema deve garantir a guarda e o manuseio dos prontuários conforme a resolução. A exclusão da conta do profissional não remove os registros de atendimentos já realizados.
- **RN02 - Validação de Registro Profissional**: O sistema deve, se possível, integrar-se a serviços para validar o número de registro profissional informado.
- **RN03 - Limite de Horário**: Os horários de atendimento cadastrados não podem ultrapassar um limite diário razoável (ex: 8 horas).
- **RN04 - Foto de Perfil**: A foto deve ser uma imagem nítida do rosto do profissional (máx. 5MB), não sendo permitidos logotipos, avatares, etc.

### UC04 - Gerenciar Conta de Profissional da Saúde

#### 1. Breve Descrição
Este caso de uso permite que profissionais visualizem, editem, troquem de senha e excluam seu próprio perfil na ConnectCare.

#### 2. Atores
- Profissional da saúde

#### 3. Pré-Condições
- O profissional da saúde deve estar autenticado no sistema.

#### 4. Fluxo Básico de Eventos
1. O caso de uso inicia quando o profissional da saúde clica no ícone "Meu Perfil".
2. O sistema apresenta as seguintes opções:
   - Visualizar
   - Editar
   - Trocar de senha
   - Excluir
3. O profissional seleciona a opção "Visualizar".
4. O sistema redireciona o profissional para sua página de perfil, exibindo as informações:
   - Foto de perfil
   - Nome
   - E-mail de contato
   - Especialidade
   - Número de registro no conselho profissional
   - Horários de atendimento
5. O caso de uso é encerrado.

#### 5. Fluxos Alternativos
**FA01 - Editar**
1. No passo 2 do fluxo básico, o profissional seleciona a opção "Editar".
2. O sistema exibe um formulário com as informações do usuário que podem ser editadas.
3. O profissional edita os detalhes registrados no seu perfil [RN02] [RN03] [RN04] [FE01].
4. O sistema valida as informações, salva e exibe a mensagem de sucesso: "Seu perfil foi atualizado com sucesso!".
5. O caso de uso é encerrado.

**FA02 - Trocar de Senha**
1. No passo 2 do fluxo básico, o profissional seleciona a opção "Trocar de senha".
2. O sistema exibe um formulário específico para alteração de senha, solicitando:
   - Senha Atual
   - Nova Senha
   - Confirmar Nova Senha
3. O profissional preenche os campos e clica em "Salvar".
4. O sistema valida se a "Senha Atual" informada está correta e salva as alterações [FE02].
5. O sistema exibe a mensagem de sucesso: "Senha alterada com sucesso!".
6. O sistema desloga o profissional e redireciona para a página de login.
7. O caso de uso é encerrado.

**FA03 - Excluir**
1. No passo 2 do fluxo básico, o profissional seleciona a opção "Excluir".
2. O sistema exibe uma janela de diálogo (modal) com o aviso: "Atenção! Você tem certeza que deseja excluir sua conta? Esta ação é permanente e não pode ser desfeita. Os atendimentos realizados ainda poderão ser acessados pelos pacientes atendidos e pelo administrador do sistema." e solicita que o profissional digite sua senha atual.
3. O profissional digita a senha e clica no botão de confirmação final: "Excluir minha conta permanentemente".
4. O sistema valida se a "Senha Atual" informada está correta e executa a rotina de exclusão da conta [FE02] [RN01].
5. O sistema desloga o profissional e o redireciona para a página inicial pública do ConnectCare.
6. O caso de uso é encerrado.

#### 6. Fluxos de Exceção
**FE01 - Dados Inválidos (FA01)**
- No passo 3 do FA01, se os dados forem inválidos, o sistema não salva as informações, exibe uma mensagem de erro indicando o(s) campo(s) problemático(s) e permanece no formulário de edição para correção.

**FE02 - Senha Atual Incorreta (FA02 passo 3, FA03 passo 3)**
- Se a senha atual informada para troca ou exclusão estiver incorreta, o sistema exibe a mensagem "Senha atual incorreta. Tente novamente." e não prossegue com a ação.

**FE03 - Novas Senhas não Coincidem (FA02)**
- Se no passo 2 a nova senha e sua confirmação não forem idênticas, o sistema exibe a mensagem "As novas senhas não coincidem." e limpa os campos para nova digitação.

#### 7. Pós-Condições
- O perfil do profissional é visualizado com sucesso.
- O perfil do profissional é atualizado com sucesso.
- A senha do profissional é alterada com sucesso.
- A conta do profissional é excluída permanentemente.

#### 8. Requisitos Especiais
- **RE01 - Acessibilidade Móvel**: Esse caso de uso deve ser acessível por dispositivo móvel.

#### 9. Regras de Negócio
- **RN01 - Resolução CFM nº 1.821/2007**: O sistema deve seguir a resolução CFM nº 1.821/2007 que aprova as normas técnicas concernentes à digitalização e uso dos sistemas informatizados para a guarda e manuseio dos documentos dos prontuários dos pacientes, autorizando a eliminação do papel e a troca de informação identificada em saúde.
- **RN02 - Número de registro no conselho profissional**: O sistema deve integrar-se com os serviços públicos dos conselhos profissionais para verificar se o registro é válido e se o profissional está com o status "Ativo". Se a verificação falhar, o perfil não pode ser publicado.
- **RN03 - Horários de atendimento**: Os horários de atendimento não podem ultrapassar 8h diárias.
- **RN04 - Foto de perfil**: A foto deve ser uma imagem nítida do rosto do profissional e ter no máximo 5MB. É proibido o uso de logotipos, avatares, paisagens, personagens ou qualquer imagem que não seja do próprio profissional.

### UC05 - Gerenciar Relatórios de Comunidade

#### 1. Breve Descrição
Este caso de uso permite que um Agente Comunitário registre e visualize relatórios sobre o estado de saúde da comunidade atendida. Os relatórios incluem dados coletados em visitas domiciliares, campanhas e observações gerais, fornecendo uma visão consolidada para apoiar decisões em saúde pública.

#### 2. Atores
- Agente Comunitário
- Administrador (visualização consolidada)

#### 3. Pré-Condições
- O Agente Comunitário deve estar autenticado no sistema.

#### 4. Fluxo Básico de Eventos
1. O caso de uso inicia quando o Agente Comunitário acessa a opção "Relatórios da Comunidade".
2. O sistema apresenta as opções: "Criar Novo Relatório" e "Visualizar Relatórios Anteriores".
3. O Agente seleciona "Criar Novo Relatório".
4. O sistema apresenta um formulário com os campos:
   - Período da Coleta
   - Áreas Visitadas
   - Problemas de Saúde Recorrentes
   - Nº de Atendimentos
   - Observações Adicionais
5. O Agente preenche os campos obrigatórios. [FE01]
6. O Agente clica em "Salvar Relatório".
7. O sistema valida os dados, armazena o relatório, exibe uma visualização resumida e uma notificação de confirmação.
8. O caso de uso se encerra.

#### 5. Fluxos Alternativos
**FA01 - Visualizar relatórios anteriores**
1. No passo 2 do fluxo básico, o Agente seleciona "Visualizar Relatórios Anteriores".
2. O sistema exibe uma lista de relatórios criados pelo Agente, filtrável por data e área.
3. O Agente seleciona um relatório e o sistema exibe seu conteúdo completo.
4. O fluxo retorna ao passo 2 deste fluxo alternativo.

**FA02 - Exportar relatório**
1. No passo 3 do FA01, ao visualizar um relatório, o Agente clica em "Exportar".
2. O sistema oferece opções de exportação (PDF, CSV).
3. O Agente escolhe o formato desejado.
4. O sistema gera o arquivo e disponibiliza para download. [FE02]
5. O fluxo retorna ao passo 3 do FA01.

#### 6. Fluxos de Exceção
**FE01 - Campos obrigatórios não preenchidos**
- Se no passo 5 campos obrigatórios estiverem vazios, o sistema exibe a mensagem: "Todos os campos obrigatórios devem ser preenchidos." e permanece no formulário.

**FE02 - Falha na exportação**
- Se ocorrer um erro no passo 4 do FA02, o sistema exibe a mensagem: "Erro ao exportar o relatório. Tente novamente mais tarde." e retorna ao fluxo anterior.

#### 7. Pós-Condições
- Um novo relatório de comunidade é criado e armazenado com sucesso.
- Um relatório existente é visualizado ou exportado.

#### 8. Requisitos Especiais
- **RE01 - Acesso Offline**: Os relatórios devem estar disponíveis para visualização offline no dispositivo do agente.
- **RE02 - Exportação**: O sistema deve permitir exportação em formatos PDF e CSV.
- **RE03 - Acessibilidade Móvel**: O caso de uso deve ser otimizado para dispositivos móveis de baixa performance.

#### 9. Regras de Negócio
- **RN01 - Preenchimento obrigatório**: O sistema não permite salvar um relatório se campos essenciais estiverem vazios.
- **RN02 - Acesso restrito**: Agentes criam e visualizam seus próprios relatórios. Administradores podem visualizar relatórios consolidados de várias regiões.
- **RN03 - Armazenamento seguro**: Os relatórios devem ser armazenados seguindo normas da LGPD.
- **RN04 - Fonte de Estatística**: Os dados podem ser consolidados e anonimizados para formulação de políticas públicas.

#### 10. Pontos de Extensão
**PE01 - Preenchimento assistido**
- **Local**: No passo 4 do fluxo básico.
- **Descrição**: O sistema pode sugerir dados (ex: número de atendimentos) com base em outros registros da plataforma para o período e região selecionados.

**PE02 - Geração de indicadores visuais**
- **Local**: Após o passo 7 do fluxo básico.
- **Descrição**: Ao salvar, o sistema pode gerar automaticamente gráficos e tabelas para uma visualização rápida dos dados do relatório.

### UC06 - Gerenciar Campanhas

#### 1. Breve Descrição
Este caso de uso permite que Parceiros criem, modifiquem, visualizem e removam campanhas de saúde no sistema, visando promover ações de prevenção e conscientização para as comunidades.

#### 2. Atores
- Parceiro

#### 3. Pré-Condições
- O Parceiro deve estar autenticado no sistema com as devidas permissões para gerenciar campanhas.

#### 4. Fluxo Básico de Eventos
1. O caso de uso inicia quando o Parceiro acessa a funcionalidade "Gerenciar Campanhas".
2. O sistema exibe uma lista de campanhas existentes e as opções: "Criar Nova Campanha", "Editar", "Visualizar" e "Remover".
3. O Parceiro seleciona uma campanha existente e clica em "Visualizar Detalhes".
4. O sistema exibe todas as informações da campanha selecionada em modo de leitura.
5. O caso de uso é encerrado.

#### 5. Fluxos Alternativos
**FA01 - Criar Nova Campanha**
1. No passo 2 do fluxo básico, o Parceiro seleciona "Criar Nova Campanha".
2. O sistema apresenta um formulário solicitando:
   - Nome
   - Descrição
   - Público-alvo
   - Período
   - Objetivos
   - Recursos
   - Status (Rascunho, Ativa, Finalizada)
3. O Parceiro preenche os dados e clica em "Salvar". [FE01]
4. O sistema valida os dados [RN01] [RN02], registra a nova campanha e exibe a mensagem: "Campanha criada com sucesso!".
5. O fluxo retorna ao passo 2 do fluxo básico.

**FA02 - Editar Campanha**
1. No passo 2 do fluxo básico, o Parceiro seleciona uma campanha e clica em "Editar".
2. O sistema carrega os dados da campanha em um formulário pré-preenchido.
3. O Parceiro modifica os dados e clica em "Salvar". [FE01]
4. O sistema valida os dados [RN01] [RN02], atualiza a campanha e exibe a mensagem: "Campanha atualizada com sucesso!".
5. O fluxo retorna ao passo 2 do fluxo básico.

**FA03 - Remover Campanha**
1. No passo 2 do fluxo básico, o Parceiro seleciona uma campanha e clica em "Remover".
2. O sistema solicita confirmação com o aviso: "Atenção! Deseja remover esta campanha? Esta ação é permanente."
3. Se o Parceiro confirmar, o sistema remove a campanha [RN03] e exibe a mensagem: "Campanha removida com sucesso!".
4. O fluxo retorna ao passo 2 do fluxo básico.

#### 6. Fluxos de Exceção
**FE01 - Dados Inválidos (FA01, FA02)**
- Se os dados forem inválidos (campos obrigatórios vazios, datas incorretas), o sistema não salva, exibe mensagens de erro indicando os campos a serem corrigidos e permanece no formulário.

**FE02 - Nenhuma Campanha Cadastrada (Fluxo Básico)**
- Se não houver campanhas, o sistema informa: "Não há campanhas cadastradas." e destaca a opção "Criar Nova Campanha".

**FE03 - Falha de Processamento**
- Em qualquer ponto de interação com o banco de dados, se houver falha, o sistema exibe: "Erro ao processar a solicitação. Tente novamente mais tarde." e aborta a ação.

#### 7. Pós-Condições
- Uma nova campanha é criada com sucesso.
- Uma campanha existente é atualizada ou removida.

#### 8. Requisitos Especiais
- **RE01 - Usabilidade**: A interface deve ser intuitiva.
- **RE02 - Validação**: Todos os campos de entrada devem ser validados.
- **RE03 - Autorização**: Somente Parceiros autorizados podem acessar esta funcionalidade.
- **RE04 - Filtragem**: A lista de campanhas deve permitir filtros e ordenação.

#### 9. Regras de Negócio
- **RN01 - Nome Único**: Cada campanha deve ter um nome único.
- **RN02 - Validação de Período**: A data de início de uma campanha não pode ser posterior à data de fim.
- **RN03 - Restrição de Remoção**: Campanhas ativas ou com dados de impacto registrados não podem ser removidas, apenas arquivadas ou desativadas.

## 📜 Histórico de Versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
|**07/07/25**|0.1|Adiciona esqueleto e Caso de Uso número 5 |Sophia|
|**07/07/25**|0.2|Adicionando o Caso de Uso número 6 |Pedro|
|**07/07/25**|0.3|Adicionando o Caso de Uso número 1 |Kaio|
|**08/07/25**|0.4|Adicionando o Caso de Uso número 4 |Maria|
|**08/07/25**|0.5|Adicionando o Caso de Uso número 3 |Wanjo Christopher|
|**15/07/25**|1.0|Corrige Casos de Uso| Wanjo Christopher|
| :- | :- | :- | :- |
|**07/07/25**|0.1|Adiciona esqueleto e Caso de Uso número 5 |Sophia|
|**07/07/25**|0.2|Adicionando o Caso de Uso número 6 |Pedro|
|**07/07/25**|0.3|Adicionando o Caso de Uso número 1 |Kaio|
|**08/07/25**|0.4|Adicionando o Caso de Uso número 4 |Maria|
|**08/07/25**|0.5|Adicionando o Caso de Uso número 3 |Wanjo Christopher|
|**15/07/25**|1.0|Corrige Casos de Uso| Wanjo Christopher|

