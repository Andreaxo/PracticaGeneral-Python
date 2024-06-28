# #Ejercicio 2


password = str(input("Ingresa una NUEVA contraseña para tu cuenta: "))
print ("Tu contraseña ha sido creada exitosamente")
nueva = str(input("Ingresa la contraseña creada para ingresar otra vez: "))


while password != nueva:
        nueva = str(input("Ingresa la contraseña creada para ingresar otra vez: "))
        if (nueva == password ):
                print (f"Es correcta, tu contraseña es {password}")
        else:
                print ("Incorrecta")
                