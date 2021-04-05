from juego import *
from jugador import *

class LogicaBooleana(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuesta, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.pregunta = pregunta
        self.respuesta = respuesta
    
    def juego(self, jugador, tiempo_inicio):
        print(self.pregunta)
        while True:
            r = input('Ingresa la respuesta ==> ').title()
            if r.replace(' ', '') == 'False' or r.replace(' ', '') == 'Falso':
                r = False
            elif r.replace(' ', '') == 'True' or r.replace(' ', '') == 'Verdadero':
                r = True

            a = False
            b = True
            out = self.pregunta[(self.pregunta.find('=')+1):]
            out = out[out.find('=')+1:]
            respuesta = eval(out)
            if r == respuesta:
                jugador.guardar_objeto(self.recompensa)
                print(f'Correcto, ganaste: {self.recompensa}')
                return True
            else:
                jugador.perder_vida(1/2)
                print(f'Incorrecto, pierdes media vida. Vidas actuales: {jugador.vidas}')
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break

