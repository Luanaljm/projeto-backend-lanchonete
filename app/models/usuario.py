from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String) 
    perfil = Column(String, default="CLIENTE") 
    pontos_fidelidade = Column(Integer, default=0) 
    aceita_termos = Column(Boolean, default=True) 
