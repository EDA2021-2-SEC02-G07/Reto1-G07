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
from DISClib.ADT import list as lt
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
    loadAdquires(catalog)
    loadIndepAndColab(catalog)
    loadNacionalities(catalog)
    load2DArtworks(catalog)

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

def loadAdquires(catalog):
    catalog['adquire'] = lt.subList(catalog['artworks'], 1, lt.size(catalog['artworks']))
    catalog['adquire'] = sortAdquires(catalog)

def loadIndepAndColab(catalog):
    for x in catalog['artworks']['elements']:
            if len(eval(x['ConstituentID'])) > 1:
                model.addColab(catalog, x)
            elif eval(x['ConstituentID']) != [-1]:
                model.addIndep(catalog, x)
    catalog['Independents'] = sortIndep(catalog)

def loadNacionalities(catalog):
    catalog['nationalities'] = {}
    for x in catalog['artists']['elements']:
        if str(x['Nationality']) != '':
            if catalog['nationalities'].get(str(x['Nationality'])) == None:
                catalog['nationalities'][str(x['Nationality'])] = lt.newList('ARRAY_LIST')
            for y in catalog['colaborations']['elements']:
                for z in eval(y['ConstituentID']):
                    if int(x['ConstituentID']) == z and y not in (catalog['nationalities'][str(x['Nationality'])]['elements']): 
                        lt.addLast(catalog['nationalities'][str(x['Nationality'])], y) 
    for x in catalog['nationalities']:
        catalog['nationalities'][x]['nation'] = x
        lt.addLast(catalog['nations'],catalog['nationalities'][x])
    catalog['nations'] = model.sortNationsSize(catalog)
    return catalog['nations']   

def load2DArtworks(catalog):
    for x in catalog['artworks']['elements']:
        if (x['Classification'] == 'Design' or x['Classification'] == 'Painting' or x['Classification'] == 'Photograph' or x['Classification'] == 'Drawing' or x['Classification'] == 'Print') and x['Date'] != '' and x['Width (cm)'] != '' and x['Height (cm)'] != '' :
            model.add2DArtworks(catalog, x)
    catalog['2DArtworks'] = model.sort2DArtworksDates(catalog)

def loadRangeOfYears2DArtworks(catalog, begin, end):
    x = catalog['2DArtworks']['elements']
    x = catalog['2DArtworks']['elements'][giveLeftArtworkPosByYear(catalog, begin):giveRightArtworkPosByYear(catalog, end)+1]
    return x
# Funciones de ordenamiento
def sortAdquires(catalog):
    """
    Ordena las adquisiciones
    """
    return model.sortAdquires(catalog)

def sortIndep(catalog):
    """
    Ordena las lista obras de un solo autor por ConstituentID
    """
    return model.sortIndependents(catalog)

# Funciones de consulta 
def giveAuthorsName(catalog, ConstituentsID):
    """
    Dado una lista de Constituent ID devuelve los nombres de los artistas asociados a esos ID
    """
    names = []

    for x in ConstituentsID:
        names.append(' '+model.giveAuthorName(catalog, x))
    return ','.join(names)

def giveRightArtworkPosByYear(catalog, year):
    return model.giveRightElementBinarySearch(catalog['2DArtworks']['elements'], 'Date', year)

def giveLeftArtworkPosByYear(catalog, year):
    return model.giveLeftElementBinarySearch(catalog['2DArtworks']['elements'], 'Date', year)