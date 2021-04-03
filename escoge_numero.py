from juego import *
from jugador import *
import random
from funciones_proyecto import ingresar_opcion


class EscogeNumero(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuesta, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.pregunta = pregunta  # str
        self.respuesta = respuesta # str
    
    def juego(self, jugador, tiempo_inicio):
        self.recompensa = 'Titulo Universitario'
        print(self.pregunta)
        numero = random.randint(1,15)
        pistas = self.pistas[0].split(', ')
        intentos = 0
        print(numero)

        while True:
            n = ingresar_opcion('un numero', range(1,16))
            if n == numero:
                print(f'Acertaste, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa)
                return True
            else:
                intentos += 1
                print(f'Incorrecto, llevas {intentos} intentos')
            
            pista = input('Ingresa "*" si quieres usar una pista u otra tecla para omitir ==>')
            if pista == "*":
                if n in range(numero-3, numero):
                    print(pistas[1])
                elif n in range(numero+1, numero+4):
                    print(pistas[0])
                elif n in range(1, numero-2):
                    print(pistas[2])
                elif n in range(numero+3, 15):
                    print(pistas[3])

            if intentos == 3:
                intentos = 0
                jugador.perder_vida(1/4)
                print(f'Fallaste 3 veces seguidas, pierdes un cuarto de vida. Vidas actuales: {jugador.vidas}')
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break



