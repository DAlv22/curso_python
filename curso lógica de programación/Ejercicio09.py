# Ejercicio 09
# Calcular la nómina para un empleado en el mes de Enero del 2022 conociendo su pago por día de $250.-

#ENTRADA DE DATOS                                                    

mes = (input("Qué mes es: "))
periodo_de_pago = (input("El pago es mensual o quincenal: "))
sueldo = int(input("Cual es el sueldo bruto: "))


# PROCESO
sueldo_neto = (((sueldo * 1.16) - (2/3 * (sueldo * .16))) - (sueldo * .1))

if (periodo_de_pago == "Mensual" or periodo_de_pago == "mensual"):
    print ( "El pago neto mensual es de: ", round (sueldo_neto,1), "MXN" )
elif (periodo_de_pago == "Quincenal" or periodo_de_pago == "quincenal"):
    print ( "El pago neto quincenal: ", round (sueldo_neto,1), "MXN" )


# El sueldo neto a cobrar es

