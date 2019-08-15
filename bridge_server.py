from bottle import route, run, request
import bottle
import numpy as np
import io

from termcolor import colored
bottle.BaseRequest.MEMFILE_MAX = 10000 *10000 # (or whatever you want)

native_print = print
def print(txt):
    native_print(colored(txt,"red"))


@route('/')
def hello():
    site = """import requests as req
            import pickle

            def get(URL = "http://167.71.35.239:8080/bridge"):
                    data = req.get(URL)
                    print(len(data.text))
                    data = bytes(data.text,encoding='iso-8859-1')#data.text.encode()
                    print(len(data))
                    return pickle.loads(data)

            def send(data, URL = "http://167.71.35.239:8080/bridge"):
                    serialized = pickle.dumps(data, protocol=0)
                    #print(serialized)
                    req.post(URL, {"data":serialized},headers={'Content-Type': 'application/octet-stream'})"""
    return site

my_arrays = []
@route('/bridge', method='POST')
def set_data():
    try:
        data = request.params.get('data')
        print(len(data))

        #print(str(data,encoding="utf-8"))
        #data = bytes(data,'iso-8859-1')#.decode('utf-8')
        #print(len(data))
        print("Received data of length " +str(len(data)))
        my_arrays.append(data)

    except Exception as e:
        print("ERROR")
        print(e)
    return "Sucessfully set data"


@route("/bridge", method ="GET")
def get_data():
    print("User requested data from stack")
    if len(my_arrays)==0:
        print("Stack is empty, return ''")
        return "stack_is_empty"
    return(my_arrays.pop())

run(host='0.0.0.0', port=8080)
