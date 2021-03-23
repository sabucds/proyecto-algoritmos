

class Juego():
    def __init__(self, nombre, recompensa, reglas, requerimento):
        self.nombre = nombre #str
        self.recompensa = recompensa #str
        self.reglas = reglas #str
        self.requerimento = requerimento #str

    def verificar_requerimento(self, inventario):
        if self.requerimento and (self.requerimento in inventario):
            return True
        else:
            return False
    
