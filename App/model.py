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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf
import time
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'independents': None,
               'colaborations': None,
               'artists': None,
               'adquire' : None,
               'nacionalities': None,
               '2DArtworks': None
               }
    
    catalog['artworks'] =      lt.newList('ARRAY_LIST')
    catalog['artists'] =       lt.newList('ARRAY_LIST')
    catalog['adquire'] =       lt.newList('ARRAY_LIST')
    catalog['independents'] =  lt.newList('ARRAY_LIST')
    catalog['colaborations'] = lt.newList('ARRAY_LIST')
    catalog['nations'] =       lt.newList('ARRAY_LIST')
    catalog['2DArtworks'] =    lt.newList('ARRAY_LIST')

    
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)

def addIndep(catalog, artwork):
    # Se adiciona la obra a la lista de obras independientes
    lt.addLast(catalog['independents'], artwork)

def addColab(catalog, artwork):
    # Se adiciona la obra a la lista de obras que son colaboraciones
    lt.addLast(catalog['colaborations'], artwork)

def addNacionality(catalog, list):
    # Se adiciona una lista con obras a la lista de naciones.
    lt.addLast(catalog['nacionalities'], list)

def add2DArtworks(catalog, artwork):
    lt.addLast(catalog['2DArtworks'], artwork)
# Funciones para creacion de datos

# Funciones de consulta
def giveAuthorName(catalog, ConstituentID):
    """Dado un valor único 'ConstituentID' devuelve el nombre del artista asociado a ese ID"""
    for x in catalog['artists']['elements']:
        if int(ConstituentID) == int(x['ConstituentID']):
            return (x['DisplayName'].split(','))[0]

def giveRightElementBinarySearch(list, key, element):
    lo = 0
    hi = len(list) - 1
    mid = 0
    result = -1
    while lo <= hi and result == -1:
        mid = (hi + lo) // 2
        if int(list[mid][key] )< element:
            lo = mid + 1
        elif int(list[mid][key]) > element:
            hi = mid - 1
        else:
            result = mid

    rsult = result
    while int(list[rsult][key]) == int(list[result][key]):
        if rsult + 1 == len(list):
            return rsult
        else:
            rsult += 1
    rsult -= 1
    return rsult

def giveLeftElementBinarySearch(list, key, element):
    lo = 0
    hi = len(list) - 1
    mid = 0
    result = -1
    while lo <= hi and result == -1:
        mid = (hi + lo) // 2
        if int(list[mid][key]) < element:
            lo = mid + 1
        elif int(list[mid][key]) > element:
            hi = mid - 1
        else:
            result = mid

    rsult = result
    while int(list[rsult][key]) == int(list[result][key]):
        if rsult + 1 == -1:
            return rsult
        else:
            rsult -= 1
    return rsult +1

    

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    if artwork1['DateAcquired'] == '' or artwork2['DateAcquired'] == '':
        x = False 
    else:
        date_object1 = datetime.strptime(artwork1['DateAcquired'], '%Y-%m-%d').date()
        date_object2 = datetime.strptime(artwork2['DateAcquired'], '%Y-%m-%d').date()
        x = ((date_object1) < (date_object2))

    return x

def cmpArtworkByConstituentID(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'ConstituentID' de artwork1 es menor que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'ConstituentID'
    artwork2: informacion de la segunda obra que incluye su valor 'ConstituentID'
    """

    return eval(artwork1['ConstituentID'])[0] <= eval(artwork2['ConstituentID'])[0]

def cmpArtworkBySize(array1, array2):
    """
    Devuelve verdadero (True) si el 'size' de array1 es mayor que el de array2
    Args:
    array1: Primera lista de tipo 'ARRAY_LIST' que contiene su valor 'Size'
    array2: Segunda lista de tipo 'ARRAY_LIST' que contiene su valor 'Size'
    """

    return lt.size(array1) > lt.size(array2)

def cmpArtworkByYear(array1, array2):
    """
    Devuelve verdadero (True) si el 'Date' de array1 es menor que el de array2
    Args:
    array1: Primera lista de tipo 'ARRAY_LIST' que contiene su valor 'Date'
    array2: Segunda lista de tipo 'ARRAY_LIST' que contiene su valor 'Date'
    """
    return int(array1['Date']) < int(array2['Date'])
# Funciones de ordenamiento

def sortAdquires(catalog):
    # Organiza una lista de obras según su fecha de adquisición.

    sorted_list = merge.sort(catalog['adquire'], cmpArtworkByDateAcquired)
    return  sorted_list

def sortIndependents(catalog):
    # Organiza una lista de obras según su fecha de adquisición.

    sorted_list = merge.sort(catalog['independents'], cmpArtworkByConstituentID)
    return  sorted_list

def sortNationsSize(catalog):
    # Organiza una lista de listas según el tamaño se sus sublistas.

    sorted_list = merge.sort(catalog['nations'], cmpArtworkBySize)
    return  sorted_list

def sort2DArtworksDates(catalog):
    # Organiza una lista de listas según el tamaño se sus sublistas.

    sorted_list = merge.sort(catalog['2DArtworks'], cmpArtworkByYear)
    return  sorted_list