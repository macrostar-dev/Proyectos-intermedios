import mysql.connector
from os import system
system("cls")

# Configura la conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='datos_2',
    port=3306)
cursor = conn.cursor()

#Creara una lista con los datos de mysql de las personID para ser utilizado en un identificador
def conjunto_cedulas_inspeccion_existencia():
    consulta = "SELECT PersonID FROM informa"
    cursor.execute(consulta)
    filas_cedula = cursor.fetchall()
    cedulas = [fila[0] for fila in filas_cedula]
    return cedulas


def creador_mysql(a, b):
    sql = "INSERT INTO informa (PersonID, Contraseña, Puntos) VALUES (%s, %s, %s)"
    valores = (int(a), b, 0)
    cursor.execute(sql, valores)
    conn.commit()

def proceso_de_cuenta_nueva():
    a = 0
    while a < 3:
        cedula_nueva = input('Por favor, digite un número de cédula: ')
        if cedula_nueva.isdigit() and len(cedula_nueva) >= 9 and cedula_nueva not in conjunto_cedulas_inspeccion_existencia():
            print('Cédula válida')
            while True:
                contraseña_nueva = input('Por favor, digite una contraseña con mínimo 8 caracteres: ')
                if len(contraseña_nueva) >= 8:
                    creador_mysql(cedula_nueva, contraseña_nueva)
                    print('La contraseña ha sido guardada con éxito')
                    input('Digite enter para continuar')
                    a=3
                    break
                else:
                    print('La contraseña contiene menos de 8 caracteres.')
                    input('Digite enter para continuar')
                    system("cls")
            break
        else:
            print('Cédula no válida.')
            input('Digite enter para continuar')
            system("cls")
            a += 1
