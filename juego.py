

class Juego():
    def __init__(self, nombre, recompensa, reglas, requerimento, pistas):
        self.nombre = nombre #str
        self.recompensa = recompensa #str
        self.reglas = reglas #str
        self.requerimento = requerimento #str
        self.pistas = pistas #lista

    def verificar_jugabilidad(self, inventario, juegos_terminados): #verifica si el juego se puede jugar con el requerimento y si ya lo jugo o no
        if (not self.requerimento or (self.requerimento.lower() in inventario)) and not (self.nombre in juegos_terminados):
            return True
        else:
            return False
    
    def ver_pista_juego(self, jugador, p):
        try:
            self.pistas[p]
            if jugador.usar_pista():
                print(self.pistas[p])
                p += 1
                return p
        except:
            print('Ya viste todas las pistas de este juego')

