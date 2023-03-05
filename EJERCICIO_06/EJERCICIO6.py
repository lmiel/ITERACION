"""Ejercicio 6: Historial de una cuenta corriente
Se quiere conservar el historial de los movimientos mensuales en una cuenta corriente.
1. Modificar el tipo CUENTA definido en el capítulo «Estructuras elementales» para conservar el rastro de los movimientos en una cuenta durante un mes.
2. Establecer el saldo a final de mes de una cuenta dada.
El saldo ya no es un atributo de la cuenta. Se obtiene recorriendo el historial mensual y anual que registra el importe del saldo de la cuenta para cada mes.
3. Rehacer las definiciones anteriores.
Una tabla clientes contiene las cuentas corrientes de un conjunto de clientes.
4. Determinar los clientes para los que la media de los importes de los movimientos es superior a una suma dada."""

"""cuenta = [nombre, [movimientos]]
movimientos = [saldo]"""
import statistics

clientes = []

while input("¿Quiere crear un cliente? (SI/NO): ") == "SI":
    cuenta_corriente = input("¿Desea abrir una cuenta corriente? (SI/NO): ")

    if cuenta_corriente == "NO":
        print("No se ha abierto una cuenta corriente")
    elif cuenta_corriente == "SI":
        print("Esta usted en su cuenta corriente")
        cuenta = [[]]
        nombre = input("¿Cual es su nombre?: ")
        cuenta = [nombre, [0]]
        print("Su saldo es de: ", cuenta[1][0]) #En la segunda posicion de cuenta, en la primera posicion de movimientos
        while input("¿Desea realizar un movimiento? (SI/NO): ") == "SI":
            ingreso = input("¿Desea realizar un ingreso? (SI/NO): ")
            if ingreso == "SI":
                cantidad_ingresar= int(input("¿Cuanto desea ingresar?: "))
                cuenta[1].append(cantidad_ingresar)
            else:
                print("No se ha realizado ningun ingreso")
            retirar = input("¿Desea retirar dinero? (SI/NO): ")
            if retirar == "SI":
                cantidad_retirar = int(input("¿Cuanto desea retirar?: "))
                cuenta[1].append(-cantidad_retirar)
            else:
                print("No se ha retirado dinero")

    saldo = 0
    for movimiento in cuenta[1]: #Recorre la lista de movimientos
        saldo = saldo + movimiento
    print("Su saldo es de: ", saldo)

    clientes.append(cuenta)

valor_medio = int(input("Introduzca un valor medio: "))
    
for cliente in clientes:
    media = statistics.mean(cliente[1])
    if media > valor_medio:
        print("La media de los movimientos de ", cliente[0], " es superior a ", valor_medio)
    
    