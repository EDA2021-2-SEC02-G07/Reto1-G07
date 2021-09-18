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
    for i in range(0,100):
        artworks=lt.getElement(catalog['artworks'], i)
        print (artworks['DateAcquired'])

    return None


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