

class Juego():
    def __init__(self, nombre, recompensa, reglas, requerimento):
        self.nombre = nombre #str
        self.recompensa = recompensa #str
        self.reglas = reglas #str
        self.requerimento = requerimento #str

    def verificar_jugabilidad(self, inventario, juegos_terminados): #verifica si el juego se puede jugar con el requerimento y si ya lo jugo o no
        if (not self.requerimento or (self.requerimento in inventario)) and not (self.nombre in juegos_terminados):
            return True
        else:
            return False

