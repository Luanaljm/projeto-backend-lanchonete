from pydantic import BaseModel

class PagamentoInput(BaseModel):
    pedido_id: int
    numero_cartao_mock: str  # Simulação: se digitar '0000' dá erro, o resto aprova
    valor: float

class PagamentoResponse(BaseModel):
    sucesso: bool
    mensagem: str
    transacao_id: str