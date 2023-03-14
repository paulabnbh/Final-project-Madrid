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

app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Restaurantes', 'Planes', 'Hoteles'])
st.sidebar.image(Image.open('../proyecto/imagenes/mapa_madrid.jpg'), use_column_width=True)



if app_mode == 'Home':
    madrid_mapa = pd.read_csv('../proyecto/madrid_mapa.csv')
    mapa = folium.Map(location=[40.4167278, -3.7033387], zoom_start=24)
    
    for i in range(0, len(madrid_mapa)):

        folium.Marker([float(madrid_mapa.lat[i]), float(madrid_mapa.long[i])], 
                            popup=str(madrid_mapa.nombre[i])
        ).add_to(mapa)
        
    st_folium(mapa, height = 500, width = 800)

if app_mode == 'Restaurantes':
    rests = pd.read_csv('../restaurantes/restaurantes-mad-dummies.csv')



#st.sidebar.header('¿Qué hacemos hoy?')
#st.sidebar.image(Image.open('../proyecto/imagenes/chulapa1.png'))
#st.sidebar.subheader('Buscar por zona')
#st.sidebar.image(Image.open('../proyecto/imagenes/mapa_madrid.jpg'))


