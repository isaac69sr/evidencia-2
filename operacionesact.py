import datetime
from math import trunc
import os
from random import randint, random
from datetime import date
from os import system
from os import path
from datetime import datetime
from numpy.lib.function_base import append
import pandas as pd
from os.path import exists

#IMPORTACION DE LIBRERIAS
now = datetime.now()
otra = []
hoy = now.strftime("%m/%d/%Y")
#CONTROL DE FECHA
#df = pd
#diccionario = {5:["refacciones","descripciones","precio","s","i"]}
lista_ani =  [["NA","NA","NA","NA","NA","NA"]]
ress = pd
diccionario = {}    
#CREACION DE DICCIONARIO VACIO
def fecha_folio(r,d,c,s,i):
  a = randint(1,9)
  b = randint(1,9)
  j = randint(1,4)
  #ESTOS VALORES REPRESENTAN UN CODIGO ALEATORIO AUTOGENERADO PUEDE REPERIRSE DEBIDO A UN ERROR QUE NO ALCANCE A INVESTIGAR
  aa = str(randint(2019,2021))
  mm = str(randint(1,12))
  dd = str(randint(1,28))
  rnd = mm+"/"+dd+"/"+aa
  rnd_date = datetime.strptime(rnd,'%m/%d/%Y')
  rnd_date = rnd_date.strftime('%m/%d/%Y')
  #ESTAS FUNCIONES DE AQUI SE CREARON CON LA INTENCION DE CREAR FECHAS ALEATORIAS PARA QUE NO TODAS FUERAN EL DIA EN QUE SE CODIFICO
  idenfy = (a*100) + (b * 10) + j

  system('cls')
  elemento = [idenfy,hoy,r,d,c,s,i]
  #SE CREA UNA LISTA CON LA INTENCION DE AGREGARLA A LAS LISTAS ANIDADAS EN LA VARIABLE OTRA QUE REPRESENTA LO RESCATADO EN EL CSV
  if os.path.exists('a.csv'):
    otra = pd.read_csv("a.csv").values.tolist()
    otra.append(elemento)
    operaciones.save_csv(otra)
    #SE AGREGA AL CSV Y SE MANDA A LA FUNCION SAVE_CSV PARA QUE QUEDEN RESGUARDADA EN DISCO
    print("Folio: ",idenfy," Fecha: ", hoy, "\nCantidad de articulos: ", r.__len__(), "\nCompra total de: $", s, 
    "\nIva correspondiente: $", i, "\nTotal a pagar: $",s+i,"\nPrecione tecla \"enter\" para continuar")
  else:
    df = pd.DataFrame([elemento], columns = ['Codigo','Dia Venta','Articulos','Descripcion','Precio','Transacción Total','IVA'])
    df.to_csv('a.csv', index=False)
    print("Folio: ",idenfy," Fecha: ", hoy, "\nCantidad de articulos: ", r.__len__(), "\nCompra total de: $", s, 
    "\nIva correspondiente: $", i, "\nTotal a pagar: $",s+i,"\nPrecione tecla \"enter\" para continuar")

  #POR MEDIO DE LA FUNCION PATHEXIST PODEMOS DETERMINAR SI EXISTE O NO EL ARCHIVO DESDE DONDE SE EJECUTA, PARA CREARLO O LEERLO Y GUARDARLO
