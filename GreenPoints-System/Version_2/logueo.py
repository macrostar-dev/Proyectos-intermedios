import mysql.connector
from os import system

# Configura la conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='datos_2',
    port=3306)
cursor = conn.cursor()

import mysql.connector

# Crear una lista con los datos de MySQL de las PersonID para ser utilizados en un identificador
def conjunto_cedulas_inspeccion_existencia():
    consulta = "SELECT PersonID FROM informa"
    cursor.execute(consulta)
    filas_cedula = cursor.fetchall()
    cedulas = [fila[0] for fila in filas_cedula]
    return cedulas

# Buscar una contraseña del usuario
def buscar_contraseña_por_cedula(PersonID):
    consulta = "SELECT Contraseña FROM informa WHERE PersonID = %s"
    cursor.execute(consulta, (PersonID,))
    filas_contraseña = cursor.fetchall()
    contraseñas = [fila[0] for fila in filas_contraseña]
    return contraseñas

# Buscar puntos de usuario
def buscar_puntos(usua):
    consulta_de_puntos = f"SELECT Puntos FROM informa WHERE PersonID = {int(usua)}"
    cursor.execute(consulta_de_puntos)
    resultado_consulta_puntos = cursor.fetchone()
    resultado_final = resultado_consulta_puntos[0]
    return resultado_final

# Actualizar puntos de un usuario
def actualizar_puntos(PersonID, nuevos_puntos):
    sql = "UPDATE informa SET Puntos = %s WHERE PersonID = %s"
    valores = (nuevos_puntos, PersonID)
    cursor.execute(sql, valores)
    conn.commit()

# Obtener puntos
def reciclar(usu):
    system("cls")
    botella = int(input('Digite los mililitros de la botella: '))
    puntos_actuales = buscar_puntos(usu)
    if botella <= 250:
        pun_ob = puntos_actuales + 100
        actualizar_puntos(usu,pun_ob)
        
    elif 250< botella <= 800:
        pun_ob = puntos_actuales + 125
        actualizar_puntos(usu,pun_ob)
        
    elif 801 < botella <= 1500:
        pun_ob = puntos_actuales + 150
        actualizar_puntos(usu,pun_ob)
        
    elif 1501 < botella <= 3000:
        pun_ob = puntos_actuales + 175
        actualizar_puntos(usu,pun_ob)
        
        
    else:
        print('Numero no posible de ser registrado por la maquina')
        input('Digita enter para continuar')

def productos():
    system("cls")
    vevidas= {'CocaCola 250m': 1000, 'Coca Cola 600m':2000, 'Chavo':150}
    for clave, valor in vevidas.items():
        print(clave, valor)
        input('Digite enter para continuar')

    
        
def comprar(usu):
    system("cls")
    vevidas= {'1':'Coca Cola 250','2':'Coca Cola 600m','3':'Chavo'}
    print('Lista de productos')
    for clave, valor in vevidas.items():
        print(clave, valor)
    seleccion=input('Digite el producto que desea comprar')
    if seleccion == '1' and buscar_puntos(usu)>= 1000:
        eliminar= int(buscar_puntos(usu))-1000
        actualizar_puntos(usu,eliminar)
    elif seleccion == '1' and buscar_puntos(usu)>= 2000:
        eliminar= int(buscar_puntos(usu))-2000
        actualizar_puntos(usu,eliminar)
    elif seleccion == '1' and buscar_puntos(usu)>= 150:
        eliminar= int(buscar_puntos(usu))-150
        actualizar_puntos(usu,eliminar) 
    else:
        print('Numero no reconocido') 
        input('Digite enter para continuar') 
    
def logueo_usuario():
    a = 0
    b = 0
    while a < 3:
        system("cls")
        usuario = input('Por favor, ingrese su número de cédula para el inicio de sesión: ')
        if int(usuario) in conjunto_cedulas_inspeccion_existencia():
            while b < 3:
                password = input('Por favor, ingrese su contraseña: ')
                contraseñas = buscar_contraseña_por_cedula(int(usuario))
                if password in contraseñas:
                    while True:
                        system("cls")
                        print('Por favor, seleccione una de las siguientes funciones:\n1. Reciclar\n2. Productos\n3. Comprar\n4. Finalizar')
                        seleccion_proceso = input('Ingrese el número de la función seleccionada: ')
                        if seleccion_proceso == '1':
                            print('Has seleccionado reciclar.')
                            reciclar(usuario)
                        elif seleccion_proceso == '2':
                            productos()
                        elif seleccion_proceso == '3':
                            comprar(usuario)
                        elif seleccion_proceso == '4':
                            break  
                        else:
                            print('Opción no válida.')
                            input('Digite neter para continuar')
                            system("cls")   
                    break                      
                else:
                    b += 1
                    print('Contraseña incorrecta.')
                    input('Digite enter para continuar')
                    system("cls")
            break
        else:
            
            print('Cédula no encontrada.')
            input('Digite enter para continuar')
            system("cls")
            a += 1