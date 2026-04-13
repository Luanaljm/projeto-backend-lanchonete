from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String) # Nunca salvamos a senha limpa!
    perfil = Column(String, default="CLIENTE") # ADMIN ou CLIENTE
    pontos_fidelidade = Column(Integer, default=0) # Requisito de Fidelização
    aceita_termos = Column(Boolean, default=True) # Registro de consentimento LGPD