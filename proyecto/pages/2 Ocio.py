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

tipo_plan, puntuacion = st.columns(2)


with tipo_plan:
    sel2 = st.selectbox('Elige categoría', ocio.columns[9::])

with puntuacion:
    sel1= st.selectbox('Elige puntuación',
                        ocio.puntuacion.unique())



ocio_filtered = ocio[(ocio.puntuacion == sel1) & (ocio[sel2] == 1)]
ocio_def = ocio_filtered[['nombre', 'ubicacion', 'barrio', 'puntuacion']]
ocio_def