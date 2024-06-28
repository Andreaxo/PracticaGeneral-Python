

estudiante1 = {"id":"2826771", "nombre":"andrea","edad":18 ,"nota":10}
estudiante2 = {"id":"2826772", "nombre":"santiago","edad":15 ,"nota":10}
estudiante3= {"id":"2826773", "nombre":"julian","edad":23 ,"nota":7}
estudiante4 = {"id":"2826774", "nombre":"andrés","edad":84 ,"nota":5}
estudiante5 = {"id":"2826775", "nombre":"juan","edad":39 ,"nota":10}

print(f"El nombre del estudiante 1 es: {estudiante1['nombre']}, Edad: {estudiante1['edad']}, Nota: {estudiante1['nota']}")
print(f"El nombre del estudiante 2 es: {estudiante2['nombre']}, Edad: {estudiante2['edad']}, Nota: {estudiante2['nota']}")
print(f"El nombre del estudiante 3 es: {estudiante3['nombre']}, Edad: {estudiante3['edad']}, Nota: {estudiante3['nota']}")
print(f"El nombre del estudiante 4 es: {estudiante4['nombre']}, Edad: {estudiante4['edad']}, Nota: {estudiante4['nota']}")
print(f"El nombre del estudiante 5 es: {estudiante5['nombre']}, Edad: {estudiante5['edad']}, Nota: {estudiante5['nota']}")

identificacion = str(input("Ingrese el ID de un estudiante: "))

if identificacion in estudiante1.values():
    print(estudiante1)
elif identificacion in estudiante2.values():
    print(estudiante2)
elif identificacion in estudiante3.values():
    print(estudiante3)
elif identificacion in estudiante4.values():
    print(estudiante4)
elif identificacion in estudiante5.values():
    print(estudiante5)
else:
    print("No hay ningún ID relacionado")
    






