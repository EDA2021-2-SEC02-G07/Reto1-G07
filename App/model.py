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
    todos las obras y artistas.
    """
    catalog = {'artworks': None,
               'artists': None,
               'artistsByID': None,
               'adquire' : None,
               'nations': None,
               'bigNation': None,
               '2DArtworks': None
               }
    
    catalog['artworks'] =      lt.newList('ARRAY_LIST')
    catalog['artists'] =       lt.newList('ARRAY_LIST')
    catalog['adquire'] =       lt.newList('ARRAY_LIST')
    catalog['nations'] =       lt.newList('ARRAY_LIST')
    catalog['bigNation'] =    lt.newList('ARRAY_LIST')
    catalog['2DArtworks'] =    lt.newList('ARRAY_LIST')

    
    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)

def add2DArtworks(catalog, artwork):
    lt.addLast(catalog['2DArtworks'], artwork)
# Funciones para creacion de datos

# Funciones de consulta
def giveAuthorName(catalog, ConstituentID):
    """
        Dado un valor único 'ConstituentID' devuelve el nombre del artista asociado a ese ID
    """
    for x in catalog['artists']['elements']:
        if int(ConstituentID) == int(x['ConstituentID']):
            return (x['DisplayName'].split(','))[0]

def giveElementBinarySearch(list, key, element):
    """
        En una lista y dado un key encuentra a través de una busqeuda binaria la posición de un elemento.
        * Si el elemento no se encuentra en la lista retorna -1
        ** Si la lista contiene más de una vez el elemento que se busca retorna el la menor posición posible de ese elemento en la lista
    """
    lo = 0
    hi = len(list) - 1
    mid = 0

    while lo <= hi :
        mid = (hi + lo) // 2
        if int(list[mid][key]) < element:
            lo = mid + 1
        elif int(list[mid][key]) > element:
            hi = mid - 1
        else:
            return mid

    return -1

def giveRightDateBinarySearch(list, element):
    """
        Dada la lista de obras organizadas por fecha de adquisición y dada 
        un fecha retorna entre todas las obras que hayan sido adquiridas en esa fecha la posición de la que tenga mayor posición.

        Si no hay ninguna obra con esa fecha escogera entre las obras con 
        fecha de adquisición inmediatamente menor y dará la posición mayor entre ellas.

       * Si el elemento no se encuentra en la lista retorna -1
       ** Si la lista contiene más de una vez el elemento que se busca retorna el la mayor posición posible de ese elemento en la lista.

       Complejidad: Al basarse en una busqueda binaria con pequeñas modificaciones sabemos que su complejidad se aproxima a
                     O(logn) con n es el número de obras
    """
    lo = 0
    hi = lt.size(list) - 1
    mid = 0
    while lo <= hi:
        mid = (hi + lo) // 2
        if cmpArtworkByDateAcquired2(lt.getElement(list, mid)['DateAcquired'], element ) == 1:
            lo = mid + 1
        elif cmpArtworkByDateAcquired2(lt.getElement(list, mid)['DateAcquired'], element ) == -1:
            hi = mid - 1
        else: 
            break
    
    
    result = mid
    while cmpArtworkByDateAcquired2(lt.getElement(list, mid)['DateAcquired'],lt.getElement(list, result)['DateAcquired']) == 0:
        mid += 1
    mid -= 1

    if cmpArtworkByDateAcquired2(element, lt.getElement(list, mid)['DateAcquired'] ) == 1:
        return mid - 1
    else:
         return mid

def giveLeftDateBinarySearch(list,element):
    """
        Dada la lista de obras organizadas por fecha de adquisición y dada 
        un fecha retorna entre todas las obras que hayan sido adquiridas en esa fecha la posición de la que tenga menor posición.

        Si no hay ninguna obra con esa fecha escogera entre las obras con 
        fecha de adquisición inmediatamente mayor y dará la posición menor entre ellas.

        * Si el elemento no se encuentra en la lista retorna -1
        ** Si la lista contiene más de una vez el elemento que se busca retorna el la menor posición posible de ese elemento en la lista

        Complejidad:  Al basarse en una busqueda binaria con pequeñas modificaciones sabemos que su complejidad se aproxima a
                       O(logn) con n es el número de obras
    """
    lo = 0
    hi = lt.size(list) - 1
    mid = 0
    while lo <= hi:
        mid = (hi + lo) // 2
        if cmpArtworkByDateAcquired2(lt.getElement(list, mid)['DateAcquired'], element ) == 1:
            lo = mid + 1
        elif cmpArtworkByDateAcquired2(lt.getElement(list, mid)['DateAcquired'], element ) == -1:
            hi = mid - 1
        else: 
            break 
    
    if lt.getElement(list, mid)['DateAcquired'] == '':
        mid -=1
    result = mid
    while cmpArtworkByDateAcquired2(lt.getElement(list, mid)['DateAcquired'],lt.getElement(list, result)['DateAcquired'] ) == 0:
        if mid - 1 == -1 or mid + 1 == lt.size(list):
            return mid
        else:
            mid -= 1
    mid += 1
    if cmpArtworkByDateAcquired2(element, lt.getElement(list, mid)['DateAcquired'] ) == -1:
        return mid + 1
        
    else:
         return mid

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menor que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    
    if artwork1['DateAcquired'] == ''and artwork2['DateAcquired'] != '' :
        x = False
    elif artwork1['DateAcquired'] != '' and artwork2['DateAcquired'] == '':
        x = True
    elif artwork1['DateAcquired'] == '' and artwork2['DateAcquired'] == '':
        x = False
    else:
        date_object1 = datetime.strptime(artwork1['DateAcquired'], '%Y-%m-%d').date()
        date_object2 = datetime.strptime(artwork2['DateAcquired'], '%Y-%m-%d').date()
        x = ((date_object1) < (date_object2))
    return x
def cmpArtworkByDateAcquired2(Date1, Date2):
    """
    Devuelve verdadero (True) si el Date1 es una fecha menor que el date2
    Args:
    Date1: fecha 1 en la forma 'AAAA-MM-DD'
    Date2: fecha 2 en la forma 'AAAA-MM-DD'
    """
    if  Date1 == '':
        return -1
    else:
        date_object1 = datetime.strptime(Date1, '%Y-%m-%d').date()
        date_object2 = datetime.strptime(Date2, '%Y-%m-%d').date()
        if ((date_object1) < (date_object2)):
            return 1
        elif ((date_object1) > (date_object2)):
            return -1
        elif ((date_object1) == (date_object2)):
            return 0
        
def cmpArtistByConstituentID(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'ConstituentID' de artist1 es menor que el de artist2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'ConstituentID'
    artwork2: informacion de la segunda obra que incluye su valor 'ConstituentID'
    """

    return int(artist1['ConstituentID']) < int(artist2['ConstituentID'])

def cmpArtworksByConstituentID(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'ConstituentID' de una obras es menor que el de artist2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'ConstituentID'
    artwork2: informacion de la segunda obra que incluye su valor 'ConstituentID'
    """

    return int(eval(artwork1['ConstituentID'])[0]) == int(eval(artwork2['ConstituentID'])[0])

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

def sortArtistID(catalog):
    # Organiza una lista de obras según su fecha de adquisición.

    sorted_list = merge.sort(catalog['artistsByID'], cmpArtistByConstituentID)
    return  sorted_list

def sortNationsSize(catalog):
    # Organiza una lista de listas según el tamaño se sus sublistas.

    sorted_list = merge.sort(catalog['nations'], cmpArtworkBySize)
    return  sorted_list

def sortBigNation(catalog):
    # Organiza una lista de listas según el tamaño se sus sublistas.

    sorted_list = merge.sort(catalog['bigNation'], cmpArtworkBySize)
    return  sorted_list

