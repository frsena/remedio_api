from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Remedio(Base):
    __tablename__ = 'remedio'

    id = Column("id", Integer, primary_key=True)
    nome = Column(String(50), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, data_insercao:Union[DateTime, None] = None):

        self.nome = nome

        if data_insercao:
            self.data_insercao = data_insercao