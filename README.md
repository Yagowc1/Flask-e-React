# Projeto Flask e React
[![Status: Complete](https://img.shields.io/badge/Status-Complete-brightgreen.svg)](https://github.com/Yagowc1/Flask-e-React)
[![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=white&style=flat-square)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)](https://www.python.org/)
[![Artigo no Medium](https://img.shields.io/badge/-Artigo%20no%20Medium-12100E?logo=medium&logoColor=white&style=flat-square)](https://medium.com/) 

## Introdução

Este projeto exemplifica a integração entre um backend Flask e um frontend React, mostrando como essas tecnologias podem ser combinadas para criar uma aplicação web moderna e dinâmica.

<div style="display: flex; align-items: center; justify-content: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" alt="React" width="100" style="margin-right: 20px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask" width="150" style="margin-right: 20px;"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="100"/>
</div>

## Tabela de Conteúdo 📋

1. [Introdução 💡](#introdução)
2. [Tecnologias Utilizadas 💻](#tecnologias-utilizadas)
3. [Estrutura de Diretórios 📁](#estrutura-de-diretórios)
4. [Observação 🔍](#observação)
5. [Configuração e Banco de Dados ⚙️](#configuração-e-banco-de-dados)
6. [Execução ▶️](#execução)
7. [Funcionalidades 🚀](#funcionalidades)
8. [Contato 📧](#contato)


## Tecnologias Utilizadas 

- **Backend (Python) 🐍**:
  - **Flask**: Um framework web leve e flexível para Python, adequado para construir APIs.
  - **Flask-SQLAlchemy**: Uma extensão do Flask que fornece suporte fácil para interação com bancos de dados SQL.
  - **Flask-CORS**: Uma extensão do Flask que lida com a política de mesma origem (CORS) para permitir solicitações entre diferentes origens de domínio.

- **Frontend (React) 🌐**:
  - **Template**: O projeto React foi criado usando o template `vite` com o modelo `react`, fornecendo um ambiente de desenvolvimento rápido e moderno.

## Estrutura de Diretórios

Os arquivos estão dividos em responsabilidades principais:

    |  Diretório  |  Funcionalidade  |
    |-------------|------------------|
    | backend     | Configurar API   |
    | frontend    | Exibir dados     |

- **backend**:
  - `config.py`: Arquivo de configuração para o Flask, onde as variáveis de ambiente e outras configurações são definidas.
  - `main.py`: O arquivo principal do backend, onde a aplicação Flask é instanciada e configurada.
  - `models.py`: Contém as definições dos modelos de dados para interagir com o banco de dados.
  - `instance/mydatabase.db`: Banco de dados SQLite para armazenar os dados da aplicação.

- **frontend**:
  - `node_modules`: Pasta que contém os módulos do Node.js necessários para o projeto.
  - `public`: Contém os arquivos públicos, como ícones, imagens ou favicon.
  - `src`: O diretório fonte do projeto React, onde os componentes, estilos e outros recursos são definidos.

## Observação <a name="observação"></a>

> **Observação: Bibliotecas Python**
>
> As bibliotecas Python necessárias para executar o projeto estão listadas no arquivo `requirements.txt`. Isso facilita a instalação das dependências e garante que o ambiente de desenvolvimento seja reproduzível.

## Configuração e Banco de Dados

A configuração da aplicação Flask, incluindo a URI do banco de dados e outras configurações, é especificada no arquivo `config.py`. O banco de dados SQLite é utilizado para simplificar o desenvolvimento, permitindo que os dados sejam armazenados localmente no arquivo `mydatabase.db`.

```python
# Exemplo de configuração do Flask e SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
```

## Execução

Para iniciar o servidor Flask, basta executar o arquivo `main.py` localizado na pasta `backend`. Isso iniciará o servidor backend e estará pronto para receber solicitações.

Para iniciar o servidor React, navegue até a pasta `frontend` e execute o comando `npm run dev`. Isso iniciará um servidor de desenvolvimento para o frontend React e abrirá automaticamente o navegador padrão com a aplicação em execução.

## Funcionalidades

O projeto possui funcionalidades para criar, listar, atualizar e deletar contatos. Essas operações são realizadas através da API Flask, que interage com o banco de dados SQLite para persistência dos dados.

## Contato

Para mais informações ou para entrar em contato com o mantenedor do projeto, você pode visitar os seguintes links:

[![Yago Cortez](https://img.shields.io/badge/LinkedIn-Yago_Cortez-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/yago-cortez-9211512a7/)
[![Yagowc1](https://img.shields.io/badge/GitHub-Yagowc1-black?style=flat-square&logo=github)](https://github.com/Yagowc1)

# Autor

<div style="border-radius: 5%; overflow: hidden; width: 115px; height: 115px;">
  <img loading="lazy" src="https://avatars.githubusercontent.com/u/143226127?v=4" width="115px">
</div>
<br>
<a href="https://github.com/Yagowc1"><sub>Yago Cortez</sub></a>
