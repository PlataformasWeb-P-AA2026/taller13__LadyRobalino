* Ejecutar en el terminal

```
export FLASK_APP=app

flask run

```

* Debe cambiar
r = requests.get("http://127.0.0.1:8000/api/edificios/",
            headers={'Authorization': 'Token tu_token'})
r = requests.get("http://127.0.0.1:8000/api/estudiantes/",
            auth=('usuario', 'clave'))

```
