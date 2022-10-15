#!/usr/bin/python
import bottle
from bottle import response
from bottle import get, run, template
import json
from Model import Model
from ModelProducts import ModelProducts
from ModelInvetary import ModelInventary

@get('/<enterprise>/<year>/')
def getOrders(enterprise, year):
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    model_db = Model(enterprise,year)
    data = model_db.get_data()
    #import ipdb;ipdb.set_trace()
    return json.dumps({'data' : data })

@get('/')
def test():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({
        'data':'Test',
        'urls' : [
            'cordovez/YYYY/',
            'imnac/YYYY/',
            'vid/YYYY/',
        ],
        'comments': 'try change the url'
        })

@get('/<enterprise>/')
def getProducts(enterprise):
    """Obtains complete catalog form company products

    Args:
        enterprise (str): Name of entrerprise

    Returns:
        json: List of company producst
    """
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    products  = ModelProducts(enterprise).get_all()
    return json.dumps({
        'data': products
    })

@get('/inventary-report/')
def getInvetaryReport():
    """Retorna el saldo del inventario de todas las empresas"""
    model_invetary = ModelInventary()
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({
        'data': model_invetary.get_all()
    })

class StripPathMiddelware(object):
    '''Get taht slash out of request '''

    def __init__(self,a):
        self.a = a

    def __call__(self,e,h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e,h)

if __name__ == '__main__':
    ''' run server configuration '''
    run(host='0.0.0.0',
        port=8000
            )
