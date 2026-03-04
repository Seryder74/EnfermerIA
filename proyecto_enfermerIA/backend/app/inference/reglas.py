def evaluar_reglas(s):

    # Regla crítica directa
    if not s.respira:
        return 10

    puntos = 0

    if not s.consciente:
        puntos += 4

    if s.convulsion:
        puntos += 3

    if s.sangrado:
        puntos += 2

    if s.quemadura_grave:
        puntos += 3

    return puntos