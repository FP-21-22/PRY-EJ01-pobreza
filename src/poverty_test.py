# -*- coding: utf-8 -*-
from poverty import *

def test_lee_fichero(fichero):
    print ("test_lee_fichero" +"="*25)
    LISTA_TUPLAS = lee_fichero(fichero)
    print('Leídos', len(LISTA_TUPLAS),'registros.')
    print('Los tres primeros registros son:',LISTA_TUPLAS[:3])
    print('Los tres últimos registros son:',LISTA_TUPLAS[-3:])
  
def mostrar_registros (registros):
    for indx, registro in enumerate(registros):
        print(f"{indx+1}-{registro}")
          
def mostrar_diccionario(dicc):
    for clave, valor in dicc.items():
        print(f"{clave}-->{valor}")        
          

def test_selecciona_registros_de_genero_y_pais(registros,  genero='Hombre', pais='A'):
    print (f"pais={pais} genero={genero}")
    res=selecciona_registros_de_genero_y_pais(registros,genero, pais)
    print (f"Hay {len(res)} registros del genero y pais dados como parámetros. Son los siguientes:")
    mostrar_registros(res)
    
def test_obten_registros_mas_dinero_banco(registros):
    res = obten_registros_mas_dinero_banco(registros)
    print (f"Hay {len(res)} registros con la cantidad máxima de dinero en el banco. Son los siguientes:")
    mostrar_registros(res)
    
def test_cuenta_endeudados (registros, genero='Hombre' ):
    res = cuenta_endeudados(registros, genero) 
    print (f"Hay {res} endeudados del género {genero}")  
    
def test_obten_n_registros_menor_num_moviles(registros, genero='Hombre', n=3):
    res = obten_n_registros_menor_num_moviles(registros,genero,n)   
    print(f"Los {n} registros del género {genero} con menor número de móviles son:")
    mostrar_registros(res)
    
def test_calcula_porcentaje_endeudados(registros, genero='Hombre'):
    res = calcula_porcentaje_endeudados (registros, genero)
    print(f"El porcentaje de endeudados de genero {genero} es {res:.2f}")
    
def test_obten_media_edad_por_nivel_educacion (registros):
    res = obten_media_edad_por_nivel_educacion(registros)
    print("La media de edad según el nivel de educación es la siguiente:")
    mostrar_diccionario(res)
    
def test_calcula_total_veces_endeudados_por_situacion_familiar(registros, edad):   
    res = calcula_total_veces_endeudados_por_situacion_familiar (registros, edad)
    print(f"El total de veces endeudados segun la situación familiar de las personas con {edad} años es el siguiente:")
    mostrar_diccionario(res)
    
def test_muestra_dinero_banco_por_nivel_educacion(registros):    
    muestra_dinero_banco_por_nivel_educacion(registros)
    
def main():

    test_lee_fichero('../data/poverty_data.csv')
    
    REGISTROS = lee_fichero('../data/poverty_data.csv')
    

    print ("test_selecciona_registros_de_genero_y_pais" +"="*25)     
    test_selecciona_registros_de_genero_y_pais(REGISTROS, 'Hombre')
    test_selecciona_registros_de_genero_y_pais(REGISTROS, 'Mujer', 'C')
   
    print ("\ntest_obten_registros_mas_dinero_banco" +"="*25)     
    test_obten_registros_mas_dinero_banco(REGISTROS)
    test_obten_registros_mas_dinero_banco(REGISTROS[:100])
    

    print ("\ntest_cuenta_endeudados" +"="*25)
    test_cuenta_endeudados(REGISTROS)
    test_cuenta_endeudados(REGISTROS, 'Mujer')

    print ("\ntest_obten_n_registros_menor_num_moviles" +"="*25)
    test_obten_n_registros_menor_num_moviles(REGISTROS, 'Hombre', n=5)
    test_obten_n_registros_menor_num_moviles(REGISTROS,'Mujer')
    
    print ("\ntest_calcula_porcentaje_endeudados" +"="*25)
    test_calcula_porcentaje_endeudados(REGISTROS)
    test_calcula_porcentaje_endeudados(REGISTROS, 'Mujer')
    
    print ("\ntest_obten_media_edad_por_nivel_educacion" +"="*25)
    test_obten_media_edad_por_nivel_educacion (REGISTROS)
    test_obten_media_edad_por_nivel_educacion (REGISTROS[:100])
    
    print("\ntest_calcula_total_veces_endeudados_por_situacion_familiar"+"="*25)
    test_calcula_total_veces_endeudados_por_situacion_familiar(REGISTROS,19)  
    test_calcula_total_veces_endeudados_por_situacion_familiar(REGISTROS[:100],19)

    print("\ntest_muestra_dinero_banco_por_nivel_educacion"+"="*25)
    test_muestra_dinero_banco_por_nivel_educacion(REGISTROS)
    test_muestra_dinero_banco_por_nivel_educacion(REGISTROS[:100]) 

   
if __name__ == '__main__':
    main()