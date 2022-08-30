# Ejercicio 07
# Pedir el nivel del agua en metros de una cisterna

# Si llega a mas de 6 m = Desbordamiento de Agua en cisterna
# Nivel 6 = Apagar bomba
# Entre 4 a 6 m = Desacelerar Bomba
# Entre 2 a 4 m = Bomba Trabajando!
# Entre 0 a 2 m = Acelerar  Bomba
# Nivel de 0 = Encender Bomba de agua
# Menor a 0 = Fuga en cisterna

# ENTRADA DE DATOS
nivel_de_agua = float(input("Indique nivel de agua: "))



# PROCESO # SALIDA DE DATOS
if (nivel_de_agua >6):
    print ("Desbordamiento de agua en cisterna")
elif (nivel_de_agua ==6):
    print ("Apagar bomba")
elif (nivel_de_agua >=4 and nivel_de_agua <6):
    print ("Desacelerar Bomba")
elif (nivel_de_agua >=2 and nivel_de_agua <4):
    print ("Bomba Trabajando")
elif (nivel_de_agua > 0 and nivel_de_agua <2):
    print ("Acelerar Bomba")
elif (nivel_de_agua == 0):
    print ("Encender Bomaba de Agua")
elif (nivel_de_agua <0):
    print ("Fuga en cisterna")







