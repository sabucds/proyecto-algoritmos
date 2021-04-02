from jugador import *
from juego import *
from funciones_proyecto import ingresar_opcion
import random

class FinalBoss(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
    
    def imprimir_tablero(self, tablero):
        linea = 1
        print()
        for fila in tablero:
            print("  ", end='')
            print(" | ".join(fila))
            if linea < 3:
                print('+---+---+---+')
                linea += 1
        print()

    
    def poner_pieza(self, letra, tablero, mov):
        if mov in range(1, 4):
            tablero[0][mov-1] = letra
        elif mov in range(4,7):
            tablero[1][mov-4] = letra
        else:
            tablero[2][mov-7] = letra
        self.imprimir_tablero(tablero)


    def ganador(self, tablero):
        for i, fila in enumerate(tablero):
            if (tablero[i][0] == tablero[i][1]) and (tablero[i][1] == tablero[i][2]) and tablero[i][0] in ('X', 'O'):
                if tablero[i][0] == 'X':
                    return 'X'
                else:
                    return 'O'
            for ii, espacio in enumerate(fila):
                if (tablero[0][ii] == tablero[1][ii]) and (tablero[1][ii] == tablero[2][ii]) and tablero[0][ii] in ('X', 'O'):
                    if tablero[0][ii] == 'X':
                        return 'X'
                    else:
                        return 'O'
                elif ((tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]) or (tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0])) and tablero[1][1] in ('X', 'O'):
                    if tablero[1][1] == 'X':
                        return 'X'
                    else:
                        return 'O'
        return False

    def elegir_random(self, tablero, condicion=False):
        mov_posibles = []
        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                if condicion:
                    if espacio == ' ' and (i,ii) in condicion:
                        if i == 0:
                            mov_posibles.append(ii+1)
                        elif i == 1:
                            mov_posibles.append(ii+1+3)
                        elif i == 2:
                            mov_posibles.append(ii+1+6)
                else:
                    if espacio == ' ':
                        if i == 0:
                            mov_posibles.append(ii+1)
                        elif i == 1:
                            mov_posibles.append(ii+1+3)
                        else:
                            mov_posibles.append(ii+1+6)
        if condicion and len(mov_posibles)>0:
            return random.choice(mov_posibles)
        if condicion and len(mov_posibles) == 0:
            return False
        if not condicion:
            return mov_posibles
        
    
    def buscar_jugada(self, tablero, letra):
        mov = False
        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                try:
                    if tablero[i][ii] == letra and (tablero[i+1][ii] == ' ' or tablero[i][ii+1] == ' ' or tablero[i+1][ii+1] == ' '):
                        mov = self.elegir_random(tablero, [(i+1, ii), (i, ii+1), (i+1, ii+1)])
                        return mov

                    elif tablero[i][ii] == letra and (tablero[i-1][ii] == ' ' or tablero[i][ii-1] == ' ' or tablero[i-1][ii-1] == ' '):
                        mov = self.elegir_random(tablero, [(i-1, ii), (i, ii-1), (i-1, ii-1)])
                        return mov

                except:
                    pass
        return mov

    def jugar_o_tapar(self, tablero, letra):
        mov = False
        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                try:
                    if tablero[i][ii] == tablero[i+1][ii+1] and tablero[i][ii] == letra:
                        print('a')
                        return self.elegir_random(tablero, [(0, 0), (1, 1), (2, 2)])
                    
                    elif tablero[i][ii] == tablero[i+1][ii-1] and tablero[i][ii] == letra:
                        print('b')
                        return self.elegir_random(tablero, [(0, 2), (1, 1), (2, 0)])

                    elif tablero[i][ii] == tablero[i+1][ii] and tablero[i][ii] == letra:
                        print('c')
                        try:
                            if tablero[i-1][ii] == ' ':
                                posicion = (i-1, ii)
                        except:
                            if tablero[i+2][ii] == ' ':
                                posicion = (i+2, ii)
                        return self.elegir_random(tablero, [posicion])

                    elif tablero[i][ii] == tablero[i][ii+1] and tablero[i][ii] == letra:
                        print('d')
                        try:
                            if tablero[i][ii+2] == ' ':
                                posicion = (i, ii+2)
                        except:
                            if tablero[i][ii-1] == ' ':
                                posicion = (i, ii-1)
                        return self.elegir_random(tablero, [posicion])

                    if tablero[i][ii] == tablero[i+2][ii] and tablero[i+1][ii] == ' ':
                        posicion = (i+1, ii)
                        return self.elegir_random(tablero, [posicion])

                    if tablero[i][ii] == tablero[i][ii+2] and tablero[i][ii+1] == ' ':
                        posicion = (i, ii+1)
                        return self.elegir_random(tablero, [posicion])

                except:
                    pass
        return mov
    
    def ia_mov(self, tablero):
        mov_posibles = self.elegir_random(tablero)
        print(mov_posibles)

        if len(mov_posibles) == 8:
            if tablero[1][1] == ' ':
                mov = 5
            elif tablero[0][0] == ' ' or tablero[0][2] == ' ' or tablero[2][0] == ' ' or tablero[2][2] == ' ':
                mov = self.elegir_random(tablero, [(0,0), (0,2), (2,0), (2,2)])
        
        elif len(mov_posibles) == 6:
            mov = self.jugar_o_tapar(tablero, 'X')

        else:
            if self.jugar_o_tapar(tablero, 'O'):
                mov = self.jugar_o_tapar(tablero, 'O')

            else:
                mov = self.jugar_o_tapar(tablero, 'X')

        if not mov:
            mov = self.buscar_jugada(tablero, 'O')

        self.poner_pieza('O', tablero, mov)


    def jugador_mov(self, tablero):
        mov = ingresar_opcion('la posicion del tablero que deseas ocupar, un numero del 1 al 9', range(1,10))
        self.poner_pieza('X', tablero, mov)

    
    def juego(self, jugador):
        tablero = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.imprimir_tablero(tablero)
        while True:
            self.jugador_mov(tablero)
            print('Le toca a cobranzas')
            self.ia_mov(tablero)
            ganador = self.ganador(tablero)
            if ganador == 'X':
                print(f'Ganaste! lograste recuperar el disco duro')
                return True
            if ganador == 'O':
                jugador.perder_vida(1)
                print(f'Gano cobranzas, pierdes una vida. Vidas actuales: {jugador.vidas}')
                return False
