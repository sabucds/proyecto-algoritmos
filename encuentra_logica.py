from jugador import *
from juego import *
from narrativas import *
from termcolor import colored

class EncuentraLogica(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, ecuacion, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.ecuacion = ecuacion  # str

    def juego(self, jugador, tiempo_inicio):
        if '45' in self.ecuacion:
            self.ecuacion = '🧡+🧡+🧡=45 \n🍌+🍌+🧡=23 \n🍌+⏰+⏰=10 \n⏰+🍌+🍌x🧡=?'
            respuesta = '67'
        else:
            self.ecuacion = '🐧+🐧+🐧=27 \n🐧+🐝+🐝=19 \n🐝+🐦+🐦=13 \n🐝x🐧-🐦=?'
            respuesta = '41'
        
        print(self.ecuacion)
        while True:
            r = input('Ingrese la respuesta ==> ')
            if r == respuesta:
                print(f'Es correcto, ganaste: {self.recompensa}')
                print(colored(narrativa3, "magenta", attrs=['bold']))
                jugador.guardar_objeto(self.recompensa)
                return True
            else:
                jugador.perder_vida(1)
                print(f'Incorrecto, parece que el título te queda muy grande, pierdes una vida. Vidas actuales: {jugador.vidas}')
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break


