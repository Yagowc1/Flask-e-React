Este código define o componente principal da aplicação React que gerencia uma lista de contatos.

### Importações

```javascript
import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import './App.css'
import ContactForm from './ContactForm'
```

1. **`useState`** e **`useEffect`**: Hooks do React. `useState` é usado para gerenciar estados dentro de componentes funcionais. `useEffect` é usado para efeitos colaterais, como chamadas de API.
2. **`ContactList`** e **`ContactForm`**: Componentes importados que listam os contatos e fornecem um formulário para criação/edição de contatos.
3. **`./App.css`**: Arquivo de estilo específico para o componente `App`.

### Função `App`

A função `App` define o componente principal que gerencia o estado e a lógica da aplicação:

```javascript
function App() {
  const [contacts, setContacts] = useState([])
  // const [contacts, setContacts] = useState([{"firstName":"Yago", "lastName":"Cortez","email":"confia@ganhamo.com"}])
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact] = useState({})

  useEffect(() => {
    fetchContacts()
  }, [])
```

- **`contacts`**: Estado que armazena a lista de contatos.
- **`isModalOpen`**: Estado que controla se o modal (janela de diálogo) está aberto.
- **`currentContact`**: Estado que armazena o contato atual que está sendo criado ou editado.
- **`useEffect`**: Chama `fetchContacts` quando o componente é montado.

### Funções Auxiliares

```javascript
  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    //console.log(data.contacts)
  }

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentContact({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (contact) => {
    if (isModalOpen) return
    setCurrentContact(contact)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }
```

- **`fetchContacts`**: Função assíncrona que busca os contatos de uma API e atualiza o estado `contacts`.
- **`closeModal`**: Fecha o modal e limpa o contato atual.
- **`openCreateModal`**: Abre o modal para criar um novo contato.
- **`openEditModal`**: Abre o modal para editar um contato existente.
- **`onUpdate`**: Fecha o modal e busca novamente os contatos para atualizar a lista.

### Renderização

```javascript
  return <>
    <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate}/>
    <button onClick={openCreateModal}>Create New Contact</button>
    {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <ContactForm existingContact={currentContact} updateCallback={onUpdate}/>
        </div>
      </div>}
  </>
}
```

- **`ContactList`**: Componente que recebe a lista de contatos e funções para atualizar um contato e lidar com atualizações.
- **Botão "Create New Contact"**: Abre o modal para criar um novo contato.
- **Modal**: Aparece se `isModalOpen` for `true`. Contém um componente `ContactForm` que recebe o contato atual e uma função de callback para atualizar a lista de contatos.

### Exportação

```javascript
export default App
```

Exporta o componente `App` para que possa ser utilizado em outras partes da aplicação.

### Resumo

Este código configura o componente principal da aplicação React, que:

1. Busca e exibe uma lista de contatos.
2. Permite criar um novo contato ou editar um contato existente usando um modal.
3. Atualiza a lista de contatos após qualquer modificação.

Os estados e efeitos são gerenciados utilizando os hooks `useState` e `useEffect`, garantindo uma interface reativa e atualizada dinamicamente.