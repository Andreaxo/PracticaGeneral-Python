# #Ejercicio 6

contrasena = (input("Ingrese una contraseña: "))
print("Lista tu contraseña")

entrada = ""

for x in range (1,6,):
        entrada = (input("Ingrese una contraseña: "))
        
        if contrasena!=entrada: 
                print("Contraseña incorrecta")        
                
        if contrasena==entrada:
                print("Bienvenido")
                break
