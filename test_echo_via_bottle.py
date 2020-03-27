from multiprocessing import Process
from bottle import route, run, request
import requests as req

@route('/echo', method='POST')
def echo():
    print(request.params.get('data'))
    return ""
p = Process(target=lambda: run(port=8080, quiet=True))
p.start()

def say(something, ret):
    req.post(" http://127.0.0.1:8080/echo", {"data":something})
    return ret
