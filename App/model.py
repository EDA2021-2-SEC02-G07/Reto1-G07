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
               'artists_mediums': None,
               'artists_tags': None, 
               'artworks_dptments': None

               }

    catalog['artworks'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['artists_mediums'] = {}
    catalog['artists_tags'] = lt.newList('ARRAY_LIST')
    catalog['artworks_dptments'] = {}

    return catalog

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)


def addArtworkdptment(catalog, dptment, dptment_name):

    catalog['artworks_dptments'][dptment_name] = dptment


def addArtistMedium(catalog, artist_medium):

    catalog['artists_mediums'][artist_medium['ID']] = artist_medium


def addArtistTag(catalog, artist_tag):

    lt.addLast(catalog['artists_tags'], artist_tag)


def fillArtworks(artlist, artwork):

    lt.addLast(artlist, artwork)




# Funciones para creacion de datos


def newDptment():
    dpment = { 
              'price':0,
              'weight':0,
              'expensive_artworks':{},
              'Artworks': lt.newList('ARRAY_LIST')
              }
    return dpment

    

def newArtistMedium(ID, name):

    artistmedium = {'ID':0 , 
                    'name': "", 
                    'mediums': {'most_used': "", 
                    'total': 0, 'mediums_list':{}}, 
                    'Artworks': None}

    artisttag = {'ID':0 ,'name': ""}
    artistmedium['ID'] = ID
    artistmedium['name'] = name
    artistmedium['Artworks'] = lt.newList('ARRAY_LIST')
    artisttag['ID'] = ID
    artisttag['name'] = name


    return artistmedium, artisttag







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


def Artworks_in_a_medium(medium, artworks):
    pos1, pos2 = binary_interval_search(artworks, 'Artworks', medium, medium, cmpArtworksByMedium, cmpArtworksByMediumItem)
    return pos1, pos2


def TagsFromName(name, catalog): 
    pos1, pos2 = binary_interval_search(catalog, 'artists_tags', name, name, cmpArtistByName, cmpArtistByNameItem)
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


def cmpArtistByName(artist1,artist2):

    if artist1['name'] == '' or artist2['name'] == '':
        x = False
    else:
        x = artist1['name'] < artist2['name']
    
    return x




def cmpArtistByNameItem(item, artist):
    name1 = artist['name']
    name2 = item

    if name2 == name1:
        return 0
    elif name2 > name1:
        return -1
    elif name2 < name1:
        return 1


def cmpArtworksByYear(artwork1, artwork2):
    if artwork1['Date'] == '' or artwork2['Date'] == '':
        x = False
    else: 
        x = artwork1['Date'] < artwork2['Date']
    
    return x



def cmpArtworksByMedium(artwork1, artwork2):

    if artwork1['Medium'] == ''  or artwork2['Medium'] == '':
        x = False
    else:
        x = artwork1['Medium'] < artwork2['Medium']

    return x

def cmpArtworksByMediumItem(item, artwork):
    medium1 = artwork['Medium']
    medium2 = item

    if medium2 == medium1:
        return 0
    elif medium2 > medium1:
        return -1
    elif medium2 < medium1:
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
    end_index = lt.size(sequence) 
    midpoint = begin_index + (end_index - begin_index) // 2

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
    end_index = lt.size(sequence) 
    midpoint = begin_index + (end_index - begin_index) // 2

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
        
    if cmpfunction2(item, lt.getElement(sequence, midpoint)) == -1:
        midpoint += 1

    

    return midpoint



def binary_interval_search(catalog, key, item1, item2, cmpfunction, cmpfunction2):
    pos1= binary_search_down(catalog, key, item1, cmpfunction, cmpfunction2)
    pos2= binary_search_up(catalog, key, item2, cmpfunction, cmpfunction2)

    return pos1, pos2


def MostUsedMedium(mediums_list):
    mostused_count = -1
    mostused = ''
    for key in mediums_list:
        value = mediums_list[key]
        if value > mostused_count:
            mostused_count = value
            mostused = key
    return mostused


def Transport_Price(Arwork):
    Heigt = Artwork['Height (cm)']
    Lenght = Arwork['Length (cm)']
    Width = Artwork['Width (cm)']
    Diameter = Artwork['Diameter (cm)']
    Weight = Artwork['Weight (kg)']
    tarifa = 72

    try:
        Price1 = (float(Heigt)/100 * float(Lenght)/100) * tarifa
    except:
        Price1 = 0
    try:
        Price2 = (3.1416 * (float(Diameter)/2) ** 2) * tarifa 
    except:
        Price2 = 0
    try:    
        Price3 = (float(Heigt)/100 * float(Lenght)/100 * float(Width)/100) * tarifa
    except:
        Price3 = 0
    try:
        Price4 = (float(Weight) * tarifa)
    except:
        Price4 = 0
    price_list = [Price1, Price2, Price3, Price4]
    expensive = -1
    for price in price_list:
        if price > expensive:
            expensive = price
    if expensive == 0:
        expensive = 48   
        
        return expensive


        

    

def size(ulist):
    size = lt.size(ulist)
    return size

def getElement(ulist, key, pos):
    element = lt.getElement(ulist, pos) [key]
    return element

def getElement1(ulist, pos):
    element = lt.getElement(ulist, pos)
    return element


def addtolist(ulist, element):
    lt.addLast(ulist, element)

    
    