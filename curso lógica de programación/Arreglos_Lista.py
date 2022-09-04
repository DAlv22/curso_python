# ARREGLOS / LISTAS
# Es el conjunto de valores o elementos de uno o más tipos de datos
# SINTAXIS
'''

nombre_del_arreglo_lista = [valores/elementos]
'''

# Declarar o crear arreglos o listas

nombres_de_pila = ["Dulce", "Eduardo", "Juan", "Toñita"]
# Índice (index)       0      1           2        3
edades = [30,31, 17, 15]
# Índice   0, 1,  2,  3

array_list = [20, 5.8, "Hola", True]


# PROCESOS (Operaciones o funciones aplicadas a los arreglos)
''' Modificar un elemento del arreglo'''
nombres_de_pila[0] = "Dulce Carolina"
edades[2] = 20
array_list[3] = False


''' Agregar un elemento al arreglo '''
nombres_de_pila.append("Roberto")
edades.append(40)
array_list.append(8.1)


''' Eliminar un elemento del arreglo'''
nombres_de_pila.pop(1)
edades.pop(1)
array_list.pop(4)


'''Ordenar elementos del arreglo'''
nombres_de_pila.sort()  # Ordenar Alfabéticamente ASCENDENTE
edades.sort()  # Ordenar valores ASC

nombres_de_pila.reverse()  # Ordenar valores DESCENDENTE
edades.reverse() # Ordenar valores DESCENDENTE

# Salida de datos
print(nombres_de_pila)
print(edades)
print(array_list)

