# EJEMPLO 3. CONDICIONALES
# Mayoría de edad de una persona


#ENTRADA DE DATOS
edad = int(input("Escribre tu edad: "))


# PROCESO
if (edad >= 18 and edad <=120): # RANGO ENTRE 18 Y 120
    print("MAYOR DE EDAD") # SALIDA DE DATOS
elif (edad >= 0 and edad < 18): # RANGO ENTRE 0 Y MENOR QUE 18
    print ("MENOR DE EDAD") # SALIDA DE DATOS
else:
    print ("La edad es inválida")




