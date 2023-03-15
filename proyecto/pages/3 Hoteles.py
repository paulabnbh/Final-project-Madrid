import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import datetime

st.set_page_config(page_title='DisfrutaMadrid • Hoteles', page_icon="🏨", layout="wide")


st.title('¿Dónde nos alojamos?')
hoteles = pd.read_csv('csv/hoteles-def.csv')

barrio, precio, puntuacion, servicios = st.columns(4)

with barrio:
    datos = hoteles.barrio.unique().tolist()
    sel1 = st.multiselect('Elige barrio', datos, default = ['Cortes', 'Sol', 'Recoletos'])

with precio:
    selmin, selmax = st.select_slider('Elige rango de precio',
                            options=[i for i in range(0, hoteles.precio.max()+1)],
                            value=[0, hoteles.precio.max()])   
st.write(selmin)

with puntuacion:
    sel3 = st.multiselect('Elige puntuación', hoteles.puntuacion.unique().tolist(), default = ['5.0'])

with servicios:
    cols = hoteles.columns[10::].tolist()
    sel4 = st.multiselect('Elige servicios', cols, default = ['Aparcamiento', 'Servicio de lavandería', 'Desayuno bufé'])



hoteles_filtered = hoteles[(hoteles['barrio'].isin(sel1)) & (hoteles['puntuacion'].isin(sel3)) & (hoteles.precio > selmin) & (hoteles.precio < selmax)] # & hoteles.precio == selmax)] #& (hoteles[sel4] == 1)]

hoteles_def = hoteles_filtered[['nombre', 'barrio', 'descripcion', 'precio', 'puntuacion']]

st.dataframe(hoteles_def)