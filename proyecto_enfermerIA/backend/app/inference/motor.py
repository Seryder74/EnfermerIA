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