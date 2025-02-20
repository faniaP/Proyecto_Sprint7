import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.title("¡Bienvenido!") 
st.caption("\n Este sitio es especial. En este sitio encontraras información sobre los anuncios de venta de autos.")
st.write("En esta vista encontrarás distintos gráficos sobre los anuncios de autos como: \n * Histogramas\n * Diagramas de dispersión\n\n Elige una opción de diagrama que desees.")

hist_button = st.button('Construir histograma') # crear un botón
scat_button = st.button('Construir diagrama de dispersión') # crear un botón


if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if scat_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear una gráfica de dispersion
    fig = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.markdown('''\n\n\n:blue[***Si no deseas utilizar los botones, puedes seleccionar una casilla.***]''', divider="gray")

show_hist = st.checkbox("Mostrar Histograma")
show_scat = st.checkbox("Mostrar diagrama de dispersión")
 
if show_hist:
    st.subheader("Histograma")
    #column = st.selectbox("Selecciona la columna para el histograma", numeric_columns)

    # Graficar el histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if show_scat:
    st.subheader("Diagrama de Dispersión")
    fig = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
