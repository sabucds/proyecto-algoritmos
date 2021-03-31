

class Juego():
    def __init__(self, nombre, recompensa, reglas, requerimento, pistas):
        self.nombre = nombre #str
        self.recompensa = recompensa #str
        self.reglas = reglas #str
        self.requerimento = requerimento #str
        self.pistas = pistas #lista

    def verificar_jugabilidad(self, inventario, juegos_terminados): #verifica si el juego se puede jugar con el requerimento y si ya lo jugo o no
        if type(self.requerimento) == list:
            if (self.requerimento[0].lower() in inventario) and (self.requerimento[1].lower() in inventario):
                if not (self.nombre in juegos_terminados):
                    return True
                else:
                    print('Ya jugaste este juego')
            else:
                print(f'No puedes jugar este juego, necesitas: {", ".join(self.requerimento)}')
        else:
            if (not self.requerimento or (self.requerimento.lower() in inventario)):
                if not (self.nombre in juegos_terminados):
                    return True
                else:
                    print('Ya jugaste este juego')
            else:
                print(f'No puedes jugar este juego, necesitas: {self.requerimento}')
    
    def ver_pista_juego(self, jugador, p):
        try:
            self.pistas[p]
            if jugador.usar_pista():
                print(self.pistas[p])
                p += 1
                return p
        except:
            print('Ya viste todas las pistas de este juego')

