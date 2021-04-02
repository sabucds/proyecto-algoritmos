from juego import *
import random
import string
from termcolor import colored

class Sopa(Juego):
    def __init__(self, nombre, recompensa, reglas, requerimento, palabras, pistas):
        super().__init__(nombre, recompensa, reglas, requerimento, pistas)
        self.palabras = palabras #lista
        self.pistas = pistas  # lista
    
    def rellenar_espacios(self, sopa, alfabeto):
        for i, fila in enumerate(sopa):
            for ii, espacio in enumerate(fila):
                if espacio == 0:
                    sopa[i][ii] = random.choice(alfabeto)
        return sopa


    def diagonal(self, palabra, sopa, ubicaciones):
        while True:
            espacio_valido = True
            pendiente = random.choice([-1,1])

            if pendiente == -1:
                fila = random.randint(0, 14-len(palabra))
                columna = random.randint(0, 14-len(palabra))

                for i, letra in enumerate(list(palabra)):
                    if not sopa[i+fila][i+columna] == 0:
                        espacio_valido = False

                if espacio_valido:
                    for i, letra in enumerate(list(palabra)):
                        sopa[i+fila][i+columna] = letra
                        ubicaciones.append((i+fila, i+columna))
                    return sopa
            else:
                fila = random.randint(len(palabra), 14)
                columna = random.randint(0, 14-len(palabra))

                for i, letra in enumerate(list(palabra)):
                    if not sopa[fila-i][i+columna] == 0:
                        espacio_valido = False

                if espacio_valido:
                    for i, letra in enumerate(list(palabra)):
                        sopa[fila-i][i+columna] = letra
                        ubicaciones.append((fila-i, i+columna))
                    return sopa
    
    def vertical(self, palabra, sopa, ubicaciones):
        while True:
            espacio_valido = True
            fila = random.randint(0, 14-len(palabra))
            columna = random.randint(0, 14)
            for i, letra in enumerate(list(palabra)):
                if not sopa[i+fila][columna] == 0:
                    espacio_valido = False

            if espacio_valido:
                for i, letra in enumerate(list(palabra)):
                    sopa[i+fila][columna] = letra
                    ubicaciones.append((i+fila, columna))
                return sopa

    def horizontal(self, palabra, sopa, ubicaciones):
        while True:
            espacio_valido = True
            fila = random.randint(0, 14)
            columna = random.randint(0, 14-len(palabra))
            for i,letra in enumerate(list(palabra)):
                if not sopa[fila][i+columna] == 0:
                    espacio_valido = False

            if espacio_valido:
                for i, letra in enumerate(list(palabra)):
                    sopa[fila][i+columna] = letra
                    ubicaciones.append((fila, i+columna))
                return sopa


    def imprimir_sopa(self, sopa, palabras_encontradas_ubicacion=False):
        divisor = '+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'

        if not palabras_encontradas_ubicacion:
            for linea in sopa:
                print('\n', divisor)
                print(' | ', end='')
                for letra in linea:
                    print(letra.upper(), end=' | ')
            print("\n", divisor)

        else:
            color = 'red'
            for i,linea in enumerate(sopa):
                print('\n', divisor)
                print(' | ', end='')
                for ii,letra in enumerate(linea):
                    letra_ubicada = False
                    for ubicaciones in palabras_encontradas_ubicacion:
                        if (i,ii) in ubicaciones:
                            letra_ubicada = True
                    if letra_ubicada:
                        print(colored(letra, color), end=' | ')
                    else:
                        print(letra.upper(), end=' | ')
            print("\n", divisor)

            



    def juego(self, jugador):

        palabras_lista = [x for x in self.palabras]
        alfabeto = list(string.ascii_lowercase)
        p = 0
        palabras_encontradas = []
        ubicaciones = {}

        sopa = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        for i in range(len(palabras_lista)):
            palabra = random.choice(palabras_lista)
            palabras_lista.remove(palabra)
            posicion = random.randint(1,3)
            palabra_inversa = random.choice([True, False])

            ubicaciones[palabra] = []
            palabra_u = palabra

            if palabra_inversa:
                palabra = palabra[::-1]

            if posicion == 1:
                sopa = self.horizontal(palabra, sopa, ubicaciones[palabra_u])
            elif posicion == 2:
                sopa = self.vertical(palabra, sopa, ubicaciones[palabra_u])
            else:
                sopa = self.diagonal(palabra, sopa, ubicaciones[palabra_u])
        
        sopa = self.rellenar_espacios(sopa, alfabeto)

        self.imprimir_sopa(sopa)

        while True:
            respuesta = input('Ingrese una palabra o "*" para usar una pista ==> ').upper()

            if respuesta in self.palabras:
                palabras_encontradas.append(ubicaciones[respuesta])
                self.imprimir_sopa(sopa, palabras_encontradas)
                self.palabras.remove(respuesta)

                if len(self.palabras) == 0:
                    print(f'Acertaste todas las palabras, ganaste: {self.recompensa}')
                    jugador.ganar_vida(1)
                    return True
                else:
                    print(f'Es correcto, te faltan {len(self.palabras)}')

            elif respuesta == '*':
                p = self.ver_pista_juego(jugador, p)

            else:
                jugador.perder_vida(1/2)
                print(f'Incorrecto, pierdes media vida. Vidas actuales: {jugador.vidas}')
    



