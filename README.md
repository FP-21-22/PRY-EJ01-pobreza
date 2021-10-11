# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  20/21)
Autor/a: Jairo Escánez García;   uvus:&lt;uvus del autor&gt;

Revisión, reestructuración y adaptación para FP: Toñi Reina

Este es un ejemplo de proyecto realizado por un estudiante en el curso 2020/21. El código del estudiante se ha corregido, reestructurado y adaptado.


El proyecto tiene como objetivo analizar los datos de pobreza publicados en el dataset de Kaggle que se puede descargar de la siguiente URL (https://www.kaggle.com/johnnyyiu/predicting-poverty). El dataset original tiene 59 columnas, ninguna de las cuales es de tipo fecha. Así que, por una parte, se ha recortado el número de columnas escogiendo sólo 13 de las 59 columnas, y se han añadido dos columnas, una de tipo entero que recoge el dinero que tiene en el banco la persona, y otra columna de tipo fecha, que se ha generado con fechas aleatorias y que representa la fecha en la que se perdió el trabajo.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **poverty.py**: Contiene funciones para explotar los datos sobre pobreza.
  * **poverty_test.py**: Contiene funciones de test para probar las funciones del módulo `poverty.py`. En este módulo está el main
  * **parsers.py**: Contiene funciones de parseo de datos.
  * **graficas.py**: Contiene funciones para dibujar gráficas 
* **/data**: Contiene el dataset o datasets del proyecto
    * **poverty_data.csv**: Archivo con los datos de pobreza que van a ser explotados.
        
## Estructura del *dataset*

Cada fila del dataset recoge los datos anonimizados de una persona, es decir, no sabemos sus nombre ni sus apellidos. Para cada persona se registran 15 datos. Por lo tanto, el dataset está compuesto por 15 columnas, con la siguiente descripción:

* **row_id**: de tipo int, es un identificador entero.
* **country**: de tipo str, representa la inicial del país del registro.
* **is_urban**: de tipo boolean, representa si el país es urbano o no.
* **age**: de tipo int, representa la edad de la persona.
* **female**: de tipo boolean, representa si es de género femenino o no.
* **married**: de tipo boolean, representa si está casado o no.
* **religion**: de tipo str, representa la religión de la persona.
* **relationship_to_hh_head**: de tipo str, representa la situación familiar, si es cabeza de familia, padre.
* **education_level**: de tipo int, representa el nivel de estudios de la persona.
* **can_add**: de tipo boolean, representa si sabe sumar.
* **num_times_borrowed_last_year**: de tipo int, representa el número de veces endeudado en el último año.
* **can_use_internet**: de tipo boolean, representa si la persona sabe usar internet.
* **phone_ownership**: de tipo int, representa el número de móviles que posee la persona.
* **dinero_en_banco**: de tipo int, representa el dinero que posee la persona en el banco. Esta columna se ha generado con datos aleatorios.
* **fecha_ultimo_trabajo**: de tipo date, representa la fecha de la última vez que estuvo trabajando. Esta columna se ha generado con datos aleatorios.


## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

`Info = namedtuple('Info','id, pais, es_urbano, edad, genero, casado, religion, situacion_familiar,nivel_educacion,sabe_sumar,
                           veces_endeudado,puede_usar_internet,num_moviles,dinero_banco,fecha_ultimo_trabajo')`

en la que los tipos de cada uno de los campos son los siguientes:

`Info(int, str, boolean, int, str. boolean, str, str, in, boolean, int, boolean, int, int, datetime.date)`

Las decisiones de diseño más destacadas de este tipo son:
* El campo genero es de tipo str, en lugar de boolean como aparece en el dataset original, y puede tomar los valores 'Hombre' o 'Mujer'.

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### &lt;modulo 1&gt;

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...

### &lt;test modulo 1&gt;

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 

### &lt;modulo 2&gt;

* **&lt;funcion 1&gt;**: Descripción de la función 1.
* **&lt;funcion 2&gt;**: Descripción de la función 2.
* ...
