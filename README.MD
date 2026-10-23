# 📚 Registros de Aprendizado (Django App)

Uma aplicação web desenvolvida em **Python** e **Django** que permite aos usuários acompanhar assuntos de estudo e registrar anotações/diários sobre o seu progresso de aprendizado.

Este projeto foi construído com base nos conceitos do livro *Curso Intensivo de Python* (Eric Matthes), adaptado e atualizado para as versões mais recentes do Django e estilizado com **Bootstrap 5**.

---

### 📚 Gerenciamento de Tópicos
- **Visualização de Tópicos:** Listagem de todos os assuntos cadastrados com data de criação.
- **Adicionar Tópico:** Criação de novos assuntos de estudo via formulários validados.
- **Excluir Tópico:** Remoção de tópicos do banco de dados (com remoção automática de todas as anotações vinculadas e caixa de confirmação no navegador).

### 📝 Gerenciamento de Anotações (Entradas)
- **Visualização por Tópico:** Exibição das anotações ordenadas cronologicamente para cada assunto.
- **Nova Anotação:** Adição de novos registros associados a um tópico específico.
- **Editar Anotação:** Atualização de conteúdos já cadastrados.
- **Excluir Anotação:** Remoção individual de anotações com solicitação de confirmação para evitar exclusões acidentais.

---

## 🎨 Interface e Usabilidade
- **Breadcrumb Navigation:** Trilha de navegação para facilitar o retorno aos tópicos e à página inicial.
- **Design Responsivo:** Layout estilizado com Bootstrap, contendo cards, botões organizados e agrupados para melhor experiência do usuário.
- **Mensagens de Confirmação:** Diálogos nativos do navegador (`confirm`) para operações críticas de exclusão.
---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Django 6.1**
- **Bootstrap 5.3** (Interface visual responsiva)
- **SQLite** (Banco de dados padrão)

---

