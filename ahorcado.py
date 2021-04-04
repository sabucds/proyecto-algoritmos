from juego import *
from funciones_proyecto import *
from jugador import *
from narrativas import divisor

class Ahorcado(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, enunciado, palabra, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.enunciado = enunciado #str
        self.palabra = palabra #str

    
    def juego(self, jugador, tiempo_inicio):
        muneco = ['''
  +---+
  |   |
      |
      |
      |
      |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

        print(self.enunciado)
        palabra = [letra.lower() for letra in self.palabra]
        formandose = ['_' for letra in self.palabra]
        p = 0
        intentos = 0
        while intentos < 7:
            print(colored(muneco[intentos], 'green', attrs=['bold']))
            for l in formandose:
                print(l, end=' ')
            print()
            r = input('Ingresa la palabra, una letra  "*" si quieres usar una pista ==> ')
            if r == "*":
                p = self.ver_pista_juego(jugador, p)
            
            elif r == self.palabra.lower():
                print(f'Es correcto, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa)
                return True
            elif r in self.palabra.lower():
                for i, letra in enumerate(palabra):
                    if letra == r:
                        formandose[i] = formandose[i].replace('_', letra)
                        if not '_' in formandose:
                            print(
                                f'completaste la palabra, ganaste: {self.recompensa}')
                            jugador.guardar_objeto(self.recompensa)
                            return True
            else:
                jugador.perder_vida(1/4)
                print(
                    f'Incorrecto, pierdes un cuarto de vida. Vidas actuales: {jugador.vidas}')
                intentos += 1
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break


            print(divisor)
        if intentos >= 7:
            print('Has perdido')
        return False




