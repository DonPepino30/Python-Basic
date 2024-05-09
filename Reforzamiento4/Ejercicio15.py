"""Queremos consumir un JSON que se encuentra alojado en la nube el cual
nos traerá los datos de una persona como la edad, nombre, email, dirección
o nombre de la compañía en donde trabaja.
La url a consumir usando Python es la siguiente:

https://jsonplaceholder.typicode.com/users

Obtener respectivamente los valores necesarios para formar la siguiente
oración: Bienvenido “nombre” “apellido”, usted tiene “edad” años. El correo que
nos proporcionó es “correo” y la compañía actual donde trabaja se llama
“nombreCompañía”. Dentro de sus datos también encontramos una website
que es: “nombreWeb”"""

import json
import requests

url = "https://jsonplaceholder.typicode.com/users"

resp = requests.get(url)

data = json.loads(resp.text)

for user in data:
    name = user["name"]
    email = user["email"]
    company = user["company"]["name"]
    website = user["website"]
    age = 45

    nombre = name.split()[0]
    apellido = name.split()[-1]

    oracion = f"\nBienvenido {nombre} {apellido}, usted tiene {age} años. El correo que nos proporcionó es {email} y la compañía actual donde trabaja se llama {company}. Dentro de sus datos también encontramos una website que es: {website}.\n"

    print(oracion)
