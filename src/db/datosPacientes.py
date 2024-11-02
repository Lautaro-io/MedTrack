from os import close
from pyexpat.errors import messages
from shutil import ExecError
import src.db.conexion as con


def save(paciente):
    paciente = paciente.__dict__
    try:
        db = con.conectar()
        #Guarda la db
        cursor = db.cursor()
        #Creamos un cursor que nos va a permitir ejecutar comandos SQL
        columnas = tuple(paciente.keys())
        # Nos devuelve las columnas que existen dentro de la tabla persona
        values  = tuple(paciente.values())
        # Nos devuelve los valores que hay dentro de cada columna
        sql = """
        INSERT INTO pacientes{campos} VALUES (?,?,?)  
        """.format(campos=columnas)
        #### CONSULTA SQL QUE VA A EJECUTAR EL CURSOR ( los '?' representan la cantida de parametros que le vamos a pasar )
        cursor.execute(sql,(values))
        #Esta linea ejecuta la consulta sql y le pasamos como parametro una tupla con los valores
        creada = cursor.rowcount>0
        #BOOLEANO devuelve TRUE si el curso
        db.commit()
        ## COMMIT se escribe siempre que el cursor modifica algun tipo de dato por ej, DELETE,UPDATE,CREATE
        if creada: #VERIFICACION SI CREADA == TRUE, cerramos el cursor y la db y devolvemos un diccionario con un mensaje que la persona se creo correctamente.
            return {"respuesta" :creada , "mensaje": "Paciente registrado."}
        else:
            cursor.close()
            db.close()
            return {"respuesta": creada, "mensaje": " No se logro registrar a la persona."}
    except Exception as ex: #Manejo de exepciones donde a la EXCEPTION le damos un alias ex el cual si algo del try no funciona entra en el except y para un buen manejo de errores devolvemos el error

        if "UNIQUE" in str(ex) and "correo" in str(ex): #en caso de que ex tenga "UNIQUE" y "correo"
            mensaje = "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "dni" in str(ex):#en caso de que ex tenga "UNIQUE" y "dni"
            mensaje = "Ya existe una persona con ese dni"
        else:
            mensaje = str(ex) #En esta variable guardamos el error convertido en string para poder devolverlo en caso que ocurra

        return {"respuesta": False, "mensaje": mensaje } # DEVOLVEMOS LA RESPUESTA Y EL MENSAJE QUE SE ALMACENO

    finally: #EN CASO QUE FUNCIONE O NO EL TRY/EXCEPT DE IGUAL MANERA SE VA A CERRAR EL CURSOR Y LA DB
        cursor.close()
        db.close()

def save_med(medicamento):
    print(dict(medicamento))
    try:
        db = con.conectar()
        cursor = db.cursor()
        columnas = tuple(medicamento.keys())
        values  = tuple(medicamento.values())
        sql = """
        INSERT INTO medicamentos{campos} VALUES (?,?)  
        """.format(campos=columnas)
        cursor.execute(sql,(values))
        creada = cursor.rowcount>0
        db.commit()
        if creada:
            return {"respuesta" :creada , "mensaje": "Medicamento registrado."}
        else:
            cursor.close()
            db.close()
            return {"respuesta": creada, "mensaje": " No se logro registrar el medicamento."}
    except Exception as ex :

        print(str(ex))

    finally:
        cursor.close()
        db.close()

def save_sintoma(sintoma):
    sintoma = dict(sintoma)
    try:
        db = con.conectar()
        cursor = db.cursor()
        columnas = tuple(sintoma.keys())
        values  = tuple(sintoma.values())
        sql = """
        INSERT INTO sintomas{campos} VALUES (?,?)  
        """.format(campos=columnas)
        cursor.execute(sql,(values))
        creada = cursor.rowcount>0
        db.commit()
        if creada:
            return {"respuesta" :creada , "mensaje": "sintoma registrado."}
        else:
            cursor.close()
            db.close()
            return {"respuesta": creada, "mensaje": " No se logro registrar el sintoma."}
    except Exception as ex:

        print(str(ex))

    finally:
        cursor.close()
        db.close()



