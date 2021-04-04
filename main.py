from funciones_proyecto import *
from manejo_api import *
from jugando import *
import json
from narrativas import *
from termcolor import colored


def main():
    while True:
        data = lista_datos()
        print(divisor)
        inicio = '''Bienvenido
1-Crear nuevo usuario
2-Ingresar con usuario existente
3-Ver los records
4-Salir
'''

        if len(data) >0:
            print(inicio)
            opcion = ingresar_opcion('una opcion', ('1', '2', '3', '4'))
        else:
            print(inicio.replace('2-Ingresar con usuario existente', ''))
            opcion = ingresar_opcion('una opcion', ('1', '3', '4'))
        print(divisor)
        if opcion == '1':
            username = crear_usuario(data)
        elif opcion == '2':

            username = usuario_existente()
            while not username:
                print(divisor)
                print('Desea volver al menu principal? (S)i o (N)o')
                opcion = ingresar_opcion('S o N', ('s', 'n'))
                if opcion == 's': break
                username = usuario_existente()
            if opcion == 's': continue
        
        elif opcion == '3':
            clear()
            ver_records(data)
            continue

        else:
            clear()
            break

        print(divisor)
        print('''1-Comenzar nueva partida
2-Ver instrucciones del juego
''')

        opcion = ingresar_opcion('una opcion', ('1', '2', '3'))
        print(divisor)
        if opcion == '1':
            jugador = nueva_partida(username)
            comenzar(jugador)

        else:
            print(colored(instrucciones, 'cyan', attrs=['bold']))

main()
