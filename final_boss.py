from jugador import *
from juego import *
from narrativas import *
from funciones_proyecto import ingresar_opcion, clear
import random
import time
from termcolor import colored

class FinalBoss(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
    
    def imprimir_tablero(self, tablero):
        print()
        linea = 1
        for fila in tablero:
            divi = 1
            print("  ", end='')
            for espacio in fila:
                if espacio == 'X':
                    print(colored(espacio, 'red', attrs=['bold']), end='')
                elif espacio == 'O':
                    print(colored(espacio, 'cyan', attrs=['bold']), end='')
                else:
                    print(espacio, end='')
                if divi < 3:
                    print(" | ", end='')
                    divi += 1
            print()
            if linea < 3:
                print('+---+---+---+')
                linea += 1


    def poner_pieza(self, letra, tablero, mov):
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


    def jugar_o_tapar(self, tablero, letra):
        mov = False
        for i, fila in enumerate(tablero):
            for ii, espacio in enumerate(fila):
                try:
                    if tablero[i][ii] == tablero[i+1][ii+1] and tablero[i][ii] == letra and tablero[i+2][ii+2] == ' ':
                        return self.elegir_random(tablero, [(0, 0), (1, 1), (2, 2)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii+1] and tablero[i][ii] == letra and tablero[i-1][ii-1] == ' ':
                        return self.elegir_random(tablero, [(0, 0), (1, 1), (2, 2)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii-1] and tablero[i][ii] == letra and tablero[i+2][ii-2] == ' ':
                        return self.elegir_random(tablero, [(0, 2), (1, 1), (2, 0)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii-1] and tablero[i][ii] == letra and tablero[i-1][ii+1] == ' ':
                        return self.elegir_random(tablero, [(0, 2), (1, 1), (2, 0)])
                except: pass

                try:
                    if tablero[i][ii] == tablero[i+1][ii] and tablero[i][ii] == letra and tablero[i+2][ii] == ' ':
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
        mov = False
        mov_posibles = self.elegir_random(tablero)

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
            mov = random.choice(mov_posibles)

        self.poner_pieza('O', tablero, mov)


    def jugador_mov(self, tablero):
        mov = ingresar_opcion('la posicion del tablero que deseas ocupar, un numero del 1 al 9', range(1,10))
        while not self.poner_pieza('X', tablero, mov):
            mov = ingresar_opcion('una posicion que no este ocupada', range(1,10))


    def juego(self, jugador, tiempo_inicio):
        tablero = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        print(colored(narrativa4, 'magenta', attrs=['bold']))

        print(colored(random.choice(dialogos_cobranzas), 'cyan'))

        time.sleep(3)
        self.imprimir_tablero(tablero)
        while True:
            print(divisor)
            self.jugador_mov(tablero)
            ganador = self.ganador(tablero)
            if ganador == 'X':
                print(f'Ganaste! Venciste a crobanzas, ahora vas a poner el disco duro en su lugar')
                time.sleep(1.5)
                clear()
                print(colored(narrativa5.format(jugador.avatar), 'magenta', attrs=['bold']))
                time.sleep(3.5)
                return True
            if ganador == 'empate':
                print('Hubo un empate')
                for r in self.requerimento:
                    jugador.guardar_objeto(r)
                return False

            print(divisor)
            print(colored('Le toca a cobranzas', 'magenta', attrs=['bold']))
            hablar = random.choice([True, False])
            if hablar:
                print(colored(random.choice(dialogos_cobranzas), 'cyan'))

            time.sleep(0.5)
            self.ia_mov(tablero)
            ganador = self.ganador(tablero)

            if ganador == 'O':
                jugador.perder_vida(1)
                print(f'Gano cobranzas, pierdes una vida. Vidas actuales: {jugador.vidas}')
                for r in self.requerimento:
                    jugador.guardar_objeto(r)
                return False
            
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break
