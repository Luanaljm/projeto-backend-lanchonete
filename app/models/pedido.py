import enum
from sqlalchemy import Column, Integer, String, Enum, Float
from app.database.db import Base

# Aqui atendemos o requisito de Multicanalidade do roteiro
class CanalEnum(str, enum.Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    canal_pedido = Column(Enum(CanalEnum), nullable=False)
    valor_total = Column(Float)
    status = Column(String, default="RECEBIDO") # Regra de negócio: todo pedido nasce como RECEBIDO