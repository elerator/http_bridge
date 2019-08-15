from bottle import auth_basic,run, request, route

def check(user, pw):
    if user == "user" and pw == "hello":
        return True
@route('/')
@auth_basic(check)
def home():
    return { 'data': request.auth }

run(host='0.0.0.0', port=8080)
