# 10. Pedir números enteros en un ciclo mientras sean positivos y en caso de
# que un número sea negativo cerrar el ciclo y al final promediar los
# números positivos ingresados por el usuario.



import statistics


# j = int(input("Indica un número entero: "))
# lista_num = [j]


# while(j >= 0):
#     j = int(input("Indica un número: "))
#     if (j >= 0):
#         lista_num.append(j)
#     print(lista_num)
    


# Promedio = statistics.mean(lista_num)
# print("El promedio de los números positivos es: ", round(Promedio,2))

num = 0
acumulador = 0
contador = 0

while(num >= 0):
    num = int(input("Indica un número: "))
    if (num >= 0):
        acumulador = acumulador + num
        contador = contador + 1
  
promedio = acumulador / contador
print("El promedio de los números positivos es: ", round(promedio,2))


# No me encanta que al colocar un número no entero simplemente se detenga la ejecución , debería poder poner un aviso tipo "Ese no es un número entero"
# FALTÓ: para garantizar que sean números enteros, manejar condicional que indique que el resitudo debe ser cero "módulo_residuo = número_1 % número_2"