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

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtworks(catalog)
    loadArtists(catalog)
    catalog['artworks'] = sortAdquires(catalog, 3)
    catalog['artists'] = sortArtists(catalog, 3)

def loadArtworks(catalog):
    """
    Carga las obras del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)  

def loadArtists(catalog):
    """
    Carga las obras del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artfile = cf.data_dir + 'Artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist) 

def loadArtistMediumsTags(catalog):
    artists = catalog['artists']

    for element in artists:
        name = element['DisplayName']
        ID = element['ConstituentID']
        artist_medium, artist_tag = model.newArtistMedium(ID, name)
        model.addArtistMedium(catalog, artist_medium)
        model.addArtistTag(catalog, artist_tag)

def fillArtistMediums(catalog):
    Artworks= catalog['artworks']
    artists_mediums = catalog['artists_mediums']
    artists_tags = catalog['artists_tags']

    for artwork in Artworks:
        IDs = artwork['ConstituentID']
        medium = artwork['Medium']

        for ID in IDs:
            pos = model.binary_search_down(catalog, 'artists_mediums' , ID, cmpfunction, cmpfunction2)#FUNCIÓN
            





# Funciones de ordenamiento

def sortAdquires(catalog, sort):
    """
    Ordena los libros por average_rating
    """
    return model.sort(catalog, sort, 'artworks', model.cmpArtworkByDateAcquired)


def sortArtists(catalog, sort):
    """
    Ordena los libros por average_rating
    """
    return model.sort(catalog, sort, 'artists', model.cmpArtistByBeginDate)


def sortArtistMediums(catalog, sort):

    return model.sort(catalog, sort, 'artist_mediums', ) #FUNCIOOOON


def sortArtistTags(catalog, sort):
    return model.sort(catalog, sort, 'artist_mediums', ) #FUNCIOOOON



# Funciones de consulta sobre el catálogo
def firsts_artworks(catalog):
    model.firstartworks(catalog)
    return None


def Artist_in_a_range(year1, year2, catalog):
    posiciones = []
    if year1 <= 0:
        year1 = 1
    pos1, pos2 = model.Artist_in_a_range(year1, year2, catalog)
    size = pos2 - pos1 + 1
    if size<=0:
        return size, None
    elif size <= 3:
        while pos1 <= pos2:
            posiciones.append(pos1)
            pos1 += 1
    else:
        posiciones=[pos1, pos1 + 1, pos1 +2, pos2 - 2, pos2 -1, pos2]

    return size, posiciones 