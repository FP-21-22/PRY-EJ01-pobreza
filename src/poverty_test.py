from poverty import *

def main():
    
    LISTA_TUPLAS = lee_fichero('../data/poverty_data.csv')
    print('Leídos', len(LISTA_TUPLAS),'registros.')
    print('Los tres primeros registros son:',LISTA_TUPLAS[:3])
    print('Los tres �ltimos registros son:',LISTA_TUPLAS[-3:])
    
    filtro1=selecciona_registros_de_genero_y_pais(LISTA_TUPLAS,'Hombre')
    print('Filtrar por genero para genero=hombre y pa�s=A:\n',filtro1[:3])
    filtro2=selecciona_registros_de_genero_y_pais(LISTA_TUPLAS,pais='C',genero='Mujer')
    print('Filtrar por genero para genero=hombre y pa�s=C:\n',filtro2[:3])
    
    
    print('La informacion de la/s persona/s que poseen m�s dinero en el banco es:',obten_registros_mas_dinero_banco(LISTA_TUPLAS))
    print('La tupla de la mujer del pa�s C que tiene m�s dinero es:',obten_registros_mas_dinero_banco(filtro2))
   
    

    
    a = cuenta_endeudados(LISTA_TUPLAS,'Hombre')
    print('El número de hombres endeudados es:',a)
    a = cuenta_endeudados(LISTA_TUPLAS)
    print('El número de hombres endeudados es:',a)
    a = cuenta_endeudados(LISTA_TUPLAS,'Mujer')
    print('El número de mujeres endeudadas es:',a)
    
    a = obten_n_registros_menor_num_moviles(LISTA_TUPLAS,'Hombre',n=5)
    print('La informacion de los 5 hombres que tengan menos móviles y que se hayan endeudado:',a)
    a = obten_n_registros_menor_num_moviles(LISTA_TUPLAS,'Mujer')
    print('La informacion de las mujeres que tengan menos móviles y que se hayan endeudado:',a)

    a = calcula_porcentaje_endeudados(LISTA_TUPLAS,'Hombre')
    print('El porcentaje de hombres que se han endeudado es:', a)
    a = calcula_porcentaje_endeudados(LISTA_TUPLAS,'Mujer')
    print('El porcentaje de mujeres que se han endeudado es:', a)
    
    

    

    print('Diccionario en que le las claves son el nivel de estudio y los valores son la media de las edades de las personas que tienen ese nivel de estudio:\n',
          obten_media_edad_por_nivel_educacion(LISTA_TUPLAS))
    print('Diccionario en que le las claves son el nivel de estudio y los valores son la media de las edades de los hombres que tienen ese nivel de estudio y son del país I:\n',obten_media_edad_por_nivel_educacion(selecciona_registros_de_genero_y_pais(LISTA_TUPLAS,'Hombre',pais='I')))


    

    print('Diccionario en el que las claves son la situación familiar de las personas de 19 años y los valores son el número total de las veces que se han endeudado\n',calcula_total_veces_endeudados_por_situacion_familiar(LISTA_TUPLAS,19))
    print('Diccionario en el que las claves son la situación familiar de los 500 primeros hombres de 25 años  que tienen menos móviles y los valores son el número total de las veces que se han endeudado\n',calcula_total_veces_endeudados_por_situacion_familiar(obten_n_registros_menor_num_moviles(LISTA_TUPLAS,'Hombre',n=500),25))



    

    print('calcula la media del dinero en el banco de las personas que tengan 1 como nivel de estudio',calcula_media_dinero_banco(LISTA_TUPLAS))

    print('calcula la media del dinero en el banco de las personas que tengan 3 como nivel de estudio',calcula_media_dinero_banco(LISTA_TUPLAS))
    
    print('calcula la media del dinero en el banco de las mujeres del país F que tengan 2 como nivel de estudio',calcula_media_dinero_banco(selecciona_registros_de_genero_y_pais(LISTA_TUPLAS,pais='F',genero='Mujer')))
    
    
    
    
    muestra_dinero_banco_por_nivel_educacion(LISTA_TUPLAS)
    print('La gráfica siguiente muestra el diagrama de barras de los hombres del país G')
    muestra_dinero_banco_por_nivel_educacion(selecciona_registros_de_genero_y_pais(LISTA_TUPLAS,pais='G',genero='Hombre'))
    print('Gráfica que muestra el dinero en el banco filtrando sobre los 100 primeros registros que cumplan que son mujeres y del país C')
    muestra_dinero_banco_por_nivel_educacion(selecciona_registros_de_genero_y_pais(LISTA_TUPLAS[:100],pais='C',genero='Mujer'))
    
    
    

    
    

    









if __name__ == '__main__':
    main()