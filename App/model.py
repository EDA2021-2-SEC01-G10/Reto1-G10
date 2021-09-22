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
from datetime import date
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
 
# Funciones para creacion de datos

# Funciones de consulta y creacion de sublistas
def subListarCronologicamenteArtistas(sortArtistas,añoInicial,añoFinal):   
    subListSortArtists=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(sortArtistas)):
        añoBegin=int(sortArtistas["elements"][i]["BeginDate"])
        if añoBegin >= añoInicial and añoBegin <= añoFinal : 
           artista=sortArtistas["elements"][i]
           lt.addLast(subListSortArtists,artista)
    return subListSortArtists           
            
def subListarCronologicamenteAdquisisiones(sortArtworks,fechaInicial,fechaFinal):     
    fechaInDate = datetime.strptime(fechaInicial.strip(), "%Y-%m-%d")
    fechaFinDate= datetime.strptime(fechaFinal.strip(), "%Y-%m-%d")
    subListSortArtworks=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(sortArtworks)): 
        dateAcquired=sortArtworks["elements"][i]["DateAcquired"]
        if dateAcquired != "" : 
           dateAcquiredDate=datetime.strptime(dateAcquired.strip(), "%Y-%m-%d")
           if dateAcquiredDate >= fechaInDate and dateAcquiredDate <= fechaFinDate: 
              artwork=sortArtworks["elements"][i]
              lt.addLast(subListSortArtworks,artwork)      
    return subListSortArtworks

def idArtist(catalog, nombreArtista): 
    artistascat=catalog["artists"]["elements"]
    artistas=lt.newList("ARRAY_LIST")
    for artist in artistascat: 
         lt.addLast(artistas,artist)
    for i in range (1,lt.size(artistas)):
        nombre=artistas["elements"][i]["DisplayName"]  
        if nombreArtista.strip() == nombre.strip() : 
           id=(artistas["elements"][i]['ConstituentID'])        
           return id 
    return ("Error")    

def obrasArtist(catalog,id): 
     obrascat=catalog["artworks"]["elements"]
     obrasArtista=lt.newList("ARRAY_LIST")
     for obra in obrascat: 
         idObra=(obra["ConstituentID"])
         idObra=idObra.replace("]","")
         idObra=idObra.replace("[","")
         idObra=idObra.split(",")
         if str(id) in idObra: 
             lt.addLast(obrasArtista,obra)  
     return obrasArtista   
         
     
            

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


# Funciones de ordenamiento

def sortArtistasCronologicamente(catalog):
     artistascat=catalog["artists"]["elements"]
     artistas=lt.newList("ARRAY_LIST")
     for artist in artistascat: 
         lt.addLast(artistas,artist)
     artistasOrdenados=merge.sort(artistas,cmpArtistByBeginDate)    
     return artistasOrdenados
     
def sortObrasCronologicamente(catalog):
    artworksCat=catalog["artworks"]["elements"]
    artworks=lt.newList("ARRAY_LIST")
    for artwork in artworksCat: 
         lt.addLast(artworks,artwork)
    artworksOrdenados=merge.sort(artworks,cmpArtworkByDateAcquired)    
    return artworksOrdenados