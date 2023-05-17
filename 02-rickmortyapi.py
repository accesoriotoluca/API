import requests
import json

#print(j.keys())

i = 1
while i < 11:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i)
    r = requests.get(url)
    j = r.json()
    name = j['name']
    status = j['status']
    print('El personaje {} tiene status: {}'.format(name,status))
    i+=1