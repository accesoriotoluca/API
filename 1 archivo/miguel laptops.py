import requests
from tabulate import tabulate

r = requests.get('https://google.com')
""" hl = [(k, v) for k, v in h.items()]
print(tabulate(hl,tablefmt="plain")) """
print(tabulate([(k, v) for k, v in r.headers.items()],tablefmt="plain"))





""" 
r.status_code = 200
r.headers = dicc tupla
r.cookies = dicc tupla
r.is_redirect = False
r.is_permanent_redirect = False
r.url = https://www.google.com/


"""
