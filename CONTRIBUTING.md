# 🛠️ Guia de Contribuição

Para manter a organização e a qualidade do código, siga estas diretrizes.

---

## ✅ Commits

Utilizamos o padrão [Conventional Commits](https://www.conventionalcommits.org/).  
Formato:
```
<tipo>(escopo): descrição breve
```

### Tipos válidos:

- `feat`: nova funcionalidade
- `fix`: correção de bugs
- `docs`: documentação
- `style`: formatação e estilo (sem alteração de código)
- `refactor`: refatoração sem mudança de comportamento
- `perf`: melhoria de performance
- `test`: testes adicionados ou atualizados
- `build`: mudanças que afetam o processo de build ou dependências
- `ci`: configuração de integração contínua
- `chore`: tarefas administrativas ou manutenção
- `revert`: desfaz alterações anteriores

### Exemplo:
```
feat(auth): implementa login com autenticação JWT
```

---

## 🌱 Nome de branch

Use o padrão:
```
<tipo>/<descricao-curta>
```

### Exemplos:
- `feat/cadastro-usuario`
- `fix/erro-listagem-produtos`
- `docs/adiciona-readme`
- `refactor/reorganiza-componentes`

---

## 🚀 Pull Request

Antes de abrir um PR, verifique:

- [ ] A branch está atualizada com a `main` ou `develop`
- [ ] Os commits seguem o padrão
- [ ] O código foi testado localmente
- [ ] A documentação (se aplicável) foi atualizada
- [ ] Nenhum arquivo sensível ou desnecessário foi incluído

### 📝 Título do PR

Mesmo padrão do commit:
```
<tipo>(escopo): descrição breve
```

**Exemplo:**
```
feat(auth): implementa login com autenticação JWT
```

### 💬 Corpo do PR

Inclua:
- O que foi feito
- Por que foi feito
- Como testar
- Pendências (se houver)
- Screenshot ou vídeo (se aplicável)

---

## 🔁 Exemplo completo

- Nome da branch:
  ```
  feat/pagina-login
  ```

- Commits:
  ```
  feat(login): cria layout da página de login
  feat(login): integra login com backend usando JWT
  ```

- Título do Pull Request:
  ```
  feat(login): implementa login funcional com autenticação JWT
  ```

- Corpo do Pull Request:
  ```markdown
  ## O que foi feito
  - Página de login com campos de email e senha
  - Integração com backend usando JWT
  - Armazenamento do token no localStorage

  ## Por que
  Esta funcionalidade é necessária para autenticar usuários e proteger rotas privadas.

  ## Como testar
  - Rodar o backend local
  - Acessar `/login` no frontend
  - Inserir credenciais válidas
  - Verificar se o token é salvo e se redireciona para `/dashboard`

  ## Pendências
  - Testes automatizados ainda não implementados
  ```

---

## 💬 Dúvidas?

Abra uma *issue* ou entre em contato com um dos mantenedores do projeto.

---
