# 🍰 Doceria API

API RESTful para gerenciamento de uma doceria, desenvolvida com **Django REST Framework**, com autenticação de usuários via **JWT**, gerenciamento de produtos, pedidos e clientes.

Projetada para integração com front-ends web ou mobile.

---

# 🚀 Funcionalidades

- 🔐 Autenticação de usuários (JWT)
- 👤 Cadastro e perfil de clientes
- 🍩 CRUD de produtos
- 🛒 Criação e gerenciamento de pedidos
- 📦 Itens de pedido vinculados
- 🖼 Upload de imagens de produtos
- ⚡ Cache para otimização de desempenho
- 🌐 CORS configurado para front-end

---

# 🛠 Tecnologias

- Python 3.x  
- Django  
- Django REST Framework  
- Simple JWT  
- PostgreSQL / SQLite  
- Supabase Storage (imagens)  
- Render (deploy)

---

# 📁 Estrutura do Projeto

doceria_api/
│
├── accounts/ # Usuários e autenticação
├── products/ # Produtos
├── sales/ # Pedidos e vendas
├── setup/ # Configurações globais
│
├── manage.py
└── requirements.txt
