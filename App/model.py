﻿"""
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
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = { 'analisis': None,
                'info': None,
                'sentimientos': None,
                'instrumentalness': None,
                'liveness': None,
                'speechiness': None,
                'danceability': None,
                'valence': None,
                'loudness': None,
                'tempo': None,
                'acousticness': None,
                'energy': None,
                'tiempo': None,
                'hashtag': None
                }
    catalog['analisis'] = lt.newList('SINGLE_LINKED', compareIds)
    catalog['instrumentalness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['liveness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['speechiness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['danceability'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['valence'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['tempo'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['acousticness'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['energy'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)

    return catalog


# Funciones para agregar informacion al catalogo
def addAnalisis(catalog, analis):
    lt.addLast(catalog['analisis'], analis)
    agregaInstru(catalog['instrumentalness'],analis)
    agregaLive(catalog['liveness'],analis)
    agregaSpee(catalog['speechiness'],analis)
    agregaDance(catalog['danceability'],analis)
    agregaVal(catalog['valence'],analis)
    agregaTemp(catalog['tempo'],analis)
    agregaAcou(catalog['acousticness'],analis)
    agregaEner(catalog['energy'],analis)
    return catalog

def agregaInstru(mapa, analis):
    dato = analis['instrumentalness']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaLive(mapa, analis):
    dato = analis['liveness']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaSpee(mapa, analis):
    dato = analis['speechiness']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaDance(mapa, analis):
    dato = analis['danceability']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaVal(mapa, analis):
    dato = analis['valence']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaTemp(mapa, analis):
    dato = analis['tempo']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaAcou(mapa, analis):
    dato = analis['acousticness']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregaEner(mapa, analis):
    dato = analis['energy']
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdata(analis)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, analis)
    return mapa

def agregar(newEntry, analis):
    lt.addLast(newEntry, analis)
    return newEntry

# Funciones para creacion de datos
def newdata(analis):
    entry = lt.newList('SINGLE_LINKED', compareIds)
    return entry
# Funciones de consulta

def sizeAnlis(catalog):
    return lt.size(catalog['analisis'])

# Funciones utilizadas para comparar elementos dentro de una lista
def compare(eve1, eve2):
  
    if (eve1 == eve2):
        return 0
    elif (eve1 > eve2):
        return 1
    else:
        return -1

def compareIds(id1, id2):
  
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

# Funciones de ordenamiento

def requerimiento1(catalog,carac,valmin,valmax):
    listi= om.values(catalog[carac],valmin,valmax)
    eventost=0
    artistast=0
    listartis=lt.newList("ARRAY_LIST")
    for dato in lt.iterator(listi):
        eventost+= lt.size(dato)
        for evento in lt.iterator(dato):
            esta=lt.isPresent(listartis,evento['artist_id'])
            if esta == 0:
                lt.addLast(listartis,evento['artist_id'])
                artistast += 1
            

    return eventost,artistast
