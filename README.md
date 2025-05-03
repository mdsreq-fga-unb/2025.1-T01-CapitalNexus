# Instruções para Configuração do Ambiente de Desenvolvimento

Este documento descreve os passos para configurar o ambiente de desenvolvimento e começar a trabalhar no projeto. 
Primeiro, certifique-se de ter o python instalado na sua máquina. Após isso, acesse essa branch e siga os seguintes passos:

## 1. Criar ambiente virtual 
Se for a sua primeira vez acessando, execute o seguinte comando no terminal:
```
python -m venv venv
```

## 2. Ativar o ambiente virtual
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