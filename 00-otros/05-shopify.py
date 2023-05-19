import requests
"""
^ "creds.py"
contener credenciales información sensible como: 
nombres de usuario, contraseñas, tokens de acceso, etc
evita exponer información confidencial en código fuente
evita compartirlo o subirlo a repositorios d código abiertos"""
import creds #credentials???

""" session use tcp connection for all requests, more efficient faster"""
def create_session():
    #session object
    s = requests.Session()
    #add the headers to be sent every req in this session
    #very time use this session will have this headers attached
    #for user agents, this case has our api access token
    s.headers.update({
        "X-Shopify-Access-Token": creds.token,
        "Content-Type": "application/json"
    })
    #every time we get a response
    #funcion to get request limit in headers response
    def api_calls(r,*args,**Kwargs):
        #split = ['1','40,]
        calls_left = r.headers['X-Shopify-Shop-Api-Call-Limit'].split("/")
        print(calls_left[0])
        #si llega al limite de req
        if int(calls_left[0]) == 39:
            print('limit close, sleeping')
            #pycharm
            time.sleep(5)
    # response hooks
    s.hooks["response"] = api_calls
    return s


def main():
    sess = create_session()
    for x in range(1,100):
        resp = sess.get(creds.url + "/admin/api/2021-07/products.json?limit=10")

    # #productos
    #!print(len(resp.json()['products]))... limit=10
    #product data from shopify api
    #!print(resp.json())
    #response headers, request limit = "X-Shopify-Shop-Api-Call-Limit: '1/40'
    #! print(resp.headers)
    #límite de requests
    #! print(resp.headers['X-Shopify-Shop-Api-Call-Limit'])
    #link con next
    #! print(resp.headers['link'])
    # search for next and previous link, get a diccionary
    #! print(resp.links['next || previous'])
    # search for next and previous link, get the link
    #! print(resp.links['next || previous'][url])


if __name__ == '__main__':
    main()