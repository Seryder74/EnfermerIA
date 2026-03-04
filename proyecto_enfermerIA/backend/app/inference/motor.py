from .reglas import evaluar_reglas
from .clasificador import clasificar

def motor_inferencia(sintomas):
    puntos = evaluar_reglas(sintomas)
    nivel = clasificar(puntos)
    return nivel