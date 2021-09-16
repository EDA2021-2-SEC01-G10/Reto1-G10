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

import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

# Construccion de modelos
def newCatalog(ltType):
    """
    Inicializa el catálogo de Artistas y obras. Crea una lista vacia para guardar
    todos los artistas y adicionalmente crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,}

    catalog['artists'] = lt.newList("SINGLE_LINKED")
             
    catalog['artworks'] = lt.newList("SINGLE_LINKED")


def newCatalog_lab4(ltType):
    """
    Inicializa el catálogo de Artistas y obras. Crea una lista vacia para guardar
    todos los artistas y adicionalmente crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    if ltType == 0:
        catalog = {'artists': None,
               'artworks': None,}

        catalog['artists'] = lt.newList("ARRAY_LIST")
                                
        catalog['artworks'] = lt.newList("ARRAY_LIST")

        return catalog

    elif ltType == 1:
        catalog = {'artists': None,
               'artworks': None,}

        catalog['artists'] = lt.newList("SINGLE_LINKED")
             
        catalog['artworks'] = lt.newList("SINGLE_LINKED")

        return catalog
     

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas                
    lt.addLast(catalog['artists'], artist)

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)    
 
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
     Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
     Args:
     artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
     artwork2: informacion de la segunda obra que incluye su valor "DateAcquired"
     """
    return ((str(artwork1['DateAcquired']) < str(artwork2['DateAcquired'])))


def compareArtist(artistname1, artist):
    if artistname1.lower() in artist["DisplayName"].lower():
        return 0
    return -1

# Funciones de ordenamiento

def sortAdquisisiones(catalog,size,sortType):
    if size > lt.size(catalog['artworks']): 
       return ("El tamaño de la muestra que desea consultar es mayor a los datos cargados.") 
    else: 
        sub_List=lt.subList(catalog['artworks'], 1, size)
        sub_List=sub_List.copy()
        if sortType == 1: 
            start_time = time.process_time()
            sorted_list= insertion.sort(sub_List, cmpArtworkByDateAcquired)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            return (elapsed_time_mseg)
        elif sortType == 2: 
            start_time = time.process_time()
            sorted_list= shell.sort(sub_List, cmpArtworkByDateAcquired)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            return (elapsed_time_mseg)
        elif sortType == 3: 
            start_time = time.process_time()
            sorted_list= merge.sort(sub_List, cmpArtworkByDateAcquired)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            return (elapsed_time_mseg)
        elif sortType == 4: 
            start_time = time.process_time()
            sorted_list= quick.sort(sub_List, cmpArtworkByDateAcquired)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            return (elapsed_time_mseg)
        else: 
            return ("Selecciones una opcion de ordenamiento valida")