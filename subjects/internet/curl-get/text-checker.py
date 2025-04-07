import jwt

SECRET = "hello-from-jusan"
PAYLOAD = "get"

def check(token):
    try:
        body = jwt.decode(token, SECRET, algorithms="HS256")
        return body.get("payload") == PAYLOAD
    except Exception:
        return False
