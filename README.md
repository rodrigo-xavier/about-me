# about-me

Passo a passo para executar o projeto no seu computador:

Primeiro instale o pyenv, para obter um ambiente python limpo.

O código a seguir executa o instalador automático do pyenv.

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

Em seguida, instale o python versão 3.8.2 utilizando o pacote pyenv, da seguinte forma:

    pyenv install 3.8.2
    pyenv shell 3.8.2

Faça um clone do meu repositório:

    git clone https://github.com/rodrigo-xavier/about-me.git

Agora faça um upgrade do pip e instale os requisitos:

    pip install --upgrade pip
    pip install -r requirements.txt

E então crie um arquivo chamado .env no diretório principal, com os seguintes dados:

    DEBUG=True
    SECRET_KEY=
    ALLOWED_HOSTS=['localhost', '127.0.0.1', '192.168.0.*']
    INTERNAL_IPS=['localhost', '127.0.0.1', '192.168.0.*']
    ENGINE = 'django.db.backends.sqlite3'
    ADMINS=[('Nome', 'email@email.com')]
    MANAGERS=[('Nome', 'email@email.com')]
    
Entre no seguinte site para gerar sua própria SECRET_KEY e insira-a no .env, no campo designado:

*https://djecrety.ir/

Agora, antes de rodar o projeto, é necessário criar um 
