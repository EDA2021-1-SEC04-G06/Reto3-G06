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
import random as rd
from datetime import datetime
import time
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
    catalog['tiempo'] = om.newMap(omaptype='RBT',
                                      comparefunction=compare)
    catalog['sentimientos']= mp.newMap(2000,
                                   maptype = 'CHAINING',
                                   loadfactor = 4.0,
                                   comparefunction = comparesenti)

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


def addInfo(catalog, info):
    agregaTiempo(catalog['tiempo'], info)


def addSentimi(catalog, info):
    sentimi = catalog['sentimientos']

    sentiss = info['hashtag']
    exists = mp.contains(sentimi, sentiss)
    if exists:
        entry = mp.get(sentimi, sentiss)
        sen = me.getValue(entry)
    else:
        entry = {'hashtag': "", 'sentimientos': None}
        entry['hashtag'] = str(sentiss)
        entry['sentimientos'] = info
        sen = entry
        mp.put(sentimi, sentiss, sen)


def agregaTiempo(mapa, info):
    fecha = info["created_at"]
    dato = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S").time()
    entry = om.get(mapa, dato)
    if entry is None:
        newEntry = newdataTime(info)
        om.put(mapa, dato, newEntry)
    else:
        newEntry = me.getValue(entry)
    agregar(newEntry, info)
    return mapa

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

def newdataTime(analis):
    entry = lt.newList('SINGLE_LINKED', compareTime)
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
  
    if (id1['track_id'] == id2['track_id']):
        return 0
    elif id1['track_id'] > id2['track_id']:
        return 1
    else:
        return -1

def compareTime(time1,time2):
    fecha1 = datetime.strptime(time1['created_at'],"%Y-%m-%d %H:%M:%S")
    fecha2 = datetime.strptime(time2['created_at'],"%Y-%m-%d %H:%M:%S")
    if (fecha1 == fecha2):
        return 0
    elif (fecha1 > fecha2):
        return 1
    else:
        return -1

def comparesenti(id, entry):
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1

# Funciones de ordenamiento

def requerimiento1(catalog,carac,valmin,valmax):
    listi = om.values(catalog[carac],valmin,valmax)
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


def requerimiento2(catalog, minEner,maxEner,minDanc,maxDanc):
    listener = om.values(catalog['energy'],minEner,maxEner)
    listdanc = om.values(catalog['danceability'],minDanc,maxDanc)
    total = 0
    listeven=lt.newList("ARRAY_LIST",compareIds)
    listeven2=lt.newList("ARRAY_LIST",compareIds)
    final=lt.newList("ARRAY_LIST",compareIds)

    for dato in lt.iterator(listener):
        for evento in lt.iterator(dato):
            esta=lt.isPresent(listeven,evento)
            if esta == 0:
                lt.addLast(listeven,evento)

    for dato2 in lt.iterator(listdanc):
        for evento2 in lt.iterator(dato2):
            esta2=lt.isPresent(listeven,evento2)
            esta3=lt.isPresent(listeven2,evento2)
            if esta2 != 0 and esta3 == 0:

                lt.addLast(listeven2,evento2)
                total +=1
    siz = lt.size(listeven2)
    for i in range(0,5):
        n=rd.randint(1,siz)
        lt.addLast(final,lt.getElement(listeven2,n))
    return total,final


def requerimiento3(catalog, minTem,maxTem,minInstru,maxInstru):
    listener = om.values(catalog['tempo'],minTem,maxTem)
    listdanc = om.values(catalog['instrumentalness'],minInstru,maxInstru)
    total = 0
    listeven=lt.newList("ARRAY_LIST",compareIds)
    listeven2=lt.newList("ARRAY_LIST",compareIds)
    final=lt.newList("ARRAY_LIST",compareIds)

    for dato in lt.iterator(listener):
        for evento in lt.iterator(dato):
            esta=lt.isPresent(listeven,evento)
            if esta == 0:
                lt.addLast(listeven,evento)

    for dato2 in lt.iterator(listdanc):
        for evento2 in lt.iterator(dato2):
            esta2=lt.isPresent(listeven,evento2)
            esta3=lt.isPresent(listeven2,evento2)
            if esta2 != 0 and esta3 == 0:
                lt.addLast(listeven2,evento2)
                total +=1
    siz = lt.size(listeven2)
    
    for i in range(0,5):
        n=rd.randint(1,siz)
        lt.addLast(final,lt.getElement(listeven2,n))
    return total,final

def requerimiento4(catalog,tablage,listage):
    dicgene={}
    total=0
    for gene in listage:
        listauto=lt.newList("ARRAY_LIST")
        numeve=0
        listgene = om.values(catalog['tempo'],str(tablage[gene][0]),str(tablage[gene][1]))
        for dto in lt.iterator(listgene):
            total += lt.size(dto)
            for eve in lt.iterator(dto):
                numeve+=1
                esta=lt.isPresent(listauto,eve['artist_id'])
                if esta == 0:
                    lt.addLast(listauto,eve['artist_id'])
        dicgene[gene]=[lt.subList(listauto,1,10),numeve,lt.size(listauto)]
    return total, dicgene

def requerimiento5(catalog, tablage, mintime, maxtime):
    
    listime = om.values(catalog['tiempo'],datetime.strptime(mintime,"%H:%M:%S").time(),datetime.strptime(maxtime,"%H:%M:%S").time())
    listt=lt.newList("ARRAY_LIST")
    mayor=0
    generom=None
    dictracks={}
    for gene in tablage.keys():
        n=0  
        dictracksg={}
        listgene = om.values(catalog['tempo'],str(tablage[gene][0]),str(tablage[gene][1]))
        for dto in lt.iterator(listgene):
            for d in lt.iterator(dto):
                lt.addLast(listt,d["track_id"])
              
        for timedata in lt.iterator(listime):
            for t in lt.iterator(timedata):
                if lt.isPresent(listt,t["track_id"]) !=0:
                    n+=1
                    if t["track_id"] in dictracksg.keys():
                        dictracksg[t["track_id"]].append(t['hashtag'])
                    else:
                        dictracksg[t["track_id"]]=[t['hashtag']]
        if n> mayor:
            mayor=n
            generom=gene
            dictracks=dictracksg
    final={}
    for can in dictracks.keys():
        nn=len(dictracks[can])
        prom=0
        suma=0
        for h in dictracks[can]:
            senti=mp.get(catalog['sentimientos'],h)
            if senti:
                m=me.getValue(senti)['sentimientos']
                if m['vader_avg'] !='':
                    suma += float(m['vader_avg'])
        prom= suma/nn
        final[can]=[nn,prom]
    return generom,mayor,final
    
    
    