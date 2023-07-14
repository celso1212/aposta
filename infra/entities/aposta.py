from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Aposta(Base):
    __tablename__ = 'aposta'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    nome_apostador = Column(String(255), nullable=False)
    time_casa = Column(Integer, nullable=False)
    time_visitante = Column(Integer, nullable=False)
    valor_aposta = Column(String(255), nullable=False)
    valor_ganho = Column(Integer, nullable=False)
    