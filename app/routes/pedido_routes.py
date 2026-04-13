from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.pedido import Pedido
from app.schemas.pedido_schema import PedidoCreate, PedidoResponse

# O erro estava na linha abaixo. Use exatamente assim:
router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", response_model=PedidoResponse)
def criar_pedido(pedido_input: PedidoCreate, db: Session = Depends(get_db)):
    novo_pedido = Pedido(
        cliente_id=pedido_input.cliente_id,
        canal_pedido=pedido_input.canal_pedido,
        valor_total=pedido_input.valor_total,
        status="AGUARDANDO_PAGAMENTO"
    )
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

@router.get("/", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()


from app.schemas.pagamento_schema import PagamentoInput, PagamentoResponse
import uuid  # Para gerar um ID de transação fake


# ... (mantenha o que já existe acima e adicione este aqui embaixo)

@router.post("/pagar", response_model=PagamentoResponse)
def pagar_pedido(pagamento: PagamentoInput, db: Session = Depends(get_db)):
    # 1. Busca o pedido no banco
    pedido_no_banco = db.query(Pedido).filter(Pedido.id == pagamento.pedido_id).first()

    if not pedido_no_banco:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    # 2. Simulação de Regra de Negócio (Mock)
    if pagamento.numero_cartao_mock == "0000":
        return PagamentoResponse(
            sucesso=False,
            mensagem="Pagamento Recusado pela Operadora (Cartão Inválido)",
            transacao_id="0"
        )

    # 3. Se aprovado, atualiza o status do pedido (Cozinha -> Pronto)
    pedido_no_banco.status = "PAGO - EM PREPARAÇÃO"
    db.commit()

    return PagamentoResponse(
        sucesso=True,
        mensagem="Pagamento Aprovado! Pedido enviado para a cozinha.",
        transacao_id=str(uuid.uuid4())
    )