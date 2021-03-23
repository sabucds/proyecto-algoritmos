

class Cuarto():
    def __init__(self, nombre, objetos, escenario):
        self.nombre = nombre
        self.objetos = objetos
        self.escenario = escenario
        self.derecha = False 
        self.izquierda = False 

    def definir_posiciones(self, derecha, izquierda): # pone como atributos los objetos cuarto que conectan con el cuarto actual
        self.derecha = derecha
        self.izquierda = izquierda

