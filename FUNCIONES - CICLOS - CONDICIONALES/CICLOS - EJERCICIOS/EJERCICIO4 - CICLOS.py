#Ejercicio 4

acum = 0 
contador = 0
contadorimpar = 0
contadorpar = 0
numgrande= 100
numerito = 0
numeromenor = 0

while True:
        numero = int(input("Ingrese un número: "))
        
        if numero>0:
                acum = acum + numero
                
        
        if numero%2==1 and numero>0:
                contadorimpar = contadorimpar + 1
                
        if numero%2==0 and numero>0:
                contadorpar = contadorpar + 1 
        
        if numero>numeromenor and numero>=1:
                numerito = numero 
                        
        if numero<numgrande and numero>=0:
                numeromenor = numero
                pass
        
        if numero<0:
                print (f"La sumatoria es {acum}")
                print (f"Hay {contadorimpar} números impares")
                print (f"Hay {contadorpar} números pares")
                print (f"El número mayor es {numerito}, y el número es menor {numeromenor}")
                break