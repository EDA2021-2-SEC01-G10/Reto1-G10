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
 """

import config as cf
import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos en la
    estructura de datos.
    """
    loadArtists(catalog)
    loadArtworks(catalog)
    

def loadArtists(catalog):
    """
    Carga todos los artistas del archivo y los agrega a la lista de artistas.
    """ 
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist) 
    

def loadArtworks(catalog):
    """
    Carga todos las obras del archivo y los agrega a la lista de obras.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)        
     

# Funciones de ordenamiento
def sortArtistasCronologicamente(catalog):
    """
    Llama la funcion sortArtistasCronologicamente del modelo y retorna la lista de artistas ordenada.
    """
    listSorted=model.sortArtistasCronologicamente(catalog)
    return listSorted

def sortObrasCronologicamente(catalog):
    """
    Llama la funcion sortObrasCronologicamente del modelo y retorna la lista de obras ordenada.
    """
    sortedArtworks=model.sortObrasCronologicamente(catalog)
    return sortedArtworks

def subListarCronologicamenteArtistas(sortArtistas,añoInicial,añoFinal):
    """
    Llama la funcion subListarCronologicamenteArtistas del modelo y retorna la sublista de artistas con el rango deseado.
    """
    subListSorted=model.subListarCronologicamenteArtistas(sortArtistas,añoInicial,añoFinal)
    return subListSorted   

def subListarCronologicamenteAdquisisiones(sortArtworks,fechaInicial,fechaFinal):
    """
    Llama la funcion ssubListarCronologicamenteAdquisisiones del modelo y retorna una sublista de obras con el rango deseado.
    """
    subListSorted=model.subListarCronologicamenteAdquisisiones(sortArtworks,fechaInicial,fechaFinal)
    return subListSorted

def ordenarPorCosto(precios):
    listOrdenada=model.ordenarPorCosto(precios)   
    return listOrdenada

def ordenarPorFecha(precios):
    listOrdenada=model.ordenarPorFecha(precios)
    return listOrdenada 
def conectarID(lista_obras,lista_artistas):
    listaID=model.conectarID(lista_obras,lista_artistas)
# Funciones de consulta y creacion se sublistas sobre el catálogo
def listNacion(catalog):
    lista_obras=catalog["artworks"]
    lista_artistas=catalog["artists"]
    listaID=conectarID(lista_obras,lista_artistas)
    return listaID

def idArtist(catalog, nombreArtista):
    id=model.idArtist(catalog, nombreArtista)
    if id != "Error": 
       return id
    else: 
         return 0   
 
def obrasArtist(catalog,id):
    obras=model.obrasArtist(catalog,id)
    return obras

def listarObrasArtista(catalog, nombreArtista):
    id=idArtist(catalog,nombreArtista)
    obras=obrasArtist(catalog,id)
    if id == 0: 
       return("No se encontro en la base de datos el nombre que usted ingreso, por favor verifiquelo.")   
    else:   
        return (id,obras) 

def listarCronologicamenteArtistas(catalog,añoInicial,añoFinal):
    """
    Llama las funciones sortArtistasCronologicamente y subListarCronologicamenteArtistas para retornar una sublista ordenada de artistas.
    """
    sortArtistas=sortArtistasCronologicamente(catalog)
    subList=subListarCronologicamenteArtistas(sortArtistas,añoInicial,añoFinal)
    return subList

def listarAdquisisionesCronologicamente(catalog,fechaInicial,fechaFinal):
    """
    Llama las funciones sortObrasCronologicamente y subListarCronologicamenteAdquisisiones para retornar una sublista ordenada de obras.
    """
    sortArtworks=sortObrasCronologicamente(catalog)
    subList=subListarCronologicamenteAdquisisiones(sortArtworks,fechaInicial,fechaFinal)
    return subList    

def listaDepartamento(catalog,departamento):  
    subLista=model.subListarDepartamento(catalog,departamento)
    return subLista

def sacarPrecios(listDepartamento): 
    listaPrecios=model.sacarPrecios(listDepartamento)
    return listaPrecios    
