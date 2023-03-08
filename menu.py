import helpers
import os
from ejercicios import ejercicio1
from ejercicios import ejercicio2
from ejercicios import ejercicio3
from ejercicios import ejercicio4
from ejercicios import descomposicion
from ejercicios import ejercicio6
from ejercicios import ejercicio7



def iniciar():
    helpers.limpiar_pantalla()
    print("BIENVENIDO AL MENÚ DE EJERCICIOS DEL PARCIAL")
    print("============================================")
    print("    ELIJA EL EJERCICIO QUE DESEA REALIZAR   ")
    print("============================================")
    print("             1. EJERCICIO 1                 ")
    print("             2. EJERCICIO 2                 ")
    print("             3. EJERCICIO 3                 ")
    print("             4. EJERCICIO 4                 ")
    print("             5. EJERCICIO 5                 ")
    print("             6. EJERCICIO 6                 ")
    print("             7. EJERCICIO 7                 ")
    print("             8. SALIR                       ")
    print("============================================")
    opcion = input("Ingrese la opción que desea: ")
    helpers.limpiar_pantalla()

    if opcion == "1":
        print("EJERCICIO 1")
        nombre1=ejercicio1.RegistroAlumno("zeréP nauJ,01")
        print("La cadena a descomponer es:", nombre1.cadena_corrupta)
        print(ejercicio1.RegistroAlumno.proper_cadena(nombre1.cadena_corrupta))
        
    elif opcion == "2":
        print("EJERCICIO 2")
        ejercicio2.NumeroMagico()

    elif opcion == "3":
        print("EJERCICIO 3")
        print("La lista 1 es:", ejercicio3.Listas.lista_1)
        print("La lista 2 es:", ejercicio3.Listas.lista_2)
        print(ejercicio3.Listas.lista(ejercicio3.Listas.lista_1, ejercicio3.Listas.lista_2))

    elif opcion == "4":
        ejercicio4.tareas()
        
    elif opcion == "5":
        descomposicion.Descomposicion()
    elif opcion == "6":
        ejercicio6.separador()
    elif opcion == "7":
        ejercicio7.Agregar()
    elif opcion == "8":
        helpers.limpiar_pantalla()
        print("Gracias por utilizar el programa")
        os._exit(0)

    input(">>> Presiona ENTER para continuar <<<")
    iniciar()