from enum import Enum
from typing import List

class Opciones(Enum):
    OPCION_1 = 1
    OPCION_2 = 2
    OPCION_3 = 3
    OPCION_4 = 4
    OPCION_5 = 5
    OPCION_6 = 6
    OPCION_7 = 7
    OPCION_8 = 8
    OPCION_9 = 9
    OPCION_10 = 10
    
class Galleta:
    def __init__(self, nombre: str, opciones: List[Opciones]) -> None:
        self.nombre = nombre
        self.opciones = opciones

class SelectorGalletas:
    def __init__(self, galletas: List[Galleta]) -> None:
        self.galletas = galletas

    def seleccionar_galletas(self, opciones_seleccionadas: List[Opciones]) -> List[str]:
        galletas_seleccionadas = []
        for galleta in self.galletas:
            if all(opcion in galleta.opciones for opcion in opciones_seleccionadas):
                galletas_seleccionadas.append(galleta.nombre)
        
        return galletas_seleccionadas

# Definición de las galletas
galletas = [
    Galleta("GALLETA NUTELLA", [Opciones.OPCION_1, Opciones.OPCION_4]),
    Galleta("GALLETA OREO TRUFFLE", [Opciones.OPCION_1, Opciones.OPCION_4, Opciones.OPCION_7]),
    Galleta("GALLETA PENAUT BUTTER & OREO", [Opciones.OPCION_4, Opciones.OPCION_7, Opciones.OPCION_9, Opciones.OPCION_10]),
    Galleta("GALLETA SALTED CARAMEL & PECAN CRUMB", [Opciones.OPCION_5, Opciones.OPCION_9]),
    Galleta("GALLETA BIRTHDAY CAKE", [Opciones.OPCION_1, Opciones.OPCION_3]),
    Galleta("GALLETA MACADAMIA & WHITE CHOCOLATE", [Opciones.OPCION_3, Opciones.OPCION_5]),
    Galleta("GALLETA KINDER & KINDER BUENO", [Opciones.OPCION_1, Opciones.OPCION_2, Opciones.OPCION_4]),
    Galleta("GALLETA MILO", [Opciones.OPCION_4]),
    Galleta("GALLETA KEY LIME PIE", [Opciones.OPCION_3, Opciones.OPCION_8]),
    Galleta("GALLETA CLASSIC CHOCOLATE CHIP", [Opciones.OPCION_4]),
    Galleta("GALLETA CINNAMON ROLL SWIRL", [Opciones.OPCION_3, Opciones.OPCION_6]),
    Galleta("GALLETA RED VELVET", [Opciones.OPCION_3, Opciones.OPCION_4]),
]

def seleccionar_galletas(opciones_seleccionadas: List[Opciones]) -> List[str]:
    selector = SelectorGalletas(galletas)
    galletas_disponibles = selector.seleccionar_galletas(opciones_seleccionadas)
    return galletas_disponibles


