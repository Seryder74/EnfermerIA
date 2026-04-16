from fastapi import APIRouter
from app.models.sintomas import Sintomas
from app.inference.motor import predecir_nivel
from app.recommendations.recomendaciones import obtener_recomendacion
from app.database import SessionLocal
from app.models.evaluacion_model import Evaluacion

router = APIRouter()

@router.post("/evaluar")
def evaluar(sintomas: Sintomas):

    # Motor ML predice nivel y probabilidades
    nivel, probabilidades = predecir_nivel(sintomas)

    # Recomendaciones detalladas según nivel y categoría
    recomendacion = obtener_recomendacion(nivel, sintomas)

    # Guardar en base de datos
    db = SessionLocal()
    nueva_eval = Evaluacion(
        respira=sintomas.respira,
        consciente=sintomas.consciente,
        confusion=sintomas.confusion,
        dolor_pecho=sintomas.dolor_pecho,
        pulso_debil=sintomas.pulso_debil,
        convulsion=sintomas.convulsion,
        paralisis_facial=sintomas.paralisis_facial,
        dificultad_respirar=sintomas.dificultad_respirar,
        labios_azules=sintomas.labios_azules,
        sangrado=sintomas.sangrado,
        sangrado_incontrolable=sintomas.sangrado_incontrolable,
        fractura_sospecha=sintomas.fractura_sospecha,
        quemadura=sintomas.quemadura,
        quemadura_extensa=sintomas.quemadura_extensa,
        quemadura_cara_cuello=sintomas.quemadura_cara_cuello,
        ingestion_sustancia=sintomas.ingestion_sustancia,
        vomito_sangre=sintomas.vomito_sangre,
        perdida_vision=sintomas.perdida_vision,
        edad_mayor_60=sintomas.edad_mayor_60,
        embarazada=sintomas.embarazada,
        nivel=nivel
    )
    db.add(nueva_eval)
    db.commit()
    db.close()

    return {
        "nivel": nivel,
        "probabilidades": {k: round(v, 3) for k, v in probabilidades.items()},
        "recomendacion": recomendacion
    }
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