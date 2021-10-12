# -*- coding: utf-8 -*-
'''
@author: Jairo Escanez
@reviewer: Toñi Reina
'''

import csv
from collections import namedtuple
from datetime import datetime
from parsers import *
import statistics
import graficas 




Info = namedtuple('Info','fila, pais, urbano, edad, genero, casado, religion, situacion_familiar,nivel_educacion,sabe_sumar,\
                          veces_endeudado,puede_usar_internet,num_moviles,dinero_banco,fecha_ultimo_trabajo')

#----------------------------------------------------------------------------------------------------------------------------
# ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
def lee_fichero(fichero):
    '''
    Devuelve una lista de tuplas de tipo Info a partir de los datos incluidos en el fichero
    csv dado como parámetro. El fichero debe estar codificado en formato utf-8.
    @param fichero: Nombre y ruta del fichero csv a leer. 
    @type fichero:srt
    @return: Una lista de tuplas de tipo Info con todos los datos del csv
    @rtype: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]  
    '''
    with open(fichero, encoding='utf-8') as f:
        
        lector = csv.reader(f)
        next(lector)
        res=[]
        for fila, pais, urbano, edad, genero, casado, religion, situacion_familiar,\
            nivel_educacion,sabe_sumar,veces_endeudado,puede_usar_internet,num_moviles,\
            dinero_banco,fecha_ultimo_trabajo in lector:
                         
            tupla = Info(int(fila), pais, parsea_booleano(urbano), int(edad), parsea_genero(genero), \
                         parsea_booleano(casado), religion,situacion_familiar, int(nivel_educacion), \
                         parsea_booleano(sabe_sumar), int(veces_endeudado), parsea_booleano(puede_usar_internet),\
                         int(num_moviles),int(dinero_banco), parsea_fecha(fecha_ultimo_trabajo) )
            res.append(tupla)
    return res   


#----------------------------------------------------------------------------------------------------------------------------
# ENTREGA 2
#----------------------------------------------------------------------------------------------------------------------------


#----- BLOQUE 1 -------------------------------------------------------------------------------------------------------------
def selecciona_registros_de_genero_y_pais(registros,genero='Hombre',pais='A'):
    '''
    Devuelve una lista de tuplas de tipo Info con los datos de las personas del género
    y pais dados como parámetros.
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @param genero: Género por el que se van a filtrar los registros. Puede tomar los valores 'Hombre' o 'Mujer'. Si no se especifica toma 'Hombre' como
    valor por defecto.
    @type genero: str  
    @param pais: Código del país por el que se va a filtrar. Si no se especifica toma 'A' como valor por defecto.
    @type pais: str
    @return: Lista de tuplas de tipo Info con los datos de las personas del género y pais dados como parámetros.
    @rtype: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]  
    '''
    res = [t for t in registros if t.genero==genero and t.pais==pais]
    return res

#----- BLOQUE 2 -------------------------------------------------------------------------------------------------------------
def cuenta_endeudados(registros,genero='Hombre'):
    '''
    Devuelve el número de personas del género dado como argumento que se han endeudado. 
    Por defecto tiene el valor Hombre
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @param genero: Género por el que se van a filtrar los registros. Puede tomar los valores 'Hombre' o 'Mujer'. Si no se especifica toma 'Hombre' como
    valor por defecto.
    @type genero: str  
    @return: El número de personas endedudadas del género dado como parámetro.
    @rtype: int
    '''
    res=0
    for t in registros:
        if t.genero==genero and t.veces_endeudado !=0:
            res=res+1
    return res


def calcula_porcentaje_endeudados(registros,genero='Hombre'):
    '''
    El porcentaje de personas endeudadas del género dado como parámetro con respecto al total de personas de ese género. Si el porcentaje no se
    puede calcular, devuelve None
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @param genero: Género por el que se van a filtrar los registros. Puede tomar los valores 'Hombre' o 'Mujer'. Si no se especifica toma 'Hombre' como
    valor por defecto.
    @type genero: str  
    @return: El porcentaje de personas endeudadas del género dado como parámetro con respecto al total de personas de ese género. Si el porcentaje no se
    puede calcular, devuelve None.  
    @rtype: float
    '''
    cont_endeudados=0
    cont_personas=0
    
    for t in registros:
        if t.genero==genero:
            cont_personas+=1
            if t.veces_endeudado!=0:
                cont_endeudados+=1
    
    res=None            
    if cont_personas >0: 
        res=cont_endeudados*100/cont_personas 
    return res

#----- BLOQUE 3 -------------------------------------------------------------------------------------------------------------
def obten_registros_mas_dinero_banco(registros):
    '''
    Devuelve una lista de tuplas de tipo Info con la información de las personas que tienen más dinero en el banco.
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @return: Lista de tuplas de tipo Info con los registros que tengan mayor cantidad de dinero en el banco
    @rtype: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]  
    '''
    maximo =  max(registros, key = lambda x:x.dinero_banco)
    res = [t for t in registros if t.dinero_banco == maximo.dinero_banco]
    return res




