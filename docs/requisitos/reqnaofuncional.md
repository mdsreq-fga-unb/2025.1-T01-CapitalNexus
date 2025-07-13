# Requisitos de software

Os requisitos não funcionais especificam as qualidades e restrições do sistema, como desempenho, segurança e usabilidade, que não estão diretamente relacionadas às funcionalidades oferecidas, mas são essenciais para garantir a qualidade do software. Para a especificação, escolhemos utilizar o modelo URPS+ para classificar os requisitos não funcionais, que engloba categorias como Usabilidade, Confiabilidade, Desempenho e Suportabilidade.

## Lista de Requisitos Não Funcionais

| ID   | Especificação | Detalhamento |
|------|-------------------| --------------------------------------------------------------------------------------------------------------------|
|RNF01|Usabilidade|Deve ser listado história, missão, valores, principais prêmios e patrocinadores da equipe na página inicial da plataforma. |
|RNF02|Usabilidade|Deve haver uma página com a lista de todos os projetos da equipe, contendo nome, período e detalhes de cada um deles. |
|RNF03|Usabilidade|A plataforma deve ser responsiva para desktop padrão (1440x1024) e android compacto (412x917). |
|RNF04|Usabilidade|O sistema, quando ocorrer um erro, deve exibir uma mensagem em linguagem simples explicando a causa do erro e com uma instrução do que o usuário deve fazer a seguir. Por exemplo, se a página não puder ser carregada no momento, ele deve imprimir a mensagem “Estamos com problema para carregar a página no momento, por favor, tente novamente mais tarde!”.|
|RNF05|Suportabilidade|O sistema deve ter todas as suas funcionalidades documentadas utilizando docstring da biblioteca pydoc, preenchendo descrição da funcionalidade, parâmetros e retorno, para gerar a documentação do sistema em HTML e facilitar a manutenibilidade.|
|RNF06|Restrição de design|Restrição de design: A área pública deve seguir a identidade visual da Capital Rocket Team, utilizando o logotipo da equipe na barra de navegação e a paleta de cores no design. O logotipo e a paleta estão disponíveis em: [Identidade Visual CRT](https://unbbr.sharepoint.com/:b:/s/Requisitos592-Desenvolvedores/Ef8Dt9_B_kRHtq5AZ5KKEU4Bmu0yK7gabL0uf1F2MqgU_w?e=UdYyem)|

## Histórico de Versão 
|**Data**|**Versão** |**Descrição** |**Autor**|
| :- | :- | :- | :- |
|**05/05/25**|0.1|Levantamento inicial de requisitos|Equipe|
|**25/05/25**|0.2|Correção de requisitos não funcionais|Sophia|
|**04/06/25**|0.3|Detalhamento dos requisitosa não funcionais|Sophia|