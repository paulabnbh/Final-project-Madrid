import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime
import time
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium

st.set_page_config(page_title='DisfrutaMadrid', page_icon="✈️", layout="wide")

st.image('proyecto/imagenes/logo-mad.png', use_column_width = True)


col1, col2 = st.columns(2)
with col1:
    st.title('¿Conoces Madrid?')
    st.header('El reloj de la Puerta del Sol es un regalo')
    st.write('El reloj de la Puerta del Sol, el que anuncia las campanadas de fin de año, es uno de los símbolos de la ciudad. Primeramente hubo un reloj en el lado este de la plaza, en la iglesia del Buen Suceso, donde ahora está la tienda Apple, pero era tan impuntual que los vecinos no podían fiarse. Por eso, cuando se derribó la iglesia, un famoso relojero decidió regalar a la ciudad un reloj que funcionase bien. Era el relojero Losada, que tardó tres años en fabricarlo en Londres. Se colocó en su ubicación actual, la Casa de Correos, en 1866.')
    st.header('Madrid también tiene una estatua de la Libertad')
    st.write('Es verdad y se trata de una de las curiosidades de Madrid más sorprendentes. Madrid tiene una estatua de la libertad, creada por el escultor aragonés Ponciano Ponzano, el mismo que esculpió los leones del Congreso. La creó en 1853. Es decir, unos veinte años antes de la de Frédéric Auguste Bartholdi, que acabó siendo un regalo del gobierno francés a los Estados Unidos. La estatua de la libertad española es más pequeña, de unos dos metros de altura, y toda de mármol blanco. Para verla sólo hay que entrar al Panteón de Hombres Ilustres, uno de los museos más curiosos de la ciudad.')
    st.image('proyecto/imagenes/mapa_madrid.jpg')
    
with col2:
    st.image('proyecto/imagenes/madrid2.jpg')
    st.header('Muchas casas tienen un cartel de Asegurada de Incendios')
    st.write('Muchas casas del centro de Madrid conservan un antiguo cartel que dice “Asegurada de incendios”. Estos carteles datan del siglo XIX y están relacionadas con las compañías aseguradoras y los cuerpos de bomberos. En realidad, lo de las placas surgió en Londres mucho tiempo antes, cuando se creó la primera aseguradora contra incendios, que decidió identificar las casas en las que actuaría su propio cuerpo de bomberos en caso de necesidad. En Madrid se creó la Sociedad de Seguros Mutuos de Incendios de Casas en 1822, en la que los socios eran a su vez asegurados. Los bomberos actuaban en las casas que pertenecían a la sociedad, y por eso había que identificarlas. El primer cuerpo de bomberos municipal se creó en 1894 y entonces dejó de tener sentido colocar las placas porque estos bomberos asistían a cualquier casa, estuviera o no asegurada.')
    st.header('A los madrileños nos llaman Gatos')
    st.write('El motivo por el que nos llaman, o nos llamamos a nosotros mismos, gatos no es la presencia masiva de felinos en la ciudad. De hecho, no está del todo claro el por qué del nombre. Pero hay una leyenda que parece explicarlo. Se dice que los cristianos que, en el siglo XI, vinieron a conquistar la ciudad, en poder de los musulmanes, se valieron de la habilidad de un vecino que era capaz de trepar las murallas por la parte más complicada y por tanto menos vigilada. Tras silenciar a la guardia, el joven, apodado el Gato, abrió las puertas de la ciudad y facilitó la conquista. La palabra Gato cobró el significado de valiente y más tarde se asimiló con los nacidos en la ciudad. El muchacho adoptó la palabra Gato en su apellido y de él se derivó un linaje duradero y conocido en la villa.')



