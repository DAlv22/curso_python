# Ejercicio 01

# ENTRADA DE DATOS
calificación_1 = float(input("Coloca primera calificación: "))
calificación_2 = float(input("Coloca segunda calificación: "))
calificación_3 = float(input("Coloca tercera calificación: "))


# PROCESOS
suma = calificación_1 + calificación_2 + calificación_3
promedio_1 = suma / 3
promedio_2 = (calificación_1 + calificación_2 + calificación_3) / 3


# SALIDA DE DATOS
print("El promedio de calificación es :", round(promedio_1, 2))
print("El promedio de calificación es :", round(promedio_2, 2))


