import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import datetime

st.set_page_config(page_title='DisfrutaMadrid • Ocio', page_icon="☀️", layout="wide")

st.image('proyecto/imagenes/logo-mad.png', width = 300)

st.title('¿Qué hacemos?')
ocio = pd.read_csv('proyecto/csv/planes-def.csv')

tipo_plan, puntuacion = st.columns(2)


with tipo_plan:
    sel2 = st.selectbox('Elige categoria', ocio.columns[9::])

with puntuacion:
    sel1= st.multiselect('Elige puntuación',
                        ocio.puntuacion.unique().tolist())



ocio_filtered = ocio[(ocio.puntuacion.isin(sel1)) & (ocio[sel2] == 1)]
ocio_def = ocio_filtered[['nombre', 'ubicacion', 'barrio', 'puntuacion']]
st.dataframe(ocio_def, width=1200)