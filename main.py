from random import randint
import sqlite3

from sqlite3 import Error
import sys
from numpy import true_divide
import pandas as pd
from datetime import date
from datetime import datetime
from os import system

def folio(clave,hoy,newa,newd,newp,newc,grandtotal,iva):
        a = ("asd","c")
        f=2
        try:
            with sqlite3.connect("evidencia3.db") as conn:
                c = conn.cursor()
                #c.execute("CREATE TABLE IF NOT EXISTS autos (clave INTEGER PRIMARY KEY, Fecha DATE NOT NULL, Articulo TEXT NOT NULL, Descripcion TEXT NOT NULL, Precio TEXT NOT NULL, Cantiddad TEXT NOT NULL, Total INTEGER NOT NULL, Iva INTEGER NOT NULL);")
                c.execute("INSERT INTO autos (clave,Fecha,Articulo,Descripcion,Precio,Cantiddad,Total,Iva) VALUES (?,?,?,?,?,?,?,?)",(clave,hoy,str(newa),str(newd),str(newp),str(newc),grandtotal,iva))
                #c.execute("UPDATE proyecto SET nombre = 'Willy' WHERE clave = 2")
                c.execute("SELECT * FROM autos")
                a = c.fetchall()
                #print(a)
                #df = pd.DataFrame(a, columns = ['clave,Fecha,Articulo,Descripcion,Precio,Cantiddad,Total,Iva,a'])
                #print (df)
                #input()
        except Error as e:
            print(e)
        except Exception:
            print(f"se producjo el siguiente error: {sys.exc_info([0])}")
        finally:
            if conn:
                conn.close()

