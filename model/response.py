# common response for all rest request
def response(data, code, message, error):
    return {
        "data": data,
        "code": code,
        "message": message,
        "error": error
    }

