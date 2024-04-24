# Arquivo `main.py`
![Flask](https://img.shields.io/badge/Flask-API-blue.svg) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-green.svg) ![SQLite](https://img.shields.io/badge/SQLite-Banco%20de%20Dados-blue.svg) ![Rotas](https://img.shields.io/badge/Rotas-Manipula%C3%A7%C3%A3o-orange.svg)

### Visão Geral

Este arquivo contém as rotas e funções que manipulam os dados da aplicação.

### Objetivos

- Definir rotas para manipular contatos.
- Implementar operações CRUD (Create, Read, Update, Delete) para os contatos.

### Funções

1. [Obtendo Contatos](#obtendo-contatos) 📇
2. [Criando um Novo Contato](#criando-um-novo-contato) ✏️
3. [Atualizando um Contato Existente](#atualizando-um-contato-existente) 🔄
4. [Excluindo um Contato](#excluindo-um-contato) 🗑️

### Importando as Bibliotecas Necessárias do Flask

Para começar, importamos as bibliotecas necessárias do Flask e outras dependências:

```python
from flask import request, jsonify
from config import app, db
from models import Contact
```

### Definindo Rotas e Funções

#### Obtendo Contatos

A rota `/contacts` permite obter todos os contatos armazenados. Ela retorna uma lista de todos os contatos em formato JSON:

```python
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})
```
Esta rota está definida para aceitar solicitações GET na URL `/contacts`. Quando essa rota é acessada, a função `get_contacts()` é executada.

Dentro da função `get_contacts()`, realizamos as seguintes operações:

1. **Definição da Rota e Método**: A rota está definida para aceitar solicitações GET na URL `/contacts`. Isso é especificado usando o decorador `@app.route("/contacts", methods=["GET"])`, que associa a função `get_contacts()` a essa rota quando ela é acessada via método GET.

2. **Consulta ao Banco de Dados**: Dentro da função `get_contacts()`, utilizamos o SQLAlchemy para consultar todos os registros da tabela de contatos (`Contact`). Isso é feito com a linha `contacts = Contact.query.all()`, onde `Contact.query` representa uma consulta à tabela de contatos e `all()` retorna todos os registros.

3. **Serialização para JSON**: Em seguida, mapeamos cada objeto `Contact` retornado pela consulta para seu equivalente JSON. Isso é feito usando a função `map()` em combinação com a função `to_json()` definida no modelo `Contact`. A função `to_json()` converte um objeto `Contact` em um dicionário JSON. O resultado é uma lista de dicionários JSON, onde cada dicionário representa um contato.

   ```python
   json_contacts = list(map(lambda x: x.to_json(), contacts))
   ```

4. **Retorno da Resposta**: Por fim, retornamos os contatos em formato JSON como resposta da solicitação. Usamos a função `jsonify()` para serializar a lista de contatos JSON e retorná-la como uma resposta HTTP. O objeto JSON retornado contém uma chave `"contacts"` cujo valor é a lista de contatos JSON que acabamos de criar.

   ```python
   return jsonify({"contacts": json_contacts})
   ```

Esses passos garantem que, ao acessar a rota `/contacts`, todos os contatos armazenados no banco de dados sejam recuperados e retornados ao cliente em formato JSON, facilitando a integração com a aplicação cliente.

#### Criando um Novo Contato

A rota `/create_contact` permite criar um novo contato. Os dados do novo contato devem ser fornecidos no corpo da solicitação HTTP no formato JSON. Esta rota valida os dados fornecidos e, se estiverem corretos, cria um novo objeto de contato e o adiciona ao banco de dados:

```python
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    # Validar dados
    if not first_name or not last_name or not email:
        return (jsonify({"message":"You must include a first name, last name and email"}), 400)

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201
```

Esta rota está definida para aceitar solicitações POST na URL `/create_contact`. Quando essa rota é acessada, a função `create_contact()` é executada.

Dentro da função `create_contact()`, realizamos as seguintes operações:

1. **Extraindo os dados do novo contato**: Aqui, estamos utilizando o método `.get()` para acessar os valores dos campos `firstName`, `lastName` e `email` do corpo JSON da solicitação HTTP. Esses valores são extraídos do corpo da solicitação e atribuídos às variáveis `first_name`, `last_name` e `email`.

   ```python
   first_name = request.json.get("firstName")
   last_name = request.json.get("lastName")
   email = request.json.get("email")
   ```

2. **Validação dos dados**: Verificamos se todos os campos necessários foram fornecidos. Se algum campo estiver ausente, retornamos uma resposta de erro com status 400 (Bad Request) e uma mensagem explicando o erro.

   ```python
   if not first_name or not last_name or not email:
       return (jsonify({"message":"You must include a first name, last name and email"}), 400)
   ```

3. **Criação de um novo objeto de contato**: Se os dados estiverem corretos, criamos um novo objeto `Contact` com os dados fornecidos.

   ```python
   new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
   ```

4. **Adição do novo contato ao banco de dados**: Adicionamos o novo objeto `Contact` à sessão do banco de dados e confirmamos a transação com `db.session.commit()`. Se ocorrer algum erro durante a operação de criação, capturamos a exceção e retornamos uma mensagem de erro com status 400.

   ```python
   try:
       db.session.add(new_contact)
       db.session.commit()
   except Exception as e:
       return jsonify({"message": str(e)}), 400
   ```

5. **Retorno de uma resposta de sucesso**: Se o novo contato for criado com sucesso, retornamos uma mensagem de sucesso com status 201 (Created).

   ```python
   return jsonify({"message": "User created!"}), 201
   ```

Esses passos são essenciais para criar um novo contato por meio da rota `/create_contact` e garantir que os dados fornecidos sejam válidos e armazenados corretamente no banco de dados.

#### Atualizando um Contato Existente

A rota `/update_contact/<int:user_id>` permite atualizar um contato existente. Os dados a serem atualizados devem ser fornecidos no corpo da solicitação HTTP no formato JSON. Esta rota procura pelo contato com o ID especificado, atualiza seus campos conforme necessário e salva as alterações no banco de dados:

```python
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "user not found"}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200
```

1. **Rota para atualização de um contato existente**: A rota `/update_contact/<int:user_id>` é responsável por permitir a atualização de um contato já existente no banco de dados. O `<int:user_id>` na rota indica que esperamos um parâmetro de ID de usuário na URL para identificar qual contato será atualizado.

2. **Obtenção do contato a ser atualizado**: Primeiro, buscamos o contato no banco de dados com o ID especificado na URL. Se o contato não for encontrado, retornamos uma mensagem de erro indicando que o usuário não foi encontrado, com um status 404 (Not Found).

   ```python
   contact = Contact.query.get(user_id)

   if not contact:
       return jsonify({"message": "user not found"}), 404
   ```

3. **Atualização dos campos do contato**: Se o contato for encontrado, extraímos os dados do corpo da solicitação HTTP no formato JSON e atualizamos os campos do contato conforme necessário. Para isso, utilizamos o método `.get()` para acessar os valores dos campos `firstName`, `lastName` e `email` do corpo JSON da solicitação. Se algum desses campos não estiver presente no corpo da solicitação, mantemos os valores existentes no banco de dados.

   ```python
   data = request.json
   contact.first_name = data.get("firstName", contact.first_name)
   contact.last_name = data.get("lastName", contact.last_name)
   contact.email = data.get("email", contact.email)
   ```

4. **Salvar as alterações no banco de dados**: Após atualizarmos os campos do contato, utilizamos `db.session.commit()` para salvar as alterações no banco de dados.

   ```python
   db.session.commit()
   ```

5. **Retorno de uma resposta de sucesso**: Finalmente, retornamos uma mensagem de sucesso indicando que o usuário foi atualizado com sucesso, com um status 200 (OK).

   ```python
   return jsonify({"message": "User updated."}), 200
   ```

Essa rota permite atualizar os dados de um contato existente, garantindo que as informações no banco de dados estejam sempre atualizadas e consistentes.

#### Excluindo um Contato

A rota `/delete_contact/<int:user_id>` permite excluir um contato. Esta rota procura pelo contato com o ID especificado e o exclui do banco de dados:

```python
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "user not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200    
```

1. **Rota para exclusão de um contato**: A rota `/delete_contact/<int:user_id>` é responsável por permitir a exclusão de um contato do banco de dados. O `<int:user_id>` na rota indica que esperamos um parâmetro de ID de usuário na URL para identificar qual contato será excluído.

2. **Obtenção do contato a ser excluído**: Primeiro, buscamos o contato no banco de dados com o ID especificado na URL. Se o contato não for encontrado, retornamos uma mensagem de erro indicando que o usuário não foi encontrado, com um status 404 (Not Found).

   ```python
   contact = Contact.query.get(user_id)

   if not contact:
       return jsonify({"message": "user not found"}), 404
   ```

3. **Exclusão do contato do banco de dados**: Se o contato for encontrado, utilizamos `db.session.delete(contact)` para remover o objeto de contato da sessão do banco de dados.

   ```python
   db.session.delete(contact)
   ```

4. **Salvar as alterações no banco de dados**: Após excluir o contato da sessão do banco de dados, utilizamos `db.session.commit()` para salvar as alterações e efetivar a exclusão.

   ```python
   db.session.commit()
   ```

5. **Retorno de uma resposta de sucesso**: Finalmente, retornamos uma mensagem de sucesso indicando que o usuário foi excluído com sucesso, com um status 200 (OK).

   ```python
   return jsonify({"message": "User deleted!"}), 200
   ```

Essa rota permite excluir um contato específico do banco de dados, mantendo a consistência e integridade dos dados armazenados na aplicação.

### Executando a Aplicação

Finalmente, executamos a aplicação Flask:

```python
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

Este trecho verifica se o arquivo `main.py` está sendo executado diretamente como um script Python (ou seja, não está sendo importado por outro arquivo). Isso é feito usando a condição `if __name__ == "__main__":`.

Dentro desta condição, há duas etapas principais:

1. `with app.app_context():`: Este bloco cria um contexto de aplicação Flask. O contexto de aplicação é necessário para executar certas operações relacionadas ao aplicativo, como criar tabelas no banco de dados usando o SQLAlchemy. O uso do gerenciador de contexto `with` garante que o contexto seja criado e destruído corretamente.

2. `db.create_all()`: Dentro do contexto de aplicação, esta linha de código cria todas as tabelas no banco de dados que foram definidas pelos modelos SQLAlchemy. Isso é feito chamando o método `create_all()` do objeto `db`, que representa a instância do SQLAlchemy configurada para a aplicação Flask.

3. `app.run(debug=True)`: Por fim, esta linha inicia o servidor de desenvolvimento embutido do Flask. Quando o aplicativo é executado desta forma, o Flask inicia um servidor web local que pode ser acessado através do navegador. O argumento `debug=True` habilita o modo de depuração, o que significa que o servidor recarrega automaticamente sempre que o código fonte é alterado e exibe mensagens de erro detalhadas no navegador em caso de exceções.

Este arquivo é essencial pois configura e inicia a execução da aplicação Flask, incluindo a criação das tabelas no banco de dados e a execução do servidor web local para servir a aplicação.