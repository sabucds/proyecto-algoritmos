from jugador import *
from narrativas import *
from escenarios import *
from cuarto import *
from objeto import *
from manejo_api import *
import json 
import os
import time


def mover_cuarto(cuarto_actual, mov):  # moverse de un cuarto a otro (izquierda o derecha)
    if mov == 1:
        cuarto_actual = cuarto_actual.derecha
    elif mov == 2:
        cuarto_actual = cuarto_actual.izquierda
    return cuarto_actual

def tocar_objeto(cuarto_actual, objeto):  # tocar objeto para jugar
    objeto_tocado= Objeto(objeto['name'], objeto['position'], objeto['game'])


def en_juego(jugando, cuarto_actual):
    tiempo_inicio = time.time()
    cronometro = jugando.tiempo * 60
    tiempo_transcurrido = 0
    while tiempo_transcurrido < cronometro:
        tiempo_transcurrido = time.time() - tiempo_inicio
        print(cuarto_actual.escenario)
        try:
            menu = f'''---Menu de opciones---
1- Ir al cuarto de la derecha 
2- Ir al cuarto de la izquierda
3- Tocar {cuarto_actual.objetos[0]["name"]}
4- Tocar {cuarto_actual.objetos[1]["name"]}
5- Tocar {cuarto_actual.objetos[2]["name"]}
6- Ver mi tiempo
7- Pausa
''' 
        except:
            menu = f'''---Menu de opciones---
2- Ir al cuarto de la izquierda
3- Tocar {cuarto_actual.objetos[0]["name"]}
6- Ver mi tiempo
7- Pausa
'''

        if cuarto_actual.nombre == 'Plaza Rectorado' or cuarto_actual.nombre == 'Cuarto de Servidores ':
            menu = menu.replace('1- Ir al cuarto de la derecha', '')
            print(menu)
            opcion = ingresar_opcion('opcion', (2, 3, 4, 5, 6, 7))
        elif cuarto_actual.nombre == 'Pasillo Laboratorios ':
            print(menu)
            opcion = ingresar_opcion('opcion', (2, 3, 6, 7))
        else:
            print(menu)
            opcion = ingresar_opcion('opcion', (1, 2, 3, 4, 5, 6, 7))

        if opcion == 1:
            cuarto_actual = mover_cuarto(cuarto_actual, opcion)
        elif opcion == 2:
            cuarto_actual = mover_cuarto(cuarto_actual, opcion)
        elif opcion == 3:
            tocar_objeto(cuarto_actual, cuarto_actual.objetos[0])
        elif opcion == 4:
            tocar_objeto(cuarto_actual, cuarto_actual.objetos[1])
        elif opcion == 5:
            tocar_objeto(cuarto_actual, cuarto_actual.objetos[2])
        elif opcion == 6:
            if cronometro > 0:
                tiempo_transcurrido = time.time() - tiempo_inicio
                print(f'Te quedan {cronometro - int(tiempo_transcurrido) } segundos')
            else:
                print('Se te acabo el tiempo')
        else:
            print('''1-Reanudar
2-Salir del juego''')
            pausa_op = ingresar_opcion('una opcion', (1, 2)) 
            if pausa_op == 2: break
            tiempo_inicio = time.time() - tiempo_transcurrido


def comenzar(jugando, api): #

    cuarto_actual = biblioteca
    print(narrativa1.format(jugando.tiempo))
    reto = ingresar_opcion('(S)i o (N)o', ('s','n'))
    if reto == 's':
        print(narrativa2.format(jugando.avatar))
        en_juego(jugando, cuarto_actual)


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
            print(i,"-",k,v)
            i += 1
    dificultad = ingresar_opcion('una dificultad', ('1', '2', '3'))
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
                y = int(input(f'Ingrese {x}: '))
            else: 
                y = input(f'Ingrese {x}: ').lower()
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
            y = int(input(f'Seleccione {x}: '))
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
    y = input(f'Ingrese {x}: ')
    while not y.isnumeric():
        y = input('Error de ingreso, intente de nuevo: ')
    return y

def ingresar_alpha(x): # Validar un input de letras
    y = input(f'Ingrese {x}: ')
    while not x.isalpha():
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


