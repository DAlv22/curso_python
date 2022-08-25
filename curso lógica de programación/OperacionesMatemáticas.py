# EJEMPLO 2. OPERACIONES MATEMÁTICAS

# IMPORTAR UNA LIBRERÍA O BIBILIOTECA DE FUNCIONES MATEMÁTICAS DE PYTHON
import math

# ENETRADAS DE DATOS
''' Declarar o crear variables '''
número_1 = float(input("Escribe el 1er número: "))
número_2 = float(input("Escribe el 2do número: "))




# PROCESOS (Operaciones o Cálculos Matermáticos y/o Lógicos)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1 % número_2



# SALIDA DE DATOS
# Suma
print("La suma es =", round(suma, 2))
print("La suma es = " + str(suma)) #Concatenación (unión o cuando juntas dos o  más textos)
# CASTEO: Convertir un tipo de dato en otro tipo de dato
print(f"La suma  es = {suma}") # Interpolación de Textos F (Formatear)
# Resta
print("La resta es =", resta)
print("La resta es = " + str(resta))
print(f"La resta es = {resta}")
# Multiplicación
print("La multiplicación es =", multiplicación)
print("La multiplicación es = " + str(multiplicación))
print(f"La multiplicación es = {multiplicación}")
# División
print("La división es =", división)
print("La división es = " + str(división))
print(f"La división es = {división}")
# Potencias
print("La potencia de num 1 a la num2 es =", potencia_1)
print("La potencia de num 1 a la num2 es =", potencia_2)
print("La potencia al cuadrado de num 1 es", cuadrado)
print("El cubo de núm 2 es =", cubo)
# Raiz
print("La raíz cuadrada de 9 es =", raíz_cuadrada_1)
print("La raíz cuadrada de 9 es =", raíz_cuadrada_2)
print("La raíz cúbica de 27 es =", raíz_cúbica)
# Módulo o Residuo
print("El módulo o residuo es=", módulo_residuo)



