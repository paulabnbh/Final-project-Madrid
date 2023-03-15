import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import datetime

st.set_page_config(page_title='DisfrutaMadrid - Restaurante', page_icon="🍽️", layout="wide")

st.title('¿Dónde comemos hoy?')
rests = pd.read_csv('csv/restaurantes-def.csv')

barrio, puntuacion, tipo_cocina, precio  = st.columns(4)

with barrio:
    sel1 = st.selectbox('Elige barrio', rests.barrio.unique())

with tipo_cocina:
    sel2 = st.selectbox('Elige tipo de cocina', rests.columns[11::])

with puntuacion:
    sel3 = st.selectbox('Elige puntuación', rests.puntuacion.unique())

with precio:
    sel4 = st.selectbox('Elige rango de precio', rests.precio.unique())

filtered_rests = rests[(rests.barrio == sel1) & (rests[sel2] == 1) & (rests.puntuacion == sel3) & (rests.precio == sel4)]
def_rests = filtered_rests[['nombre', 'direccion_completa', 'puntuacion', 'precio']]
st.dataframe(def_rests)

