# -*- coding: utf-8 -*-
'''
Created on 25 nov. 2020

@author: reinaqu_2
'''
from matplotlib import pyplot as plt

'''
En este módulo se incluyen las funciones relacionadas con el dibujo de gráficas
'''
    

def dibujar_grafica_barras(etiquetas, valores, titulo, etiqueta_eje_x=None,etiqueta_eje_y=None):
    '''
        La función dibuja una gráfica de barras teniendo como etiquetas del eje X la lista dada por el
        parámetro etiquetas, como alturas de la barras los valores dados por el parámetro valores,
        como título el dado por el parámetro título, como etiquetas de los ejes X e Y las dadas por 
        los parámetros etiqueta_eje_x y etiqueta_eje_y.
        
        ENTRADAS:
        @param etiquetas: Lista de etiquetas que se se van a representar en el eje X 
                     para cada una de las barras.
        @type etiquetas: list(str). 
        @param valores: Lista de valores que determinan la altura de cada una de la barras.
                    Es el valor representado en el eje Y.
        @type valores: list(int/float). 
        @param titulo: Cadena que contiene el título de la gráfica.
        @type titulo: str.  
        @param etiqueta_eje_x: Etiqueta del eje X. Valor por defecto: None
        @type etiqueta_eje_x: str.  
        @param etiqueta_eje_y: Etiqueta del eje Y. Valor por defecto: None
        @type etiqueta_eje_y: str. 
    '''
    plt.title(titulo)
    indice = range(len(etiquetas))
    plt.bar(indice, valores)
    plt.xticks(indice, etiquetas, fontsize=8)
    plt.xlabel (etiqueta_eje_x)
    plt.ylabel (etiqueta_eje_y)
    plt.show() 

