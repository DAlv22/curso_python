# Ejercicio 04
# Pedir la cantidad de grados y convertirlos a °C, °F y °K

# ENTRADA DE DATOS
temperatura = float(input("Escribe la temperatura de la que quieres partir: "))
# escoger unidad de medida
unidad_de_medida = input("Coloca la unidad de medida de la temperatura, puede ser C, F, K: ")

# PROCESOS

# Una vez dada la unidad de medida, se procederá a calcular automáticamente ambas posibles conversiones

''' AQUÍ ME GUSTARÍA METER UN "IF"'''
# SI ( unidad_de_medida = C, devuelve el resultado de ck y cf, SI (unidad_de_medida = K, devuelve el resultado de kc y kf, SI (unidad_de_medida = F, devuelve el resultado de fc y fk, "")))))

# Celsius
'''Celsius a Kelvin'''
ck = temperatura + 273.15

'''Celsius a fahrenheit'''
cf = ((9 * temperatura) / 5 ) + 32

# Kelvin
''' Kelvin a Celsius'''
kc = temperatura - 273.15

'''Kelvin a Fahrenheit'''
kf = (((temperatura - 273.15) * 9 ) / 5 ) + 32

# Fahrenheit
'''Fahrenheit a Celsius'''
fc = ((temperatura -32) * 5 ) / 9

'''Fahrenheit a Kelvin'''
fk = (((temperatura - 32) * 5) / 9) + 273.15



# SALIDA DE DATOS
if unidad_de_medida == "C":
    print("La temperatura en grados kelvin es: ", round (ck, 1), "K" )
    print("La temperatura en grados fahrenheit es: ", round (cf, 1), "°F" )
elif unidad_de_medida == "K":
    print("La temperatura en grados celsius es: ", round (kc, 1), "°C" )
    print("La temperatura en grados fahrenheit es: ", round (kf, 1), "°F" )
else:
    print("La temperatura en grados celsius es: ", round (fc, 1), "°C" )
    print("La temperatura en grados kelvin es: ", round(fk, 1), "K" )

