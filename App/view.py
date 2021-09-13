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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Seleccionar algoritmo de ordenamiento ")
    print("3- listar cronológicamente las adquisiciones")
    print("4- clasificar las obras de un artista por técnica")
    print("5- clasificar las obras por la nacionalidad de sus creadores")
    print("6- clasificar las obras de un artista por técnica")
    print("0- Salir")

def initCatalog(tipo: str):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tipo)
    
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
        print('Titulo: ' + artwork['Title'] + ' Adquisición: ' + artwork['DateAcquired'])
        i+=1
catalog = None
sort = ''
"""
Menu principal
"""
while True:
    printMenu()
   
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('1- ARRAY_LIST')
        print('2- LINKED_LIST')
        tipo = input('Seleccione el tipo de TAD lista\n')
        if int(tipo[0]) == 1:
            catalog = initCatalog('ARRAY_LIST')
            loadData(catalog)
        elif int(tipo[0]) == 2:
            catalog = initCatalog('LINKED_LIST')
            loadData(catalog)
        print("Cargando información de los archivos ....")
        print('Obras cargados: ' + str(lt.size(catalog['artworks'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
    
    elif int(inputs[0]) == 2:
        print('1- Insertion')
        print('2- Shell')
        print('3- Merge')
        print('4- Quick Sorts')
        ord = input("Eliga el algoritmo de ordenamiento\n ")
        sort = int(ord)
    elif int(inputs[0]) == 3:
        size = input("Indique tamaño de la muestra: ")
        result = controller.sortAdquires(catalog, int(size), sort)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printSortResults(result[1])
    else:
        sys.exit(0)
sys.exit(0)
