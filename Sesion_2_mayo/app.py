from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Saludar", methods=["POST"])
def saludar():
    nombre = request.form.get("nombre")
    mensaje = f"Hola. {nombre}!, mucho gusto en conocerte!"
    return render_template("saludo.html",mensaje = mensaje)

if __name__ == "__main__":
    app.run(debug=True)