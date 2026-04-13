from pydantic import BaseModel, EmailStr, ConfigDict


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    aceita_termos: bool  # Para LGPD


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str
    pontos_fidelidade: int

    model_config = ConfigDict(from_attributes=True)