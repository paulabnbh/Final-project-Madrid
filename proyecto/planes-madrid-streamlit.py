import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import datetime
import time
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import folium

st.set_page_config(page_title='DisfrutaMadrid', page_icon="✈️", layout="wide")
st.sidebar.header('¿Qué hacemos hoy?')
app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Restaurantes', 'Planes', 'Hoteles'])
st.sidebar.image(Image.open('../proyecto/imagenes/mapa_madrid.jpg'), use_column_width=True)

if app_mode == 'Home':
    st.header('¿Dónde te apetece ir hoy?')
    rest_mapa = pd.read_csv('../proyecto/restaurantes_mapa.csv')
    hotel_mapa = pd.read_csv('../proyecto/hotel_mapa.csv')
    planes_mapa = pd.read_csv('../proyecto/planes_mapa.csv')
    
    filtro1

    with filtro1:
        columnas = df.columns
        selection = st.multiselect('Filtrar Columnas', columnas, default=['Team',
                                                                      'Player', 
                                                                      'Position', 
                                                                      'Matchs', 
                                                                      'Goals',
                                                                      'Total_Points'])

    mapa = folium.Map(location=[40.4167278, -3.7033387], zoom_start=15, tiles = 'Stamen Terrain')
    
    for i in range(0, len(hotel_mapa)):

        popup_txt = folium.Popup(hotel_mapa.nombre[i], hotel_mapa.puntuacion[i])

        folium.Marker([float(hotel_mapa.lat[i]), float(hotel_mapa.long[i])], 
                            popup=popup_txt,
                            icon = folium.Icon(color = 'blue')
        ).add_to(mapa)
    
    for i in range(0, len(rest_mapa)):

        popup_txt = folium.Popup(rest_mapa.nombre[i], rest_mapa.puntuacion[i])

        folium.Marker([float(rest_mapa.lat[i]), float(rest_mapa.long[i])], 
                            popup=popup_txt,
                            icon = folium.Icon(color = 'pink')
        ).add_to(mapa)

    
    for i in range(0, len(planes_mapa)):

        popup_txt = folium.Popup(planes_mapa.nombre[i], planes_mapa.puntuacion[i])

        folium.Marker([float(planes_mapa.lat[i]), float(planes_mapa.long[i])], 
                            popup=popup_txt,
                            icon = folium.Icon(color = 'green')
        ).add_to(mapa)
        
    st_folium(mapa, height = 550, width = 1000)

#elif app_mode == 'Restaurantes':
    #rests = pd.read_csv('../restaurantes/restaurantes-mad-dummies.csv')

    #tipo_cocina, puntuacion, precio

    #with filtros:
    #columnas = rests.columns
    #selection = st.multiselect('Filtrar Columnas', columnas)



#st.sidebar.image(Image.open('../proyecto/imagenes/chulapa1.png'))
#st.sidebar.subheader('Buscar por zona')
#st.sidebar.image(Image.open('../proyecto/imagenes/mapa_madrid.jpg'))


