from storage import identification_process, user_login

print("Bienvenido al sistema de gestión de usuarios y puntos.")

while True:
    while True:
        selection_order = input('Por favor, elija la acción que desea realizar:\n1. Iniciar sesión\n2. Crear una cuenta\n')
        if selection_order == '2':
            identification_process()
        elif selection_order == '1':
            break
        else:
            print(f'La opción {selection_order} no se ha logrado identificar correctamente, por favor, vuelva a seleccionar.')

    user_login()