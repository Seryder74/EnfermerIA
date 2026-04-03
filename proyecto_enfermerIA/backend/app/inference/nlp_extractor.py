import re

class ExtractorNLPLocal:
    def __init__(self):
        # Base de conocimiento semántico
        # Mapea expresiones del lenguaje humano a nuestros 'Hechos' formales lógicos
        self.patrones = {
            "respira": {
                "negativos": r"\b(no respira|ahoga|asfixia|sin aire|morado|paro respiratorio|dejó de respirar)\b"
            },
            "consciente": {
                "negativos": r"\b(desmayó|inconsciente|no responde|no despierta|desmayado|coma|perdió el conocimiento)\b"
            },
            "sangrado": {
                "positivos": r"\b(sangre|sangrando|hemorragia|cortada profunda|herida abierta|charco de sangre)\b"
            },
            "convulsion": {
                "positivos": r"\b(convulsiona|ataque|tiembla mucho|epilepsia|espumarajo)\b"
            },
            "quemadura_grave": {
                "positivos": r"\b(quemó|fuego|hirviendo|quemaduras|electrocutó|ácido|estalló)\b"
            }
        }
        
    def procesar_texto(self, texto: str) -> dict:
        """ 
        Intérprete heurístico que usa procesamiento puro en Python.
        Permite inferir síntomas a partir del texto ingresado por el usuario de forma 100% offline.
        """
        texto_limpio = texto.lower().strip()
        
        # Asignamos valores por defecto a los hechos
        hechos_extraidos = {
            "respira": True,
            "consciente": True,
            "sangrado": False,
            "convulsion": False,
            "quemadura_grave": False,
            "_metodo_extraccion": "nlp_local"
        }
        
        # Evaluamos cada patrón en el texto
        if re.search(self.patrones["respira"]["negativos"], texto_limpio):
            hechos_extraidos["respira"] = False
            
        if re.search(self.patrones["consciente"]["negativos"], texto_limpio):
            hechos_extraidos["consciente"] = False
            
        if re.search(self.patrones["sangrado"]["positivos"], texto_limpio):
            hechos_extraidos["sangrado"] = True
            
        if re.search(self.patrones["convulsion"]["positivos"], texto_limpio):
            hechos_extraidos["convulsion"] = True
            
        if re.search(self.patrones["quemadura_grave"]["positivos"], texto_limpio):
            hechos_extraidos["quemadura_grave"] = True
            
        return hechos_extraidos
