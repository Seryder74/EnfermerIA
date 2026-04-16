<<<<<<< HEAD
from pydantic import BaseModel

class Sintomas(BaseModel):
    # --- Conciencia y respiración ---
    respira: bool                  # ¿La persona respira?
    consciente: bool               # ¿Está consciente / responde?
    confusion: bool                # ¿Está confundida o desorientada?

    # --- Cardiovascular ---
    dolor_pecho: bool              # ¿Tiene dolor en el pecho?
    pulso_debil: bool              # ¿El pulso es débil o no se siente?

    # --- Neurológico ---
    convulsion: bool               # ¿Tuvo o está teniendo convulsiones?
    paralisis_facial: bool         # ¿Tiene la cara caída de un lado?

    # --- Respiratorio ---
    dificultad_respirar: bool      # ¿Le cuesta respirar?
    labios_azules: bool            # ¿Tiene labios o uñas azulados?

    # --- Traumatismos ---
    sangrado: bool                 # ¿Tiene sangrado visible?
    sangrado_incontrolable: bool   # ¿El sangrado no para con presión?
    fractura_sospecha: bool        # ¿Se sospecha hueso roto?

    # --- Quemaduras ---
    quemadura: bool                # ¿Tiene quemadura?
    quemadura_extensa: bool        # ¿Cubre más del 10% del cuerpo?
    quemadura_cara_cuello: bool    # ¿Está en cara, cuello o manos?

    # --- Intoxicación ---
    ingestion_sustancia: bool      # ¿Ingirió algo tóxico / medicamento?
    vomito_sangre: bool            # ¿Vomita sangre o material oscuro?
    perdida_vision: bool           # ¿Perdió o ve borroso repentinamente?

    # --- General ---
    edad_mayor_60: bool            # ¿Tiene más de 60 años?
    embarazada: bool               # ¿Está embarazada?
=======
class Sintomas:
    def __init__(self, respira: bool, consciente: bool, sangrado: bool,
                convulsion: bool, quemadura_grave: bool):
        self.respira = respira
        self.consciente = consciente
        self.sangrado = sangrado
        self.convulsion = convulsion
        self.quemadura_grave = quemadura_grave
>>>>>>> cd89b184339915b6ebbd1300adb8913199a11a6c
