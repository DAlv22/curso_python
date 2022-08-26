# Ejercicio 05
# Obtener valores para: a, b y c. Calcular la fórmula general.

# ENTRADA DE DATOS
# Al colocar "Float" que pasa si no me colocan numeros con decimales
a = float(input("Coloca valor conocido de a: "))
b = float(input("Coloca valor conocido de b: "))
c = float(input("Coloca valor conocido de c: "))


# PROCESOS
x1 = ((- b - (pow ((b ** 2) - (4 * a * c), 1/2)))/ (2 * a))

x2 = ((- b + (pow ((b ** 2) - (4 * a * c), 1/2)))/ (2 * a))



# SALIDA DE DATOS
print("x1 es = ", x1)
print("x2 es = ", x2)





