from juego import *
from jugador import *

class PreguntasPython(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, pregunta, respuesta, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.pregunta = pregunta  # str
        self.respuesta = respuesta  # str

    def juego(self, jugador):
        print(self.pregunta)
        frase = self.pregunta[self.pregunta.find('"'): self.pregunta.find('"', self.pregunta.find('"')+1)+1]
        
        if '50' in frase:
            respuesta = 50
            #SOLUCION: int(frase[frase.find('5'):frase.find('0')+1])
        else:
            respuesta = frase[::-1]
            #SOLUCION: frase[::-1]
        
        p = 0
        while True:
            codigo = input('Ingrese el codigo o "*" para ver una pista ==> ')
            try:
                if eval(codigo) == respuesta:
                    print(f'Correcto, ganaste: {self.recompensa}')
                    jugador.guardar_objeto(self.recompensa)
                    return True
            except: pass
            if codigo == "*":
                p = self.ver_pista_juego(jugador, p)
            else:
                jugador.perder_vida(1/2)
                print(f'Incorrecto, pierdes media vida. Vidas actuales: {jugador.vidas}')



