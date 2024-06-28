contadorF = 0
contadorB = 0
contadorBF = 0
deportes = {}
sports = []

print("----------- INSCRIPCIÓN A DEPORTES ------------")
usuarios = int(input("¿Cuántos estudiantes son?: "))

for y in range(usuarios):
    nombre = input("Ingrese el nombre del estudiante: ")
    sports.append(input("Ingrese el deporte al que quiere ingresar (b o f): "))
    
    pregunta = input("¿Quieres ingresar otro deporte? (Si/No): ")
    while pregunta.lower() == "si":
        sports.append(input("Ingrese el deporte al que quiere ingresar (Si son los dos: bf): "))
        pregunta = input("¿Quieres ingresar otro deporte? (Si/No): ")

for deporte in sports:
    if deporte == "f":
        contadorF += 1
    elif deporte == "b":
        contadorB += 1
    elif deporte == "bf":
        contadorBF += 1


print(f"Los estudiantes inscritos en futbol son {contadorF}")
print(f"Los estudiantes inscritos en basquetball son {contadorB}")
print(f"Los estudiantes inscritos en ambos deportes son {contadorBF}")      
DeporteSolo = contadorF + contadorB
print(f"Los estudiantes de un solo deporte son: {DeporteSolo}")
