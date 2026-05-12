import sqlite3

DB_PATH = "reto_ismael.db"

def crear_bd_y_insertar():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Crear la tabla LOGS
    cur.execute("""
    CREATE TABLE IF NOT EXISTS LOGS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        evento TEXT NOT NULL
    )
    """)

    # 30 eventos inventados
    eventos = [
        "Usuario registrado",
        "Inicio de sesión",
        "Cierre de sesión",
        "Contraseña cambiada",
        "Perfil actualizado",
        "Error al cargar imagen",
        "Subida de archivo",
        "Descarga de reporte",
        "Acceso denegado",
        "Sesión expirada",
        "Notificación enviada",
        "Base de datos respaldada",
        "Base de datos restaurada",
        "Nueva solicitud creada",
        "Solicitud aprobada",
        "Solicitud rechazada",
        "Conexión perdida",
        "Conexión restablecida",
        "Permiso concedido",
        "Permiso revocado",
        "Cache limpiado",
        "Tarea programada ejecutada",
        "Mail enviado",
        "Error en proceso pago",
        "Pago completado",
        "Elemento eliminado",
        "Elemento creado",
        "Reporte generado",
        "Sesión administradora iniciada",
        "Token renovado"
    ]

    # Insertar los eventos
    cur.executemany("INSERT INTO LOGS (evento) VALUES (?)", [(e,) for e in eventos])

    conn.commit()
    conn.close()
    print(f"Base de datos '{DB_PATH}' creada y 30 filas insertadas en LOGS.")

if __name__ == "__main__":
    crear_bd_y_insertar()