class operaciones:
    def revisa_fecha(fechasel):
        now = datetime.now()
        hoy = now.strftime("%m/%d/%Y")
        la_fecha = datetime.strptime(fechasel,'%m/%d/%Y')
        la_fecha = la_fecha.strftime('%m/%d/%Y')
        if la_fecha > hoy:
            ex="fecha superior a la actual del sistema."
            return ex
    def consulta_la_fecha(consulta):
        try:
            now = datetime.now()
            hoy = now.strftime("%m/%d/%Y")
            la_fecha = datetime.strptime(consulta,'%m/%d/%Y')
            la_fecha = la_fecha.strftime('%m/%d/%Y')
        
            if la_fecha > hoy:
                system('cls')
                print("fecha superior a la fecha actual del sistema.")
                input('\npresione Enter para continuar')
                system('cls')
            else:
                
                try:
                    system('cls')
                    with sqlite3.connect("evidencia3.db") as conn:
                        c = conn.cursor()
                        c.execute("SELECT * FROM autos where Fecha=?", (la_fecha,))
                        
                        a = c.fetchall()
                        
                    
                        if a.__len__() !=0:
                            df = pd.DataFrame(a, columns = ['clave','Fecha','Articulo','Descripcion','Precio','Cantiddad','Total','Iva'])
                            #df = pd.DataFrame(resultado, columns = ['Fecha'])
                            print(df)
                            print("Grant Total $", df['Total'].sum(axis=0)," de la fecha ", la_fecha)
                            input()
                        else:
                            print("Fecha no encontrada.Presione Enter para continuar")
                            input()
                            system('cls')
                except Error as e:
                    print(e)
                except Exception:
                    print(f"se producjo el siguiente error: ")
                finally:
                    if conn:
                        conn.close()
        except Exception:
            print("error en el formato de la fecha.\npresione Enter para continuar.")
            input()
            system('cls')
    def consulta_venta():
        try:
            with sqlite3.connect("evidencia3.db") as conn:
                c = conn.cursor()
                c.execute("SELECT Fecha FROM autos")
                a = c.fetchall()
                df = pd.DataFrame(a, columns = ['Fecha'])
                print (df)
                
                
        except Error as e:
            print(e)
        except Exception:
            print(f"se producjo el siguiente error: {sys.exc_info([0])}")
        finally:
            if conn:
                conn.close()
    
    def agregar_vente():
        aa = str(randint(2019,2021))
        mm = str(randint(1,12))
        dd = str(randint(1,28))
        rnd = mm+"/"+dd+"/"+aa
        rnd_date = datetime.strptime(rnd,'%m/%d/%Y')
        rnd_date = rnd_date.strftime('%m/%d/%Y')
        clave =2
        now = datetime.now()
        hoy = now.strftime("%m/%d/%Y")
        articulo = []
        descripcion =[]
        precio = []
        cantidad = []
        grandtotal = 0
        a = ""
        b = ""
        cnt = 0
        jj = 0
        articulos = ""
        while cnt != "2":
            
            while a == "" or a.isspace():
                a = input("Escriba el Articulo: ")
                jj += 1
                if jj > 1:
                    system('cls')
                    print("\n Nombre vacio o rellenado con espacio, escriba correctamente el nombre del articulo\n")

            jj = 0
            system('cls')
            while b == "" or b.isspace():
                b = input("Descripción el Articulo: ")
                jj += 1
                if jj > 2:
                    system('cls')
                    print("\n Nombre vacio o rellenado con espacio, escriba correctamente la descripcion del articulo\n")
            system('cls')
            print("Articulo: ",a,"\n")
            print("Descripción: ",b,"\n")
            c = int(input("\nPrecio:"))
            while c <= 0:
                c = int(input("\nEl precio debe ser mayor a 0, ingrese de nuevo el precio.\n"))
            d = int(input("\nCantidad de articulos:"))
            while d <= 0 :
                d = int(input("\nLa cantidad de articulos debe ser mayor a 0, ingrese de nuevo el precio.\n"))

            cnt = input("\nDesea Agregar un nuevo Artiuclo?\n1.-Agregar articulo a venta\n2.-Finalizar compra.\nSelección:")
            system('cls')
            articulos = articulos + a + ","
            articulo.append(a)
            descripcion.append(b)
            precio.append(c)
            cantidad.append(d)
            grandtotal += int(c) * int(d)
            iva = grandtotal*.16
            jj= 0
            a = ""
            b=  ""
            c = 0

        try:
            with sqlite3.connect("evidencia3.db") as conn:
                c = conn.cursor()
                #c.execute("CREATE TABLE IF NOT EXISTS autos (clave INTEGER PRIMARY KEY, Fecha DATE NOT NULL, Articulo TEXT NOT NULL, Descripcion TEXT NOT NULL, Precio TEXT NOT NULL, Cantiddad TEXT NOT NULL, Total INTEGER NOT NULL, Iva INTEGER NOT NULL);")
                c.execute("SELECT clave FROM autos")
                ccantidad = c.fetchall().__len__()
                clave = ccantidad + 2
                c.execute("INSERT INTO autos (clave,Fecha,Articulo,Descripcion,Precio,Cantiddad,Total,Iva) VALUES (?,?,?,?,?,?,?,?)",(clave,hoy,articulos,str(descripcion),str(precio),str(cantidad),grandtotal,iva))
                #c.execute("UPDATE proyecto SET nombre = 'Willy' WHERE clave = 2")
                c.execute("SELECT * FROM autos")
                a = c.fetchall()
                #print(a)
                #df = pd.DataFrame(a, columns = ['clave,Fecha,Articulo,Descripcion,Precio,Cantiddad,Total,Iva,a'])
                #print (df)
                #input()
        except Error as e:
            print(e)
        except Exception:
            print(f"se producjo el siguiente error: {sys.exc_info([0])}")
        finally:
            if conn:
                conn.close()
        print("Venta de: ", articulos, "\n", "Total de $",grandtotal,"Iva correspondiente$ ",iva,"\nTotal + iva $", grandtotal+iva,"\nAlmacenado al día de: ", hoy)
        input("\nPresione enter para continuar.")
        system('cls')
    
class error(Exception):
    """El valor debe ser superior a 0"""
    pass

    
    

