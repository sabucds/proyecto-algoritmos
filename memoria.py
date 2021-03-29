from juego import *
from funciones_proyecto import *


class Memoria(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, tablero, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.tablero = tablero
    
    def juego(self, jugador):
        print('COMO SE JUEGA: Se tiene un tablero 4x4 con cartas de memoria, ')
        self.tablero = [['😀', '🙄', '🤮', '🥰'], ['🤮', '😨', '🤓', '😷'], [
            '😨', '🤓', '🥰', '😷'], ['🤑', '🤑', '🙄', '😀']]
        tablero_juego = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], [
            'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]
        print(self.tablero)
        for r in tablero_juego:
            print(r)
        
        

