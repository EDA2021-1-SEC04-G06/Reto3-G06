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
    print("1- Inicializar Catalogo")
    print("2- Cargar información")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("6- Requerimiento 4")
    print("7- Requerimiento 5")
    print("0- Salir")


catalog = None
tablage = {'reggae':[60,90],'down-tempo':[70,100],'chill-out':[90,120],'hip-hop':[85,115],'jazzandfunk':[120,150],'pop':[100,130],'r&b':[60,80],'rock':[110,140],'metal':[100,160]}

def initCatalog(tipo):
    return controller.initCatalog(tipo)


def loadData(catalog):
    controller.loadData(catalog)


def impResultados(resultados):
    n=1
    for even in lt.iterator(resultados):
        print( 'Track '+ str(n) + ':  ' + str(even['track_id']) + ' con Energy de ' + str(even['energy']) + '  y Danceability de ' + str(even['danceability']) )
        n+=1


def impResultados2(resultados):
    n=1
    for even in lt.iterator(resultados):
        print( 'Track '+ str(n) + ':  ' + str(even['track_id']) + ' con Tempo de ' + str(even['tempo']) + '  y Instrumentalness de ' + str(even['instrumentalness']) )
        n+=1

def impResultados3(resultados):
    for gene in resultados.keys():
        print("Para el " + str(gene).upper())
        print('Tiene ' + str(resultados[gene][1]) + ' reproducciones')
        print('Tiene ' + str(resultados[gene][2]) + ' diferentes artistas')
        print('Algunos artistas son:')
        n=1
        for art in resultados[gene][0]['elements']:
            print('Artista'+str(n)+" : " + str(art))
            n+=1

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print("Eventos cargados: " + str(controller.sizeAnlis(catalog)))
        print("Total de artistas: ")
        print("Total de pistas de audio: ")
        print("Los primeros 5 eventos : ")
        print("Los ultimos 5 eventos : ")
    elif int(inputs[0]) == 3:
        carac = input('Ingrese la característica: ')
        valmin = input('Ingrese el valor minimo: ')
        valmax = input('Ingrese el valor maximo: ')
        respuesta = controller.requerimiento1(catalog,carac,valmin,valmax)
        print('El total de eventos en es rango es: ' + str(respuesta[0]))
        print('El Numero de artistas es: ' + str(respuesta[1]))
    elif int(inputs[0]) == 4:
        minEner = input('Ingrese el el valor minimo de Energy que quiere ')
        maxEner = input('Ingrese el el valor maximo de Energy que quiere ')
        minDanc = input('Ingrese el el valor minimo de Danceability que quiere ')
        maxDanc = input('Ingrese el el valor maximo de Danceability que quiere ')
        respuesta = controller.requerimiento2(catalog, minEner,maxEner,minDanc,maxDanc)
        print('El total de pistas unicas es: ' + str(respuesta[0]))
        print('5 pistas aleatorias que cumplen estas condiciones son')
        impResultados(respuesta[1])
    elif int(inputs[0]) == 5:
        minTem  = input("Ingrese el el valor minimo del rango para el Tempo que quiere ")
        maxTem  = input("Ingrese el el valor maximo del rango para el Tempo que quiere ")
        minInstru  = input("Ingrese el el valor minimo rango para Instrumentalnes que quiere ")
        maxInstru  = input("Ingrese el el valor maximo rango para Instrumentalnes que quiere ")
        respuesta = controller.requerimiento3(catalog,minTem, maxTem, minInstru, maxInstru)
        print('El total de pistas unicas es: ' + str(respuesta[0]))
        print('5 pistas aleatorias que cumplen estas condiciones son')
        impResultados2(respuesta[1])

    elif int(inputs[0]) == 6:
        print("Genero         BPM Tipico ")
        print("Reggae          60 a 90")
        print("Chill-out       90 a 120")
        print("Hip-hop         85 a 115")
        print("Jazz and Funk  120 a 125")
        print("Pop            100 a 130")
        print("R&B             60 a 80")
        print("Rock           110 a 140")
        print("Metal          100 a 160")
        yon=input("Ingrese 1 si desea agregar un genero que no esta en la tabla (0 en caso contrario) ")
        if yon == 1:
            gene=input('Ingrese el nombre del genero ')
            minge=input('Ingrese el vaalor minimo del rango de Tempo del genero ')
            maxge=input('Ingrese el vaalor maximo del rango de Tempo del genero ')
            tablage[gene.lower()]=[minge,maxge]
        generosf= input('Ingrese la lista de generos que desea buscar (separados por ",") ')
        listage = generosf.lower().strip().split(",")
        respuesta= controller.requerimiento4(catalog,tablage,listage)
        print('El total de reproducciones de estos generos es: ' + str(respuesta[0]))
        impResultados3(respuesta[1])

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
