from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from passlib.context import CryptContext

# Configuração da criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/usuarios", tags=["Usuários e LGPD"])


@router.post("/", response_model=UsuarioResponse)
def cadastrar_usuario(user: UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica se o e-mail já existe
    db_user = db.query(Usuario).filter(Usuario.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    # Transforma a senha em HASH (Requisito de Segurança)
    hashed_password = pwd_context.hash(user.senha)

    novo_usuario = Usuario(
        nome=user.nome,
        email=user.email,
        senha_hash=hashed_password,
        aceita_termos=user.aceita_termos
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario