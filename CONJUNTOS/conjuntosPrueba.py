

#Conjuntos
#La clase set es un conjunto -> 
mi_conjunto = {2,5,6,2,3,4,2,6}
print(mi_conjunto)
print(type(mi_conjunto))

mi_conjunto.add("Subele mamawebo") #Add ES PARA AÑADIR.
print(mi_conjunto)

mi_conjunto = set(range(1,4)) #El set es para que se vuelva un conjunto. #El rango es para que de ciertos numeros.
print (mi_conjunto)

# num1 = (int(input("Ingrese un numero")))
# print(num1)

# print(f"Está el numero {num1} en el conjunto {mi_conjunto}?: {num1 in mi_conjunto}")

mi_conjunto = {2,43,5,67,8,23,45}
x = 3

for x in mi_conjunto:
    print(x)
    
    
c = {5,3,4,5,6,7,8}
c.discard(5)
print(c)

c1 = {2,5,7}
c2 = {9,3,1}
print(f"c1 disjoint c2 = {c1.isdisjoint(c2)}")
c3 = {9,3,5}
print(f"c1 disjoint c3 = {c1.isdisjoint(c3)}")


a1 = {2,5,7}
a2 = {2,5,4}

print(f"A es Subconjunto de A2 {a1.issuperset(a2)}")

print(f"La unión de los dos es: {a1.union(a2)}")

print(f"La diferencia de A1 Y A2 {a2.difference(a1)}")

b1 = {2,5,7}
b2 = {2,5,3}

print(f"C1 symmetric_differences C2 = {b1.symmetric_difference(b2)}")

t1 = {2,7,5}
t2 = {2,5,3}
print(f"c1 INTERSECTION C2 = {t1.intersection(t2)}")