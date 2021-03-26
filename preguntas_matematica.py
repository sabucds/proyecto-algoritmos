from jugando import *
from funciones_proyecto import *
from juego import *

class PreguntasMate(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuesta, pista):
        super().__init__(nombre, recompensa, reglas, requerimento)
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.pista = pista
