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
    loadArtistMediumsTags(catalog)
    loadDptments(catalog)
    catalog['artworks'] = sortAdquires(catalog, 3)
    catalog['artists'] = sortArtists(catalog, 3)
    fillArtistMediums(catalog)
    fillMostUsedMediums(catalog)
    catalog['artists_tags'] = sortArtistTags(catalog, 3)
    sort_dptments(catalog)
    print(catalog['artworks_dptments']['Drawings & Prints'])
    
   


    

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
    artfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist) 


def loadDptments(catalog):
    artworks = catalog['artworks']
    size = model.size(artworks)
    for i in range(0, size + 1):
        artwork = model.getElement1(artworks, i)
        dptment = artwork['Department']

        if dptment in catalog['artworks_dptments']:
            pass

        else: 
            new_dptment = model.newDptment()
            model.addArtworkdptment(catalog, new_dptment, dptment)

        model.addtolist(catalog['artworks_dptments'][dptment]['Artworks'], artwork)
        try:
            weight = float(artwork['Weight (kg)'])
            catalog['artworks_dptments'][dptment]['weight'] += weight
        except: 
            pass

        catalog['artworks_dptments'][dptment]['price']







def loadArtistMediumsTags(catalog):
    artists = catalog['artists']
    size = model.size(artists) 

    for i in range(0, size + 1):
        name = model.getElement(artists, 'DisplayName', i)   
        ID = model.getElement(artists, 'ConstituentID', i) 
        artist_medium, artist_tag = model.newArtistMedium(ID, name)
        model.addArtistMedium(catalog, artist_medium)
        model.addArtistTag(catalog, artist_tag)



def fillArtistMediums(catalog):
    Artworks = catalog['artworks']
    artists_mediums = catalog['artists_mediums']
    size = model.size(Artworks)

    for i in range(0, size + 1):
        artwork = model.getElement1(Artworks, i)
        IDs = model.getElement(Artworks, 'ConstituentID', i)
        IDs = IDs.replace('[','').replace(']','').split(',')
        medium = model.getElement(Artworks, 'Medium', i)

        for ID1 in IDs:
            ID = str(ID1)
            try:
                artlist = artists_mediums [ID] ['Artworks']
                mediums = artists_mediums[ID]['mediums']
            except: 
                continue 

            model.fillArtworks(artlist, artwork)
            

            if medium in mediums['mediums_list']:
                mediums['mediums_list'][medium] += 1

            else:
                mediums['mediums_list'][medium] = 1
                mediums['total'] += 1
    


def fillMostUsedMediums(catalog):
    artists_mediums=catalog['artists_mediums']

    for key in artists_mediums:
        artist_medium = artists_mediums[key]['mediums']
        artist_medium_list = artists_mediums[key]
        mediums_list = artist_medium['mediums_list']
        most_used_medium = model.MostUsedMedium(mediums_list)
        artist_medium['most_used'] = most_used_medium
        artist_medium_list['Artworks'] = sortArworksByMedium(artist_medium_list, 3)

    
def sort_dptments(catalog):
    artworks_dptments = catalog['artworks_dptments']

    for key in artworks_dptments:
        dptment = artworks_dptments[key]
        dptment['Artworks'] = sortArtworksByYear(dptment, 3)





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


def sortArworksByMedium(artistmedium, sort):
    return model.sort(artistmedium, sort, 'Artworks', model.cmpArtworksByMedium)


def sortArtworksByYear(Dptment, sort):
    return model.sort(Dptment, sort, 'Artworks', model.cmpArtworksByYear)


def sortArtistTags(catalog, sort):
    return model.sort(catalog, sort, 'artists_tags', model.cmpArtistByName) 



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





def Artworks_in_a_medium(name, catalog):
    pos1, pos2= model.TagsFromName(name, catalog)
    ID = model.getElement(catalog['artists_tags'], 'ID', pos2)
    Artist_medium = catalog['artists_mediums'][ID]
    medium = Artist_medium['mediums']['most_used']
    total = Artist_medium['mediums']['total']
    pos1, pos2 = model.Artworks_in_a_medium(medium, Artist_medium)
    size = pos2 - pos1 +1

    return ID, medium, total, pos1, pos2, size

