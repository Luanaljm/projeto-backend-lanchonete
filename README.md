# Projeto Backend Lanchonete

Sistema de gerenciamento de pedidos multicanal desenvolvido com FastAPI, SQLAlchemy e SQLite para a rede Raízes do Nordeste.

## Como executar o projeto localmente:
1. Ative o ambiente virtual: `.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (Mac/Linux).
2. Instale as dependências: `pip install fastapi[all] sqlalchemy passlib[bcrypt]`
3. Execute o servidor: `python main.py`
4. A documentação automática estará em: http://127.0.0.1:8000/docs

## Como executar os testes (Ordem Sugerida):
Para testar a API, utilize o arquivo `Lanchonete.postman_collection.json` incluído neste repositório. Importe-o no Postman e execute as requisições na seguinte ordem:

1. **Cadastrar Usuário (POST `/usuarios/`)**: Realiza o cadastro do cliente aplicando as validações de consentimento da LGPD.
2. **Criar Pedido (POST `/pedidos/`)**: Envia o pedido identificando a origem do canal. Use o JSON de exemplo no Body: `{"canal_pedido": "TOTEM", "valor_total": 50.0}`.
3. **Listar Pedidos (GET `/pedidos/`)**: Valida se o pedido foi gravado com persistência real no banco SQLite e permite filtrar por canal.
4. **Simular Pagamento (POST `/pagamentos/simular`)**: Orquestra a integração simulada com o gateway externo de pagamento (Mock) atualizando o status do pedido.

## Observações:
* **Ambiente**: As rotas estão configuradas por padrão para o ambiente de desenvolvimento local (`127.0.0.1:8000`).
* **Coleção de Testes**: O arquivo JSON da coleção contém cenários positivos e negativos para cobrir integralmente o plano de testes do relatório técnico.
