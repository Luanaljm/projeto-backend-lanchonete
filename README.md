# Projeto Backend Lanchonete 

Sistema de gerenciamento de pedidos multicanal desenvolvido com FastAPI, SQLAlchemy e SQLite.

## 🚀 Como executar o projeto localmente:
1. Ative o ambiente virtual: `.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (Mac/Linux).
2. Instale as dependências: `pip install fastapi[all] sqlalchemy passlib[bcrypt]`
3. Execute o servidor: `python main.py`
4. A documentação automática estará em: `http://127.0.0.1:8000/docs`

## 🧪 Como executar os testes (Ordem Sugerida):

Para testar a API, utilize o arquivo `Lanchonete.postman_collection.json` incluído neste repositório. Importe-o no Postman e siga a ordem:

1. **Criar Pedido (POST):** Envie um pedido para o endpoint `/pedidos/`.
   - *Ambiente:* Localhost (127.0.0.1:8000).
   - *Seed:* Utilize o JSON de exemplo no Body: `{"cliente_id": 1, "canal_pedido": "TOTEM", "valor_total": 50.0}`.
2. **Listar Pedidos (GET):** Verifique se o pedido foi gravado com sucesso no endpoint `/pedidos/`.
3. **Pagamento (POST):** Utilize o endpoint `/pedidos/pagar` (se implementado) enviando o ID do pedido criado.

**Observações:** - **Token:** Esta versão 0.1.0 utiliza acesso público para facilitar a avaliação, sem necessidade de Bearer Token.
- **Ambiente:** As rotas estão configuradas para o ambiente de desenvolvimento local.
