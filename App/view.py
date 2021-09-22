"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from typing import KeysView
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información de los artistas y obras")
    print("2- (Req.1) Listar cronológicamente los artistas")
    print("3- (Req.2) Listar cronológicamente las adquisiciones")
    print("4- (Req.3) Clasificar las obras de un artista por técnica")
    print("5- (Req.4) Clasificar las obras por la nacionalidad de sus creadores ")
    print("6- (Req.5) Transportar obras de un departamento ")
    print("7- (Req.6) proponer una nueva exposición en el museo")
    print("8- mostrar")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de artistas y obras 
    """
    return controller.initCatalog()


def loadData(catalog): 
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def listarCronologicamenteArtistas(catalog,añoInicial,añoFinal):    
    """
    Inicializa la funcion listar cronologicamente artistas en el controlador
    """
    listArtistas=controller.listarCronologicamenteArtistas(catalog,añoInicial,añoFinal)
    return listArtistas

def listarAdquisisionesCronologicamente(catalog,fechaInicial,fechaFinal):
    listAdquisisiones=controller.listarAdquisisionesCronologicamente(catalog,fechaInicial,fechaFinal)
    return listAdquisisiones

def listaObrasArtista(catalog, nombreArtista):   
    listaObras=controller.listarObrasArtista(catalog, nombreArtista)
    return listaObras 

def prueba(catalog):
    s=controller.sortObrasCronologicamente(catalog)
    return s 
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
       
    elif int(inputs[0]) == 2:
         añoInicial=int(input("Ingrese el año de nacimiento para el rango inicial de artistas deseado:"))
         añoFinal=int(input("Ingrese el año de nacimiento para el rango final de artistas deseado:"))
         listaArtistas=listarCronologicamenteArtistas(catalog,añoInicial,añoFinal)
         print("Hay " + str(lt.size(listaArtistas)) +" artistas nacidos entre "+str(añoInicial)+" y "+str(añoFinal))

    elif int(inputs[0]) == 3:
        fechaInicial=input("Ingrese la fecha que desee consultar como rango inicial de las adquisisiones: ")
        fechaFinal=input("Ingrese la fecha que desee consultar como rango final de las adquisisiones: ")
        listAdquisisiones=listarAdquisisionesCronologicamente(catalog,fechaInicial,fechaFinal)
        print("El MoMA adquirio "+str(lt.size(listAdquisisiones))+" piezas unicas entre "+fechaInicial+" y "+fechaFinal) 
        compradas=0          
        for i in lt.iterator(listAdquisisiones):
            creditLine=i["CreditLine"]
            if creditLine == "Purchase":
               compradas+=1
        print("Con un total de "+str(compradas)+" obras compradas.")  

    elif int(inputs[0]) == 4:
         nombreArtista=input("Ingrese el nombre del artista que desea consultar: ")
         retorno=listaObrasArtista(catalog,nombreArtista)
         obras=retorno[1]
         id=retorno[0]
         print (nombreArtista+" con MoMA ID "+id+" tiene "+str(lt.size(obras))+" piezas con su nombre en el museo.")
    
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass  
    elif int(inputs[0]) == 8:
         for i in lt.iterator(catalog["artists"]):
             print(i)
    else:
        sys.exit(0)
sys.exit(0)


