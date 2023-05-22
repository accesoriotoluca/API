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


^ El código 1 y el código 2 son diferentes en términos de la función que se está utilizando y el tipo de objeto al que se aplica.
En el código 1, json.loads('request'), se utiliza la función json.loads() para cargar una cadena JSON en un objeto de Python. json.loads() convierte una cadena JSON válida en un objeto de Python (por ejemplo, un diccionario o una lista) que se puede manipular en el código. En este caso, estás intentando cargar la cadena 'request' como un objeto JSON, pero 'request' no es una cadena JSON válida, por lo que este código generará un error.
En el código 2, 'request'.json(), se está intentando acceder a un método llamado json() en un objeto de cadena. Sin embargo, las cadenas en Python no tienen un método json(), por lo que este código generará un error.
En cuanto al código 3, json.dumps('data'), la función json.dumps() se utiliza para convertir un objeto de Python en una cadena JSON. En este caso, estás intentando convertir la cadena 'data' en una cadena JSON válida. Esto puede ser necesario si deseas enviar datos a través de una solicitud HTTP y necesitas que los datos estén en formato JSON. La función json.dumps() serializa el objeto de Python en una cadena JSON, que luego se puede enviar como parte de la carga útil de una solicitud HTTP.

^ El código 1 y el código 2 son diferentes formas de parsear datos JSON de una solicitud HTTP, mientras que el código 3 es utilizado para convertir datos en formato JSON a una cadena de texto.
json.loads(request): Este código asume que request es una cadena de texto que contiene datos en formato JSON. La función json.loads() convierte la cadena de texto JSON en un objeto Python. Por lo tanto, json.loads(request) tomaría una solicitud HTTP en formato JSON y la convertiría en un objeto Python que se puede manipular y acceder a sus datos.
request.json(): Este código se usa en el contexto de un objeto de solicitud HTTP en un framework o biblioteca específica. La llamada a request.json() intenta analizar los datos de la solicitud HTTP y devuelve un objeto Python con los datos JSON. Es una forma más conveniente y directa de obtener los datos JSON de una solicitud HTTP en comparación con json.loads().
En cuanto al código 3, json.dumps(data), se utiliza para convertir datos de Python en formato JSON. Toma un objeto Python (en este caso, la variable data) y lo convierte en una cadena de texto que representa los datos en formato JSON. Esta cadena JSON se puede enviar como parte del cuerpo de una solicitud HTTP o se puede almacenar en un archivo.
Es necesario utilizar el código 3 en la data del request cuando se necesita enviar datos en formato JSON como parte de una solicitud HTTP. Al convertir los datos en formato JSON utilizando json.dumps(), se garantiza que los datos se envíen correctamente en el formato esperado por el servidor o la API a la que se realiza la solicitud. Sin esta conversión, los datos podrían enviarse en un formato no reconocido por el servidor, lo que podría dar lugar a errores o respuestas incorrectas.

^ En los dos códigos que proporcionas, json.loads(requests.get('https://api.mercadolibre.com/sites/MLM/listing_types').content) y requests.get('https://api.mercadolibre.com/sites/MLM/listing_types').json(), ambos realizan una solicitud HTTP GET a la URL especificada y luego analizan la respuesta JSON recibida.
La razón por la cual ambos códigos dan la misma respuesta es que en realidad están haciendo prácticamente lo mismo, pero utilizando diferentes métodos proporcionados por la biblioteca requests y el módulo json. Veamos cada uno de ellos:
json.loads(requests.get('https://api.mercadolibre.com/sites/MLM/listing_types').content): En este código, estás utilizando la función requests.get() para realizar una solicitud HTTP GET a la URL proporcionada. requests.get() devuelve un objeto de respuesta que contiene el contenido de la respuesta HTTP. Luego, utilizas content para obtener el contenido de la respuesta en forma de una cadena de bytes y lo pasas a json.loads() para analizarlo como JSON. Esto devuelve un objeto Python que representa la respuesta JSON.
requests.get('https://api.mercadolibre.com/sites/MLM/listing_types').json(): En este código, también utilizas requests.get() para realizar una solicitud HTTP GET. En lugar de acceder al contenido de la respuesta directamente con content, utilizas el método .json() proporcionado por la biblioteca requests. Este método automáticamente analiza la respuesta HTTP como JSON y devuelve un objeto Python que representa la respuesta JSON.
En resumen, tanto json.loads(requests.get(...).content) como requests.get(...).json() logran el mismo resultado: analizar el contenido de la respuesta HTTP como JSON y devolver un objeto Python que representa ese JSON. La diferencia radica en la forma en que se accede al contenido de la respuesta y se realiza el análisis JSON.

^ Por que error
r = json.loads(requests.get('https://www.google.com.mx/').content) 
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xfa in position 8244: invalid start byte
r = requests.get('https://www.google.com.mx/').json() 
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
r = requests.get('https://www.google.com.mx/')
print(r.content)

