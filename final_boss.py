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
        print(mov)
        if mov in range(1, 4):
            if not tablero[0][mov-1] == ' ': 
                return False
            tablero[0][mov-1] = letra

        elif mov in range(4,7):
            if not tablero[1][mov-4] == ' ':
                return False
            tablero[1][mov-4] = letra

        else:
            if not tablero[2][mov-7] == ' ':
                return False
            tablero[2][mov-7] = letra
        self.imprimir_tablero(tablero)
        return True


    def ganador(self, tablero):
        empate = True
        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                if espacio == ' ':
                    empate = False
                
                if (tablero[i][0] == tablero[i][1]) and (tablero[i][1] == tablero[i][2]) and tablero[i][0] in ('X', 'O'):
                    if tablero[i][0] == 'X':
                        return 'X'
                    else:
                        return 'O'
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
        if empate:
            return 'empate'
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

        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                try:
                    if tablero[i][ii] == letra and tablero[i+1][ii] == ' ':
                        mov = self.elegir_random(tablero, [(i+1, ii), (i, ii+1), (i+1, ii+1)])
                        return mov
                except: pass
                try:
                    if tablero[i][ii] == letra and tablero[i][ii+1] == ' ':
                        mov = self.elegir_random(tablero, [(i+1, ii), (i, ii+1), (i+1, ii+1)])
                        return mov
                except: pass

                try:
                    if tablero[i][ii] == letra and tablero[i+1][ii+1] == ' ':
                        mov = self.elegir_random(tablero, [(i+1, ii), (i, ii+1), (i+1, ii+1)])
                        return mov
                except: pass

                try:
                    if tablero[i][ii] == letra and tablero[i-1][ii] == ' ':
                        mov = self.elegir_random(tablero, [(i-1, ii), (i, ii-1), (i-1, ii-1)])
                        return mov
                except:
                    pass

                try:
                    if tablero[i][ii] == letra and tablero[i][ii-1] == ' ':
                        mov = self.elegir_random(tablero, [(i-1, ii), (i, ii-1), (i-1, ii-1)])
                        return mov
                except: pass

                try:
                    if tablero[i][ii] == letra and tablero[i-1][ii-1] == ' ':
                        mov = self.elegir_random(tablero, [(i-1, ii), (i, ii-1), (i-1, ii-1)])
                        return mov
                except: pass


    def jugar_o_tapar(self, tablero, letra):
        mov = False
        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                try:
                    if tablero[i][ii] == tablero[i+1][ii+1] and tablero[i][ii] == letra and tablero[i+2][ii+2] == ' ':
                        print('a')
                        return self.elegir_random(tablero, [(0, 0), (1, 1), (2, 2)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii+1] and tablero[i][ii] == letra and tablero[i-1][ii-1] == ' ':
                        return self.elegir_random(tablero, [(0, 0), (1, 1), (2, 2)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii-1] and tablero[i][ii] == letra and tablero[i+2][ii-2] == ' ':
                        print('b')
                        return self.elegir_random(tablero, [(0, 2), (1, 1), (2, 0)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii-1] and tablero[i][ii] == letra and tablero[i-1][ii+1] == ' ':
                        return self.elegir_random(tablero, [(0, 2), (1, 1), (2, 0)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii] and tablero[i][ii] == letra and tablero[i+2][ii] == ' ':
                        print('c')
                        posicion = (i+2, ii)
                        return self.elegir_random(tablero, [posicion])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii] and tablero[i][ii] == letra and tablero[i-1][ii] == ' ':
                        posicion = (i-1, ii)
                        return self.elegir_random(tablero, [posicion])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i][ii+1] and tablero[i][ii] == letra and tablero[i][ii+2] == ' ':
                        print('d')
                        posicion = (i, ii+2)
                        return self.elegir_random(tablero, [posicion])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i][ii+1] and tablero[i][ii] == letra and tablero[i][ii-1] == ' ':
                        posicion = (i, ii-1)
                        return self.elegir_random(tablero, [posicion])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+2][ii] and tablero[i+1][ii] == ' ' and tablero[i][ii] == letra:
                        posicion = (i+1, ii)
                        return self.elegir_random(tablero, [posicion])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i][ii+2] and tablero[i][ii+1] == ' ' and tablero[i][ii] == letra:
                        posicion = (i, ii+1)
                        return self.elegir_random(tablero, [posicion])
                except: pass
                
                try:
                    if tablero[i][ii] == tablero[i+2][ii+2] and tablero[i][ii] == letra and tablero[i+1][ii+1] == ' ':
                        posicion = (i+1, ii+1)
                        return self.elegir_random(tablero, [posicion])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+2][ii-2] and tablero[i][ii] == letra and tablero[i+1][ii+1] == ' ':
                        posicion = (i+1, ii-1)
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
                j = random.randint(1,2)
                if j == 1:
                    mov = self.jugar_o_tapar(tablero, 'X')

        if not mov:
            print('hola')
            mov = self.buscar_jugada(tablero, 'O')

        self.poner_pieza('O', tablero, mov)


    def jugador_mov(self, tablero):
        mov = ingresar_opcion('la posicion del tablero que deseas ocupar, un numero del 1 al 9', range(1,10))
        while not self.poner_pieza('X', tablero, mov):
            mov = ingresar_opcion('una posicion que no este ocupada', range(1,10))

    
    def juego(self, jugador):
        tablero = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.imprimir_tablero(tablero)
        while True:
            self.jugador_mov(tablero)
            ganador = self.ganador(tablero)
            if ganador == 'X':
                print(f'Ganaste! lograste recuperar el disco duro')
                return True
            if ganador == 'empate':
                print('Hubo un empate')
                return False

            print('Le toca a cobranzas')
            self.ia_mov(tablero)
            ganador = self.ganador(tablero)

            if ganador == 'O':
                jugador.perder_vida(1)
                print(f'Gano cobranzas, pierdes una vida. Vidas actuales: {jugador.vidas}')
                return False
