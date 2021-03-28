#!/usr/bin/python3
''' This module lists all states from the database hbtn_0e_0_usa '''
import sys
import MySQLdb


if __name__ = "__main__":

    # Estableciendo la conexion
    # Los argumentos se reciben de la linea de comandos
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Creando un objeto "cursor" con la función cursor()
    # Este método permite usar otras funciones integradas
    cur = db.cursor()
    # Ejecutando una funcion de MySQL con la función execute()
    cur.execute("SELECT * FROM states")
    # Obteniendo las filas de la consulta y se retorna una lista con fetchall()
    rows = cur.fetchall()
    # Recorriendo la lista para imprimir el contenido de la consulta
    for i in rows:
        print(i)
    # Cerrando la conexion
    cur.close()
    db.close()
