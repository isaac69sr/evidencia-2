from os import system
from datetime import datetime, time
from operacionesact import  operaciones, diccionario
##importación de librerias, y librerias personalizada

now = datetime.now()
hoy = now.strftime("%m/%d/%Y")
folio = 0
datos = ["1","2","3"]
seleccion = 1

##Menu
while seleccion != "3":
    system('cls')
    print("Menu\n1.- Registrar Venta\n2.- Consultar Venta.\n3.- Salir\nOpción Seleccionada: ")
    if seleccion == "1":
        system('cls')
        operaciones.agregar_venta()

        ##CICLO MENU
    if seleccion == "2":
        ##UTILIZACION DE EXPECTIONES PARA EVITAR CORTES EN BUSQUEDA POR FALTA DE ARCHIVO O FECHA SIN FORMATO
        system('cls')
        try:
            operaciones.imprimir_Est()
            print("Para ver detallada la información esriba una fecha en el formato:MM/DD/AAAA:\n Su selección: ")
            x = input()
            try:
                operaciones.detalle_venta(x)
            except:
                print("Error, Formato no admitido. MM/DD/AAAA \n Enter para continuar.")
        except:
            print("Información no encontrada. \n Enter para continuar.")
    if seleccion == "3":
        
        print("Buen Día")
    seleccion = input()




##print(diccionario[0].__getitem__(1)[0]) ## asi seleccionamos en un diccionario un elemento dentro de una lista que esta dentro de un diccionario