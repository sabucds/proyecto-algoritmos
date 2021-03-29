from jugando import *
from jugador import *
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
        print(self.pregunta.replace("tan(x))", "(tan(x))").replace('sen(x))/2', '(sen(x))/2'))
        i = self.pregunta.find('=')
        funcion = self.pregunta[i+1:]
        x = sympy.symbols('x')
        funcion = funcion.replace("tan(x))", "(tan(x))").replace('sen(x))/2', '(sin(x))/2').replace('sen', 'sin')
        funcion = sympy.parse_expr(funcion)
        derivada = funcion.diff(x)
        evalua = self.pregunta[self.pregunta.find('p'):self.pregunta.find(' ', self.pregunta.find('p'))].replace('pi', 'sympy.pi')

        if evalua == 'pi':
            respuesta = derivada.subs(x, sympy.pi)
        elif evalua == 'pi/2':
            respuesta = derivada.subs(x, (sympy.pi)/2)
        else: 
            respuesta = derivada.subs(x, (sympy.pi)/3)
        p = 0

        while True:
            r = input('Ingrese la respuesta o ingrese "*" para ver una pista ==> ')
            if r =='*':
                p = self.ver_pista_juego(jugador, p)
            elif float(r.replace(' ', '')) == respuesta: 
                print(f'Es correcto, ganaste: {self.recompensa}')
                jugador.ganar_vida(1)
                return True
            else:
                jugador.perder_vida(1/4)
                print(f'Incorrecto, a este paso no llegaras a mate II... Pierdes un cuarto de vida. \nVidas actuales: {jugador.vidas}')






