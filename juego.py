from termcolor import colored

class Juego():
    def __init__(self, nombre, recompensa, reglas, requerimento, pistas):
        self.nombre = nombre #str
        self.recompensa = recompensa #str
        self.reglas = reglas #str
        self.requerimento = requerimento #str
        self.pistas = pistas #lista

    def verificar_jugabilidad(self, jugador, juegos_terminados): #verifica si el juego se puede jugar con el requerimento y si ya lo jugo o no
        if (self.nombre in juegos_terminados):
            print(colored('Ya jugaste este juego', 'magenta', attrs=['bold']))
            return False
        
        if self.nombre == 'Juego Libre' and len(juegos_terminados) < 12:
            print(colored('Para desbloquear este juego necesitas un carnet y haber ganado los demas juegos', 'magenta', attrs=['bold']))
            return False

        if self.nombre == 'Adivinanzas' and 'contraseÃ±a' in jugador.inventario:
            c=input('Ingresa la contrasena que conseguiste ==> ')
            return True

        if type(self.requerimento) == list:
            try:
                if (self.requerimento[0] in jugador.inventario) and (self.requerimento[1] in jugador.inventario[jugador.inventario.index('Mensaje: Si estas gradudado puedes pisar el SamÃ¡n')]):
                    jugador.inventario[jugador.inventario.index('Mensaje: Si estas gradudado puedes pisar el SamÃ¡n')] = 'Mensaje'
                    return True
                else:
                    jugador.perder_vida(1)
                    print(colored('Pisaste el Saman!! Pierdes una vida', 'magenta', attrs=['bold']))
                    print(colored(f'No puedes jugar este juego, necesitas: {", ".join(self.requerimento)}', 'magenta', attrs=['bold']))
            except:
                jugador.perder_vida(1)
                print(colored('Pisaste el Saman!! Pierdes una vida', 'magenta', attrs=['bold']))
                print(colored(f'No puedes jugar este juego, necesitas: {", ".join(self.requerimento)}', 'magenta', attrs=['bold']))
        else:
            if (not self.requerimento or (self.requerimento in jugador.inventario)):
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

