import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime

st.set_page_config(page_title='DisfrutaMadrid - Restaurante', page_icon="🍽️", layout="wide")

st.image('proyecto/imagenes/logo-mad.png', width = 300)

st.title('¿Dónde comemos?')

rests = pd.read_csv('proyecto/csv/restaurantes-def.csv')

barrio, puntuacion, tipo_cocina, precio  = st.columns(4)

with barrio:
    sel1 = st.multiselect('Elige barrio', rests.barrio.unique(), default=['Cortes','Sol','Recoletos'])

with tipo_cocina:
    cols = rests.columns[11::].tolist()
    sel2 = st.multiselect('Elige tipo de cocina', cols)

with puntuacion:
    sel3 = st.multiselect('Elige puntuación', rests.puntuacion.unique().tolist())

with precio:
    sel4 = st.selectbox('Elige rango de precio', rests.precio.unique())

filtered_rests = rests[(rests.barrio.isin(sel1)) & (rests.puntuacion.isin(sel3)) & (rests.precio == sel4)]
filtered_rests = filtered_rests[filtered_rests[sel2].notnull().all(axis=1) & (filtered_rests[sel2] == 1).any(axis=1)]

def_rests = filtered_rests[['nombre','barrio','direccion_completa', 'puntuacion', 'precio']]
st.dataframe(def_rests, width = 1200)

