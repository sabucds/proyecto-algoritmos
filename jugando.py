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


def mover_cuarto(cuarto_actual, mov):  # moverse de un cuarto a otro (izquierda o derecha)
    if mov == 1:
        cuarto_actual = cuarto_actual.derecha
    elif mov == 2:
        cuarto_actual = cuarto_actual.izquierda
    return cuarto_actual


def llamar_juego(jugador, cuarto_actual, objeto_tocado, juegos_terminados):
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
                print(colored(f'Tienes {juego_en_curso.requerimento} en tu inventario. Deseas usarlo?', 'magenta', attrs=['bold']))
                r = ingresar_opcion('(S)i o (N)o', ('s','n'))
                print()
                if r == 's':
                    jugador.usar_objeto(juego_en_curso.requerimento)
                else:
                    return False
            
        print(colored('Regla: ' + juego_en_curso.reglas, 'magenta', attrs=['bold']))
        print()
        if juego_en_curso.juego(jugador):
            juegos_terminados.append(juego_en_curso.nombre)
    print(divisor)

    time.sleep(2)
    

def tocar_objeto(jugador, cuarto_actual, objeto, juegos_terminados):  # tocar objeto para jugar

    objeto_tocado = Objeto(objeto['name'], objeto['position'], objeto['game'])
    llamar_juego(jugador, cuarto_actual, objeto_tocado, juegos_terminados)

    if 'Lógica Booleana' in juegos_terminados and objeto_tocado.juego['name'] == 'Lógica Booleana':
        cuarto_actual = mover_cuarto(cuarto_actual, 1)

    return cuarto_actual


def en_juego(jugador, cuarto_actual):
    juegos_terminados = []
    tiempo_inicio = time.time()
    cronometro = jugador.tiempo * 60
    tiempo_transcurrido = 0
    while tiempo_transcurrido < cronometro and jugador.vidas>0:
        tiempo_transcurrido = time.time() - tiempo_inicio
        if len(juegos_terminados) == 13:
            record = tiempo_transcurrido
            jugador.tiempo = record
            jugador.registrar_record()
            print(f'Tu record de {record} segundos se ha registrado correctamente')
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
            cuarto_actual = tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[0], juegos_terminados)
        elif opcion == 4:
            cuarto_actual = tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[1], juegos_terminados)
        elif opcion == 5:
            cuarto_actual = tocar_objeto(jugador, cuarto_actual, cuarto_actual.objetos[2], juegos_terminados)
        elif opcion == 6:
            print("Inventario: ",", ".join(jugador.inventario))
        else:
            tiempo_transcurrido = time.time() - tiempo_inicio
            print('''PAUSA
1-Reanudar
2-Salir del juego
''')
            pausa_op = ingresar_opcion('una opcion', (1, 2))
            if pausa_op == 2:
                break
            tiempo_inicio = time.time() - tiempo_transcurrido
    clear()
    

def comenzar(jugador, api):
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
