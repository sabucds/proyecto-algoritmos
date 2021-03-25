from funciones_proyecto import *
from manejo_api import *
import json


def main():
    while True:
        data = lista_datos()
        inicio = '''Bienvenido
1-Crear nuevo usuario
2-Ingresar con usuario existente
3-Salir'''
        if len(data) >0:
            print(inicio)
            opcion = ingresar_opcion('una opcion', ('1', '2', '3'))
        else:
            print(inicio.replace('2-Ingresar con usuario existente', ''))
            opcion = ingresar_opcion('una opcion', ('1', '3'))
        
        if opcion == '1':
            username = crear_usuario(data)
        elif opcion == '2':

            username = usuario_existente()
            while not username:
                print('Desea volver al menu principal? (S)i o (N)o')
                opcion = ingresar_opcion('S o N', ('s', 'n'))
                if opcion == 's': break
                username = usuario_existente()
            if opcion == 's': continue

        else:
            break
        
        print('''1-Comenzar nueva partida
2-Ver instrucciones del juego
3-Ver los records
''')
        opcion = ingresar_opcion('una opcion', ('1', '2', '3'))
        if opcion == '1':
            jugando = nueva_partida(username)
            comenzar(jugando, api)

        elif opcion=='2':
            pass
        else:
            pass



main()
