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
    loadNacionalities(catalog)
    load2DArtworks(catalog)

def loadArtworks(catalog):
    """
    Carga las obras del archivo.  
    """
    artfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadArtists(catalog):
    """
    Carga loas artista en el cátalogo y los organiza por su 'ConstituentID'.

    Complejidad:  O(n + nlogn) n es el número de obras.
    """
    artfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist) 
    catalog['artistsByID'] = catalog['artists']    
    catalog['artistsByID'] = model.sortArtistID(catalog)

def loadAdquires(catalog):
    """
        Carga en el catálogo el la llave 'adquires'una sublista de las obras y la organiza con respecto a su fecha de adquisición

        Complejidad:  O(nlogn) n es el número de obras.
    """
    catalog['adquire'] = lt.subList(catalog['artworks'], 1, lt.size(catalog['artworks']))
    catalog['adquire'] = sortAdquires(catalog)

def loadNacionalities(catalog):
    """
        * Carga en el catálogo el la llave 'nations' una lista de listas, cada sub lista contiene todas la obras de una nacionalidad específica
        ** Carga en el catálogo en el la llave 'bigNation' la lista de obras del país que más obras tiene en el MoMA 

        Complejidad:  tilda(2m+nlogm) n es el número de obras y m el número de artistas, en archivo large m igual al 11% de n
    """
    catalog['nationSize'] = {}
    catalog['nationalities'] = {}
    catalog['nationalities']['Unknown'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction= None, key='ConstituentID')
    catalog['nationalities']['Unknown']['nation'] = 'Unknown'
    catalog['nationSize']['Unknown'] =lt.newList(datastructure='ARRAY_LIST', cmpfunction= None, key='ConstituentID')
    catalog['nationSize']['Unknown']['nation'] = 'Unknown'
    for x in lt.iterator(catalog['artists']):
        if str(x['Nationality']) != '':
            if catalog['nationalities'].get(str(x['Nationality'])) == None:
                catalog['nationSize'][str(x['Nationality'])] = lt.newList(datastructure='ARRAY_LIST', cmpfunction= None, key='ConstituentID')
                catalog['nationSize'][str(x['Nationality'])]['nation'] = str(x['Nationality'])
                catalog['nationalities'][str(x['Nationality'])] = lt.newList(datastructure='ARRAY_LIST', cmpfunction= None, key='ConstituentID')
                catalog['nationalities'][str(x['Nationality'])]['nation'] = str(x['Nationality'])
    for y in lt.iterator(catalog['artworks']):
        for z in eval(y['ConstituentID']):
            pos = model.giveElementBinarySearch(catalog['artists']['elements'],'ConstituentID',int(z))
            if pos != -1:
                nationality = str(catalog['artists']['elements'][pos]['Nationality'])
                if nationality != '' and nationality != 'Nationality unknown':
                    lt.addLast(catalog['nationSize'][nationality], y) 
                    if lt.isPresent(catalog['nationalities'][nationality], y) == 0:
                        lt.addLast(catalog['nationalities'][nationality], y) 
                else: 
                    lt.addLast(catalog['nationSize']['Unknown'], y)
                    if lt.isPresent(catalog['nationalities']['Unknown'], y) == 0:
                        lt.addLast(catalog['nationalities']['Unknown'], y)
    for x in catalog['nationalities']:
        lt.addLast(catalog['bigNation'],catalog['nationalities'][x])
    catalog['bigNation'] = model.sortBigNation(catalog)
    catalog['bigNation'] = catalog['bigNation']['elements'][0]
    for x in catalog['nationSize']:
        lt.addLast(catalog['nations'],catalog['nationSize'][x])
    catalog['nations'] = model.sortNationsSize(catalog)
    
def load2DArtworks(catalog):
    """
        Carga en el cátalogo el la llave '2DArtworks' una sublista de las obras que sean de dos dimensiones (cuadros y fotos) 
    """
    for x in lt.iterator(catalog['artworks']):
        if x['Date'] != '' and x['Width (cm)'] != '' and x['Height (cm)'] != '' :
            model.add2DArtworks(catalog, x)
    
# Funciones de ordenamiento
def sortAdquires(catalog):
    """
    Ordena las adquisiciones
    """
    return model.sortAdquires(catalog)

# Funciones de consulta 
def giveAuthorsName(catalog, ConstituentsID):
    """
    Dado una lista de Constituent ID devuelve los nombres de los artistas asociados a esos ID
    """
    names = []

    for x in ConstituentsID:
        names.append(' '+model.giveAuthorName(catalog, x))
    return ','.join(names)

def loadRangeOfYears2DArtworks(catalog, begin, end):
    """
        Devuelve una lista con las obras de 2 dimensiones en un determinado rango de años

        Complejidad:  tilda(2m) n es el número de obras y m el número de obras de 2 dimensiones, en archivo large m es igual al 80% de n
    """
    Artworks = []
    for x in lt.iterator(catalog['2DArtworks']):
        if int(x['Date']) >= begin and int(x['Date']) <= end:
            Artworks.append(x)

    return Artworks

def giveRightPosArtworkstByDateAcquired(catalog, date):
    return model.giveRightDateBinarySearch(catalog['adquire'], date)

def giveLeftPosArtworkstByDateAcquired(catalog, date):
    return model.giveLeftDateBinarySearch(catalog['adquire'], date)

def giveRangeOfDates(catalog, begin, end):
    """
        Dados por parametro el catálogo, una fecha de inicio y una fecha final, devuelve una lista con todos las obras que hayan sido adquiridas n ese rango de fechas
        
        Debido a que llama a dos busquedas binarias y nada más sabemos que su complejidad se aproxima a:

            Complejidad:  O(2logn) n es el número de obras.
    """
    posI = giveLeftPosArtworkstByDateAcquired(catalog, begin)
    posF = giveRightPosArtworkstByDateAcquired(catalog, end)
    return catalog['adquire']['elements'][posI:posF+1]
