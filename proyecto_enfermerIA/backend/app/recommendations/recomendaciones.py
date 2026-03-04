def obtener_recomendacion(nivel):

    recomendaciones = {
        "CRÍTICO": "Llame inmediatamente al 911 e inicie maniobras básicas si sabe realizarlas.",
        "URGENTE": "Busque atención médica lo antes posible.",
        "MODERADO": "Aplicar primeros auxilios básicos y observar evolución.",
        "LEVE": "Mantener en observación."
    }

    return recomendaciones.get(nivel)