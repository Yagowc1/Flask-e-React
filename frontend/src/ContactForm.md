O componente `ContactForm` é responsável por gerenciar o formulário de criação e edição de contatos.

### Importações

```javascript
import { useState } from "react";
```

- **`useState`**: Hook do React utilizado para gerenciar o estado do componente.

### Definição do Componente `ContactForm`

```javascript
const ContactForm = ({ existingContact = {}, updateCallback }) => {
```

- **`existingContact`**: Prop que pode conter um objeto de contato existente para edição. Se não for fornecido, será um objeto vazio por padrão.
- **`updateCallback`**: Função de callback a ser chamada após a criação ou atualização de um contato.

### Estados

```javascript
const [firstName, setFirstName] = useState(existingContact.firstName || "");
const [lastName, setLastName] = useState(existingContact.lastName || "");
const [email, setEmail] = useState(existingContact.email || "");
```

- **`firstName`, `lastName`, `email`**: Estados para armazenar os valores dos campos de entrada do formulário. Se `existingContact` contiver valores, eles serão usados como valores iniciais; caso contrário, os campos serão inicialmente vazios.

### Determinação do Modo (Criação ou Atualização)

```javascript
const updating = Object.entries(existingContact).length !== 0;
```

- **`updating`**: Variável booleana que determina se o formulário está em modo de atualização (verdadeiro) ou criação (falso). Se `existingContact` não estiver vazio, significa que estamos editando um contato existente.

### Manipulador de Submissão do Formulário

```javascript
const onSubmit = async (e) => {
    e.preventDefault();

    const data = {
        firstName,
        lastName,
        email
    };

    const url = `http://127.0.0.1:5000/${updating ? `update_contact/${existingContact.id}` : "create_contact"}`;

    const options = {
        method: updating ? "PATCH" : "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    };

    const response = await fetch(url, options);
    if (response.status !== 201 && response.status !== 200) {
        const data = await response.json();
        alert(data.message);
    } else {
        updateCallback();
    }
};
```

- **`e.preventDefault()`**: Evita o comportamento padrão de recarregar a página ao submeter o formulário.
- **`data`**: Objeto que contém os dados do formulário.
- **`url`**: URL da API. Se `updating` for verdadeiro, usa a rota de atualização com o ID do contato; caso contrário, usa a rota de criação.
- **`options`**: Configurações da requisição HTTP, incluindo o método (PATCH para atualização, POST para criação), cabeçalhos e corpo da requisição.
- **`fetch(url, options)`**: Faz a requisição HTTP. Se a resposta não for um sucesso (status 200 ou 201), mostra uma mensagem de erro; caso contrário, chama `updateCallback()` para atualizar a lista de contatos na aplicação principal.

### Renderização do Formulário

```javascript
return <form onSubmit={onSubmit}>
    <div>
        <label htmlFor="firstName">First Name:</label>
        <input type="text" id="firstName" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
    </div>

    <div>
        <label htmlFor="lastName">Last Name:</label>
        <input type="text" id="lastName" value={lastName} onChange={(e) => setLastName(e.target.value)} />
    </div>

    <div>
        <label htmlFor="email">Email:</label>
        <input type="text" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
    </div>

    <button type="submit">{updating ? "Update" : "Create"}</button>
</form>
```

- **`<form onSubmit={onSubmit}>`**: Define o manipulador de envio do formulário.
- **Campos de entrada**:
  - **`<input type="text" id="firstName" value={firstName} onChange={(e) => setFirstName(e.target.value)} />`**: Campo de entrada para o primeiro nome, com estado vinculado e manipulador de mudança.
  - **`<input type="text" id="lastName" value={lastName} onChange={(e) => setLastName(e.target.value)} />`**: Campo de entrada para o sobrenome.
  - **`<input type="text" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />`**: Campo de entrada para o email.
- **`<button type="submit">{updating ? "Update" : "Create"}</button>`**: Botão de envio do formulário, com texto condicional baseado no modo (criação ou atualização).

### Exportação

```javascript
export default ContactForm;
```

- Exporta o componente `ContactForm` para que ele possa ser usado em outras partes da aplicação.

### Resumo

O componente `ContactForm`:

- Gerencia um formulário de criação/edição de contatos.
- Usa estados para armazenar e atualizar os valores dos campos de entrada.
- Determina se está no modo de criação ou atualização.
- Faz requisições HTTP para criar ou atualizar contatos na API.
- Chama uma função de callback para atualizar a lista de contatos após uma operação bem-sucedida.