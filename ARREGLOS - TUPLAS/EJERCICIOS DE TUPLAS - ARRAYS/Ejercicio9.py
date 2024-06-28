
precios = [50, 75, 46, 22, 80, 65, 8]

precios.sort()
print(f"Precios de menor a mayor: {precios}")
precios.sort(reverse=True)
print(f"Precios de mayor a menor: {precios}")

print(f"El mayor de toda la lista es {max(precios)}")
print(f"El menor de toda la lista es: {min(precios)}")