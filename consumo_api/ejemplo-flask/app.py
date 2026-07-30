from flask import Flask, render_template, request, redirect, url_for
import requests
from config import token, base_url

app = Flask(__name__, template_folder='templates')


def auth_headers():
    return {"Authorization": f"Token {token}"}

@app.route("/")
def hello_world():
    return redirect(url_for("los_edificios"))


@app.route("/edificios")
def los_edificios():
    r = requests.get(f"{base_url}/edificios/", headers=auth_headers())
    payload = r.json()
    datos = payload.get('results', [])
    numero = payload.get('count', 0)
    return render_template("edificios.html", datos=datos, numero=numero)


@app.route("/departamentos")
def los_departamentos():
    r = requests.get(f"{base_url}/departamentos/", headers=auth_headers())
    payload = r.json()
    datos = payload.get('results', [])
    numero = payload.get('count', 0)
    return render_template("departamentos.html", datos=datos, numero=numero)


@app.route("/crear-edificio", methods=['GET', 'POST'])
def crear_edificio():
    if request.method == 'POST':
        payload = {
            'nombre': request.form['nombre'],
            'direccion': request.form['direccion'],
            'ciudad': request.form['ciudad'],
            'tipo': request.form['tipo'],
        }
        requests.post(f"{base_url}/edificios/", data=payload, headers=auth_headers())
        return redirect(url_for('los_edificios'))
    return render_template("crear_edificio.html")


@app.route("/crear-departamento", methods=['GET', 'POST'])
def crear_departamento():
    edificios = requests.get(f"{base_url}/edificios/", headers=auth_headers()).json().get('results', [])
    if request.method == 'POST':
        payload = {
            'nombre_propietario': request.form['nombre_propietario'],
            'costo_departamento': request.form['costo_departamento'],
            'numero_cuartos': request.form['numero_cuartos'],
            'edificio': request.form['edificio'],
        }
        requests.post(f"{base_url}/departamentos/", data=payload, headers=auth_headers())
        return redirect(url_for('los_departamentos'))
    return render_template("crear_departamento.html", edificios=edificios)
