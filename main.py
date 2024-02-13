import math
from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado() :

    if request.method == "POST" :
        numero1 = request.form.get("n1")
        numero2 = request.form.get("n2")
        res_suma = numero1 + numero2
        res_resta = numero1 - numero2
        res_multiplicacion = numero1 * numero2
        res_division = numero1 / numero2

        if request.form.get("suma") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_suma)
        elif request.form.get("resta") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_resta)
        elif request.form.get("multiplicacion") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_multiplicacion)
        elif request.form.get("division") :
            return "La suma de {} + {} da como resultado {}".format(numero1, numero2, res_division)
    return "No aplica"

@app.route("/operaciones", methods=['GET','POST'])
def operaciones():

    return render_template("index.html")

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    nom=""
    apa = ""
    ama = ""
    email = ""
    edad =""
    alumno_clase=forms.UserForm(request.form)
    if request.method == "POST" :
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        email = alumno_clase.email.data
        edad = alumno_clase.edad.data

        print('Nombre: {}'.format(nom))
        print('apaterno: {}'.format(apa))
        print('amaterno: {}'.format(ama))
        print('edad: {}'.format(edad))
        print('email: {}'.format(email))


    return render_template("alumnos.html", form=alumno_clase,nom=nom,apa=apa,ama=ama,email=email)

@app.route("/maestros", methods=['GET','POST'])
def distancia():
  
    "Hola desde FLASK"
    return "Hola desde FLASK"

if __name__ == "__main__":

    app.run(debug=True)

