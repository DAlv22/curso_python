# Ejercicio 02
# Calcular el área y perímetro de un círculo

#IMPORTAR LA LIBRERIA O BIBLIOTECA DE FUNCIONES MATEMATICAS / CONSTANTES MATEMATICAS
import math


#Crear una función para calcunlar el área de un círculo
def CancularÁreaCírculo(radio): # Obtiene o recibe parámetros o argumentos dentro del paréntesis
    área = PI * (radio ** 2)
    return área  #Regresa, devuelve o retorna un valor




# ENTRADA DE DATOS
radio = float(input("Escribe el radio del círculo: "))
PI = 3.1416  # DECLARAR CONSTANTE PI CON MAYÚSCULA
unidad_medida = input("Escribe la unidad_medida: ")




# PROCESOS
área = PI * (radio ** 2)
perímetro = (2 * math.pi) * radio

# SALIDA DE DATOS
print("El área del circulo es de =", round (área, 2), unidad_medida + "2")
print("El perímetro del circulo es de =", round (perímetro, 2), unidad_medida)
# Mandar a llamar o invocar una función
# Envían o pasan los parámetros o argumentos
print(f"El área es = {CancularÁreaCírculo(2)}")


# Dudas:
# ¿podemos asignar una undiad de medida? Ej. cm
# ¿Tiene guardados valores constantes como pi?
# ¿Tiene formulas generales guardadas como "perimetro de un circulo"?