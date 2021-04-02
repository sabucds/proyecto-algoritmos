from jugador import *
from juego import *
import random
from narrativas import divisor

class PalabraMezclada(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, categoria, palabras, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.pregunta = pregunta  # str
        self.categoria = categoria  # str
        self.palabras = palabras # lista
    
    def juego(self, jugador):
        cambiadas = 0
        print(self.pregunta)
        print("Categoria:", self.categoria)
        palabras_mez = []
        for palabra in self.palabras:
            palabra_desordenada = random.sample(palabra, len(palabra))
            palabras_mez.append("".join(palabra_desordenada))
        
        while True:
            print(divisor)
            print('Palabras:', ", ".join(palabras_mez))

            p = input('Ingresa una palabra de forma ordenada ==> ').lower()
        
            if p in self.palabras:
                for ii,palabra in enumerate(self.palabras):
                    if p == palabra.lower():
                        palabras_mez[ii] = p
                        cambiadas += 1
                        
            else:
                jugador.perder_vida(1/2)
                print(f'Incorrecto, pierdes media vida. Vidas actuales: {jugador.vidas}')
            
            if cambiadas == len(palabras_mez):
                print(f'Ordenaste todas las palabras, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa)
                return True



