from pydantic import BaseModel, ConfigDict
from enum import Enum


class CanalEnum(str, Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"


class PedidoCreate(BaseModel):
    cliente_id: int
    canal_pedido: CanalEnum
    valor_total: float


class PedidoResponse(PedidoCreate):
    id: int
    status: str

    # Isso aqui remove o aviso amarelo do terminal:
    model_config = ConfigDict(from_attributes=True)