de los anteriores 3 ejemplos por que los dos primeros tienen error y el tercero si funciona?
Los dos primeros ejemplos generan errores debido a la forma en que se intenta interpretar la respuesta de la solicitud HTTP de Google.
En el primer ejemplo, se utiliza la función json.loads() para intentar cargar la respuesta de la solicitud como un objeto JSON. Sin embargo, la respuesta de requests.get('https://www.google.com.mx/').content es una cadena de bytes, no un objeto JSON. Al intentar decodificar los bytes utilizando el codificador UTF-8, se encuentra un byte inválido en la posición 8244, lo que genera un error de decodificación.
En el segundo ejemplo, se intenta utilizar el método .json() de la respuesta de la solicitud para obtener directamente un objeto JSON. Sin embargo, la respuesta de requests.get('https://www.google.com.mx/') no contiene un contenido JSON válido. Esto se evidencia en la excepción JSONDecodeError que indica que se esperaba un valor en la línea 1, columna 1 (es decir, el contenido de la respuesta no comienza con un valor JSON válido).
En el tercer ejemplo, simplemente se imprime el contenido de la respuesta utilizando print(r.content). Esto imprimirá los bytes de la respuesta tal como se reciben, sin intentar interpretarlos como JSON. Por lo tanto, no se produce un error al intentar cargar un objeto JSON y se imprime el contenido de la respuesta sin problemas.

^ Checando errores
r = requests.get('https://www.google.com.mx/').json()
print(r)
raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
r = requests.get('https://www.google.com.mx/').json
print(r)
<bound method Response.json of <Response [200]>>
y en los anteriores 2 ejemplos, por que cuando se pone json() da error y cuando es .json sin paréntesis da un resultado?

En el primer ejemplo, al utilizar requests.get('https://www.google.com.mx/').json(), se intenta llamar al método .json() de la respuesta de la solicitud de requests.get(). Este método es responsable de decodificar el contenido de la respuesta en formato JSON y devolverlo como un objeto Python. Sin embargo, en este caso, la respuesta de requests.get('https://www.google.com.mx/') no es un contenido JSON válido, por lo que se produce una excepción JSONDecodeError indicando que no se puede decodificar el contenido esperado.
En el segundo ejemplo, se intenta imprimir el resultado de requests.get('https://www.google.com.mx/').json sin llamar realmente al método .json(). En lugar de devolver el resultado decodificado en formato JSON, se muestra <bound method Response.json of <Response [200]>>. Esto se debe a que .json sin paréntesis hace referencia al método .json en sí mismo, en lugar de llamarlo. Por lo tanto, en lugar de obtener el resultado deseado del contenido JSON, simplemente se obtiene una representación en cadena del método.
Para obtener el contenido JSON de una respuesta HTTP utilizando la biblioteca requests, debes llamar al método .json() con paréntesis, como se muestra en el primer ejemplo corregido. Esto asegura que el contenido de la respuesta se decodifique correctamente y se devuelva como un objeto Python que puedas utilizar.

^ Los parámetros que mencionas se refieren a objetos relacionados con una respuesta de una solicitud HTTP realizada mediante la biblioteca requests en Python. Aquí te explico brevemente qué información proporciona cada uno de ellos:
.reason: Este atributo proporciona la frase de estado asociada con el código de estado de la respuesta. Por ejemplo, si recibes una respuesta con el código de estado 200, el atributo .reason contendrá la cadena de texto "OK". Esto puede ser útil para obtener una descripción legible de la respuesta sin tener que analizar el código de estado directamente.
.history: Este atributo es una lista de objetos Response que rastrean las redirecciones que se produjeron durante la solicitud. Si una solicitud inicial fue redirigida, el atributo .history contendrá los objetos Response de las redirecciones anteriores en orden cronológico. Esto puede ser útil para seguir el historial de redirecciones y analizar cómo se llegó a la respuesta final.
.elapsed: Este atributo proporciona el tiempo transcurrido entre el envío de la solicitud y la recepción de la respuesta. Devuelve un objeto timedelta que representa la duración en segundos y microsegundos. Puedes acceder a diferentes propiedades de este objeto, como .seconds o .microseconds, para obtener más información sobre el tiempo transcurrido.
Es importante destacar que estos atributos están disponibles en la biblioteca requests de Python y son específicos para el manejo de solicitudes y respuestas HTTP en ese contexto. Otros lenguajes o bibliotecas pueden tener estructuras de datos similares pero con nombres o implementaciones diferentes.

^ Los resultados de print(response.json()), print(response.text), y print(response.content) representan diferentes formas de acceder y visualizar la respuesta de una solicitud HTTP en Python utilizando la biblioteca Requests.
response.json() intenta analizar la respuesta de la solicitud como JSON y devuelve un objeto Python correspondiente. Si la respuesta no se puede analizar como JSON, se generará una excepción.
Este método es útil cuando se espera que la respuesta de la solicitud sea un objeto JSON y se desea acceder a los datos de forma estructurada en Python.
response.text devuelve el contenido de la respuesta de la solicitud como una cadena de texto.
Este método es útil para obtener el contenido de la respuesta en su forma original, sin procesar. Puede contener texto, HTML, JSON u otros formatos, dependiendo de la respuesta del servidor.
response.content devuelve el contenido de la respuesta de la solicitud en forma de bytes.
Este método es útil cuando se necesita acceder al contenido de la respuesta en su forma binaria, como cuando se descargan archivos u otros datos que no son texto plano.
En el código que proporcionaste, response es el objeto de respuesta devuelto por la solicitud HTTP GET realizada con requests.request. Puedes utilizar cualquiera de los métodos mencionados (response.json(), response.text o response.content) para acceder y visualizar la respuesta de la solicitud de acuerdo a tus necesidades.








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