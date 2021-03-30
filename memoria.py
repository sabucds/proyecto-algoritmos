from juego import *
from funciones_proyecto import *
from narrativas import divisor


class Memoria(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, tablero, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.tablero = tablero
    
    def imprimir_tablero(self, tablero, numeros, letras):
        print(divisor)
        print(' '*3, end=' ')
        for num in numeros:
            print(num, end='  ')
        print()
        for i, r in enumerate(tablero):
            print(letras[i], end=' | ')
            for carta in r:
                print(carta, end=' ')
            print('|')
    
    def no_son_par(self, tablero_juego, carta_volteada1, carta_volteada2):
        for i, r in enumerate(self.tablero):
            for ii, c in enumerate(r):
                if c == carta_volteada1:
                    tablero_juego[i][ii] = 'X'
                if c == carta_volteada2:
                    tablero_juego[i][ii] = 'X'
        return tablero_juego

    def voltear_par(self, carta1, carta2, tablero_juego, numeros, letras):
        for i, r in enumerate(tablero_juego):
            for ind, c in enumerate(r):
                if i == letras.index(carta1[0]):
                    if ind == int(carta1[1])-1:
                        volteada1 = self.tablero[i][ind]
                        tablero_juego[i][ind] = volteada1
                
                if i == letras.index(carta2[0]):
                    if ind == int(carta2[1])-1:
                        volteada2 = self.tablero[i][ind]
                        tablero_juego[i][ind] = volteada2
        self.imprimir_tablero(tablero_juego, numeros, letras)
        return volteada1, volteada2

    def ingresar_carta(self, msg, letras, numeros):
        carta = input(f'{msg}').upper().replace(' ', '')
        while not (carta[0] in letras and carta[1] in numeros):
            carta = input('Error de ingreso. Ingresa el formato correcto ==> ').upper().replace(' ', '')
        return carta

    
    def juego(self, jugador):
        print('COMO SE JUEGA: Se tiene un tablero 4x4 con cartas de memoria, las columnas tienen letras asignadas y las filas numeros. \nPara voltear una carta debes colocar la letra seguido del numero (como en Excel). \nEjemplo: escribir "A1" para voltear la primera carta')
        self.tablero = [['😀', '🙄', '🤮', '🥰'], ['🤮', '😨', '🤓', '😷'], [
            '😨', '🤓', '🥰', '😷'], ['🤑', '🤑', '🙄', '😀']]
        tablero_juego = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], [
            'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]
        print(self.tablero)
        letras = ['A', 'B', 'C', 'D']
        numeros = ['1', '2', '3', '4']
        
        while True:
            gana = True
            self.imprimir_tablero(tablero_juego, numeros, letras)
            print()
            carta1 = self.ingresar_carta('Ingresa la carta a voltear ==> ', letras, numeros)
            carta2 = self.ingresar_carta('Ingresa la segunda carta a voltear ==> ', letras, numeros)
            if carta1 == carta2:
                print('Escoge dos cartas diferentes')
                continue

            carta_volteada1, carta_volteada2 = self.voltear_par(carta1,carta2, tablero_juego, numeros, letras)

            if not carta_volteada1 == carta_volteada2:
                tablero_juego = self.no_son_par(tablero_juego, carta_volteada1, carta_volteada2)
                jugador.perder_vida(1/4)
                print(f'\nIncorrecto, pierdes un cuarto de vida. Vidas actuales: {jugador.vidas}\n')

            for renglon in tablero_juego:
                if 'X' in renglon:
                    gana = False
            if gana:
                jugador.guardar_objeto(self.recompensa)
                print(f'Felicidades, ganaste: {self.recompensa}')
                return True





