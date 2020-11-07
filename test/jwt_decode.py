import ast
import json
import re

import jwt
import base64

id_token ="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtnMkxZczJUMENUaklmajRydDZKSXluZW4zOCIsImtpZCI6ImtnMkxZczJUMENUaklmajRydDZKSXluZW4zOCJ9.eyJhdWQiOiI2NWY3ZmYxNC03NTQ4LTRhMmYtYTMzMi02OWVkOWUyZDViMTkiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9kYWJkNWQ5MC04N2MyLTQ0YzktOTNjZC03ODNlMDMyMzZlNDAvIiwiaWF0IjoxNjA0NjUyMTAwLCJuYmYiOjE2MDQ2NTIxMDAsImV4cCI6MTYwNDY1NjAwMCwiYWlvIjoiRTJSZ1lOakZYUmxxa3FMLzdWdjRITzM0R3g5VkZxbi96Sm9uc2tWUTZDbTcxdjdtSkJjQSIsImFtciI6WyJ3aWEiXSwiZmFtaWx5X25hbWUiOiJMaXUiLCJnaXZlbl9uYW1lIjoiU2hlbmcgRG9uZyIsImluX2NvcnAiOiJ0cnVlIiwiaXBhZGRyIjoiMTg1LjE2Mi4xMTQuNjgiLCJuYW1lIjoiU2hlbmcgRG9uZyBMaXUiLCJub25jZSI6ImU2ZDMwMTFmMDJlZTQyZDI5NTk1Mjk3NjRiNDBiNzkyIiwib2lkIjoiOWEwNTk1NDYtNzliZS00MDExLTliZDEtNGQ0MWJhYjI5MDAyIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTQyNzIyNzc4NjYtMzE4NzY5MDg0Mi0xNjcyNTAyMDI4LTUzMDA0IiwicmgiOiIwLkFRVUFrRjI5MnNLSHlVU1R6WGctQXlOdVFCVF85MlZJZFM5S296SnA3WjR0V3hrRkFKMC4iLCJzdWIiOiJlRXlGdERrd3pULU14d3Fqa0J2NHRUbTdvME50MzdNRUkxU2RBZDFCOTdjIiwidGlkIjoiZGFiZDVkOTAtODdjMi00NGM5LTkzY2QtNzgzZTAzMjM2ZTQwIiwidW5pcXVlX25hbWUiOiI5MTI3NjBAZ3J1bmRmb3MuY29tIiwidXBuIjoiOTEyNzYwQGdydW5kZm9zLmNvbSIsInV0aSI6IjhYTGFlYk9hUmsyczlNdEdpZl9xQUEiLCJ2ZXIiOiIxLjAifQ.IR-cBAmXtVF6mcAXOIBTir9TD2PZNYVmH7S4dKaZT0d2wTBDIe4mFUPHy9Rro41qIF3PHWPaFFsyVuJOue6wc7-iKcPegabRYzSfJi2FrM6SrLPV_rn39rUULFl7_fJB4JVr_OYh6tOcwx5XzS8kbXuMnTaF4p6xO8WteecGOs3OjLoH3Ndy6auMDIh3ylFajFRunWzseIYLGi-ZWSMlM8dB6i7JvcE4V-ISUBMPCT2v6F0klmOD4sAH0vjMmPE3YZgIoMu0u75C6WvOTZy6aN7XOiLEhmRgtDKOffeqdgdNIw4A6KjUfdKklzWHVlszdVUO5gtNRNHk2iQv6c5QCg"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

header,payload,signature = id_token.split(".")
def equal(b: str):
    """用来补齐被JWT去掉的等号"""
    rest = len(b) % 4
    return b + '=' * rest
payloadbt = base64.urlsafe_b64decode(equal(payload))

payloadstr = bytes.decode(payloadbt)
payloadjson = json.loads(payloadstr)
# pat = r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'
# email1 = re.search(pat,strdata).group()
email1 = payloadjson.get("upn")




# head = PyJWT.decode(id_token, 'b7.fJEgase_m_3c8L5.7.mu15BGDhYQHJ5', algorithms=['HS256'])
# header = PyJWT.get_unverified_header(id_token)
# print (header)
# print (header['kid'])


def validate_token(token):
    '''
    校验token的函数，校验通过则返回解码信息
    '''
    # global SECRET_KEY
    payload = None
    msg = None
    try:
        payload = jwt.decode(token, '123455', verify=False)
        # jwt有效、合法性校验
    except jwt.exceptions.ExpiredSignatureError:
        msg = 'token已失效'
    except jwt.DecodeError:
        msg = 'token认证失败'
    except jwt.InvalidTokenError:
        msg = '非法的token'
    return (payload, msg)
res = validate_token(id_token)
email2 = res[0].get("upn")



# https://www.pythonf.cn/read/38290