"""Ejercicio 9: Búsqueda de palabras en un diccionario
Sea una tabla de PALABRAS en español. Las palabras se guardan en una tabla llamada diccionario. Se utilizan otras dos tablas para recorrer el diccionario. Para cada palabra, una tabla llamada siguiente da el número de la celda ocupada por la palabra que le sigue en orden alfabético en el diccionario. La tabla anterior también da, para cada palabra, el número de la celda del diccionario que contiene la palabra anterior en orden alfabético. A la primera palabra de la lista ordenada le corresponde un número de celda del anterior igual a índice_min(diccionario) - 1. Igualmente, a la última palabra de la lista ordenada le corresponde un número de celda de la siguiente igual al mismo valor. La tabla que aparece debajo muestra un ejemplo de estas tres tablas.

i       diccionario     anterior        siguiente

1          avión            3               4
2          tren             4              ...
3          auto             0               1
4         camión            1               2
5          ...             ...             ...

Se ve que para ‘camión’, en la celda 4, la palabra siguiente en orden alfabético ocupa la celda 2 y la anterior ocupa la celda 1. Entonces, el orden alfabético de estas tres palabras es ‘avión’, ‘camión’ y ‘tren’.
1. Escribir el algoritmo que da la lista de las palabras guardadas empezando por una letra dada.
Así, por ejemplo, el algoritmo aplicado a la lista anterior dará (‘avión’, ‘auto’) para la letra ’a’.
También es posible definir un tipo nuevo de datos, PALABRA, formado con una cadena de caracteres para la palabra propiamente dicha y con dos números enteros para descubrir la palabra anterior y la siguiente en el diccionario. En este caso, el diccionario se convierte en una simple tabla de PALABRAS.
2. Definir el tipo PALABRA y rehacer el algoritmo anterior para utilizarlo.
3. Escribir el algoritmo que permite añadir una palabra nueva al diccionario.
4. Escribir el algoritmo de eliminación de una palabra.
Puede encontrar este ejercicio resuelto y la solución analizada en los elementos disponibles para descargar desde la página Información."""
diccionario =   [["limón", 9, 1],
["manzana", 0, 2],
["melocotón", 1, 8],
["banana", -1, 4],
["fresa", 3, 9],
["uva", 6, -1],
["sandía", 7, 5],
["pera", 8, 6],
["naranja", 2, 7],
["kiwi", 4, 0]]

primera_palabra = 3
ultima_palabra = 5

def buscar_palabra():
    letra = input("Introduzca la letra por la que empiecen las palabras que desee buscar: ")
    i = primera_palabra
    for palabra in range(len(diccionario)):
        if diccionario[i][0][0] == letra:
            break
        else:
            i = diccionario[i][2]
    solucion = []
    while diccionario[i][0][0] == letra:
        solucion.append(diccionario[i][0])
        i = diccionario[i][2]
    print(solucion)


buscar_palabra()
