# Instruções para Configuração do Ambiente de Desenvolvimento

Este documento descreve os passos para configurar o ambiente de desenvolvimento e começar a trabalhar no projeto. 

### Certifique-se de ter o arquivo .env com as credenciais do banco.

## 1. Sincronizar repositório
Primeiramente, sempre, execute:
```
git pull
```

# Comandos Docker para Projeto Django

Este arquivo reúne os principais comandos Docker para criar, rodar, testar e gerenciar seu projeto Django dentro de containers.

---

## 2. Construir a imagem Docker

```bash
docker compose build
``` 

## 3. Iniciar o container

```bash
docker compose up
``` 

## 3. Entrar no container (modo interativo)

```bash
docker start capital-nexus
docker exec -it capital-nexus /bin/bash
```
## 4. Migrações

python manage.py makemigrations
python manage.py migrate

## 5. Aplicar migrações

docker exec -it capital-nexus python manage.py migrate

## 6. Teste

docker exec -it capital-nexus python manage.py test
