from tabulate import tabulate
import requests
import datos

url = "https://api.mercadolibre.com/users/me"
headers = {
    "Authorization": f"Bearer {datos.ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)

# Verificar el código de respuesta
if response.status_code == 200:
    data = response.json()
    # Aquí puedes procesar la respuesta como desees
    print(data)
else:
    print("Error en la solicitud:", response.status_code)


