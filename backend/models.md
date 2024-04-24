# Models
![Flask](https://img.shields.io/badge/Flask-API-blue.svg) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-green.svg) ![SQLite](https://img.shields.io/badge/SQLite-Banco%20de%20Dados-blue.svg) ![Modelos](https://img.shields.io/badge/Modelos-Estrutura-orange.svg)

### Visão Geral
O arquivo `models.py` contém as definições dos modelos de dados utilizados na aplicação.

### Objetivos
- Importar o Objeto de Banco de Dados
- Definir o Modelo de Contato
- Implementar o Método `to_json()`

### Importando o Objeto de Banco de Dados

Para começar, importamos o objeto de banco de dados `db` da configuração:

```python
from config import db
```

Esse objeto é necessário para definir os modelos de dados e interagir com o banco de dados.

### Definindo o Modelo de Contato

A classe `Contact` é definida como um modelo de dados e herda da classe `db.Model`, que é fornecida pelo SQLAlchemy:

```python
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

Este modelo possui as seguintes colunas:
- `id`: Um identificador único para cada contato (chave primária).
- `first_name`: O primeiro nome do contato.
- `last_name`: O sobrenome do contato.
- `email`: O endereço de e-mail do contato.

### Método `to_json()`

Retorna uma representação JSON do objeto `Contact`:

```python
def to_json(self):
    return {
        "id": self.id,
        "firstName": self.first_name,
        "lastName": self.last_name,
        "email": self.email
    }
```

Este método é útil para serializar objetos `Contact` em formato JSON, facilitando o envio de dados pela API.

Essas definições de modelo são essenciais para representar os dados da aplicação de forma estruturada e manipulá-los conforme necessário.