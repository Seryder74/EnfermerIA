from fastapi import APIRouter
from app.models.sintomas import Sintomas
from app.inference.motor import motor_inferencia
from app.recommendations.recomendaciones import obtener_recomendacion
from app.database import SessionLocal
from app.models.evaluacion_model import Evaluacion

router = APIRouter()

@router.post("/evaluar")
def evaluar(data: dict):

    sintomas = Sintomas(
        respira=data["respira"],
        consciente=data["consciente"],
        sangrado=data["sangrado"],
        convulsion=data["convulsion"],
        quemadura_grave=data["quemadura_grave"]
    )

    nivel = motor_inferencia(sintomas)
    recomendacion = obtener_recomendacion(nivel)

# Guardar en base de datos
    db = SessionLocal()

    nueva_eval = Evaluacion(
        respira=data["respira"],
        consciente=data["consciente"],
        sangrado=data["sangrado"],
        convulsion=data["convulsion"],
        quemadura_grave=data["quemadura_grave"],
        nivel=nivel
    )

    db.add(nueva_eval)
    db.commit()
    db.close()
    
    return {
        "nivel": nivel,
        "recomendacion": recomendacion
    }