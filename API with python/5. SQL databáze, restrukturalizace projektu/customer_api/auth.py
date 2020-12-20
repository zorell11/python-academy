from flask import request

API_KEY = '6222e030-423f-11eb-8cb1-d0c637448f4e'

def api_key_required(decorated_method):
    def wrapper(*args, **kwargs):
        print(request.headers)
        for i in request.headers:
            if i[0] == 'Api-Key' and i[1] == API_KEY:
                return decorated_method(*args, **kwargs)
        else:
            return {'error' : 'invalid API key'}, 404
    return wrapper
