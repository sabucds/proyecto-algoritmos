import requests
import json


def get_data_api():
    try:
        x = requests.get('https://api-escapamet.vercel.app/')
        return json.loads(x.text)
    except:
        print('Error getting data from API')
        return []


def print_rooms_name(json):
    for i in json:
        print('You are in: ', i['name'])


def main():
    json = get_data_api()
    if len(json) > 0:
        print_rooms_name(json)
    print('\nTHE END')


main()
