<<<<<<< HEAD
"""
Motor de inferencia basado en ML (Random Forest).
Se entrena con datos sintéticos la primera vez y guarda el modelo en disco.
"""
import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Ruta donde se guarda el modelo entrenado
MODEL_PATH = os.path.join(os.path.dirname(__file__), "modelo_entrenado.pkl")

# Orden fijo de features (debe coincidir con Sintomas)
FEATURES = [
    "respira", "consciente", "confusion",
    "dolor_pecho", "pulso_debil",
    "convulsion", "paralisis_facial",
    "dificultad_respirar", "labios_azules",
    "sangrado", "sangrado_incontrolable", "fractura_sospecha",
    "quemadura", "quemadura_extensa", "quemadura_cara_cuello",
    "ingestion_sustancia", "vomito_sangre", "perdida_vision",
    "edad_mayor_60", "embarazada"
]

NIVELES = ["LEVE", "MODERADO", "URGENTE", "CRÍTICO"]


def _generar_datos_entrenamiento():
    """Genera dataset sintético basado en criterios clínicos de primeros auxilios."""
    X, y = [], []

    def caso(sintomas: dict, nivel: str):
        fila = [int(sintomas.get(f, False)) for f in FEATURES]
        X.append(fila)
        y.append(nivel)

    # ─── CRÍTICO ───────────────────────────────────────────────
    # No respira
    for _ in range(40):
        caso({"respira": False, "consciente": False}, "CRÍTICO")
    # Paro cardíaco aparente
    for _ in range(30):
        caso({"respira": False, "pulso_debil": True, "dolor_pecho": True}, "CRÍTICO")
    # Sangrado incontrolable
    for _ in range(30):
        caso({"sangrado": True, "sangrado_incontrolable": True, "consciente": True}, "CRÍTICO")
    # Convulsión + inconsciente
    for _ in range(25):
        caso({"convulsion": True, "consciente": False, "respira": True}, "CRÍTICO")
    # Quemadura extensa en cara
    for _ in range(25):
        caso({"quemadura": True, "quemadura_extensa": True, "quemadura_cara_cuello": True, "dificultad_respirar": True}, "CRÍTICO")
    # Intoxicación grave
    for _ in range(25):
        caso({"ingestion_sustancia": True, "vomito_sangre": True, "consciente": False}, "CRÍTICO")
    # Labios azules + inconsciente
    for _ in range(20):
        caso({"labios_azules": True, "consciente": False, "dificultad_respirar": True}, "CRÍTICO")
    # ACV aparente
    for _ in range(20):
        caso({"paralisis_facial": True, "consciente": False, "perdida_vision": True}, "CRÍTICO")

    # ─── URGENTE ───────────────────────────────────────────────
    # Dolor de pecho consciente
    for _ in range(35):
        caso({"dolor_pecho": True, "consciente": True, "respira": True, "edad_mayor_60": True}, "URGENTE")
    # Dificultad respiratoria seria
    for _ in range(30):
        caso({"dificultad_respirar": True, "labios_azules": True, "respira": True, "consciente": True}, "URGENTE")
    # Convulsión pero consciente después
    for _ in range(25):
        caso({"convulsion": True, "consciente": True, "confusion": True, "respira": True}, "URGENTE")
    # Sangrado con posible fractura
    for _ in range(25):
        caso({"sangrado": True, "fractura_sospecha": True, "consciente": True, "respira": True}, "URGENTE")
    # Quemadura extensa
    for _ in range(20):
        caso({"quemadura": True, "quemadura_extensa": True, "consciente": True, "respira": True}, "URGENTE")
    # Intoxicación consciente
    for _ in range(20):
        caso({"ingestion_sustancia": True, "confusion": True, "consciente": True, "respira": True}, "URGENTE")
    # Embarazada con síntomas
    for _ in range(20):
        caso({"embarazada": True, "dolor_pecho": True, "consciente": True, "respira": True}, "URGENTE")
    # Parálisis facial
    for _ in range(20):
        caso({"paralisis_facial": True, "consciente": True, "confusion": True, "respira": True}, "URGENTE")

    # ─── MODERADO ──────────────────────────────────────────────
    # Fractura sin sangrado
    for _ in range(35):
        caso({"fractura_sospecha": True, "consciente": True, "respira": True, "sangrado": False}, "MODERADO")
    # Quemadura leve
    for _ in range(30):
        caso({"quemadura": True, "quemadura_extensa": False, "consciente": True, "respira": True}, "MODERADO")
    # Sangrado controlable
    for _ in range(30):
        caso({"sangrado": True, "sangrado_incontrolable": False, "consciente": True, "respira": True}, "MODERADO")
    # Dificultad leve para respirar
    for _ in range(25):
        caso({"dificultad_respirar": True, "labios_azules": False, "consciente": True, "respira": True}, "MODERADO")
    # Confusión leve
    for _ in range(20):
        caso({"confusion": True, "consciente": True, "respira": True}, "MODERADO")
    # Ingestion sin síntomas graves
    for _ in range(20):
        caso({"ingestion_sustancia": True, "consciente": True, "respira": True, "vomito_sangre": False}, "MODERADO")

    # ─── LEVE ──────────────────────────────────────────────────
    for _ in range(50):
        caso({"respira": True, "consciente": True}, "LEVE")
    for _ in range(30):
        caso({"respira": True, "consciente": True, "fractura_sospecha": False, "sangrado": False}, "LEVE")
    for _ in range(30):
        caso({"respira": True, "consciente": True, "quemadura": False, "confusion": False}, "LEVE")

    return np.array(X), np.array(y)


