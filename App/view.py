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
from tabulate import tabulate


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- listar cronológicamente los artistas ")
    print("3- listar cronológicamente las adquisiciones")
    print("4- clasificar las obras de un artista por técnica")
    print("5- clasificar las obras por la nacionalidad de sus creadores")
    print("6- clasificar las obras de un artista por técnica")
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

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        
    elif int(inputs[0]) == 2:
        try:
            year1=int(input('Ingrese el año inicial: '))
            year2=int(input('Ingrese el año final: '))
        except:
            print('Por favor ingrese un año válido')
        size, positions = controller.Artist_in_a_range(year1, year2, catalog)
        
        if positions == None:
            print('No hay artistas en el rango')
        
        else:
            print('Hay', size, 'Artista(s) entre los años ingresados')
            print('Los primeros y los últimos 3 artistas (si los hay) son:')
            table = [['Nombre', 'Año de nacimiento', 'Año de fallecimiento', 'Nacionalidad', 'Género']]
            for i in positions:
                artista = lt.getElement(catalog['artists'], i)
                Nombre = artista['DisplayName']
                Nacimiento = artista['BeginDate']
                Fallecimiento = artista['EndDate']
                Nacionalidad = artista['Nationality']
                Genero = artista['Gender']
                table.append([Nombre, Nacimiento, Fallecimiento, Nacionalidad, Genero])
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    
    elif int(inputs[0]) == 4:

        name = input('Ingrese el nombre del artista: ')


        ID, medium, total, pos1, pos2, size = controller.Artworks_in_a_medium(name, catalog)

        
        print('La cantidad de obras del artista es: ', size)
        print('El medio más empleado es: ', medium) 
        print('En número de técnicas utilizadas es: ', total)
        print('Las obras en las que se utilizó', medium, 'son: ')
        table = [['Título', 'Fecha', 'Medio', 'Dimensiones']]
        while pos1 <= pos2:
            obra = lt.getElement(catalog['artists_mediums'][ID]['Artworks'], pos1)
            Titulo = obra['Title']
            Fecha = obra['Date']
            Medio = obra['Medium']
            Dimensiones = obra['Dimensions']
            table.append([Titulo, Fecha, Medio, Dimensiones])
            pos1 += 1
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


    else:
        sys.exit(0)
sys.exit(0)


