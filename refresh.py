import requests, datos

""" h = {
    'accept: application/json',
    'content-type: application/x-www-form-urlencoded'
}
!probar si funciona con este pedo de dump
d = json.dumps({
    'grant_type': 'refresh_token',
    'client_id': f'{datos.CLIENT_ID}',
    'client_secret': f'{datos.CLIENT_SECRET}',
    'refresh_token': f'{datos.REFRESH_TOKEN}'
})

r = requests.request('POST','https://api.mercadolibre.com/oauth/token',headers=h,data=d)
print(r.text) """


h = {'accept': 'application/json','content-type': 'application/x-www-form-urlencoded'}
d = 'grant_type=refresh_token&client_id='f'{datos.CLIENT_ID}''&client_secret='f'{datos.CLIENT_SECRET}''&refresh_token='f'{datos.REFRESH_TOKEN}'

response = requests.request("POST", 'https://api.mercadolibre.com/oauth/token', headers=h, data=d)
print(response.text)



