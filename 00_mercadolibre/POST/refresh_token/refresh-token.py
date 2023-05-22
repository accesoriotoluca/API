import requests, datos

["curl -X POST \
-H 'accept: application/json' \
-H 'content-type: application/x-www-form-urlencoded' \
'https://api.mercadolibre.com/oauth/token' \
-d 'grant_type=refresh_token' \
-d 'client_id="f'{datos.APP_ID}'" \
-d 'client_secret="f'{datos.SECRET_KEY}'" \
-d 'refresh_token="f'{datos.REFRESH_TOKEN}'""]


h = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded'
}

d = {
    'grant_type': 'refresh_token',
    'client_id': f'{datos.APP_ID}',
    'client_secret': f'{datos.SECRET_KEY}',
    'refresh_token': f'{datos.REFRESH_TOKEN}'
}
p = ''
m = 'POST'
u = 'https://api.mercadolibre.com/oauth/token'

r = requests.request(m,u, headers=h, data=d).json()
print(r)