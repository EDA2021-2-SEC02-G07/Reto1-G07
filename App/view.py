"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- listar cronológicamente las adquisiciones")
    print("3- clasificar las obras de un artista por técnica")
    print("4- clasificar las obras por la nacionalidad de sus creadores")
    print("5- clasificar las obras de un artista por técnica")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()
    
def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printSortResults(ord_artworks, sample=10):

    size = lt.size(ord_artworks)
    if size > sample:
        print("Las primeros ", sample, " obras ordenados son:")
    i=1
    while i <= sample:
        artwork = lt.getElement(ord_artworks,i)
        print('Titulo: ' + artwork['ConstituentID'] + ' Adquisición: ' + artwork['DateAcquired'])
        i+=1

def printSort2DArtworksByYear(catalog, begin, end, area, sample=5):
    artworks = controller.loadRangeOfYears2DArtworks(catalog, begin, end)
    n = 0
    finalArea = 0
    for x in artworks:
        if (float(x['Height (cm)'])*float(x['Width (cm)']))/10000 + finalArea <= area:
            finalArea += (float(x['Height (cm)'])*float(x['Width (cm)']))/10000
            n += 1
    print('El MoMA va a exhibir obras entre', begin, 'y', end)
    print('Hay', len(artworks), 'posibles obras para exponer en un área disponible de:', area, 'm²')
    print('La posible exhibición podría tener', n ,'elementos')
    print('Se utilizaron', round(finalArea,3), 'm² de los', area, 'm² disponibles')
    print()
    print("Las primeras y últimas", sample, " obras ordenadas en el rango de años dado son:")
    print()
    j = len(artworks)
    i=1
    while i <= sample:
        artwork = artworks[i]
        print('ObjectID:  ' + artwork['ObjectID'] + '  Title:  ' + artwork['Title'] + '  ArtistNames:  ' 
        + controller.giveAuthorsName(catalog, eval(artwork['ConstituentID'])) + '  Medium:  ' + artwork['Medium'] +
        '  Date:  ' + artwork['Date'] + '  Dimensions:  ' + artwork['Dimensions'] + '  Department:  ' + artwork['Department'] + 
        '  Classification:  ' + artwork['Classification'] +
         '  Área ocupada:  ', (float(artwork['Height (cm)'])*float(artwork['Width (cm)']))/10000 ,
        '  URL:  ' + artwork['URL']  )
        print()
        i+=1
    i = len(artworks) - 1
    while i >= j-sample:
        artwork = artworks[i]
        print('ObjectID:  ' + artwork['ObjectID'] + '  Title:  ' + artwork['Title'] + '  ArtistNames:  ' 
        + controller.giveAuthorsName(catalog, eval(artwork['ConstituentID'])) + '  Medium:  ' + artwork['Medium'] +
        '  Date:  ' + artwork['Date'] + '  Dimensions:  ' + artwork['Dimensions'] + '  Department:  ' + artwork['Department'] + 
        '  Classification:  ' + artwork['Classification'] +
         '  Área ocupada:  ', (float(artwork['Height (cm)'])*float(artwork['Width (cm)']))/10000 ,
        '  URL:  ' + artwork['URL']  )
        print()
        i-=1

    

def printBigNation(ord_artworks, sample =3):
    
    print("Las primeras y últimas", sample, " obras ordenadas de nacionalidad ", "'",ord_artworks['nation'],"'"," son:")
    print()
    j = lt.size(ord_artworks)
    i=1
    while i <= sample:
        artwork = lt.getElement(ord_artworks,i)
        print('ObjectID:  ' + artwork['ObjectID'] + '  Title:  ' + artwork['Title'] + '  ArtistNames:  ' 
        + controller.giveAuthorsName(catalog, eval(artwork['ConstituentID'])) + '  Medium:  ' + artwork['Medium'] +
        '  Date:  ' + artwork['Date'] + '  Dimensions:  ' + artwork['Dimensions'] + '  Department:  ' + artwork['Department'] + 
        '  Classification:  ' + artwork['Classification'] + '  URL:  ' + artwork['URL']  )
        print()
        i+=1
    i = lt.size(ord_artworks) - 1
    while i >= j-sample:
        artwork = lt.getElement(ord_artworks,i)
        print('ObjectID:  ' + artwork['ObjectID'] + '  Title:  ' + artwork['Title'] + '  ArtistNames:  ' 
        + controller.giveAuthorsName(catalog, eval(artwork['ConstituentID'])) + '  Medium:  ' + artwork['Medium'] +
        '  Date:  ' + artwork['Date'] + '  Dimensions:  ' + artwork['Dimensions'] + '  Department:  ' + artwork['Department'] + 
        '  Classification:  ' + artwork['Classification'] + '  URL:  ' + artwork['URL']  )
        print()
        i-=1

def printSortNations(nations, sample=10):

    size = lt.size(nations)
    if size > sample:
        print("Las primeras ", sample, " naciones ordenados son:")
    i=1
    while i <= sample:
        artwork = lt.getElement(nations,i)
        print('Nationality: ' + artwork['nation'] + '   Artworks: ' + str(lt.size(artwork)))
        i+=1
        
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
   
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        catalog = initCatalog()
        loadData(catalog)

        print("Cargando información de los archivos ....")
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('Obras que son de un solo autor cargadas: ' + str(lt.size(catalog['independents'])))
        print('Obras que son colaboraciones de varios autores cargadas: ' + str(lt.size(catalog['colaborations'])))
        print('Obras que son de dos dimensiones cargadas: ' + str(lt.size(catalog['2DArtworks'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
    
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        print('=============== Req No.4 Inputs ===============')
        print('Clasificando las obras por la nacionalidad de sus creadores... ')
        print()
        print('=============== Req No.4 Answer ===============')
        print()
        printSortNations(catalog['nations'])
        print()
        printBigNation(catalog['nations']['elements'][0])
    elif int(inputs[0]) == 5:
        
        print(controller.giveLeftArtworkPosByYear(catalog, 2017))  
    elif int(inputs[0]) == 6:
        InitialYear = int(input('Escriba el año inicial de las obras: '))
        EndingYear = int(input('Escriba el año final de las obras: '))
        area = float(input('Indique el área disponible en m² para los objetos planos(cuadros y fotos): '))
        print()
        print('=============== Req No.6 Inputs ===============')
        print('Busca obras entre ', InitialYear, ' y ', EndingYear)
        print('Con un área disponible de:', area, 'm²')
        print()
        print('=============== Req No.6 Answer ===============')
        printSort2DArtworksByYear(catalog, InitialYear, EndingYear, area)
        

    else:
        sys.exit(0)
sys.exit(0)

