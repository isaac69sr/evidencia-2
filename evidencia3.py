import sys
from main import operaciones
from os import error, system
seleccion = 1.5
system('cls')
while seleccion != 3:
    try:
        if seleccion <= 0 or seleccion >= 4: 
            system('cls')
            print("\nDebe elegirse un valor númerico de las opciones presentadas")
        seleccion = int(input("Menu\n1.- Registrar Venta\n2.- Consultar Venta.\n3.- Salir\nOpción Seleccionada: "))
        if seleccion == 1:
            system('cls')
            try:
                operaciones.agregar_vente()
            except Exception:
                print("error de ejecución, intente de nuevo. presione Enter para continuar")
                input()
                system('cls')
        if seleccion == 2:
            system('cls')
            operaciones.consulta_venta()
            a = input("\nEscribe que fecha quieres revisar:\n")
            operaciones.consulta_la_fecha(a)
            #system('cls')
        if seleccion == 3:
            print("Buen Día")
    except Exception:
        print("error desconocido\n Presione enter para continuar.")
        input()
        system('cls')
        

            
           
  