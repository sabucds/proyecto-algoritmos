from jugando import *
from funciones_proyecto import *
from juego import *
import sympy
from sympy.parsing.sympy_parser import *

class PreguntasMate(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuesta, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento)
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.pistas = pistas
    
    def juego(self, jugador):
        print(self.pregunta)
        i = self.pregunta.find('=')
        funcion = self.pregunta[i+1:]
        x = sympy.symbols('x')
        funcion = funcion.replace('random(1,9)', '3').replace('random(1,3)', '2')
        print(funcion)
        funcion = parse_expr(funcion)
        print(funcion)
        # derivada = funcion.diff(x)
        # print(derivada)
        // FIXME - NO SIRVE 

        r = input('Ingrese la respuesta ==> ')





