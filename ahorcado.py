from juego import *
from funciones_proyecto import *
from jugador import *

class Ahorcado(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, enunciado, palabra, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento)
        self.enunciado = enunciado #str
        self.palabra = palabra #str
        self.pistas = pistas #lista

    
    def juego(self, jugador):
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
            print(muneco[intentos])
            for l in formandose:
                print(l, end=' ')
            print()
            print('''1-Ingresar palabra o letra
2-Usar una pista''')
            op = ingresar_opcion('una opcion', (1,2))
            if op == 1:
                intento = ingresar_alpha('palabra o letra').lower()
                if intento == self.palabra.lower():
                    print(f'Es correcto, ganaste: {self.recompensa}')
                    jugador.guardar_objeto(self.recompensa)
                    return True
                elif intento in self.palabra.lower():
                    for i, letra in enumerate(palabra):
                        if letra == intento:
                            formandose[i] = formandose[i].replace('_', letra)
                            if not '_' in formandose:
                                print(f'completaste la palabra, ganaste: {self.recompensa}')
                                jugador.guardar_objeto(self.recompensa.lower())
                                return True
                else:
                    jugador.perder_vida(1/4)
                    print(f'Incorrecto, pierdes un cuarto de vida. Vidas actuales: {jugador.vidas}')
                    intentos += 1
            else:
                p = self.ver_pista_juego(jugador, p)


            print()
        print('Has perdido')
        return False




