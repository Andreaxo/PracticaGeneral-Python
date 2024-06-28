

#BUCLES      
for i in range(3):
    print(i)

print ("---------------------")
for i in range(100):
    if i == 0:
        continue #Omitir
    print(i)



print ("====================")

x=0
while True:
    print(x)
    if x == 9:
        break
    x+=1


variable = None

#None null =
#Null = Permite que el dato quede vacío -> Con astericos none null

#FUNCIONES 
print ("===========")
def funcion():
    pass

print(funcion())

def funcion_suma(a,b):
    return (a+b)    #El return espera siempre un valor
                    # El print solo imprime lo que haya en ese momento

suma = funcion_suma(3,5)
print("La suma es", suma)


print("La suma es", (lambda a, b: a+b)(3,5)) #Funciones anonimas
