O componente `ContactList` é responsável por exibir a lista de contatos e fornecer opções para atualizar ou deletar cada contato.

### Importação

```javascript
import React from "react";
```

- **React**: Biblioteca principal do React para criar componentes e utilizar JSX.

### Definição do Componente `ContactList`

```javascript
const ContactList = ({ contacts, updateContact, updateCallback }) => {
```

- **`contacts`**: Prop que contém a lista de contatos a ser exibida.
- **`updateContact`**: Função de callback para atualizar um contato existente.
- **`updateCallback`**: Função de callback a ser chamada após a exclusão de um contato, para atualizar a lista de contatos.

### Função `onDelete`

```javascript
const onDelete = async (id) => {
    try {
        const options = {
            method: "DELETE"
        };
        const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, options);
        if (response.status === 200) {
            updateCallback();
        } else {
            console.error("Failed to delete");
        }
    } catch (error) {
        alert(error);
    }
};
```

- **`onDelete`**: Função assíncrona que faz uma requisição para deletar um contato.
  - **`options`**: Configurações da requisição HTTP, usando o método DELETE.
  - **`fetch`**: Envia a requisição para deletar o contato com o ID especificado.
  - **Verificação do status da resposta**: Se a resposta for bem-sucedida (status 200), chama `updateCallback` para atualizar a lista de contatos. Caso contrário, loga um erro no console.
  - **Tratamento de erros**: Exibe um alerta se ocorrer um erro durante a requisição.

### Renderização da Lista de Contatos

```javascript
return <div>
    <h2>Contacts</h2>
    <table>
        <thead>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {contacts.map((contact) => (
                <tr key={contact.id}>
                    <td>{contact.firstName}</td>
                    <td>{contact.lastName}</td>
                    <td>{contact.email}</td>
                    <td>
                        <button onClick={() => updateContact(contact)}>Update</button>
                        <button onClick={() => onDelete(contact.id)}>Delete</button>
                    </td>
                </tr>
            ))}
        </tbody>
    </table>
</div>
```

- **Estrutura HTML**:
  - **`<h2>Contacts</h2>`**: Título da seção de contatos.
  - **`<table>`**: Tabela que exibe a lista de contatos.
    - **`<thead>`**: Cabeçalho da tabela com os títulos das colunas.
    - **`<tbody>`**: Corpo da tabela, onde os contatos são listados.
      - **`contacts.map((contact) => (...)`**: Itera sobre a lista de contatos e cria uma linha (`<tr>`) para cada contato.
        - **`<td>`**: Colunas que exibem o primeiro nome, último nome e email do contato.
        - **Botões de ação**:
          - **`<button onClick={() => updateContact(contact)}>Update</button>`**: Botão para atualizar o contato, chamando a função `updateContact`.
          - **`<button onClick={() => onDelete(contact.id)}>Delete</button>`**: Botão para deletar o contato, chamando a função `onDelete`.

### Exportação

```javascript
export default ContactList;
```

- Exporta o componente `ContactList` para que ele possa ser utilizado em outras partes da aplicação.

### Resumo

O componente `ContactList`:

- Recebe uma lista de contatos e funções de callback para atualizar ou deletar contatos.
- Renderiza uma tabela com os dados dos contatos.
- Fornece botões para atualizar e deletar cada contato.
- Faz uma requisição DELETE para remover um contato e atualiza a lista de contatos ao receber uma resposta bem-sucedida.

Este componente trabalha em conjunto com os outros componentes (`App` e `ContactForm`) para gerenciar a exibição e manipulação da lista de contatos na aplicação.