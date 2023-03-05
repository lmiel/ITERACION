"""Ejercicio 7: Edición de un número entero
1. Escribir un algoritmo iterativo que transforme un número entero n cualquiera en su representación en una base B ≥ 2 cualquiera.
Cuando la base es superior a 36, se puede utilizar la representación de los números en base diez, pero separando cada cifra de la representación del número en base B mediante un separador convenido, por ejemplo, un punto. Eso es lo que se usa para expresar, por ejemplo, la dirección IP de un host en una red con IPv4. Así, por ejemplo, la representación en base 256 de 3000, expresada aquí en base diez, se escribirá: 11 184256 = 3000diez.
Este ejercicio está completamente resuelto en el capítulo «Edición de un número». """

n = int(input("Introduzca un numero entero: "))
base = int(input("Introduzca una base: "))
resultado = []
valores = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 
    15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 
    20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 
    25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 
    30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 
    35: 'Z'
}

if base < 2:
    print("La base debe ser mayor o igual que 2")
elif base < 36:
    cociente = n//base
    resto = n%base
    resultado.append(valores[resto])
    while cociente > base:
        cociente = cociente//base
        resto = cociente%base
        resultado.append(valores[resto])
    resultado.append(valores[cociente])
    resultado.reverse()
    print(resultado)
else:
    cociente = n//base
    resto = n%base
    resultado.append("." + str(resto))
    while cociente > base:
        cociente = cociente//base
        resto = cociente%base
        resultado.append("." + str(resto))
    resultado.append(str(cociente))
    resultado.reverse()
    print(resultado)

