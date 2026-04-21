"""
Recomendaciones detalladas por nivel de gravedad y tipo de emergencia detectada.
"""

def _detectar_categoria(sintomas) -> str:
    """Detecta la categoría principal de emergencia según los síntomas."""
    if not sintomas.respira or sintomas.pulso_debil:
        return "cardiaco"
    if sintomas.convulsion or sintomas.paralisis_facial or sintomas.perdida_vision:
        return "neurologico"
    if sintomas.dificultad_respirar or sintomas.labios_azules:
        return "respiratorio"
    if sintomas.sangrado or sintomas.sangrado_incontrolable or sintomas.fractura_sospecha:
        return "traumatismo"
    if sintomas.quemadura:
        return "quemadura"
    if sintomas.ingestion_sustancia or sintomas.vomito_sangre:
        return "intoxicacion"
    return "general"


RECOMENDACIONES = {
    "CRÍTICO": {
        "cardiaco": {
            "titulo": "Posible paro cardiorrespiratorio",
            "pasos": [
                "Llame al 911 AHORA o pida a alguien que lo haga mientras usted actúa.",
                "Coloque a la persona boca arriba en una superficie firme.",
                "Inicie RCP: 30 compresiones en el centro del pecho (fuerte y rápido), luego 2 respiraciones de rescate.",
                "Continúe el ciclo hasta que llegue la ambulancia o la persona responda.",
                "Si hay un desfibrilador (DEA) cerca, úselo siguiendo las instrucciones de voz.",
            ],
            "advertencia": "No deje sola a la persona. No le dé agua ni comida."
        },
        "neurologico": {
            "titulo": "Emergencia neurológica grave",
            "pasos": [
                "Llame al 911 inmediatamente.",
                "No sujete a la persona si convulsiona; retire objetos peligrosos a su alrededor.",
                "Colóquela de lado (posición de recuperación) para evitar que se ahogue.",
                "No introduzca nada en su boca.",
                "Anote la hora de inicio y duración de la convulsión para informar al médico.",
            ],
            "advertencia": "No le dé medicamentos sin indicación médica."
        },
        "respiratorio": {
            "titulo": "Insuficiencia respiratoria grave",
            "pasos": [
                "Llame al 911 inmediatamente.",
                "Siente o recueste a la persona en posición cómoda (semi-sentada suele ayudar).",
                "Afloje ropa ajustada en cuello y pecho.",
                "Si la persona tiene inhalador propio, ayúdela a usarlo.",
                "Monitoree la respiración constantemente hasta que llegue ayuda.",
            ],
            "advertencia": "No acueste a la persona completamente si le cuesta respirar."
        },
        "traumatismo": {
            "titulo": "Traumatismo grave con sangrado incontrolable",
            "pasos": [
                "Llame al 911 inmediatamente.",
                "Presione la herida con una tela limpia sin soltar durante al menos 10 minutos.",
                "Si es un miembro (brazo/pierna), aplique presión por encima de la herida.",
                "No retire objetos clavados; estabilícelos con apósitos alrededor.",
                "Mantenga a la persona quieta y abrigada para prevenir shock.",
            ],
            "advertencia": "No mueva a la persona si sospecha lesión en cuello o columna."
        },
        "quemadura": {
            "titulo": "Quemadura grave o extensa",
            "pasos": [
                "Llame al 911 inmediatamente.",
                "Enfríe la quemadura con agua fría (no helada) durante 10-20 minutos.",
                "Cubra con una tela limpia y húmeda; no use algodón.",
                "No aplique cremas, mantequilla ni remedios caseros.",
                "Mantenga a la persona abrigada para evitar hipotermia.",
            ],
            "advertencia": "No reviente las ampollas. No retire ropa pegada a la piel."
        },
        "intoxicacion": {
            "titulo": "Intoxicación grave",
            "pasos": [
                "Llame al 911 y al Centro de Toxicología más cercano inmediatamente.",
                "Si la persona está inconsciente, colóquela de lado.",
                "Intente identificar qué sustancia ingirió y cuánta.",
                "No provoque el vómito a menos que el médico o toxicólogo lo indique.",
                "Guarde el envase o muestra de la sustancia para mostrársela al médico.",
            ],
            "advertencia": "No dé leche ni agua sin indicación médica."
        },
        "general": {
            "titulo": "Emergencia crítica",
            "pasos": [
                "Llame al 911 inmediatamente.",
                "Mantenga a la persona consciente hablándole con calma.",
                "No la mueva a menos que haya peligro inmediato.",
                "Monitoree respiración y pulso hasta que llegue ayuda.",
            ],
            "advertencia": "Siga las instrucciones del operador del 911."
        }
    },

    "URGENTE": {
        "cardiaco": {
            "titulo": "Posible problema cardíaco",
            "pasos": [
                "Traslade a urgencias lo antes posible o llame al 911.",
                "Siente a la persona; evite que haga esfuerzo físico.",
                "Afloje ropa ajustada.",
                "Si tiene aspirina y no es alérgica, puede masticar 1 tableta de 325mg (solo adultos).",
                "Monitoree si pierde el conocimiento para iniciar RCP si es necesario.",
            ],
            "advertencia": "No conduzca usted mismo si es el afectado."
        },
        "neurologico": {
            "titulo": "Síntomas neurológicos urgentes",
            "pasos": [
                "Traslade a urgencias inmediatamente.",
                "Anote la hora exacta en que aparecieron los síntomas.",
                "No le dé alimentos ni bebidas.",
                "Si pierde el conocimiento, colóquela de lado.",
            ],
            "advertencia": "Los síntomas de ACV requieren atención en menos de 3 horas."
        },
        "respiratorio": {
            "titulo": "Dificultad respiratoria",
            "pasos": [
                "Traslade a urgencias o llame al 911.",
                "Mantenga a la persona sentada o semi-incorporada.",
                "Afloje cualquier ropa que oprima el pecho.",
                "Si tiene inhalador, adminístrelo.",
                "Tranquilice a la persona; el pánico empeora la respiración.",
            ],
            "advertencia": "Si los labios se tornan azules, llame al 911 de inmediato."
        },
        "traumatismo": {
            "titulo": "Traumatismo que requiere atención médica",
            "pasos": [
                "Traslade a urgencias.",
                "Controle el sangrado con presión directa.",
                "Inmovilice la zona afectada si hay sospecha de fractura.",
                "Aplique hielo envuelto en tela (no directo a la piel) para reducir inflamación.",
            ],
            "advertencia": "No intente alinear huesos rotos manualmente."
        },
        "quemadura": {
            "titulo": "Quemadura que requiere atención médica",
            "pasos": [
                "Traslade a urgencias.",
                "Enfríe con agua fría durante 10-15 minutos.",
                "Cubra con gasa estéril o tela limpia.",
                "No aplique nada sobre la quemadura.",
            ],
            "advertencia": "Las quemaduras en cara, manos o genitales siempre son urgentes."
        },
        "intoxicacion": {
            "titulo": "Posible intoxicación",
            "pasos": [
                "Traslade a urgencias o llame al Centro de Toxicología.",
                "Identifique y lleve consigo la sustancia ingerida.",
                "Monitoree el nivel de consciencia.",
                "No provoque el vómito sin indicación médica.",
            ],
            "advertencia": "Algunos tóxicos empeoran si se provoca el vómito."
        },
        "general": {
            "titulo": "Situación urgente",
            "pasos": [
                "Busque atención médica lo antes posible.",
                "Monitoree los signos vitales.",
                "Mantenga a la persona calmada y en reposo.",
            ],
            "advertencia": "Si los síntomas empeoran, llame al 911."
        }
    },

    "MODERADO": {
        "traumatismo": {
            "titulo": "Traumatismo moderado",
            "pasos": [
                "Limpie y cubra heridas con gasa estéril.",
                "Aplique hielo envuelto en tela por 20 minutos cada hora.",
                "Inmovilice la zona lesionada con un cabestrillo o vendaje.",
                "Acuda a urgencias o médico en las próximas horas.",
            ],
            "advertencia": "Si el dolor aumenta o aparece entumecimiento, vaya a urgencias."
        },
        "quemadura": {
            "titulo": "Quemadura leve o moderada",
            "pasos": [
                "Enfríe con agua fría durante 10 minutos.",
                "Cubra con gasa estéril.",
                "No reviente las ampollas.",
                "Tome un analgésico de venta libre si hay dolor.",
                "Acuda al médico si la quemadura es mayor que la palma de la mano.",
            ],
            "advertencia": "Vigilar signos de infección en los próximos días."
        },
        "respiratorio": {
            "titulo": "Dificultad respiratoria leve",
            "pasos": [
                "Siente a la persona en posición cómoda.",
                "Respire lentamente por la nariz y exhale por la boca.",
                "Aléjese de posibles irritantes (humo, polvo).",
                "Si no mejora en 15 minutos, acuda a urgencias.",
            ],
            "advertencia": "Si aparecen labios azules, llame al 911."
        },
        "intoxicacion": {
            "titulo": "Posible ingesta de sustancia",
            "pasos": [
                "Llame al Centro de Toxicología para orientación.",
                "Identifique la sustancia y la cantidad aproximada.",
                "Monitoree el estado de consciencia.",
                "Acuda al médico para evaluación.",
            ],
            "advertencia": "No espere a que aparezcan síntomas graves."
        },
        "general": {
            "titulo": "Situación moderada",
            "pasos": [
                "Aplique primeros auxilios básicos según la lesión.",
                "Monitoree los síntomas durante las próximas horas.",
                "Acuda al médico hoy.",
            ],
            "advertencia": "Si los síntomas empeoran, busque atención urgente."
        }
    },

    "LEVE": {
        "general": {
            "titulo": "Situación leve",
            "pasos": [
                "Mantenga a la persona en reposo y tranquila.",
                "Observe la evolución de los síntomas.",
                "Si hay heridas menores, limpie con agua y jabón y cubra.",
                "Consulte con un médico si los síntomas persisten más de 24 horas.",
            ],
            "advertencia": "Si aparece cualquier síntoma nuevo o el estado empeora, busque atención médica."
        }
    }
}


def obtener_recomendacion(nivel: str, sintomas) -> dict:
    """
    Devuelve un diccionario con:
    - titulo: nombre de la emergencia detectada
    - pasos: lista de acciones a seguir
    - advertencia: advertencia importante
    - nivel: nivel de gravedad
    - categoria: tipo de emergencia
    """
    categoria = _detectar_categoria(sintomas)
    nivel_data = RECOMENDACIONES.get(nivel, RECOMENDACIONES["LEVE"])

    # Busca la categoría específica; si no existe, usa "general"
    rec = nivel_data.get(categoria, nivel_data.get("general"))

    return {
        "nivel": nivel,
        "categoria": categoria,
        "titulo": rec["titulo"],
        "pasos": rec["pasos"],
        "advertencia": rec["advertencia"]
    }
