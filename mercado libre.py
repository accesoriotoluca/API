import requests, datos

h = {'Content-type': 'application/json','Authorization': f'Bearer {datos.ACCESS_TOKEN}'}
d = {'site_id=MLM',}

r = requests.request('POST','https://api.mercadolibre.com/users/test_user',headers=h,data=d).json()
print(r)


import requests
import json

url = "https://api.mercadolibre.com/users/test_user"

payload = json.dumps({
  "site_id": "MLM"
})

headers = {
  'Authorization': 'Bearer APP_USR-6726018526982523-052103-493143c22dd93117eef7c03b503d78be-721673001',
  'Content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
