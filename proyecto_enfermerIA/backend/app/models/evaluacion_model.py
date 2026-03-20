from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Evaluacion(Base):
    __tablename__ = "evaluaciones"

    id = Column(Integer, primary_key=True, index=True)

    respira = Column(Boolean)
    consciente = Column(Boolean)
    sangrado = Column(Boolean)
    convulsion = Column(Boolean)
    quemadura_grave = Column(Boolean)

    nivel = Column(String)