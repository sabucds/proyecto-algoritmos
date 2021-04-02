from termcolor import colored
import json

class Jugador():
    def __init__(self, username, contrasena, edad, avatar, pistas, vidas, tiempo, dificultad):
        self.username = username
        self.contrasena = contrasena
        self.edad = edad #int
        self.avatar = avatar #str
        self.tiempo = tiempo #tiempo que tiene para jugar
        self.inventario = [] 
        self.pistas = pistas #int
        self.vidas = vidas #int
        self.tiempo = tiempo #int
        self.dificultad = dificultad
        self.cuartos = {} #aca va cada cuarto con la cantidad de veces que ingreso

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
        if type(objeto) == list:
            for obj in objeto:
                self.inventario.remove(obj)
        else:
            self.inventario.remove(objeto)
    
    def perder_vida(self, cant_vida): #restar vida perdida a la vida total
        if not self.vidas <= 0:
            self.vidas -= cant_vida
        

    def ganar_vida(self, cant_vida):  # sumar vida perdida a la vida total
        if not self.vidas <= 0:
            self.vidas += cant_vida
    
    def registrar_record(self):
        with open('dificultad.json') as dificultad:
            dic_nivel = json.load(dificultad)
        with open('datos.json') as datos:
            data = json.load(datos)
        
        for i,dic in enumerate(data):
            if dic['username'] == self.username:
                if not data[i].get('records'):
                    data[i]['records'] = []
                partida = {}
                print(data[i]['records'])
                partida['dificultad'] = self.dificultad
                partida['tiempo'] = self.tiempo
                partida['cuartos'] = self.cuartos
                print(partida)
                data[i]['records'].append(partida)

        with open('datos.json', 'w') as datos:
            json.dump(data, datos)





