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
               'artists': None,

               }

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)

# Funciones para creacion de datos






# Funciones de consulta

def firstartworks(catalog):
    for i in range(0,20):
        artworks=lt.getElement(catalog['artworks'], i)
        print (artworks['DateAcquired'])
    for j in range(0,20):
        artists=lt.getElement(catalog['artists'], j)
        print(artists['BeginDate'])

    return None


def Artist_in_a_range(year1, year2, catalog):
    pos1, pos2 = binary_interval_search(catalog, 'artists', year1, year2, cmpArtistByBeginDate, cmpArtistByBeginDateItem)
    return pos1, pos2






# Funciones de comparación
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    # Funciones de consulta sobre el catálogo
    """
    if artwork1['DateAcquired'] == '' or artwork2['DateAcquired'] == '':
        x = False 
    else:
        date_object1 = datetime.strptime(artwork1['DateAcquired'], '%Y-%m-%d').date()
        date_object2 = datetime.strptime(artwork2['DateAcquired'], '%Y-%m-%d').date()
        x = ((date_object1) < (date_object2))

    return x




def cmpArtistByBeginDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'BeginDate' de artist1 es menores que el de artist2
    """
    if artist1['BeginDate'] == '' or artist2['BeginDate'] == '':
        x = False 
    else:
        date_object1 = artist1['BeginDate']
        date_object2 = artist2['BeginDate']
        x = ((date_object1) < (date_object2))

    return x


def cmpArtistByBeginDateItem(item, artist):

    date1 = int(artist['BeginDate'])
    date2 = item

    if date2 == date1:
        return 0
    elif date2 > date1:
        return -1
    elif date2 < date1:
        return 1




# Funciones de ordenamiento

def sort(catalog, sort, key, cmpfunction):
    # TODO completar modificaciones para el laboratorio 4
    size=lt.size(catalog[key])
    sub_list = lt.subList(catalog[key], 1, size)
    sub_list = sub_list.copy()
    if sort == 1:
        start_time = time.process_time()
        sorted_list = insertion.sort(sub_list, cmpfunction)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif sort == 3:
        start_time = time.process_time()
        sorted_list = merge.sort(sub_list, cmpfunction)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    elif sort == 4:
        start_time = time.process_time()
        sorted_list = quick.sort(sub_list, cmpfunction)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
    else:
        start_time = time.process_time()
        sorted_list = shell.sort(sub_list, cmpfunction)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000    
    return sorted_list




# Funciones auxiliares de carga y consulta


def binary_search_up(catalog, key, item, cmpfunction, cmpfunction2):
    sequence= catalog[key]
    begin_index = 0
    end_index = lt.size(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = lt.getElement(sequence, midpoint)

        if  cmpfunction2(item, midpoint_value) == 0:
            try:
                midpoint_next_value = lt.getElement(sequence, midpoint + 1)

                if cmpfunction(midpoint_value, midpoint_next_value) == True:
                    return midpoint
                else:
                    begin_index = midpoint + 1
            except:
                return midpoint

        elif cmpfunction2(item, midpoint_value) ==  1:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1


    if cmpfunction2(item, lt.getElement(sequence, midpoint)) == 1:
        midpoint -= 1

    return midpoint




def binary_search_down(catalog, key, item, cmpfunction, cmpfunction2):
    sequence = catalog[key]
    begin_index = 0
    end_index = lt.size(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = lt.getElement(sequence, midpoint)
        if cmpfunction2(item, midpoint_value) == 0:
            try:
                midpoint_next_value = lt.getElement(sequence, midpoint -1)

                if cmpfunction(midpoint_next_value, midpoint_value) == True:
                    return midpoint
                else:
                    end_index = midpoint - 1
            except:
                return midpoint

        elif cmpfunction2(item, midpoint_value) == 1:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    if cmpfunction2(item, lt.getElement(sequence, midpoint)) == -1 < item:
        midpoint += 1
    return midpoint



def binary_interval_search(catalog, key, item1, item2, cmpfunction, cmpfunction2):
    pos1= binary_search_down(catalog, key, item1, cmpfunction, cmpfunction2)
    pos2= binary_search_up(catalog, key, item2, cmpfunction, cmpfunction2)

    return pos1, pos2


