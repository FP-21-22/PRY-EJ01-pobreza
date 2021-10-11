# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  &lt;20&gt;/&lt;21&gt;)
Autor/a: Jairo Escánez García;   uvus:&lt;uvus del autor&gt;

Revisión, reestructuración y adaptación para FP: Toñi Reina

Este es un ejemplo de proyecto realizado por un estudiante en el curso 2020/21. El código del estudiante se ha corregido, reestructurado y adaptado.


El proyecto tiene como objetivo analizar los datos de pobreza publicados en el dataset de Kaggle que se puede descargar de la siguiente URL (https://www.kaggle.com/johnnyyiu/predicting-poverty). El dataset original tiene 59 columnas, ninguna de las cuales es de tipo fecha. Así que, por una parte, se ha recortado el número de columnas escogiendo sólo 14 de las 59 columnas, y se ha añadido una columna de tipo fecha, que se ha generado con fechas aleatorias y que representa la fecha en la que se perdió el trabajo.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **&lt;poverty.py&gt;**: Contiene funciones para explotar los datos sobre pobreza.
  * **&lt;poverty_test.py&gt;**: Contiene funciones de test para probar las funciones del módulo `poverty.py`. En este módulo está el main
  * **&lt;parsers.py&gt;**: Contiene funciones de parseo de datos.
  * **&lt;graficas.py&gt;**: Contiene funciones para dibujar gráficas 
* **/data**: Contiene el dataset o datasets del proyecto
    * **&lt;poverty_data.csv&gt;**: Archivo con los datos de pobreza que van a ser explotados.
        
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por &lt;N&gt; columnas, con la siguiente descripción:

* **&lt;columna 1>**: de tipo &lt;tipo&gt;, representa....
* **&lt;columna 2>**: de tipo &lt;tipo&gt;, representa....
....

## Tipos implementados

Descrbe aquí la o las namedtuple que defines en tu proyecto.

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
