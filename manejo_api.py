from urllib.request import urlopen
import json
import ssl

url = 'https://api-escapamet.vercel.app/'
coneccion = urlopen(url).read()
#datos = coneccion.decode()
js = json.loads(coneccion)

