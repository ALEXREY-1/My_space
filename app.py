import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import streamlit as st

car_data = pd. read_csv('vehicles_us.csv')

st.header('VENTA DE AUTOS')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir un Grafico de Dispersion')
if disp_button:
    fig = scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)