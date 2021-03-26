from funciones_proyecto import *
from ahorcado import *
from jugador import *
from escenarios import *
from cuarto import *
from objeto import *


def llamar_juego(jugador, objeto_tocado, juegos_terminados):
    if objeto_tocado.juego['name'] == 'ahorcado':
        estructura = seleccion_random(objeto_tocado.juego['questions'])
        pistas = generar_lista(estructura)
        juego_en_curso = Ahorcado(
            objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], False, estructura['question'], estructura['answer'], pistas)

    if juego_en_curso.verificar_jugabilidad(jugador.inventario, juegos_terminados):
        if juego_en_curso.juego(jugador):
            juegos_terminados.append(juego_en_curso.nombre)
    else:
        print(f'No puedes jugar este juego porque no tienes {juego_en_curso.requerimento} o ya lo completaste')


def mover_cuarto(cuarto_actual, mov):  # moverse de un cuarto a otro (izquierda o derecha)
    if mov == 1:
        cuarto_actual = cuarto_actual.derecha
    elif mov == 2:
        cuarto_actual = cuarto_actual.izquierda
    return cuarto_actual


def tocar_objeto(jugador, cuarto_actual, objeto, juegos_terminados):  # tocar objeto para jugar
    objeto_tocado = Objeto(objeto['name'], objeto['position'], objeto['game'])
    llamar_juego(jugador, objeto_tocado, juegos_terminados)


def en_juego(jugador, cuarto_actual):
    juegos_terminados = []
    tiempo_inicio = time.time()
    cronometro = jugador.tiempo * 60
    tiempo_transcurrido = 0
    while tiempo_transcurrido < cronometro:
        tiempo_transcurrido = time.time() - tiempo_inicio
        print(cuarto_actual.escenario)
        try:
            menu = f'''Menu de opciones
{divisor}
1- Ir a {cuarto_actual.derecha.nombre}
2- Ir a {cuarto_actual.izquierda.nombre}
3- Tocar {cuarto_actual.objetos[0]["name"]}
4- Tocar {cuarto_actual.objetos[1]["name"]}
5- Tocar {cuarto_actual.objetos[2]["name"]}
6- Ver mi tiempo
7- Pausa
{divisor}'''
        except:
            menu = f'''Menu de opciones
{divisor}
2- Ir a {cuarto_actual.izquierda.nombre}
3- Tocar {cuarto_actual.objetos[0]["name"]}
6- Ver mi tiempo
7- Pausa
{divisor}'''

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
            tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[0], juegos_terminados)
        elif opcion == 4:
            tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[1], juegos_terminados)
        elif opcion == 5:
            tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[2], juegos_terminados)
        elif opcion == 6:
            if cronometro > 0:
                tiempo_transcurrido = time.time() - tiempo_inicio
                print(
                    f'Te quedan {cronometro - int(tiempo_transcurrido) } segundos')
            else:
                print('Se te acabo el tiempo')
        else:
            print('''1-Reanudar
2-Salir del juego''')
            pausa_op = ingresar_opcion('una opcion', (1, 2))
            if pausa_op == 2:
                break
            tiempo_inicio = time.time() - tiempo_transcurrido


def comenzar(jugador, api):

    cuarto_actual = biblioteca
    print(narrativa1.format(jugador.tiempo))
    reto = ingresar_opcion('(S)i o (N)o', ('s', 'n'))
    if reto == 's':
        print(narrativa2.format(jugador.avatar))
        en_juego(jugador, cuarto_actual)
