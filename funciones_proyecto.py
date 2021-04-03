from jugador import *
from narrativas import *
from escenarios import *
from cuarto import *
from objeto import *
import json 
import os
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def ver_records(data):
    print(divisor)
    top_5 = []
    mejores_tiempos = []

    for i, dic in enumerate(data):
        if data[i].get('records'):
            data[i]['records'] = sorted(dic['records'], key=lambda k: k['tiempo'])[0]
        else:
            data.pop(i)
    data = sorted(data, key = lambda x: x['records']['tiempo'])
    for i in range(5):
        try:
            top_5.append(data[i])
        except: pass
    
    print(colored('TOP 5 MEJORES JUGADORES\n', 'grey', 'on_white'))
    for i,juga in enumerate(top_5):
        mejores_tiempos.append(int(juga['records']['tiempo']))
        print(colored(str(i+1) + '- Usuario: '+ juga['username']+ '\nMejor tiempo: '+ str(int(juga['records']['tiempo']//60)) + ':' + str(int(juga['records']['tiempo']%60)) + '\nDificultad: '+ juga['records']['dificultad'], 'cyan', attrs=['bold']))
        print(colored('Cuartos mas jugados: ', 'cyan', attrs=['bold']))
        cuartos_visitados = dict(sorted(juga['records']['cuartos'].items(), key = lambda item: item[1], reverse=True))
        z = 0
        for cuarto, cant in cuartos_visitados.items():
            print(colored(f'{cuarto}- {cant} veces', 'cyan', attrs=['bold']))
            z += 1
            if z == 3:
                break
        print(divisor)
    print()
    print(colored('USUARIOS QUE MAS HAN JUGADO\n', 'grey', 'on_white'))

    data = lista_datos()
    usuarios = []
    cantidad_partidas = []

    for i, dic in enumerate(data):
        if dic.get('records'):
            data[i]['records'] = len(data[i]['records'])
        else:
            data.pop(i)
    data = sorted(data, key=lambda x: x['records'], reverse = True)
    for i in range(5):
        try:
            usuarios.append(data[i]['username'])
            cantidad_partidas.append(data[i]['records'])
            print(colored(str(i+1)+'- '+ data[i]['username']+ "\nCantidad de partidas completadas: "+ str(data[i]['records']), 'cyan', attrs=['bold']))
            print(divisor)
        except: pass
    
    op = input('Ingresa "*" para ver graficas de las estadisticas u otra tecla para salir ==> ')
    if op == '*':

        x = np.arange(len(usuarios))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, mejores_tiempos, width, label='Mejor tiempo')
        rects2 = ax.bar(x + width/2, cantidad_partidas, width, label='Cantidad de partidas ganadas')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Record')
        ax.set_title('Records de tiempo y partidas ganadas por cada jugador')
        ax.set_xticks(x)
        ax.set_xticklabels(usuarios)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        plt.show()

    else:
        clear()

def clear():
    return os.system('clear')

def generar_lista(dic): #genera una lista con las pistas de un diccionario
    lista = []
    for k,v in dic.items():
        if 'clue' in k:
            lista.append(v)
    return lista


def seleccion_random(algo): #hace una seleccion random de una lista
    return random.choice(algo)


def lista_datos(): # Mete una lista vacia en el archivo de datos en caso de que este en blanco
    with open('datos.json') as datos:
        try:
            data = json.load(datos)
        except:
            data = []
    return data

def buscar_dict_usuario(username): #busca un usuario en el archivo json y retorna su diccionario
    data = lista_datos()
    for dic in data:
        if dic['username'] == username:
            return dic

def nueva_partida(username):
    jugador = buscar_dict_usuario(username)
    i = 1
    with open('dificultad.json') as dificultad:
        dic_nivel = json.load(dificultad)
        for k, v in dic_nivel.items():
            print(f'{i}- {k.title()} ==> ', end='')
            for ke,va in v.items():
                print(f'{ke.title()}: {va}', end=' | ')
            print()
            i += 1
    print()
    dificultad = ingresar_opcion('una dificultad', ('1', '2', '3'))
    print(divisor)
    if dificultad == '1':
        dificultad = 'facil'
        pistas = dic_nivel['facil']['pistas']
        vidas = dic_nivel['facil']['vidas']
        tiempo = dic_nivel['facil']['tiempo']
    elif dificultad == '2':
        dificultad = 'intermedio'
        pistas = dic_nivel['intermedio']['pistas']
        vidas = dic_nivel['intermedio']['vidas']
        tiempo = dic_nivel['intermedio']['tiempo']
    else:
        dificultad = 'dificil'
        pistas = dic_nivel['dificil']['pistas']
        vidas = dic_nivel['dificil']['vidas']
        tiempo = dic_nivel['dificil']['tiempo']
    
    jugando = Jugador(jugador['username'], jugador['contrasena'], jugador['edad'], jugador['avatar'], pistas, vidas, tiempo, dificultad)

    return jugando

def ingresar_opcion(x, rango): #valida la seleccion de una opcion
    while True:
        try:
            if type(rango[0]) == int:
                y = int(input(f'Ingrese {x} ==> '))
            else: 
                y = input(f'Ingrese {x} ==> ').lower()
            if not y in rango:
                raise Exception
            break
        except:
            print('Error de ingreso')
    return (y)

def ingresar_index(x, rango):
    """[Valida que un numero ingresado sea un index de una lista]

    Args:
        x ([str]): [mensaje de lo que se pide]
        rango ([range]): [rango del len de la lista]

    Raises:
        Exception: [si el num no pertenece al rango, se le resta 1 porque al usuario se le muestra desde el 1]

    Returns:
        [int]: [el index]
    """
    while True:
        try:
            y = int(input(f'Seleccione {x} ==> '))
            if not y-1 in rango:
                raise Exception
            break
        except:
            print('Error de ingreso')
    return (y-1)


def mostrar_avatares():
    """[Muestra los avatares de la lista avatares que se encuentra en el archivo narrativas.py]
    """
    for i,avatar in enumerate(avatares):
        print(i+1, '-', avatar)



def validar_dato(dato): 
    """[valida si un dato ingresado ya existe (contrasena, usuario, etc)]

    Args:
        dato ([str]): [input del usuario]

    Returns:
        [bool]: [si se encuentra: True. Si no se encuentra: False]
    """

    data = lista_datos()
    for dic in data:
        for k, v in dic.items():
            if v == dato: 
                return True
    return False


def validar_contrasena(): #valida que la contrasena tenga al menos 8 caracteres con numeros y letras amyusculas y minusculas
    while True:
        contrasena = input('Ingrese contrasena. Debe contener al menos 8 caracteres con numeros, letras mayusculas y minusculas: ')
        if (len(contrasena) >= 8) and (not " " in contrasena):
            for digito in contrasena:
                for mayus in contrasena:
                    if mayus.isupper():
                        for minus in contrasena:
                            if minus.islower():
                                print('Contraseña ingresada correctamente')
                                return contrasena

        print("La contraseña elegida no es válida")

def ingresar_num_positivo(x): #valida numero positivo
    y = input(f'Ingrese {x} ==> ')
    while not y.isnumeric():
        y = input('Error de ingreso, intente de nuevo: ')
    return y

def ingresar_alpha(x): # Validar un input de letras
    y = input(f'Ingrese {x} ==> ')
    while not y.isalpha():
        y = input('Error de ingreso, intente de nuevo: ')
    return y

def crear_usuario(data):
    n_jugador = {}

    while True:
        username = input('Ingrese su nombre de usuario: ')
        if not validar_dato(username):
            break
        print('El usuario ya existe, ingrese otro')

    contrasena = validar_contrasena()
    edad = ingresar_num_positivo('su edad')
    mostrar_avatares()
    avatar = avatares[ingresar_index('un avatar: ', range(len(avatares)))]
    n_jugador['username'] = username
    n_jugador['contrasena'] = contrasena 
    n_jugador['edad'] = edad 
    n_jugador['avatar'] = avatar 
    data.append(n_jugador)
    with open('datos.json', 'w') as datos:
        json.dump(data, datos)
    return username


def usuario_existente():
    username = input('Ingrese su nombre de usuario: ')
    contrasena = input('Ingrese su contrasena: ')

    if not validar_dato(username) or not validar_dato(contrasena):
        print('El usuario o contrasena ingresado es incorrecto ')
        return False
    return username


