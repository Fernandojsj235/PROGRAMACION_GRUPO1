import streamlit as st
import  requests
import pandas as pd
import os
st . título ( "Grupo 1" )
st . markdown ( """El grupo número 1 está conformado por estudiantes del quinto ciclo de la Carrera Profesional de Ingeniería Ambiental de la Universidad Peruana Cayetano Heredia:""" )
de  imagen de importación PIL  
imagen  =  Imagen . abierto ( 'Integrantes_grupo1.jpeg' )
st . image ( imagen , pie de foto = 'Fernando Jara,Josselyn Santi, Nancy Perez, Jose vega' , use_column_width = True )
file_data = "TB_CENTRO_VACUNACION.csv"
full_path_data=os.path.join(os.path.join(__file__,"../"),file_data)
peru_locations = "TB_UBIGEOS.csv"
data_peru = pd.read_csv(peru_locations)
ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
loc_info = requests.get(f'https://ipapi.co/{ip}/json/').json()
data = pd.read_csv(file_data)
st.title("Descripcion de la Data")
st.table(data.describe())

st.title("Lugares de Vacunacion Segun Region")
opt = st.selectbox(label="Elija Departamaento",options=data_peru.groupby("region")["fips"].count().index.values)
id_u = data_peru.loc[data_peru["region"] == opt,["id_ubigeo"]].values[0,0]
# print(id_u)
data_location = data.loc[data["id_ubigeo"] == id_u,["latitud","longitud"]]
data_location.columns = ["lat","lon"]
print(data_location[data_location["lon"] > 0].index.values)
data_location=data_location.drop(data_location[data_location["lon"] > -69].index.values)
st.map(data_location,zoom=11.25)

st.title("Lugares de Vacunacion Segun Entidad que Suminstra")
opt = st.selectbox(label="Elija Departamaento",options=data.groupby("entidad_administra")["entidad_administra"].count().index.values)
id_v = data.loc[data["entidad_administra"] == opt,["id_ubigeo"]].values[0,0]
print(id_v)

data_location2 = data.loc[data["id_ubigeo"] == id_v,["latitud","longitud"]]
data_location2.columns = ["lat","lon"]
data_location2=data_location2.drop(data_location2[data_location2["lon"] > -69].index.values)
st.map(data_location2,zoom=11.25)