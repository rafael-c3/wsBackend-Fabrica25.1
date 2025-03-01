Projeto de Cadastro de Filmes e Usuários
Este projeto permite o cadastro de usuários e filmes associados. Os usuários podem adicionar filmes à sua lista, e o sistema registra os filmes relacionados a cada usuário. A aplicação foi construída utilizando o Django.

Funcionalidades
Cadastro de usuários com nome, sobrenome, email, data de nascimento e senha.
Cadastro de filmes com título e ano.
Relacionamento entre usuários e filmes (cada filme é associado a um usuário).
Interface de administração do Django para gerenciar usuários e filmes.
Tecnologias Utilizadas
Python 3.x
Django 3.x
Banco de dados SQLite (padrão do Django)
Instalação
Clonar o repositório:

bash
Copiar
Editar
git clone https://github.com/seu_usuario/seu_projeto.git
Instalar dependências: Primeiro, crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
Em seguida, instale as dependências do projeto:

bash
Copiar
Editar
pip install -r requirements.txt
Configuração do Banco de Dados: O Django utiliza SQLite por padrão, então não é necessário configurar um banco de dados separado. Porém, se você estiver utilizando outro banco de dados, ajuste a configuração no arquivo settings.py.

Criar as migrações e aplicar ao banco de dados:

Para garantir que as tabelas e campos necessários sejam criados no banco de dados, execute os seguintes comandos:

bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
Criar superusuário para acessar o painel administrativo (opcional):

Caso queira acessar o painel de administração do Django para gerenciar usuários e filmes, crie um superusuário:

bash
Copiar
Editar
python manage.py createsuperuser
Siga as instruções para criar o superusuário.

Rodando o Servidor de Desenvolvimento
Para rodar o servidor de desenvolvimento e acessar a aplicação no navegador, use o seguinte comando:

bash
Copiar
Editar
python manage.py runserver
Isso iniciará o servidor na URL http://127.0.0.1:8000/. Você poderá acessar a aplicação diretamente no navegador.

Acessando o Painel de Administração
Se você criou um superusuário, poderá acessar o painel de administração do Django em:

arduino
Copiar
Editar
http://127.0.0.1:8000/admin/
Faça login com as credenciais do superusuário para gerenciar usuários e filmes.

Endpoints
Cadastro de Usuário:

URL: /cadastro/
Método: POST
Formulário: Cadastro de nome, sobrenome, email, nascimento e senha do usuário.
Adicionar Filme:

URL: /filmes/<usuario_id>/
Método: POST
Formulário: Adiciona filmes com título e ano para um usuário específico.
Contribuindo
Fork este repositório.
Crie uma nova branch (git checkout -b feature/nova-feature).
Faça suas modificações e commit (git commit -am 'Adicionando nova feature').
Push para a branch (git push origin feature/nova-feature).
Abra um Pull Request.
