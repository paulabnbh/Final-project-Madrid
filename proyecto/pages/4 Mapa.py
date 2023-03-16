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

st.set_page_config(page_title='DisfrutaMadrid • Mapa', page_icon="🗺️", layout="wide")

st.image('proyecto/imagenes/logo-mad.png', width = 300)


st.title('¿Dónde te apetece ir hoy?')
rest = pd.read_csv('proyecto/mapa-madrid/restaurantes_mapa.csv')
hotel = pd.read_csv('proyecto/mapa-madrid/hotel_mapa.csv')
ocio = pd.read_csv('proyecto/mapa-madrid/planes_mapa.csv')    

mapa = folium.Map(location=[40.4167278, -3.7033387], zoom_start=15, tiles = 'Stamen Terrain')

for i in range(0, len(rest)):

    folium.Marker([float(rest.lat[i]), float(rest.long[i])], 
                        popup=rest.nombre[i],
                        icon = folium.Icon(color = 'pink')).add_to(mapa)

for i in range(0, len(hotel)):

    folium.Marker([float(hotel.lat[i]), float(hotel.long[i])], 
                        popup=hotel.nombre[i],
                        icon = folium.Icon(color = 'green')).add_to(mapa)

for i in range(0, len(ocio)):

    folium.Marker([float(ocio.lat[i]), float(ocio.long[i])], 
                        popup=ocio.nombre[i],
                        icon = folium.Icon(color = 'blue')).add_to(mapa)
st_folium(mapa, height = 550, width = 1200)