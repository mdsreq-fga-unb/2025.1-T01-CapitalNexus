# Instruções para Configuração do Ambiente de Desenvolvimento

Este documento descreve os passos para configurar o ambiente de desenvolvimento e começar a trabalhar no projeto. 
Primeiro, certifique-se de ter o python instalado na sua máquina. Após isso, acesse essa branch (develop) e siga os seguintes passos:

### Certifique-se de ter o arquivo .env com as credenciais do banco.

## 1. Sincronizar repositório
Primeiramente, sempre, execute:
```
git pull
```

## 2. Criar ambiente virtual (Apenas se você nunca tiver feito!)
Se for a sua primeira vez acessando, execute o seguinte comando no terminal:
```
python -m venv venv
```

## 3. Ativar o ambiente virtual
No terminal, execute:

Windows:
```
venv\Scripts\activate
```
Linux/MacOS:
```
source venv/bin/activate
```

## 3. Instale as dependências
Execute:
```
pip install -r requirements.txt
```

## 5. Rodar as migrações do banco de dados
Execute:
```
python manage.py migrate
```

## 6. Verifique se está funcionando corretamente
Execute:
```
python manage.py runserver
```