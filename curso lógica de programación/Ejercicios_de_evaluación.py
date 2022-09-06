# EJERCICIO DE EVALUACIÓN:
# Realizar un programa que realice un
# cuestionario con las siguientes 12 preguntas, muestre su resultado x /
# 12 y mostrar el promedio:

import statistics

lista_calificacion = []

aciertos = 0

a = ("a")
b = ("b")  
c = ("c")
d = ("d")                                                                                                                                                                                                                                                                                                                                                      



print("Ejercicio de Evalución")

print("Coloca la letra de la respuesta que consideres correcta")

print("1.- Herramienta de programación, parecido al lenguaje español utilizado para crear código")
print(" a: IDE     b: Pseudocódigo     c: Compilador     d: ANSI / ISO")
respuesta_1 = input("Indica la letra de la opción correcta: ")

if (respuesta_1 == b):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)



print("2.- Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")
print(" a: Información     b: Datos     c: Programa     d: Código")
respuesta_2 = input("Indica la letra de la opción correcta: ")


if (respuesta_2 == a):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print ("3.- Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo")
print ("a: IEEE     b: IDE     c: ANSI/ISO     d: VSCode")
respuesta_3 = input("Indica la letra de la opción correcta: ")

if (respuesta_3 == c):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("4.- Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema")
print("a) Proceso     b) Solución     c) Función     d) Algoritmo")
respuesta_4 = input("Indica la letra de la opción correcta: ")

if (respuesta_4 == d):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print ("5. Conjunto de elementos que se relacionan para cumplir una función determinada")
print ("a) Estructura     b) Datos     c) Operación     d) Sistema")
respuesta_5 = input("Indica la letra de la opción correcta: ")

if (respuesta_5 == d):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina")
print("a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete")
respuesta_6 = input("Indica la letra de la opción correcta: ")

if (respuesta_6 == d):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor")
print("a) Constante     b) Variable     c) Librería     d) Tipo de Dato")
respuesta_7 = input("Indica la letra de la opción correcta: ")

if (respuesta_7 == b):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("8. Conjunto de símbolos, letras, números que no tienen un significado")
print("a) Datos     b) Estructura     c) Información     d) Sistema")
respuesta_8 = input("Indica la letra de la opción correcta: ")

if (respuesta_8 == a):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento")
print("a) Filosofía     b) Sociología     c)Lógica     d)Argumentación")
respuesta_9 = input("Indica la letra de la opción correcta: ")

if (respuesta_9 == c):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto")
print("a) Evento     b) Estándar     c) Calidad     d) Productividad")
respuesta_10 = input("Indica la letra de la opción correcta: ")

if (respuesta_10 == b):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico")
print("a) Estructura     b) Sistema     c) Objeto     d) Virtual")
respuesta_11 = input("Indica la letra de la opción correcta: ")

if (respuesta_11 == a):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)


print("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar")
print("a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando")
respuesta_12 = input("Indica la letra de la opción correcta: ")

if (respuesta_12 == c):
    aciertos = aciertos + 1
    lista_calificacion.append(aciertos)

print("El número de aciertos obtenido es: ", aciertos, "de 12")
promedio = (aciertos / 12) * 10
print ("El promedio obtenido es: ", round(promedio, 2))





