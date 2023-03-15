import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import datetime

st.set_page_config(page_title='DisfrutaMadrid • Ocio', page_icon="☀️", layout="wide")

st.title('¿Qué hacemos?')
ocio = pd.read_csv('csv/planes-def.csv')

barrio, puntuacion, tipo_plan = st.columns(3)

with barrio:
    sel1 = st.selectbox('Elige un barrio', ocio.barrio.unique())

with puntuacion:
    sel_min, sel_max = st.multiselect('Elige puntuación', 
                                      options = [i for i in range(-1, ocio.puntuacion.max()+1)],
                                      value = [-1, ocio.puntuacion.max()])

with tipo_plan:
    sel3 = st.multiselect('Elige categoría', ocio.columns[7::])

ocio_filtered = ocio[(ocio.barrio == sel1)] #& (ocio.puntuacion == sel2) & (ocio[sel3] == 1)]
ocio_def = ocio_filtered[['nombre', 'ubicacion', 'barrio', 'puntuacion']]