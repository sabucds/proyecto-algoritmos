from termcolor import colored

class Jugador():
    def __init__(self, username, contrasena, edad, avatar, pistas, vidas, tiempo, dificultad):
        self.username = username
        self.contrasena = contrasena
        self.edad = edad #int
        self.avatar = avatar #str
        self.tiempo = [] #lista de diccionarios con dificultad de partida jugada, tiempo, si gano o perdio
        self.inventario = [] 
        self.pistas = pistas #int
        self.vidas = vidas #int
        self.tiempo = tiempo #int
        self.dificultad = dificultad

    def usar_pista(self): #gastar una pista en un juego
        if self.pistas > 0:
            self.pistas -= 1
            return True
        else:
            print(colored('No tienes mas pistas', 'magenta', attrs=['bold']))
            return False

    def guardar_objeto(self, objeto):  # guardar objeto en inventario
        self.inventario.append(objeto)

    def usar_objeto(self, objeto):  # usar un objeto guardado para desbloquear juego
        self.inventario.remove(objeto)
    
    def perder_vida(self, cant_vida): #restar vida perdida a la vida total
        if not self.vidas <= 0:
            self.vidas -= cant_vida
        

    def ganar_vida(self, cant_vida):  # sumar vida perdida a la vida total
        if not self.vidas <= 0:
            self.vidas += cant_vida
    
    






