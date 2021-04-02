from termcolor import colored

class Juego():
    def __init__(self, nombre, recompensa, reglas, requerimento, pistas):
        self.nombre = nombre #str
        self.recompensa = recompensa #str
        self.reglas = reglas #str
        self.requerimento = requerimento #str
        self.pistas = pistas #lista

    def verificar_jugabilidad(self, inventario, juegos_terminados): #verifica si el juego se puede jugar con el requerimento y si ya lo jugo o no
        if (self.nombre in juegos_terminados):
            print(colored('Ya jugaste este juego', 'magenta', attrs=['bold']))
            return False

        if type(self.requerimento) == list:
            if (self.requerimento[0] in inventario) and (self.requerimento[1] in inventario):
                return True
            else:
                print(colored(f'No puedes jugar este juego, necesitas: {", ".join(self.requerimento)}', 'magenta', attrs=['bold']))
        else:
            if (not self.requerimento or (self.requerimento in inventario)):
                return True
            else:
                print(colored(f'No puedes jugar este juego, necesitas: {self.requerimento}', 'magenta', attrs=['bold']))
    
    def ver_pista_juego(self, jugador, p):
        try:
            self.pistas[p]
            if jugador.usar_pista():
                print(self.pistas[p])
                p += 1
                return p
        except:
            print(colored('Ya viste todas las pistas de este juego', 'magenta', attrs=['bold']))

