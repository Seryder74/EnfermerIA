def evaluar_reglas(sintomas):
    puntos = 0

    if not sintomas.respira:
        puntos += 5
    
    if not sintomas.consciente:
        puntos += 4
    
    if sintomas.convulsion:
        puntos += 3
    
    if sintomas.sangrado:
        puntos += 2
    
    if sintomas.quemadura_grave:
        puntos += 3

    return puntos