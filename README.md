<h1 align="center"> Delivery Application Challenge </h1>


# Índice 


* [📚 Informações do documento](#📚-Informações-do-documento)

* [📁 Case](#📁-Case)
* [🎯 Coding Part](#🎯-Coding-part)
* [🛠️ Abrir e rodar o projeto](#🛠️-Abrir-e-rodar-o-projeto)
* [✔️ Técnicas e tecnologias utilizadas](#✔️-Técnicas-e-tecnologias-utilizadas)


# 📚 Informações do documento

Este documento é composto por três seções:

- **Documento**:
    - `README.md`
        - Nele contém todas as explicações necessárias sobre o programa. 
        
- **Questões**:
    - `Questions.pdf`
        - Nele contém as respostas das seis questões apresentadas no Caso do desafio.
        - [Questions](\Questions.pdf)

- **Code**:
    - `Core, query_distance, venv and all`:
        - Nela contém todos os códigos para a execução do programa 
            - [Código aplicação](\core)
            - [Código projeto](\query_distance)
            - [Dockerfile](\Dockerfile) (Arquivo usado para construir o contêiner Docker)
            - [Requirements](\requirements.txt) (Arquivo usado para especificar as dependências de um projeto Python)

# 📁 Case

Para acessar os questões do caso basta abrir o documento [Questions.pdf](\Questions.pdf).

# 🎯 Coding Part

Os próximos tópicos são referentes a aplicação implementada.

# 🔨 Funcionalidade do projeto

- `Funcionalidade`: O programa deve ter uma interface simples onde dois enderços podem ser inseridos: source e destination. Ao enviar os dados, o aplicativo deve exibir uma mensagem com distância em quilômetros entre esses dois endereços. Se não conseguir calcular por algum motivo, ele deve exibir uma mensagem de erro. O aplicativo deve armazenar todas as consultas históricas. 

# 📁 Acesso ao projeto

Existem duas maneiras de você acessar o projeto:

1. Executar o arquivo `manage.py` via **Editor de Código** 
2. Executar o arquivo `manage.py` via **Builds Conteinerizados** 
3. URL `manage.py` via **Heruko** 



# 🛠️ Abrir e rodar o projeto

**IMPORTANTE** : Antes de rodar o projeto verifique se possui o Python instalado em sua máquina, caso não possua faça o [Download](https://www.python.org/ "Download Python") e realiza a instalação.
    

1. Via **Editor de Código** 

    Na implementação foi utilizado o [Pycharm](https://www.jetbrains.com/pt-br/pycharm/ "Pycharm"), mas você pode utilizar outros Editores de Código que são capazes de rodar arquivos Python, como [Notepad++](https://notepad-plus-plus.org/downloads/ "Notepad++"), [Visual Studio](https://visualstudio.microsoft.com   "Visual Studio"), dentro outros... 

    - Faça o download do **Editor de Código** desejado para executar o programa python.
    - Abra a pasta em que está o arquivo manager.py
    - Execute o comando:
    ```bash
        python manage.py runserver
    ```
    - Pronto! O programa irá rodar na porta padrão, basta acessar 
        - http://127.0.0.1:8000/ para realizar o cálculo da distância
        - http://127.0.0.1:8000/historical para verificar o histórico de consultas

2. Via **Builds Conteinerizados** 
    
    Na implementação foi utilizado o [Docker](https://www.docker.com/ "Docker"), para rodar a aplicação via Docker container realize os seguintes passos:
    
    - Faça o [Download](https://www.docker.com/ "Download Docker") e instale a plataforma em seu computador.
    - Restart Docker Desktop
    - Abra o **Prompt de Comando** .
    - Navegue até o diretório em que você salvou o projeto manage.py
    - Execute o comando "docker build" para criar a imagem:
    ```bash
        docker build -t img-querydistance-docker .
    ```
    - Em seguida execute o container com a opção "8000:8000" acessar o localhost:8000 :
    ```bash
        docker run -p 8000:8000 img-querydistance-docker
    ```
    - Pronto! O programa irá rodar na porta padrão, basta acessar 
        - http://127.0.0.1:8000/ para realizar o cálculo da distância
        - http://127.0.0.1:8000/historical para verificar o histórico de consultas


2. Via **Heruko**
    
    Ao tentar hospedar a aplicação em um servidor gratuito com o Heruko, obtive o seguindo erro:

    remote:  ! This article goes into details on the behavior:
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/querydistance.git'
    
    Tentei encontrar soluções que para a aplicação, porém até o momento não consegui hospedar no servidor.

# ✔️ Técnicas e tecnologias utilizadas

- ``Python``
- ``Docker``
- ``Markdown``
- ``Html``
- ``django``
- ``bootstrap``
- ``API Nominatim``
- ``geopy``




