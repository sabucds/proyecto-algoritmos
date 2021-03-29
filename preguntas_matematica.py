from jugando import *
from funciones_proyecto import *
from juego import *
import sympy
from sympy.parsing.sympy_parser import *

class PreguntasMate(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuesta, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.pregunta = pregunta
        self.respuesta = respuesta
    
    def juego(self, jugador):
        print(self.pregunta.replace('random(1,9)', '3').replace('random(1,3)x', '2*x').replace('tan2(2*x)', 'tan(4*x)'))
        i = self.pregunta.find('=')
        funcion = self.pregunta[i+1:]
        x = sympy.symbols('x')
        funcion = funcion.replace('random(1,9)', '3').replace('random(1,3)x', '2*x').replace('tan2(2*x)', 'tan(4*x)')
        funcion = parse_expr(funcion)
        derivada = str(funcion.diff(x))
        print(derivada)
        p = 0

        #FIXME: DERIVA MAL LA TANGENTE

        while True:
            r = input('Ingrese la respuesta o ingrese "*" para ver una pista ==> ')
            if r =='*':
                p = self.ver_pista_juego(jugador, p)
            elif r.replace(' ', '').lower() == derivada.replace(' ', ''): 
                print(f'Es correcto, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa)
                return True
            else:
                print(f'Incorrecto, a este paso no llegaras a mate II... Pierdes un cuarto de vida. \nVidas actuales: {jugador.vidas}')
            