def findAll(tabla):
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {tabla} ".format(tabla = tabla))
        filas = cursor.fetchall()
        if filas:
            cursor.close()
            db.close()
            return {"respuesta":True,"personas":filas, "mensaje" : "Listado OK."}
        else:
            cursor.close()
            db.close()
            return {"respuesta": False, "personas": filas, "mensaje": "No hay personas registradas."}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta" : False , "mensaje": str(ex)}

def find(dniPersona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM paciente where dni = '{dniPersona}' ".format(dniPersona=dniPersona))
        result = cursor.fetchall()
        if result:
            info = result[0]
            #1, '43260468', 23, 'Lautaro', 'Ildarraz', '44-1259', 'ildarrazlautaro@gmail.com')
            persona = {"id":info[0],"dni":info[1],"nombre":info[2],"apellido":info[3],"nacimiento":info[4],"ingreso":info[5] }
            cursor.close()
            db.close()
            return {"respuesta":True,"persona":persona, "mensaje" : "Paciente encontrado."}
        else:
            cursor.close()
            db.close()
            return {"respuesta": False,  "mensaje": "No existe el paciente"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta" : False , "mensaje": str(ex)}


def update(persona):
    try :
        db = con.conectar()
        cursor = db.cursor()
        persona = persona.__dict__ ##CONVERTIMOS EL PARAMETRO EN UN DICCIONARIO
        dniPersona = persona.get('dni') #OBTENEMOS EL VALOR 'DNI' DE PERSONA Y LO GUARDAMOS EN UNA VARIABLE
        persona.pop('dni') # BORRAMOS DNI DE PERSONA PARA QUE NO SE PUEDA CAMBIAR
        values = tuple(persona.values()) #GUARDAMOS LOS VALORES DE LAS FILAS EN UNA TUPLA
        sql = """
        UPDATE paciente 
        SET 
        nombre = ?,
        apellido = ?,
        nacimiento =?,
        ingreso = ?,
        sintomas = ?,
        medicacion = ?,
        hora_ingesta = ?
        WHERE dni= '{dni}'
        """.format(dni= dniPersona) ## CONSULTA SQL IMPORTANTE ,EL ORDEN DEL SET TIENE Q SER IGUAL AL ORDEN DE LAS COLUMNAS DE LA TABLA
        cursor.execute(sql,values)
        modificada = cursor.rowcount>0 # DE NUEVO BOOL SI SE MODIFICO LA TABLA CONTANDO LAS TABLAS
        db.commit() # COMMIT PARA EJECUTAR LA SENTENCIA
        cursor.close()
        db.close()
        if modificada:
            return {"respuesta":modificada,"mensaje":"Paciente actualizado."}
        else:
            return {"respuesta": modificada, "mensaje": "No existe un paciente con ese DNI."}

    except Exception as ex:
        if "UNIQUE" in str(ex) and "dni" in str(ex):#en caso de que ex tenga "UNIQUE" y "dni"
            mensaje = "Ya existe un paciente con ese dni"
        else:
            mensaje = str(ex) #En esta variable guardamos el error convertido en string para poder devolverlo en caso que ocurra

        cursor.close()
        db.close()
        return  {"respuesta":False,"mensaje":str(ex)}


def delete(idPersona):
    try :
        db = con.conectar()
        cursor = db.cursor()
        sql = "DELETE FROM paciente WHERE id= {id}".format(id= idPersona) ## CONSULTA SQL IMPORTANTE ,EL ORDEN DEL SET TIENE Q SER IGUAL AL ORDEN DE LAS COLUMNAS DE LA TABLA
        cursor.execute(sql)
        deleted = cursor.rowcount>0 # DE NUEVO BOOL SI SE MODIFICO LA TABLA CONTANDO LAS TABLAS
        db.commit() # COMMIT PARA EJECUTAR LA SENTENCIA
        cursor.close()
        db.close()
        if deleted:
            return {"respuesta":deleted,"mensaje":"Paciente eliminado."}
        else:
            return {"respuesta": deleted, "mensaje": "No existe un paciente con ese ID."}

    except Exception as ex:
        cursor.close()
        db.close()
        return  {"respuesta":False,"mensaje":str(ex)}