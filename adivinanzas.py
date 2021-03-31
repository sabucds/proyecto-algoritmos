from juego import *
from jugador import *

class Adivinanzas(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuestas, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.pregunta = pregunta  # str
        self.respuestas = respuestas  # lista
    
    def juego(self, jugador):
        print(self.pregunta)
        p = 0
        while True:
            respuesta = input('Ingresa la respuesta o "*" para usar una pista ==> ')

            if respuesta in self.respuestas:
                print(f'Adivinaste, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa)
                return True
            elif respuesta == '*':
                p = self.ver_pista_juego(jugador, p)

            else:
                jugador.perder_vida(1/2)
                print(f'Incorrecto, pierdes media vida. Vidas actuales: {jugador.vidas}')

