import requests
import json
from cuarto import *
from escenarios import *


def get_data_api():
    try:
        x = requests.get('https://api-escapamet.vercel.app/')
        api = json.loads(x.text)
        return api
    except:
        print('No se pudo extraer los datos de la API')
        return []


api = get_data_api()

for i, dic in enumerate(api): # crea los objetos cuarto con los datos de la API
    if dic['name'] == 'Biblioteca':
        biblioteca = Cuarto(dic['name'], dic['objects'], biblioteca_escenario)
    elif dic['name'] == 'Laboratorio SL001':
        laboratorio_sl = Cuarto(dic['name'], dic['objects'], laboratorio_sl_escenario)
    elif dic['name'] == 'Plaza Rectorado':
        plaza_rectorado = Cuarto(dic['name'], dic['objects'], plaza_rectorado_escenario)
    elif dic['name'] == 'Pasillo Laboratorios ':
        pasillo_labs = Cuarto(dic['name'], dic['objects'], pasillo_labs_escenario)
    else:
        cuarto_servidores = Cuarto(dic['name'], dic['objects'], cuarto_servidores_escenario)

biblioteca.definir_posiciones(pasillo_labs, plaza_rectorado)
laboratorio_sl.definir_posiciones(cuarto_servidores, pasillo_labs)
plaza_rectorado.definir_posiciones(False, biblioteca)
pasillo_labs.definir_posiciones(False, biblioteca)
cuarto_servidores.definir_posiciones(False, laboratorio_sl)
