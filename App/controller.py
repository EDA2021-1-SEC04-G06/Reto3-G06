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


def loadData(catalog):

    loadAnalisis(catalog)
    return catalog


# Funciones para la carga de datos
def loadAnalisis(catalog):
    analisisfile = cf.data_dir + 'context_content_features-small.csv'
    input_file = csv.DictReader(open(analisisfile, encoding='utf-8'))
    for ana in input_file:
        model.addAnalisis(catalog, ana)


def loadSentimientos(catalog):
    sentifile = cf.data_dir + 'sentiment_values.csv'
    input_file = csv.DictReader(open(sentifile, encoding='utf-8'))
    for senti in input_file:
        model.addSentimi(catalog, senti)


def loadInfo(catalog):
    infofile = cf.data_dir + 'user_track_hashtag_timestamp-small.csv'
    input_file = csv.DictReader(open(infofile, encoding='utf-8'))
    for info in input_file:
        model.addInfo(catalog, info)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def sizeAnlis(catalog):
    return model.sizeAnlis(catalog)

def requerimiento1(catalog,carac,valmin,valmax):
    return model.requerimiento1(catalog,carac,valmin,valmax)

def requerimiento2(catalog, minEner,maxEner,minDanc,maxDanc):
    return model.requerimiento2(catalog, minEner,maxEner,minDanc,maxDanc)

def requerimiento3(catalog, minTem,maxTem,minInstru,maxInstru):
    return model.requerimiento2(catalog, minTem,maxTem,minInstru,maxInstru)
    
