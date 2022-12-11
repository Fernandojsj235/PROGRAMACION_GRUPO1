import streamlit as st
import  requests
import pandas as pd
import os
import numpy as np
import altair as alt
import urllib.request
import base64
st.title("CENTROS DE VACUNACIÓN(COVID-19)")
st.title("Equipo 01:")
st.markdown("""El grupo número 1 está conformado por estudiantes del quinto ciclo de la Carrera Profesional de Ingeniería Ambiental de la Univerisdad Peruana Cayetano Heredia:
- Jara Garcia, Fernando ALipio
- Perez Noriega, Nancy
- Santi Huayllani, Josselyn Alicia 
- Vega Rojas, Jose Mauricio""")
from PIL import Image
image = Image.open('Integrantes_grupo1.jpeg')
st.image(image, caption='Integrantes del grupo 1' ,use_column_width=True)
st.markdown("""Esta tabla contiene la lista de los centros de vacunación programadas según 
entidad y ubicación geográfica(longitud y latitud) a nivel nacional del territorio peruano.""")

from PIL import Image
image = Image.open('Centros_vacunación.jpg')
st.image(image, caption='Centro de vacunación en Lima', use_column_width=True)
file_data = "TB_CENTRO_VACUNACION.csv"
full_path_data=os.path.join(os.path.join(__file__,"../"),file_data)
peru_locations = "TB_UBIGEOS.csv"
data_peru = pd.read_csv(peru_locations)
ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
loc_info = requests.get(f'https://ipapi.co/{ip}/json/').json()
data = pd.read_csv(file_data)
st.title("Dashboard")
st.table(data.describe())
st.title("Guia del usuario:")
st.markdown("""
- Gráfico de dispersión de los centros de vacunación, según el departamento a la cual pertenece. Para ello el usuario debera seleccionar un departamento, después se mostrarán los puntos en donde se encuentra el centro de vacunación
- Gráfico de dispersión de los centros de vacunación según la entidad, a la cual pertenece. Para ello el usuario deberá seleccionar el una entidad administradora, por ejemplo, DIRESA(Dirección Reginal de Salud)""")
st.title("Gráfico de centros de vacunación según el departamento, a la cual pertenece")
opt = st.selectbox(label="Elija Departamaento",options=data_peru.groupby("region")["fips"].count().index.values)
id_u = data_peru.loc[data_peru["region"] == opt,["id_ubigeo"]].values[0,0]
# print(id_u)
data_location = data.loc[data["id_ubigeo"] == id_u,["latitud","longitud"]]
data_location.columns = ["lat","lon"]
print(data_location[data_location["lon"] > 0].index.values)
data_location=data_location.drop(data_location[data_location["lon"] > -69].index.values)
st.map(data_location,zoom=11.25)

st.title("Gráfico de centros de vacunacion según la entidad que administra")
opt = st.selectbox(label="Elija a la entidad administradora",options=data.groupby("entidad_administra")["entidad_administra"].count().index.values)
id_v = data.loc[data["entidad_administra"] == opt,["id_ubigeo"]].values[0,0]
print(id_v)

data_location2 = data.loc[data["id_ubigeo"] == id_v,["latitud","longitud"]]
data_location2.columns = ["lat","lon"]
data_location2=data_location2.drop(data_location2[data_location2["lon"] > -69].index.values)
st.map(data_location2,zoom=11.25)
