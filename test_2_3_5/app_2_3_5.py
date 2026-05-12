# Importamos la función para manejar plantillas
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/debug")
def ver_coleccion():
    # 1. Conectamos con el archivo de la base de datos
    conexion = sqlite3.connect("reto_ismael.db")
    
    # 2. Configuramos la conexión para que devuelva diccionarios (más fácil para Jinja2)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    # 3. Aseguramos que la tabla LOGS exista antes de leerla
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS LOGS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT NOT NULL
        )
        """
    )
    
    # 4. Ejecutamos la consulta SQL
    cursor.execute("SELECT * FROM LOGS")
    
    # 5. Guardamos todos los resultados en una variable
    datos = cursor.fetchall()
    
    # 5. Cerramos la conexión
    conexion.close()
    
    # 6. Enviamos los datos reales a la plantilla
    return render_template("galeria.html", logs=datos)

    # Comprobamos si el script se está ejecutando directamente (y no importado como módulo)
if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)