
users = {}
points = {}

def identification_process():
    while True:
        new_user = input('Por favor, digite su cédula para ser guardada: ')
        if len(new_user) >= 11:
            if new_user in users:
                print(f'El usuario {new_user} ya existe, por favor vuelva a intentar.')  
            else:
                while True:
                    new_password = input('Por favor, digite una contraseña con mínimo 8 caracteres: ')
                    if len(new_password) >= 8:
                        users[new_user] = new_password
                        points[new_user] = 0
                        
                        print('La contraseña ha sido guardada con éxito')
                        return
                    else:
                        print('La contraseña contiene menos de 8 caracteres.')
        else:
            print(f'El usuario {new_user} contiene insuficientes dígitos, por favor vuelva a ejecutar el proceso')

vevidas= {'1': 1000, '2':2000, '3':150}
def obtencion(a,b):
    botella=int(input('Digite los mililitros de la botella: '))
    if botella <= 250:
        pun_ob = int(a[b]) + 100
        a[b]= pun_ob
    elif 250< botella <= 800:
        pun_ob = int(a[b]) + 125
        a[b]= pun_ob
    elif 801 < botella <= 1500:
        pun_ob = int(a[b]) + 150
        a[b]= pun_ob
    elif 1501 < botella <= 3000:
        pun_ob = int(a[b]) + 175
        a[b]= pun_ob
    else:
        print('Numero no posible de ser registrado por la maquina')

def comprar(a,b):
    while True:
        numero_vevida=input('Digite el numero de la bevida que desa tomar')
        pun_ob = int(a[b]) - vevidas[numero_vevida]
        if int(a[b]) >= 0:
            a[b]= pun_ob
            break
        else:
            print('Insufiecients puntos para esta vevidad')
            break
        
def productos():
    print(vevidas)

def user_login():
    while True:
        username = input('Por favor, digite su nombre de usuario: ')
        if username in users:
            password = input('Digite la contraseña por favor: ')
            if password == users[username]:
                print('Se ha logrado iniciar sesión con éxito')
                break
            else:
                print('Contraseña incorrecta')
        else:
            print('El usuario no se ha logrado identificar')
            
        while True:
            numero=input('Porfavor digite un numero de la funcion que desa usar: 1.Desea conseguir puntos por medio de reciclaje 2.Si desean ver algun producto de los premios 3.Solisitar alguno de los productos 4.Cerrar sesion')
            if int(numero) == 1:
                obtencion(username,points)
            elif int(numero) == 2:
                comprar(username,points)
            elif int(numero) == 3:
                productos()
            else:
                break 