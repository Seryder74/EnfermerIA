from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Evaluacion(Base):
    __tablename__ = "evaluaciones"

    id = Column(Integer, primary_key=True, index=True)

    # Conciencia y respiración
    respira = Column(Boolean)
    consciente = Column(Boolean)
    confusion = Column(Boolean)

    # Cardiovascular
    dolor_pecho = Column(Boolean)
    pulso_debil = Column(Boolean)

    # Neurológico
    convulsion = Column(Boolean)
    paralisis_facial = Column(Boolean)

    # Respiratorio
    dificultad_respirar = Column(Boolean)
    labios_azules = Column(Boolean)

    # Traumatismos
    sangrado = Column(Boolean)
    sangrado_incontrolable = Column(Boolean)
    fractura_sospecha = Column(Boolean)

    # Quemaduras
    quemadura = Column(Boolean)
    quemadura_extensa = Column(Boolean)
    quemadura_cara_cuello = Column(Boolean)

    # Intoxicación
    ingestion_sustancia = Column(Boolean)
    vomito_sangre = Column(Boolean)
    perdida_vision = Column(Boolean)

    # General
    edad_mayor_60 = Column(Boolean)
    embarazada = Column(Boolean)

    nivel = Column(String)
