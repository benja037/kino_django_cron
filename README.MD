# Stats Kino

Sitio web que muestra estadísticas (graficos) del kino y sus sorteos:
1. Kino
2. Rekino
3. Chanchito Regalón
4. Combo Marraqueta
5. Chao Jefe 1 Millón
6. Chao Jefe 2 Millones
7. Chao Jefe 3 Millones

## Herramientas Principales
Este sitio web fue realizado con Django y Bootstrap, con el fin de realizar las siguientes funciones principales:
1. Pasar datos desde un excel creado por la agencia Lotería a una base de datos Postgres
2. Automatizar la actualización de la base de datos a medida que se realizaran más sorteos (django_crontab)
3. Mostrar gráficos con ChartJs

## Paso1
Lo primero que se realizó para extraer los datos fue generar el respectivo input para ingresar el archivo al sitio web.
Después, ese archivo fue leído por el programa mediante la librería de python openpyxl. Luego de obtener todos los datos en una lista, esta fue ingresada a la base de datos con la función bulk_create de django, la cual tenía un mejor tiempo en comparación a otras.

## Paso2
Para la automatización de la actualización de la base de datos se ocupó un cron "(1 2 * * 1,4,6)" lo que significa que el código se va a ejecutar tods los lunes, jueves y viernes a las 02:01, que sería horas después de cada sorteo.
Y dentro del codigo se ejecuta una petición request al sitio web ["https://chileresultados.com/kino/ultimosorteo"](https://chileresultados.com/kino/ultimosorteo) el cuál tiene una mejor estructura html para obtener los datos (los datos del html fueron obtenidos con beautifulsoap).

## Paso3

Los graficos fueron creados con los datos que se pasaron mediante la vista de django, gracias a la función render se podían pasar los datos mediante un context(diccionario).