def _entrenar_modelo():
    X, y = _generar_datos_entrenamiento()
    clf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    clf.fit(X, y)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(clf, f)
    return clf


def _cargar_modelo():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    return _entrenar_modelo()


# Carga el modelo al importar el módulo
_modelo = _cargar_modelo()


def predecir_nivel(sintomas) -> tuple[str, dict]:
    """
    Recibe un objeto Sintomas y devuelve:
    - nivel: str  ("LEVE", "MODERADO", "URGENTE", "CRÍTICO")
    - probabilidades: dict con la confianza por nivel
    """
    # Reglas críticas absolutas (no negociables)
    if not sintomas.respira:
        return "CRÍTICO", {"CRÍTICO": 1.0}
    if sintomas.sangrado_incontrolable and not sintomas.consciente:
        return "CRÍTICO", {"CRÍTICO": 1.0}

    fila = np.array([[int(getattr(sintomas, f, False)) for f in FEATURES]])
    nivel = _modelo.predict(fila)[0]
    probs = dict(zip(_modelo.classes_, _modelo.predict_proba(fila)[0]))

    return nivel, probs
=======
from .reglas import crear_base_conocimiento

class MotorInferencia:
    def __init__(self):
        self.base_conocimiento = crear_base_conocimiento()
        self.memoria_trabajo = {}  # Hechos

    def agregar_hechos(self, hechos: dict):
        self.memoria_trabajo.update(hechos)

    def razonar(self):
        historial_razonamiento = []
        historial_razonamiento.append(f"Hechos iniciales analizados: {self.memoria_trabajo}")
        
        nivel_asignado = "LEVE"
        jerarquia = {"LEVE": 1, "MODERADO": 2, "URGENTE": 3, "CRÍTICO": 4}
        
        for regla in self.base_conocimiento:
            if all(condicion(self.memoria_trabajo) for condicion in regla.condiciones):
                historial_razonamiento.append(f"-> Regla activada: {regla.nombre}")
                resultado = regla.conclusion(self.memoria_trabajo)
                
                nuevo_nivel = resultado.get("nivel")
                historial_razonamiento.append(f"   Deducción de regla: Gravedad {nuevo_nivel} ({resultado.get('razon')})")
                
                if jerarquia.get(nuevo_nivel, 0) > jerarquia.get(nivel_asignado, 0):
                    nivel_asignado = nuevo_nivel
                    historial_razonamiento.append(f"-> Actualización: Nivel de Gravedad ajustado a {nivel_asignado}")
        
        self.memoria_trabajo['nivel_calculado'] = nivel_asignado
        historial_razonamiento.append(f"Conclusión final: Nivel {nivel_asignado}")
        
        return nivel_asignado, historial_razonamiento
>>>>>>> cd89b184339915b6ebbd1300adb8913199a11a6c
