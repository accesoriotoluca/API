import requests, datos, json

h = {'Authorization' : 'Bearer ' f'{datos.ACCESS_TOKEN}',}
r = requests.request('GET','https://api.mercadolibre.com/applications/'f'{datos.APP_ID}', headers=h)

""" print('status_code = ', r.status_code)
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
with open('response.json', 'w') as a: json.dump(dict(r.json()), a) """
# print('__doc__ = ', f"'{r.__doc__}'")
# print('__dict__ = ', r.__dict__)
# print('__getstate__() = ', r.__getstate__())
# print('__reduce__() = ', r.__reduce__())

""" 
status_code =  200
reason =  'OK'
history =  []
links =  {}
next =  None
elapsed =  '0:00:00.148241'
__hash__ =  134710076593   
is_permanent_redirect =  False
raise_for_status =  None
cookies =  '<RequestsCookieJar[]>'
__attrs__ =  ['_content', 'status_code', 'headers', 'url', 'history', 'encoding', 'reason', 'cookies', 'elapsed', 'request']

"""

