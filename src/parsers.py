# -*- coding: utf-8 -*-
'''
Created on 10 oct 2021

Este módulo contiene todas las funciones auxiliares relacionadas con el parseo 
de tipos.

@author: To�i Reina
'''
from datetime import datetime

def parsea_booleano(cadena):
    '''
    Toma una cadena y si la cadena contiene el literal 'verdadero' (independientemente
    de si está escrtio en mayúsculas o minúsculas) la función devuelve True, si contiene
    el literal 'falso' entonces devuelve falso y con cualquier otra cadena, devuelve None.
    
    @param cadena: Cadena de caracteres con el valor verdadero
    @type cadena: str
    @return: True, False o None, dependiendo de si la cadena que se pasa como parámetro tiene 
    el literal 'verdadero', el literal 'falso' o cualquier otra cadena
    @rtype: bool 
    '''
    res = None
    cadena = cadena.upper()
    if cadena == 'VERDADERO':
        res =True
    elif cadena == 'FALSO':
        res=False
    return res


def parsea_genero(cadena):
    '''
    Toma una cadena y si la cadena contiene el literal 'verdadero' (indpendientemente
    de si está escrtio en mayúsculas o minúsculas) la función devuelve 'Mujer', si contiene
    el literal 'falso' entonces devuelve 'Hombre' y con cualquier otra cadena, devuelve None.
    
    @param cadena: Cadena de caracteres con el valor verdadero
    @type cadena: str
    @return: 'Mujer', 'Hombre' o None, dependiendo de si la cadena que se pasa como parámetro 
    tiene el literal 'verdadero', el literal 'falso' o cualquier otra cadena
    @rtype: str 
    '''
    res = None
    cadena = cadena.upper()
    if cadena == 'VERDADERO':
        res ='Mujer'
    elif cadena == 'FALSO':
        res='Hombre'
    return res

def parsea_fecha(cadena):
    '''
    @param cadena: Cadena con una fecha en formato dia/mes/año
    @type param: str
    @return: Un objeto de tipo date con la fecha a la que se refiere la cadena de entrada.
    @rtype: datetime.date
     
    '''
    return  datetime.strptime(cadena,'%d/%m/%Y').date()