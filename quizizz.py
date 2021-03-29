from funciones_proyecto import *
from jugador import *
from juego import *
from narrativas import divisor


class Quizizz(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, opciones, respuesta_correcta, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)        
        self.pregunta = pregunta #str
        self.opciones = opciones #lista
        self.respuesta_correcta = respuesta_correcta #str

    
    def juego(self, jugador):
        self.opciones = random.sample(self.opciones, len(self.opciones))
        p = 0
        print(self.pregunta)
        for i, opcion in enumerate(self.opciones):
            print(i+1, '-', opcion, end=' / ')

        print()
        while True:
            print(divisor)
            
            r = ingresar_index('la opcion correcta o ingresa "5" para usar una pista', range(0,5))

            if r in range(0, 4) and self.opciones[r] == self.respuesta_correcta:
                print(f'Acertaste, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa.lower())
                return True

            elif r == 4:
                p = self.ver_pista_juego(jugador, p)

            else:
                jugador.perder_vida(1/2)
                print(f'Incorrecto, pierdes media vida. Vidas actuales: {jugador.vidas}')



