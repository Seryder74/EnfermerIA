class Regla:
    def __init__(self, nombre, condiciones, conclusion):
        self.nombre = nombre
        self.condiciones = condiciones
        self.conclusion = conclusion

def crear_base_conocimiento():
    reglas = []
    
    # R1: Paro respiratorio -> CRÍTICO
    reglas.append(
        Regla(
            nombre="R1 - Paro respiratorio",
            condiciones=[lambda hechos: hechos.get("respira") is False],
            conclusion=lambda hechos: {"nivel": "CRÍTICO", "razon": "El paciente no respira."}
        )
    )
    
    # R2: Inconsciencia con respiración
    reglas.append(
        Regla(
            nombre="R2 - Inconsciencia",
            condiciones=[lambda hechos: hechos.get("consciente") is False, lambda hechos: hechos.get("respira") is True],
            conclusion=lambda hechos: {"nivel": "CRÍTICO" if hechos.get("sangrado") else "URGENTE", "razon": "Paciente no responde a estímulos."}
        )
    )

    # R3: Convulsiones
    reglas.append(
        Regla(
            nombre="R3 - Convulsión",
            condiciones=[lambda hechos: hechos.get("convulsion") is True],
            conclusion=lambda hechos: {"nivel": "URGENTE", "razon": "Paciente presentando convulsiones activas."}
        )
    )

    # R4: Hemorragia
    reglas.append(
        Regla(
            nombre="R4 - Hemorragia",
            condiciones=[lambda hechos: hechos.get("sangrado") is True],
            conclusion=lambda hechos: {"nivel": "URGENTE", "razon": "Hemorragia o sangrado activo presente."}
        )
    )

    # R5: Quemadura
    reglas.append(
        Regla(
            nombre="R5 - Quemaduras graves",
            condiciones=[lambda hechos: hechos.get("quemadura_grave") is True],
            conclusion=lambda hechos: {"nivel": "URGENTE", "razon": "Quemadura extensa o profunda reportada."}
        )
    )
    
    return reglas