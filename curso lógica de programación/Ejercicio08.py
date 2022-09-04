# 8. Obtener un número y determinar lo siguiente:
    # a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
    # b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
    # c) en otro caso imprimir No Válido


# número = int(input("Coloca el número a trabajar: "))



# if (número < 0 and número >= -100):			
# 	while (número < 0 and número >= -100):		
# 		print(número)	
# 		número = número + 2 	
# elif (número >= 0 and número <= 100):
#     while (número >= 0 and número <= 100):
#         print(número)	
# 		número = número -1


# número = 50
# while(número < 0 and número >= -100):
#     if (número < 0 and número >= -100):                                  
#         print(número)                                
#         número = número - 2
#     elif (número >= 0 and número <= 100):
#         while(número >= 0 and número <= 100):          
#             print(número)                                
#             número = número + 2


# número = -101
# while (número < 0 and número >= -100):
#     if (número < 0 and número >= -100):                                  
#         print(número)                                
#         número = número - 2
# while (número >= 0 and número <= 100):
#     if (número >= 0 and número <= 100):          
#         print(número)                               
#         número = número + 2



# ENTRADA DE DATOS

número = int(input("Ingrese un número entero entre el -100 al 100: "))  # SER ESPECIFICOS CON EL USUARIO

Num_Impar = -1
Num_Par = 2 



# PROCESOS y SALIDA DE DATOS    ESTE FUE EL BUENO

# if (número < 0 and número >= -100):
#     print("Los números impares son: ")           # SÓLO PARA DENOTAR LOS NUMS IMPARES QUE SE DEVUELVEN
#     while (Num_Impar < 0 and Num_Impar >= -100):                
#         print(Num_Impar)                           
#         Num_Impar = Num_Impar - 2
# elif (número >0 and número <= 100):
#     print("Los números pares son: ")              # LO MISMO, PARA DENOTAR LOS PARES
#     while (Num_Par > 0 and Num_Par <= 100):          
#         print(Num_Par)                               
#         Num_Par = Num_Par + 2
# else:
#     print("El número ingresado no es válido")


if (número < 0 and número >= -100):
    print("Los números impares son: ")           
    for i in range(Num_Impar, -101, - 2):              
        print(i)                           
elif (número >0 and número <= 100):
    print("Los números pares son: ")             
    for i in range(Num_Par, 101, + 2):          
        print(i)                               
else:
    print("El número ingresado no es válido")

