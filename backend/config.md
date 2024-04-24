# Configuração da Aplicação e Banco de Dados
![Flask](https://img.shields.io/badge/Flask-API-blue.svg) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-green.svg) ![SQLite](https://img.shields.io/badge/SQLite-Banco%20de%20Dados-blue.svg) ![Configuração](https://img.shields.io/badge/Configura%C3%A7%C3%A3o-yellow.svg)

### Visão Geral

Este arquivo contém a configuração da aplicação Flask e do banco de dados SQLAlchemy. 🛠️

### Objetivos

- Importar as bibliotecas necessárias do Flask.
- Instanciar um objeto Flask para representar a aplicação web.
- Habilitar o CORS para lidar com solicitações de diferentes origens.
- Configurar a URI do banco de dados SQLAlchemy para conectar-se a um banco de dados SQLite.
- Desativar o rastreamento de modificações para melhorar o desempenho.
- Instanciar um objeto SQLAlchemy para interagir com o banco de dados.

### Importando as Bibliotecas Necessárias do Flask

Para começar, importamos as bibliotecas necessárias do Flask:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
```

- **Flask**: É o framework web que usamos para construir nossa aplicação. 🌐
- **SQLAlchemy**: É uma biblioteca que facilita a interação com bancos de dados relacionais em Python. 🗃️
- **CORS**: É uma extensão Flask que lida com a política de mesma origem (CORS), permitindo solicitações de diferentes origens. 🔄

### Instanciando um Objeto Flask

Em seguida, criamos uma instância da classe `Flask`:

```python
app = Flask(__name__)
```

Essa instância representa a nossa aplicação web Flask. O argumento `__name__` é usado para determinar a localização dos arquivos estáticos, entre outras coisas.

### Habilitando o CORS

Para lidar com solicitações de diferentes origens, habilitamos o CORS:

```python
CORS(app)
```

Isso permite que nossa aplicação receba solicitações de diferentes domínios.

### Configuração da URI do Banco de Dados SQLAlchemy

Definimos a URI do banco de dados SQLAlchemy para apontar para um banco de dados SQLite:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
```

Neste caso, estamos usando um banco de dados SQLite chamado `mydatabase.db`. A URI especifica o tipo de banco de dados (SQLite), o caminho para o arquivo do banco de dados e seu nome.

### Desativando o Rastreamento de Modificações

Por questões de desempenho, desativamos o rastreamento de modificações no SQLAlchemy:

```python
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
```

Isso evita que o SQLAlchemy rastreie modificações desnecessárias no estado dos objetos e melhora o desempenho geral da aplicação.

### Instanciando um Objeto SQLAlchemy

Finalmente, instanciamos um objeto `SQLAlchemy` para interagir com o banco de dados:

```python
db = SQLAlchemy(app)
```

Este objeto representa a camada de abstração de banco de dados da nossa aplicação, permitindo-nos manipular os dados de forma orientada a objetos.

Essas configurações são essenciais para garantir que a aplicação Flask funcione corretamente e possa se comunicar com o banco de dados SQLite.