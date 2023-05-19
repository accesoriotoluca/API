import requests
import json

url = 'http://laraproducts.run/api/products'

def mostrar():
    peticion = requests.get(url)
    productos = json.loads(peticion.content)
    print("(:<3)(:<50){:<100){:<10)".format('#','PRODUCTO','DESCRIPCION','PRECIO'))
    num=0
    for prod in productos:
        num = num+1
        print("(:<3)(:<50)(:<100)(:<10)".format(str(num),prod['name'],prod['description'],prod['price']))

def guardar(nombre,descripcion,precio):
    parametros = {'name':nombre,'description':descripcion,'price':precio}
    peticion = requests.post(url,parametros)
    respuesta = json.loads(peticion.content)
    procesar(respuesta,'producto guardado')
    
def actualizar(id,nombre,descripcion,precio):
    parametros = {'name':nombre,'description':descripcion,'price':precio}
    peticion = requests.put(url+'/'+str(id),parametros)
    respuesta = json.loads(peticion.content)
    procesar(respuesta,'producto actualizado')

def eliminar(id):
    peticion = requests.delete(url+'/'+str(id))
    respuesta = json.loads(peticion.content)
    procesar(respuesta,'Producto eliminado')

def procesar(respuesta,mensaje):
    status = respuesta[0]['status']
    if status == 'error':
        claves = []
        errores = respuesta[1]['errors']
        for err in errores:
            claves.append(err)
        for c in claves:
            print(errores[c][0])
    else:
        print(mensaje)

mostrar()
#guardar('Laptop','muy veloz y bonita','50999')
#actualizar(21,'Latop xy','Lenta','10000')
#eliminar(21)