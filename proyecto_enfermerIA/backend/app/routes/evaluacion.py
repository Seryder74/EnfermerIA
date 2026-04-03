from fastapi import APIRouter
from app.models.sintomas import Sintomas
from app.inference.motor import MotorInferencia
from app.inference.nlp_extractor import ExtractorNLPLocal
from app.recommendations.recomendaciones import obtener_recomendacion

router = APIRouter()

# Instanciamos el extractor puro sin llamadas web
nlp_extractor = ExtractorNLPLocal()

@router.post("/evaluar")
def evaluar(data: dict):

    # Determinar si el usuario mandó texto libre
    texto_usuario = data.get("mensaje")

    if texto_usuario:
        # Extraemos los hechos detectando palabras clave localmente
        hechos_iniciales = nlp_extractor.procesar_texto(texto_usuario)
    else:
        # Fallback a checks booleanos si no hay texto
        hechos_iniciales = {
            "respira": data.get("respira", True),
            "consciente": data.get("consciente", True),
            "sangrado": data.get("sangrado", False),
            "convulsion": data.get("convulsion", False),
            "quemadura_grave": data.get("quemadura_grave", False)
        }

    motor = MotorInferencia()
    motor.agregar_hechos(hechos_iniciales)
    
    nivel, razonamiento = motor.razonar()
    recomendacion = obtener_recomendacion(nivel)

    return {
        "nivel": nivel,
        "recomendacion": recomendacion,
        "pensamiento_ia": razonamiento,
        "hechos_interpretados": hechos_iniciales
    }