#!/usr/bin/python3
from servidor.DAO import mostrarCarro
import cgi
import json

data=cgi.FieldStorage()
print('Content-Type: text/json')
print('')

impcarros=mostrarCarro()
print("[")
longitud=len(impcarros)
i=1
for carro in impcarros:
    print(json.dumps(carro.__dict__))
    if  i<longitud:
        print(",")
        i=i+1
print("]")




