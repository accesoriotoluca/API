import requests
import json

url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()
#print(j.keys())
personajes = j['characters']
list_names_human = list()
list_names_other = list()

for personaje in personajes:
    req = requests.get(personaje)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
        list_names_human.append(name)
    else:
        list_names_other.append(name)

print(list_names_human)
print(list_names_other)