class operaciones:
    def agregar_venta():

      suma = 0
      continuar = 0
      while continuar != "2":
        system('cls')
        print("Venta\n************************************\n")
        Art = input("Articulo de Venta: ")
        Desc = input("Redacte una breve descripción: ")
        prec = input("adjente el precio (omitir signo de denominación ): ")
        if suma == 0:
          refacciones = [Art]
          descripciones = [Desc]
          precio = [prec]
          #CREACION DINAMICA DE LISTA POR PRIMERAE OCASIÓN
        else:
          refacciones[len(refacciones):] = [Art]
          descripciones[len(descripciones):] = [Desc] 
          precio[len(precio):] = [prec]
          #AGREGAR CONTENIDO A LA LISTA EN EL CASO DE QUE SE AGREGUE NUEVOS REFACCION A LA VENTA
        suma = suma + int(prec)
        iva = suma*.16
        continuar = input("¿Desea agregar un nuevo articulo? 1.- agregar articulo 2.- Para finalizar venta.\nSelección: ")
        system('cls')
      fecha_folio(refacciones,descripciones,precio,suma,iva) ##MANDAMOS LLAMAR AL METODO FECHA_FOLIO PARA CREAR EL FOLIO, Y ENVIAMOS LOS DATOS RESULTANTES
      ##DE LAS LISTAS DE REFACCIONES, DESC, Y PRECIOS, TANTO LA SUMA Y EL IVA

    def mostrar_venta():
      conteo = 1
      system('cls')
      print("Registro de Venta por Código\n************************************\n")
      for key in diccionario.keys() :
        print (conteo,"-: ", key)
        conteo += 1
    ##IMPRESIÓN DE LAS LLAVES O CLAVES DE LAS LISTAS PARA IDENTIFICAR LA VENTA QUE QUEREMOS DESPLEGAR
    def detalle_venta(f):
      rnd_date = datetime.strptime(f,'%m/%d/%Y')
      rnd_date = rnd_date.strftime('%m/%d/%Y')
      #CONVERSION DE LA VARIABLE F QUE RECIBIMOS DEL ARCHIVO PRINCIPAL A TIPO FECHA
      system('cls')
      lista_ani = pd.read_csv("a.csv")
      df = pd.DataFrame(lista_ani, columns = ['Codigo','Dia Venta','Articulos','Descripcion','Precio','Transacción Total','IVA']) 
      dat = 0
      resumen=[]
      total = 0
      iva_total = 0
      #A ESTE PUNTO LEEMOS EL CSV, LE DAMOS FORMATO Y PROCEDEMOS A LEER LA COLUMNA VENTA Y OBTENER SU VALOR PARA COMPARARLO CON F QUE REPRESENTA EL VALOR RECIBIDO
      while df.__len__()!= dat:
        
        if rnd_date == df['Dia Venta'].__getitem__(dat):
          data = [df['Codigo'].__getitem__(dat),df['Articulos'].__getitem__(dat),df['Transacción Total'].__getitem__(dat),df['IVA'].__getitem__(dat)]
          resumen.append(data)
          #UNA VEZ QUE ENCONTRAMOS UNA COINCIDENCIA EN FECHA, LAS GUARDAMOS EN UNA LISTA ANIDAD, COMO SI FUERAMOS A GUARDAR UN ARCHIVO NUEVO DE CSV
          #print(df['Codigo'].__getitem__(dat)) 
          total = total + df['Transacción Total'].__getitem__(dat)
          iva_total = total + df['IVA'].__getitem__(dat)
        dat += 1
        
      if total !=0:
        xx = pd.DataFrame(resumen, columns = ['Codigo','Articulos','Total','Iva'])
        print(xx)
        print("\n Gran Total de la cuenta del día: ",f," $",total )
        #LES DAMOS FORMATO DE TABLA Y LAS IMPRIMIMOS EN PANTALLA, MUENTRAS SE REALIZA LA EXPLORACIÓN SE SUMA EL TOTAL Y SE IMPRIME AL FINAL
      else:
        print("Fecha no encontrada\n Presione enter para continuar")
#impresion tabulador CODIGO PARA IMPRIMIR REVISAMOS LA EXISTENCIA DEL ARCHIVO,
    def imprimir_Est():
      if FileExistsError == 0:
        lista_ani = pd.read_csv("a.csv")
        df = pd.DataFrame(lista_ani, columns = ['Codigo','Dia Venta','Articulos','Descripcion','Precio','Transacción Total','IVA'])
        print(df[["Codigo","Dia Venta"]])
      else:
        lista_ani = pd.read_csv("a.csv")
        df = pd.DataFrame(lista_ani, columns = ['Codigo','Dia Venta','Articulos','Descripcion','Precio','Transacción Total','IVA'])
        print(df[["Codigo","Dia Venta"]]) 
      ##.__getitem__(0)[0]
    def save_csv(lista):
        df = pd.DataFrame(lista, columns = ['Codigo','Dia Venta','Articulos','Descripcion','Precio','Transacción Total','IVA'])
        df.to_csv('a.csv', index=False)
      #print(rnd)  
    def cargar():
      nota = pd.read_csv("a.csv")
      lista_ani = nota
      print(lista_ani)
      
  
    
      
          
       
    
    
    



    


      
        


