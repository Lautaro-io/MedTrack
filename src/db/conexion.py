import sqlite3


def conectar():
    mi_conexion = sqlite3.connect("Pacientes.db")
    cursor = mi_conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                dni TEXT NOT NULL,
                ingreso TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_medicamento TEXT NOT NULL,
                detalle TEXT)

        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sintomas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sintoma TEXT NOT NULL,
                detalle TEXT NOT NULL)

            
        ''')
        return mi_conexion

    except Exception as ex:
        print("Error de conexion", ex)

    finally:
        cursor.close()

conectar()