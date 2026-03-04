def clasificar(puntos):

    if puntos >= 8:
        return "CRÍTICO"
    elif puntos >= 4:
        return "URGENTE"
    elif puntos >= 2:
        return "MODERADO"
    else:
        return "LEVE"