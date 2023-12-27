# Actualizar base de datos de Stats Kino
## Cron.py
Para la automatización de la actualización de la base de datos se ocupó un cron "(31 11 * * 1,4,6)" lo que significa que el código se va a ejecutar tods los lunes, jueves y viernes a las 11:31, que sería horas después de cada sorteo. Y dentro del codigo se ejecuta una petición request al sitio web "https://chileresultados.com/kino/ultimosorteo" el cuál tiene una mejor estructura html para obtener los datos (los datos del html fueron obtenidos con beautifulsoap). El código de esta parte esta en https://github.com/benja037/kino_django_cron, el código es similar pero sin todos los elementos de las vistas y url, además se incorporó un archivo cron.py que tiene todos los pasos de recolección y transferencia de datos. También, lo más importante de este paso el archivo yml que crea una instancia de ubuntu para correr el código en las fechas indicadas.


