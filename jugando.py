#!/usr/bin/env python
# -*- coding: latin-1 -*-
from funciones_proyecto import *
from manejo_api import *
from preguntas_matematica import *
from sopa import *
from palabra_mezclada import *
from preguntas_python import *
from escoge_numero import *
from final_boss import *
from quizizz import *
from adivinanzas import *
from ahorcado import *
from logica_booleana import *
from encuentra_logica import *
from criptograma import *
from memoria import *
from jugador import *
from escenarios import *
from cuarto import *
from objeto import *
import time
from termcolor import colored


def mover_cuarto(cuarto_actual, mov):  
    """[moverse de un cuarto a otro (izquierda o derecha)]

    Args:
        cuarto_actual ([objeto]): [objeto cuarto en el que se encuentra actualmente]
        mov ([int]): [un numero que indica si es a la derecha o a la izquierda]

    Returns:
        [objeto]: [el nuevo cuarto al que se mueve el usuario]
    """
    if mov == 1:
        cuarto_actual = cuarto_actual.derecha
    elif mov == 2:
        cuarto_actual = cuarto_actual.izquierda
    return cuarto_actual


def llamar_juego(jugador, cuarto_actual, objeto_tocado, juegos_terminados, tiempo_inicio):
    """[crea el objeto juego dependiendo del objeto que toco el usuario, verifica si el usuario lo puede jugar y llama al juego]

    Args:
        jugador ([objeto]): [jugador]
        cuarto_actual ([objeto]): [el cuarto en el que se encuentra]
        objeto_tocado ([objeto]): [el objeto tocado por el usuario]
        juegos_terminados ([list]): [lista de juegos que ya jugo el usuario]
        tiempo_inicio ([float]): [tiempo en el que el usuario comenzo a jugar]

    Returns:
        [bool]: [retorna falso si el usuario decide no usar el objeto requerido para iniciar el juego]
    """
    print(divisor)
    estructura = seleccion_random(objeto_tocado.juego['questions'])
    try:
        pistas = generar_lista(estructura)
    except:
        pistas = []

    if objeto_tocado.juego['name'] == 'ahorcado':
        juego_en_curso = Ahorcado(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['answer'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Preguntas matemáticas':
        juego_en_curso = PreguntasMate(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['answer'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Quizizz Cultura Unimetana':
        juego_en_curso = Quizizz(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], [v for k, v in estructura.items() if 'answer' in k], estructura['correct_answer'], pistas)
    
    elif objeto_tocado.juego['name'] == 'memoria con emojis':
        juego_en_curso = Memoria(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Lógica Booleana':
        juego_en_curso = LogicaBooleana(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['answer'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Criptograma':
        juego_en_curso = Criptograma(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['desplazamiento'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Encuentra la lógica y resuelve':
        juego_en_curso = EncuentraLogica(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura, pistas)
    
    elif objeto_tocado.juego['name'] == 'Preguntas sobre python':
        juego_en_curso = PreguntasPython(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['answer'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Adivinanzas':
        juego_en_curso = Adivinanzas(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['answers'], pistas)
    
    elif objeto_tocado.juego['name'] == 'Palabra mezclada':
        juego_en_curso = PalabraMezclada(objeto_tocado.juego['name'], objeto_tocado.juego['award'],objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['category'], estructura['words'], pistas)
    
    elif objeto_tocado.juego['name'] == 'escoge un número entre':
        juego_en_curso = EscogeNumero(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], estructura['question'], estructura['answer'], pistas)
    
    elif objeto_tocado.juego['name'] == 'sopa_letras':
        juego_en_curso = Sopa(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], [v.upper() for k, v in estructura.items() if 'answer' in k], pistas)
    
    else:
        juego_en_curso = FinalBoss(objeto_tocado.juego['name'], objeto_tocado.juego['award'], objeto_tocado.juego['rules'], objeto_tocado.juego['requirement'], pistas)

    try:
        print(colored(objeto_tocado.juego['message_requirement'], 'magenta', attrs=['bold']))
        print()
    except:
        pass 

    if juego_en_curso.verificar_jugabilidad(jugador, juegos_terminados):
        if juego_en_curso.requerimento:
            if not juego_en_curso.nombre == 'Adivinanzas': 
                # Pregunta si quieres usar el objeto necesario para jugar. En el caso de Adivinanzas no muestro el mensaje porque yo cree un un mensaje especial para este juego
                print(colored(f'Tienes {juego_en_curso.requerimento} en tu inventario. Deseas usarlo?', 'magenta', attrs=['bold']))
                r = ingresar_opcion('(S)i o (N)o', ('s','n'))
                print()
                if r == 's':
                    jugador.usar_objeto(juego_en_curso.requerimento)
                else:
                    return False
            
        print(colored('Regla: ' + juego_en_curso.reglas, 'magenta', attrs=['bold']))
        print()
        if juego_en_curso.juego(jugador, tiempo_inicio):
            juegos_terminados.append(juego_en_curso.nombre)
            
    print(divisor)
    time.sleep(2)
    

def tocar_objeto(jugador, cuarto_actual, objeto, juegos_terminados, tiempo_inicio):  
    """[tocar objeto para jugar. Valida si el juego que se completo es el del pasillo de los labs para moverte a el laboratorio de una vez]

    Args:
        jugador ([objeto]): [description]
        cuarto_actual ([objeto]): [description]
        objeto ([dict]): [diccionario del objeto escogido por el usuario (diccionario que se estrajo de la API)]
        juegos_terminados ([list]): [lista de juegos ganados]
        tiempo_inicio ([float]): [tiempo real en el que el jugador comenzo a jugar]

    Returns:
        [objeto]: [retorna el objeto cuarto en el que se situa el usuario]
    """
    objeto_tocado = Objeto(objeto['name'], objeto['position'], objeto['game'])
    llamar_juego(jugador, cuarto_actual, objeto_tocado, juegos_terminados, tiempo_inicio)

    if 'Lógica Booleana' in juegos_terminados and objeto_tocado.juego['name'] == 'Lógica Booleana':
        cuarto_actual = mover_cuarto(cuarto_actual, 1)
    return cuarto_actual


def en_juego(jugador, cuarto_actual):
    """[aca se imprime el cuarto junto con el menu, se actualiza el tiempo transcurrido y comprueba si el usuario gano todos los juegos para registrar el record]

    Args:
        jugador ([objeto]): [objeto jugador]
        cuarto_actual ([objeto]): [objeto cuarto actual]
    """

    juegos_terminados = []
    tiempo_inicio = time.time()
    cronometro = jugador.tiempo * 60
    tiempo_transcurrido = True
    while tiempo_transcurrido:
        tiempo_transcurrido = jugador.actualizar_tiempo(tiempo_inicio)

        if len(juegos_terminados) == 13:
            jugador.tiempo = tiempo_transcurrido
            jugador.registrar_record()
            print(colored(f'Tu record de {int(tiempo_transcurrido//60)}:{int(tiempo_transcurrido%60)} se ha registrado correctamente', 'magenta', attrs=['bold']))
            break
            
        print(colored(cuarto_actual.escenario.format(jugador.vidas, jugador.pistas, (cronometro - int(tiempo_transcurrido))//60, (cronometro - int(tiempo_transcurrido)) % 60), 'cyan', attrs=['bold']))
        try:
            jugador.cuartos[cuarto_actual.nombre] += 1
        except:
            jugador.cuartos[cuarto_actual.nombre] = 1

        menu = '''Menu de opciones
1- Ir a {}
2- Ir a {}
3- Tocar {}
4- Tocar {}
5- Tocar {}
6- Ver mi inventario
7- Pausa
'''


        if cuarto_actual.nombre == 'Plaza Rectorado' or cuarto_actual.nombre == 'Cuarto de Servidores ':
            menu = menu.replace('1- Ir a {}', '')
            print(menu.format(cuarto_actual.izquierda.nombre, cuarto_actual.objetos[0]["name"], cuarto_actual.objetos[1]["name"], cuarto_actual.objetos[2]["name"]))
            opcion = ingresar_opcion('opcion', (2, 3, 4, 5, 6, 7))

        elif cuarto_actual.nombre == 'Pasillo Laboratorios ':
            if 'Lógica Booleana' in juegos_terminados:
                menu = menu.replace('4- Tocar {}', '').replace('5- Tocar {}', '').replace('3- Tocar {}', '')
                print(menu.format(
                    cuarto_actual.derecha.nombre, cuarto_actual.izquierda.nombre))
                opcion = ingresar_opcion('opcion', (1, 2, 6, 7))
            else:
                menu = menu.replace(
                    '1- Ir a {}', '').replace('4- Tocar {}', '').replace('5- Tocar {}', '')
                print(menu.format(cuarto_actual.izquierda.nombre, cuarto_actual.objetos[0]["name"]))
                opcion = ingresar_opcion('opcion', (2, 3, 6, 7))

        else:
            print(menu.format(cuarto_actual.derecha.nombre, cuarto_actual.izquierda.nombre, cuarto_actual.objetos[0]["name"], cuarto_actual.objetos[1]["name"], cuarto_actual.objetos[2]["name"]))
            opcion = ingresar_opcion('opcion', (1, 2, 3, 4, 5, 6, 7))

        clear()
        if opcion == 1:
            cuarto_actual = mover_cuarto(cuarto_actual, opcion)
        elif opcion == 2:
            cuarto_actual = mover_cuarto(cuarto_actual, opcion)
        elif opcion == 3:
            cuarto_actual = tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[0], juegos_terminados, tiempo_inicio)
        elif opcion == 4:
            cuarto_actual = tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[1], juegos_terminados, tiempo_inicio)
        elif opcion == 5:
            cuarto_actual = tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[2], juegos_terminados, tiempo_inicio)
        elif opcion == 6:
            print("Inventario: ",", ".join(jugador.inventario))
        else:
            tiempo_transcurrido = jugador.actualizar_tiempo(tiempo_inicio)
            print('''PAUSA
1-Reanudar
2-Salir del juego
''')
            pausa_op = ingresar_opcion('una opcion', (1, 2))
            if pausa_op == 2:
                break
            tiempo_inicio = time.time() - tiempo_transcurrido
    
        tiempo_transcurrido = jugador.actualizar_tiempo(tiempo_inicio)

    if not len(juegos_terminados) == 13 and (jugador.vidas <= 0 or not tiempo_transcurrido):
        print()
        print(colored('HAS PERDIDO','white', 'on_red'))
        print()
        time.sleep(2)
    print(colored('\nSaliendo...', 'magenta', attrs=['bold']))
    time.sleep(1.5)
    clear()
    

def comenzar(jugador):
    """[imprime la primera narrativa y valida que el usuario acepte el reto de jugar, sino vuelve al menu]

    Args:
        jugador ([objeto]): [objeto jugador]
    """
    cuarto_actual = biblioteca
    clear()
    print(colored(narrativa1.format(jugador.tiempo), 'magenta', attrs=['bold']))
    print()
    reto = ingresar_opcion('(S)i o (N)o', ('s', 'n'))
    print(divisor)
    if reto == 's':
        print(colored(narrativa2.format(jugador.avatar), 'magenta', attrs=['bold']))
        time.sleep(4)
        en_juego(jugador, cuarto_actual)
