from funciones_proyecto import *
import json

def main():
    while True:
        data = lista_datos()
        print('''Bienvenido
1-Crear nuevo usuario
2-Ingresar con usuario existente
==>''')
        if len(data) >0:
            opcion = ingresar_opcion('una opcion', ('1', '2'))
        else:
            opcion = '1'
        
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
        
        print('''1-Comenzar nueva partida
2-Ver instrucciones del juego
3-Ver los records
''')
        opcion = ingresar_opcion('una opcion', ('1', '2', '3'))
        if opcion == '1':
            jugando = nueva_partida(username)
            en_juego(jugando)

        elif opcion=='2':
            pass
        else:
            pass



main()
