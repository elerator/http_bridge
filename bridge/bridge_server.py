from bottle import route, run, request
import bottle
import numpy as np
import io

from termcolor import colored
bottle.BaseRequest.MEMFILE_MAX = 10000000000 *10000000000

native_print = print
def print(txt):
    native_print(colored(txt,"red"))


@route('/')
def hello():
    site = """
    from bridge import *
    import numpy as np
    send(np.ones(100))
    print(get())
    """
    site = '<div style="white-space: pre-wrap;">' + site + '</div>'
    return bytes(site,"Latin1")

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
        #print(bytes(data,'iso-8859-1'))
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
        return " "
    return(my_arrays.pop())

run(host='0.0.0.0', port=80)