#----------------------------------------------------------------------------------------------------------------------------
# ENTREGA 3
#----------------------------------------------------------------------------------------------------------------------------


#----- BLOQUE 4 -------------------------------------------------------------------------------------------------------------

def obten_n_registros_menor_num_moviles(registros,genero='Hombre',n=3):
    '''
    Devuelve una lista con los datos de las n personas endeudadas con menor número de móviles
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @param genero: Género por el que se van a filtrar los registros. Puede tomar los valores 'Hombre' o 'Mujer'. Si no se especifica toma 'Hombre' como
    valor por defecto.
    @type genero: str  
    @param n: Número de elementos de la lista resultante.
    @type n: int
    @return: Una lista de tuplas tipo Info con las n personas endeudadas que tengan menor número de teléfonos móviles.
    '''
    res=sorted ((t for t in registros if t.genero==genero), key= lambda t:t.num_moviles) 
    return res[:n]


def calcula_total_veces_endeudados_por_situacion_familiar(lista,edad):
    '''
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @param edad: Edad para la que se va a calcular el total de veces endeudados.
    @type edad: int 
    @return: Un diccionario en el que las claves representan una situación familiar, y los valores son el total de veces que se han
        endeudado las personas con la edad dada como parámetro que están en la situación familiar representada por la clave.
    @rtype: {str: int}
    '''
    dicc={}
    for p in lista:
        if p.edad ==edad:
            if p.situacion_familiar in dicc:
                dicc[p.situacion_familiar]+=p.veces_endeudado
            else:
                dicc[p.situacion_familiar]=p.veces_endeudado
    return dicc



#----- BLOQUE 5 -------------------------------------------------------------------------------------------------------------
def obten_media_edad_por_nivel_educacion(registros):
    '''
    Devuelve un diccionario en el que las claves representan el nivel de educacion y los valores la media de edad de las personas que tienen ese nivel de educación.
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @return: Un diccionario en el que las claves representan el nivel de educacion y los valores la media de edad de las personas que tienen ese nivel de educación.
    @rtype: {int:float}
    '''
    dicc=agrupa_por_nivel_educacion(registros)
    res = {clave:calcula_media_edad(lista_valores) for clave, lista_valores in dicc.items()}
    return res

def calcula_media_edad(registros):
    '''
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @return: La media de edad de las personas cuya información se recoge en la lista de tuplas dada como parámetro. Si no se puede 
        calcular eleva la excepcion StatisticsError.
    @rtype: float
    '''
    return statistics.mean(t.edad for t in registros)

def agrupa_por_nivel_educacion (registros):
    '''
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @return: Un diccionario en el que las claves representan el nivel de educación,y los valores son listas de los registros que tienen ese nivel de educación.
    @rtype: {int: [Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]}
    '''
    res = dict()
    for t in registros:
        if t.nivel_educacion in res:
            res[t.nivel_educacion].append(t)
        else:
            res[t.nivel_educacion]= [t]
    return res


def obten_media_dinero_banco_segun_nivel_educacion(registros):
    '''
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @return: Un diccionario en el que las claves representan el nivel de educación,y el valor es la media de dinero que tienen en el banco
        las personas de ese nivel de educación.
    @rtype: {int: float}
    ''' 
    dicc= agrupa_por_nivel_educacion(registros)
    res = {clave: calcula_media_dinero_banco(lista_valores) for clave, lista_valores in dicc.items()}
    return res


def calcula_media_dinero_banco(registros):
    '''
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    @return: La media de la cantidad que tienen en el banco las personas cuya información se recoge en la lista de tuplas dada como parámetro. Si no se puede 
        calcular eleva la excepcion StatisticsError.
    @rtype: float
    '''
    return statistics.mean(t.dinero_banco for t in registros)


def muestra_dinero_banco_por_nivel_educacion(registros):
    '''
    Muestra un diagrama de barras en el que por cada nivel de educación  (eje x) se muestra la media del dinero que
    tienen en el banco las personas de esa edad.
    
    @param registros:  lista de tuplas con los datos de pobreza
    @type registros: [ Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)]
    '''
    dicc=obten_media_dinero_banco_segun_nivel_educacion(registros)
    X, Y = zip(*sorted(dicc.items()))    
    titulo ='Dinero en el banco según cada nivel de estudio'
    etiqueta_eje_x = 'Nivel de estudio'
    etiqueta_eje_y = 'Dinero'
    graficas.dibujar_grafica_barras(X, Y, titulo, etiqueta_eje_x, etiqueta_eje_y)    
        
    

