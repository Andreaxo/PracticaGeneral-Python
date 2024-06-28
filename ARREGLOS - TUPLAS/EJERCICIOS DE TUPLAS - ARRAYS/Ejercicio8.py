
tupla_num = (14,5,6,7,124,643,12)
print (tupla_num)

tupla1 = list(tupla_num)
tupla1.sort(reverse=True)
print (f"El numeros de mayor es este: {tupla1[0]}")
tupla1.sort()
print (f"El numero de menor es este: {tupla1[0]} ")