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
            self.ecuacion = '๐งก+๐งก+๐งก=45 \n๐+๐+๐งก=23 \n๐+โฐ+โฐ=10 \nโฐ+๐+๐x๐งก=?'
            respuesta = '67'
        else:
            self.ecuacion = '๐ง+๐ง+๐ง=27 \n๐ง+๐+๐=19 \n๐+๐ฆ+๐ฆ=13 \n๐x๐ง-๐ฆ=?'
            respuesta = '41'
        
        print(self.ecuacion)
        while True:
            r = input('Ingrese la respuesta ==> ')
            if r.replace(' ','') == respuesta:
                print(f'Es correcto, ganaste: {self.recompensa}')
                print(colored(narrativa3, "magenta", attrs=['bold']))
                jugador.guardar_objeto(self.recompensa)
                return True
            else:
                jugador.perder_vida(1)
                print(f'Incorrecto, parece que el tรญtulo te queda muy grande, pierdes una vida. Vidas actuales: {jugador.vidas}')
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break


