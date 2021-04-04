from termcolor import colored
import json
import time

class Jugador():
    def __init__(self, username, contrasena, edad, avatar, pistas, vidas, tiempo, dificultad):
        self.username = username  # str
        self.contrasena = contrasena  # str
        self.edad = edad #int
        self.avatar = avatar #str
        self.inventario = [] 
        self.pistas = pistas #int
        self.vidas = vidas #int
        self.tiempo = tiempo #int
        self.dificultad = dificultad #str
        self.cuartos = {} #aca va cada cuarto con la cantidad de veces que ingreso al mismo

    def usar_pista(self): 
        """[gastar una pista en un juego]

        Returns:
            [bool]: [retorna true en caso de el jugador pueda usar una pista, False si ya gasto todas las pistas que tenia]
        """
        if self.pistas > 0:
            self.pistas -= 1
            return True
        else:
            print(colored('No tienes mas pistas', 'magenta', attrs=['bold']))
            return False

    def guardar_objeto(self, objeto):  
        """[guardar objeto en inventario]

        Args:
            objeto ([str]): [nombre de la recompensa adquirida]
        """
        self.inventario.append(objeto)

    def usar_objeto(self, objeto):  
        """[usar un objeto guardado para desbloquear juego]

        Args:
            objeto ([str]): [nombre del objeto usado]
        """
        if type(objeto) == list:
            for obj in objeto:
                self.inventario.remove(obj)
        else:
            self.inventario.remove(objeto)
    
    def perder_vida(self, cant_vida):
        """[restar vida perdida a la vida total]

        Args:
            cant_vida ([int]): [cantidad de vida a restar]
        """
        if not self.vidas <= 0:
            self.vidas -= cant_vida
        

    def ganar_vida(self, cant_vida):  
        """[sumar vida perdida a la vida total]

        Args:
            cant_vida ([int]): [cantidad de vida a sumar]
        """
        if not self.vidas <= 0:
            self.vidas += cant_vida
    
    def registrar_record(self):
        """[busca el usuario que esta jugando y mete su record en su diccionario en el archivo datos]
        """
        with open('dificultad.json') as dificultad:
            dic_nivel = json.load(dificultad)
        with open('datos.json') as datos:
            data = json.load(datos)
        
        for i,dic in enumerate(data):
            if dic['username'] == self.username:
                if not data[i].get('records'):
                    data[i]['records'] = []
                partida = {}
                partida['dificultad'] = self.dificultad
                partida['tiempo'] = self.tiempo
                partida['cuartos'] = self.cuartos
                data[i]['records'].append(partida)

        with open('datos.json', 'w') as datos:
            json.dump(data, datos)
    
    def actualizar_tiempo(self, tiempo_inicio):
        """[actualiza el tiempo transcurrido y verifica que aun no se haya acabado el tiempo del juego]

        Args:
            tiempo_inicio ([float]): [tiempo en que el usuario comenzo a jugar]

        Returns:
            [bool]: [retorna falso si el usuario se quedo sin vidas o tiempo, sino, retorna el tiempo actualizado]
        """
        tiempo_transcurrido = time.time() - tiempo_inicio
        if (tiempo_transcurrido >= (self.tiempo*60)) or (self.vidas == 0):
            return False
        else:
            return tiempo_transcurrido








