# Final-project-Madrid
![portada](https://github.com/paulabnbh/final-project-madrid/blob/main/proyecto/imagenes/logo-mad.png)

## Estructura
1) Las carpetas **restaurantes**, **turismo** y **hoteles** contienen el código para la extracción de los datos y su posterior limpieza.
2) La carpeta **presentacion** contiene la presentación del proyecto.
3) La carpeta **proyecto** contiene lo siguiente:
+ en **.streamlit** todo la configuración estética de la web.
+ en **csv** los documentos csv que están incluidos en el código de streamlit.
+ en **pages** el código de cada una de las páginas de streamlit.

## Objetivo

El objetivo de este proyecto es crear una app que ofrezca diferentes planes de ocio en Madrid a través de un filtrado geográfico, por precio, por puntuación y por tipos de características.

## Paso a paso

### ETL

El proceso de extracción de datos se ha hecho a través de la técnica de webscraping de tripadvisor.com, de donde he obtenido todos los datos posibles sobre **restaurantes**, **hoteles** y **planes de ocio**. Durante la propia extracción se han cargado los datos a MongoDB.

Una vez extraidos todos los datos, hemos procedido a la limpieza de estos, teniendo siempre en cuenta el objetivo del del proyecto: poder filtrar sobre estas bases de datos.

### VISUALIZACIÓN

He utilizado Streamlit para que se pueda acceder a todos los datos obtenidos anteriormente como usuario. He utilizado diferentes métodos de filtrado que ofrece la herramienta para que el usuario pueda filtrar a su gusto los datos obtenidos.

https://user-images.githubusercontent.com/120376042/225705627-da53bfdb-4661-4a70-a008-8e6fc003c325.mp4

## NEXT STEPS

+ Llevar a cabo una limpieza más profunda de los datos que permita que en la app podamos ver los filtros de tipo de cocina (restaurantes), servicios de hotel (hoteles) y tipo de actividad (ocio).

+ Habilitar la página **Mapa** con todos los datos y con opción de filtrado.

+ Crear una página nueva llamada 'Hazte un plan" combinando restaurantes, planes y hoteles con opciones de filtrado para que aparezcan todas las opciones en función de los filtros seleccionados. 
