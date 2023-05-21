"""
^ monitoreo endpoints api
~ disponibilidad:
verificar continuamente endpoints están disponibles, responden correctamente, herramientas de monitoreo si no está disponible o devuelve código d error, genera alerta para notificar
~ tiempo de respuesta:
medir tiempo d respuesta, establecer umbrales d tiempo d respuesta aceptables y generar alertas si tiempos respuesta superan esos umbrales.
~ rendimiento:
métricas de rendimiento: uso de recursos (CPU, memoria, ancho de banda), capacidad de manejar cargas d trabajo altas, identificar cuellos de botella, problemas de escalabilidad o limitaciones de recursos
~ errores:
monitorear registrar errores identificar problemas recurrentes inusuales. herramientas de monitoreo de registros para capturar analizar los registros generados por los endpoints
~ seguridad:
detectar intentos de acceso no autorizados, soluciones para monitorean el tráfico, detectan patrones sospechosos y bloquean o notifican sobre actividades maliciosas
~ cambios:
cambios en endpoints, monitorear su impacto. verificar si las solicitudes y respuestas siguen siendo compatibles, problemas de compatibilidad o degradación del rendimiento. pruebas de regresión automatizadas y monitorear las métricas relevantes para asegurarse de que cambios no introduzcan problemas inesperados

! endpoints están directamente relacionados con las URL
endpoints son las rutas que se envían solicitudes para realizar operaciones o acceder a recursos
Cada endpont representa una funcionalidad o recurso específico 
^ parámetros '&' parámetros '=' valor 
se denominan "parámetros de consulta" o "parámetros de URL"
mayoría d casos, no es importante el orden d los parámetros
El servidor de la API debería poder interpretar y procesarlos

^ "Schema Definitions"
describen estructura, formato de datos qc envían o reciben
define tipos de datos permitidos, propiedades, restricciones y relaciones entre datos
suelen seguir formato específico, JSON Schema o GraphQL Schema
contrato o acuerdo entre clientes y servidor
~ Validación de datos:
asegura cumplan estructura, restricciones especificadas. mantener integridad coherencia de datos
~ Generación de documentación:
generardo automáticamente, descripciones de los campos, tipos de datos esperados, reglas de validación y ejemplos
~ Generación de código:
es posible generar automáticamente código del lado del cliente o del servidor. acelera proceso d desarrollo y reduce la posibilidad de errores en implementación
~Flexibilidad y evolución:
definiciones de esquemas permiten realizar cambios de manera controlada y predecible. pueden ser versionados y gestionados de manera independiente, facilita la evolución de la API sin romper la compatibilidad

^ SDK
conjunto de herramientas, bibliotecas, documentación y ejemplos de código, compiladores, depuradores, emuladores, herramientas de prueba y más. que facilitan el desarrollo de aplicaciones para una plataforma específica. SDK está diseñado para trabajar con un sistema operativo, una plataforma de hardware o un entorno de desarrollo específico.

^ $ curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN'  https://api.mercadolibre.com/users/me
El signo "$" al inicio de una variable en la línea de comandos de Linux o Unix se utiliza para indicar que se trata de una variable de entorno. En el ejemplo que proporcionaste, "$ACCESS_TOKEN" es una variable de entorno que almacena un token de acceso.
Cuando se ejecuta el comando en la terminal, el sistema operativo reemplaza "$ACCESS_TOKEN" con el valor real almacenado en la variable de entorno antes de ejecutar la solicitud CURL. Por lo tanto, se debe quitar el signo "$" para que CURL interprete correctamente el valor de la variable de entorno y lo incluya en la solicitud 

^ SINTAXIS:
h = {'Authorization': f'Bearer {creds.ACCESS_TOKEN}'}
r = requests.get('https://api.mercadolibre.com/users/me', headers=h)
if r.status_code == 200:
    data = r.json()
    print(data)
else:
    print(r.status_code)

-----------------------
^ SINTAXIS:
h = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded'
}

d = {
    'grant_type': 'authorization_code',
    'client_id': '6726018526982529',
    'client_secret': 'niTvOEDg6qWC7ewHdycLyiQcK9p4lVk9',
    'code': 'TG-6468526423606c0001dfa01b-721673009',
    'redirect_uri': 'https://www.granados.ml/',
    'code_verifier': '$CODE_VERIFIER'
}

r = requests.post('https://api.mercadolibre.com/oauth/token', headers=h, data=d).json()
print(r)



^ CURL a URL

curl -X POST \
-H 'accept: application/json' \
-H 'content-type: application/x-www-form-urlencoded' \
https://api.mercadolibre.com/oauth/token' \
-d 'grant_type=authorization_code' \
-d 'client_id=6726018526982523' \
-d 'client_secret=niTvOEDg6qWC7ewHdycLyiQcK9p4lVkU' \
-d 'code=TG-6468526423606c0001dfa01b-721673001' \
-d 'redirect_uri=https://www.granados.ml/' \
-d 'code_verifier=$CODE_VERIFIER'

https://api.mercadolibre.com/oauth/token?grant_type=authorization_code&client_id=6726018526982523&client_secret=niTvOEDg6qWC7ewHdycLyiQcK9p4lVkU&code=TG-6468526423606c0001dfa01b-721673001&redirect_uri=https://www.granados.ml/&code_verifier=$CODE_VERIFIER

^ SINTAXIS

r = requests.get('https://api.mercadolibre.com/oauth/token?grant_type=authorization_code&client_id=6726018526982523&client_secret=niTvOEDg6qWC7ewHdycLyiQcK9p4lVkU&code=TG-6468526423606c0001dfa01b-721673001&redirect_uri=https://www.granados.ml/&code_verifier=$CODE_VERIFIER').json()
print(r)


^ carpeta "__pycache__" y archivo "datos.cpython-311.pyc"
generados x Python cuando c importa un módulo en el código
para optimizar tiempo d carga d los módulos

Cuando importas módulo "creds.py" en tu código
Python compila código fuente d módulo en código de byte optimizado
y lo guarda en archivo con extensión ".pyc" en carpeta "pycache"
c utiliza para acelerar importaciones posteriores d mismo módulo
evita compilar código fuente nuevamente, siempre y cuando código fuente d módulo no ha cambiado
seguros de ignorar, puedes eliminarlos, Python generará nuevamente cuando sea necesario

^ SINTAXIS CON USERID (tambien desde creds)

h = {'Authorization': f'Bearer {creds.ACCESS_TOKEN}'}
r = requests.get(f'https://api.mercadolibre.com/users/{creds.User_id}', headers=h).json()
print(r)

^ API puede no requerir token
~ Acceso público:
datos que no son confidenciales ni privados, como pronósticos del clima, información de transporte público o bases de datos de información pública
~ Límites de uso:
nivel de acceso gratuito limitado sin autenticación, pero imponen ciertos límites
~ Datos abiertos:
datos públicos, Organizaciones gubernamentales, instituciones académicas o proyectos comunitarios, promover transparencia e intercambio de información

^ SINTAXIS extraer data/json objects de json:
r = json.loads(requests.get('https://api.mercadolibre.com/sites/MLM/search?nickname=ONVE9085981').content)
for i,n in enumerate(r['results'], start=1):
    t = n['title']
    print(f'{i}. {t}')

^ SINTAXIS extraer data/json objects de json ANIDADOS:
r = json.loads(requests.get('https://api.mercadolibre.com/sites/MLM/search?nickname=ONVE9085981').content)
for i,n in enumerate(r['results'], start=1):
    t = n['seller_address']['state']['name']
    print(f'{i}. {t}')

^ SINTAXIS extraer data/json objects de json en arrays:
r = json.loads(requests.get('https://api.mercadolibre.com/sites/MLM/search?nickname=ONVE9085981').content)
for i,n in enumerate(r['results'], start=1):
    t = n['tags'][1]
    print(f'{i}. {t}')

^ SINTAXIS verificar cada anidación:
data = json.loads(json_data)
for result in data['results']:

    if result['seller_address'] is not None:
        seller_address = result['seller_address']

        if seller_address['state'] is not None:
            state = seller_address['state']

            if state['name'] is not None:
                city = state['name']
                print(city)
            else:
                print('La propiedad 'name' en 'state' es null')
        else:
            print('El objeto 'state' en 'seller_address' es null')
    else:
        print('El objeto 'seller_address' es null')

^ Sintaxis si un valor es igual a algo jeje:
r = json.loads(requests.get('https://api.mercadolibre.com/categories/MLM26287/attributes').content)
for i,n in enumerate(r, start=0):
    if 'tags' in n:
        tags = n['tags']
        if 'required' in tags:
            required = tags['required']
            if required == True:
                print(f'{i}. si requerido: {n['name']}')
            else:
                print(f'{i}. no requerido: {n['name']}')

^ Sintaxis a CSV:
import json, csv, requests
d = requests.get('https://api.mercadolibre.com/sites/MLM/shipping_methods').json()
c = list(d[0].keys())
with open('p.csv', 'w', newline='') as csv_f:
    x = csv.DictWriter(csv_f, fieldnames=c)
    x.writeheader()
    for p in d:
        x.writerow(p)

^ Sintaxis guardar JSON
r = requests.post('https://api.mercadolibre.com/sites/MLM/listing_types',headers=h,data=d).json()
with open('d.json', 'w') as a:
    json.dump(r, a) 

r = json.loads(requests.get('https://api.mercadolibre.com/sites/MLM/listing_types',headers=h,data=d).content)
with open('d.json', 'w') as a:
    json.dump(r, a)


^ En el caso de la solicitud con requests.get, la función response.json() ya realiza la decodificación del contenido de la respuesta HTTP en formato JSON y devuelve directamente un objeto Python. Por lo tanto, no es necesario utilizar json.loads() para cargar el JSON en este caso.

La función response.json() de la biblioteca requests realiza automáticamente la decodificación del contenido JSON de la respuesta HTTP y devuelve un objeto Python equivalente. Esta función internamente utiliza json.loads() para realizar la decodificación.

En resumen, cuando se utiliza response.json(), no es necesario utilizar json.loads() adicionalmente, ya que la función response.json() se encarga de convertir directamente la respuesta en JSON a un objeto Python.


---------------------------------------------------------------
en el siguiente json de una peticion como puedo iterar para que entre a "results", luego a "tags", luego a "seller_address", luego a "city" y mande "name" de cada uno de los objetos json 
{
  "site_id": "MLM",
  "results": [
    {
        "id": "MLM1629121764",
        "title": "Samsung Galaxy A03 64 Gb Rojo 4 Gb Ram",
        "tags": [
            "good_quality_picture",
            "good_quality_description 01"
            "seller_address": {
                "address_line": "",
                "state": {
                    "name": "San Luis Potosí"
                },
                "city": {
                    "name": "San Luis Potosí 1"
                }
            },
        ],  
    },
    {
        "id": "MLM1629121764",
        "title": "Samsung Galaxy A03 64 Gb Rojo 4 Gb Ram",
        "tags": [
            "good_quality_picture",
            "good_quality_description 01"
            "seller_address": {
                "address_line": "",
                "state": {
                    "name": "San Luis Potosí"
                },
                "city": {
                    "name": "San Luis Potosí 1"
                }
            },
        ],  
    },
    {
        "id": "MLM1629121764",
        "title": "Samsung Galaxy A03 64 Gb Rojo 4 Gb Ram",
        "tags": [
            "good_quality_picture",
            "good_quality_description 01"
            "seller_address": {
                "address_line": "",
                "state": {
                    "name": "San Luis Potosí"
                },
                "city": {
                    "name": "San Luis Potosí 1"
                }
            },
        ],  
    },
  ],
  "sort": {},
  "available_filters": []
}


en python request, en el siguiente json de una petición, como puedo iterar para saber si existe: "required" es igual a false, en cada anidación?:
[
  {
    "id": "BRAND",
    "name": "Marca",
    "tags": {
      "required": true
    },
  },
  {
    "id": "BRAND",
    "name": "Marca",
    "tags": {
      "required": false
    },
  },
  {
    "id": "BRAND",
    "name": "Marca",
    "tags": {
      "required": true
    },
  },
]

"""