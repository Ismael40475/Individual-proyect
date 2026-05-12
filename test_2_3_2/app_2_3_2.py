# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Buscamos el archivo 'index.html' dentro de la carpeta /templates
    # También podemos pasar datos como variables (nombre="Ismael Domínguez")
    return render_template("perfil_2_3_2.html", estudiante="Ismael Domínguez", nickname="alpha", id_dev="2389" )
# Comprobamos si el script se está ejecutando directamente (y no importado como módulo)
if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)