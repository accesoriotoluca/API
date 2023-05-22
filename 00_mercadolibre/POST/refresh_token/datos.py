app_name = 'datos'

ACCESS_TOKEN = 'APP_USR-6726018526982523-052210-6c69d272e4c96830226c3b53aca1286b-721673001'
REFRESH_TOKEN = 'TG-64685b1a23606c0001dfba86-721673001'
SECRET_KEY = 'niTvOEDg6qWC7ewHdycLyiQcK9p4lVkU'
APP_ID = '6726018526982523'

"""
h = {
    '': '',
}
d = {
    '': '',
    '': f'{datos.APP_ID}',
}
p = ''
m = 'POST'
u = 'https://api.mercadolibre.com/applications/'f'{datos.APP_ID}'
r = requests.request(m,u, headers=h, data=d)

print('status_code = ', r.status_code)
print('reason = ', f"'{r.reason}'") 
print('history = ', r.history)
print('links = ', r.links)
print('next = ', r.next)
print('elapsed = ', f"'{r.elapsed}'")
print('__hash__ = ', r.__hash__())
print('is_permanent_redirect = ', r.is_permanent_redirect)
print('raise_for_status = ', r.raise_for_status())
print('cookies = ', f"'{r.cookies}'")
print('__attrs__ = ', r.__attrs__)
with open('headers.json', 'w') as a: json.dump(dict(r.headers), a)
with open('response.json', 'w') as a: json.dump(dict(r.json()), a)
 
# print('__doc__ = ', f"'{r.__doc__}'")
# print('__dict__ = ', r.__dict__)
# print('__getstate__() = ', r.__getstate__())
# print('__reduce__() = ', r.__reduce__())

"""