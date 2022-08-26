# Ejercicio 03
# Determinar la edad de una persona conociendo el año actual y el año de nacimiento

# Importar una librería para el manejo de fehcas

import datetime



# ENTRADA DE DATOS
año_de_nacimiento = int(input("Indique fecha_de_nacimiento: "))
hoy = datetime.date.today().year
''' cómo colocar la fecha de hoy'''


# PROCESOS
edad = hoy - año_de_nacimiento 
'''colocar el resultado en años'''



# SALIDA DE DATOS
print ("La edad actual de esta persona es: ", edad, "años")


