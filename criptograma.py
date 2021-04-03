from juego import *
from jugador import *
import string
from narrativas import divisor


class Criptograma(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, frase, desplazamiento, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.frase = frase  # str
        self.desplazamiento = desplazamiento  # int
    
    def juego(self, jugador, tiempo_inicio):
        alfabeto = list(string.ascii_lowercase)
        alfabeto_desplazado = []
        frase_desplazada = list(self.frase.replace('Ã¡', 'a').lower())

        for i, x in enumerate(alfabeto):
            try:
                alfabeto_desplazado.append(alfabeto[i+self.desplazamiento])
            except:
                i = (self.desplazamiento+i) - (len(alfabeto))
                alfabeto_desplazado.append(alfabeto[i])

        print('Frase: ', end='')
        for i,letra in enumerate(list(self.frase.replace('Ã¡', 'a').lower())):
            try:
                ind = alfabeto.index(letra)
                frase_desplazada[i] = alfabeto_desplazado[ind]
            except:
                pass
        frase_desplazada = ''.join(frase_desplazada)
        print(frase_desplazada)
        print()
        print('Alfabeto desplazado:')
        for letra in alfabeto_desplazado:
            print(letra, end=' | ')
        print()
        print(divisor)
        print()
        print('Alfabeto original:')
        for letra in alfabeto:
            print(letra, end=' | ')
        print()
        print(divisor)

        while True:
            respuesta = input('Ingrese la frase intercambiando las letras desplazadas por las originales ==> ')
            if respuesta.lower() == self.frase.replace('Ã¡', 'a').lower():
                print(f'Es correcto, ganaste: {self.recompensa}')
                jugador.guardar_objeto(self.recompensa)
                return True
            else:
                jugador.perder_vida(1)
                print(f'Incorrecto, pierdes una vida. Vidas actuales: {jugador.vidas}')
            if not jugador.actualizar_tiempo(tiempo_inicio):
                break

