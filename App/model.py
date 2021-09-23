"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
from datetime import datetime 
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de Artistas y obras. Crea una lista vacia para guardar
    todos los artistas y adicionalmente crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,}

    catalog['artists'] = lt.newList("ARRAY_LIST")
             
    catalog['artworks'] = lt.newList("ARRAY_LIST")
    
    return catalog 
# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas                
    lt.addLast(catalog['artists'], artist)

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)    
 

# Funciones de consulta y creacion de sublistas
def subListarDepartamento(catalog,departamento):
    subListaDepartamento=lt.newList("ARRAY_LIST")
    for i in lt.iterator(catalog["artworks"]):
        departamentoObra=i["Department"]
        if departamentoObra == departamento: 
           lt.addLast(subListaDepartamento,i)
    return subListaDepartamento
           
def subListarCronologicamenteArtistas(sortArtistas,añoInicial,añoFinal):   
    subListSortArtists=lt.newList("ARRAY_LIST")
    for i in lt.iterator(sortArtistas):
        añoBegin=int(i["BeginDate"])
        if añoBegin >= añoInicial and añoBegin <= añoFinal : 
           artista=i
           lt.addLast(subListSortArtists,artista)
    return subListSortArtists           
            
def subListarCronologicamenteAdquisisiones(sortArtworks,fechaInicial,fechaFinal):     
    fechaInDate = datetime.strptime(fechaInicial.strip(), "%Y-%m-%d")
    fechaFinDate= datetime.strptime(fechaFinal.strip(), "%Y-%m-%d")
    subListSortArtworks=lt.newList("ARRAY_LIST")
    for i in lt.iterator(sortArtworks):
        dateAcquired=i["DateAcquired"]
        if dateAcquired != "" : 
           dateAcquiredDate=datetime.strptime(dateAcquired.strip(), "%Y-%m-%d")
           if dateAcquiredDate >= fechaInDate and dateAcquiredDate <= fechaFinDate: 
              artwork=i
              lt.addLast(subListSortArtworks,artwork)      
    return subListSortArtworks

def idArtist(catalog, nombreArtista): 
    artistas=lt.newList("ARRAY_LIST")
    for artist in lt.iterator(catalog["artists"]): 
         lt.addLast(artistas,artist)
    for i in lt.iterator(artistas):
        nombre=i["DisplayName"]  
        if nombreArtista.strip() == nombre.strip() : 
           id=i['ConstituentID']      
           return id 
    return ("Error")    

def obrasArtist(catalog,id): 
     obrasArtista=lt.newList("ARRAY_LIST")
     for obra in lt.iterator(catalog["artworks"]):
         idObra=obra["ConstituentID"]
         idObra=idObra.replace("]","")
         idObra=idObra.replace("[","")
         idObra=idObra.split(",")
         if str(id) in idObra: 
             lt.addLast(obrasArtista,obra)  
     return obrasArtista   
         
def sacarPrecios(listDepartamento):
    preciosObras=lt.newList("ARRAY_LIST")
    for i in lt.iterator(listDepartamento): 
        dimensiones=[]
        alturaObra=i["Height (cm)"] 
        anchuraObra=i["Width (cm)"]    
        profundidadObra=i["Depth (cm)"]  
        if alturaObra != "" and alturaObra != "0": 
           alturaObra=float(alturaObra)/100
           dimensiones.append(alturaObra)
        if anchuraObra != "" and anchuraObra != "0": 
           anchuraObra=float(anchuraObra)/100
           dimensiones.append(anchuraObra) 
        if profundidadObra != "" and profundidadObra != "0": 
           profundidadObra=float(profundidadObra)/100
           dimensiones.append(profundidadObra) 
        productoDimensiones=1   
        for dimension in dimensiones:
            productoDimensiones*=dimension        
        preciosObra=[]   
        preciosObra.append(productoDimensiones * 72.00)
        peso=i["Weight (kg)"]   
        if peso != "" and peso != "0": 
           peso=float(peso)  
           preciosObra.append(peso*72.00)
        precioMayor=max(preciosObra)
        i["CostoObra"]=precioMayor             
        lt.addLast(preciosObras,i)   
       
    return preciosObras  
               
            

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
     Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
     Args:
     artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
     artwork2: informacion de la segunda obra que incluye su valor "DateAcquired"
     """
    return ((str(artwork1['DateAcquired']) < str(artwork2['DateAcquired'])))

def cmpArtistByBeginDate(artista1, artista2):
    """
     Devuelve verdadero (True) si el 'BeginDate' de artista1 es menor que el de artista2
     Args:
     artista1: informacion del primer artista que incluye su valor 'BeginDate'
     artista2: informacion del segundo artista que incluye su valor 'BeginDate'
     """
    return ((int(artista1['BeginDate']) < int(artista2['BeginDate'])))

def cmpArtworkByCost (artwork1,artwork2): 
    """
     Devuelve verdadero (True) si el 'CostoObra' de artwork1 es menor que el de artwork2
     Args:
     artwork1: informacion del primer artwork que incluye su valor 'CostoObra'
     artwork2: informacion del segundo artwork que incluye su valor 'CostoObra'
    """
    return ((float(artwork1['CostoObra']) < float(artwork2['CostoObra'])))

def cmpArtworkByDate(artwork1,artwork2): 
    """
     Devuelve verdadero (True) si el 'Date' de artwork1 es menor que el de artwork2
     Args:
     artwork1: informacion del primer artwork que incluye su valor 'Date'
     artwork2: informacion del segundo artwork que incluye su valor 'Date'
    """    
    return ((str(artwork1['Date']) < str(artwork2['Date'])))

# Funciones de ordenamiento

def sortArtistasCronologicamente(catalog):
     artistas=lt.newList("ARRAY_LIST")
     for artist in lt.iterator(catalog["artists"]): 
         lt.addLast(artistas,artist)
     artistasOrdenados=merge.sort(artistas,cmpArtistByBeginDate)    
     return artistasOrdenados
     
def sortObrasCronologicamente(catalog):
    artworks=lt.newList("ARRAY_LIST")
    for artwork in lt.iterator(catalog["artworks"]):
         lt.addLast(artworks,artwork)
    artworksOrdenados=merge.sort(artworks,cmpArtworkByDateAcquired)    
    return artworksOrdenados

def ordenarPorCosto(precios):
    obrasConPrecio=lt.newList("ARRAY_LIST")  
    for obra in lt.iterator(precios):
         lt.addLast(obrasConPrecio,obra)
    obrasConPrecioOrdenados=merge.sort(obrasConPrecio,cmpArtworkByCost)    
    return obrasConPrecioOrdenados 

def ordenarPorFecha(precios):     
    obrasPorFecha=lt.newList("ARRAY_LIST")  
    for obra in lt.iterator(precios):
         lt.addLast(obrasPorFecha,obra)
    obrasPorFechaOrdenadas=merge.sort(obrasPorFecha,cmpArtworkByDate)    
    return obrasPorFechaOrdenadas 