import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
df = pd.read_csv('Miriams_all.csv')

# Limpiar datos
df = df.dropna(subset=['Company', 'Role'])  # Eliminar filas donde 'Company' o 'Role' sean nulos

# Convertir 'Application Date' a datetime
df['Application Date'] = pd.to_datetime(df['Application Date'])

# Título de la aplicación
st.title('Análisis de Aplicaciones de Empleo')

# Distribución de Aplicaciones por Sector
st.header('Número de Aplicaciones por Sector')
sector_counts = df['Sector'].value_counts().reset_index()
sector_counts.columns = ['Sector', 'Count']
fig_sector = px.bar(sector_counts, x='Sector', y='Count', title='Número de Aplicaciones por Sector', 
                    labels={'Sector': 'Sector', 'Count': 'Número de Aplicaciones'}, color='Count')
st.plotly_chart(fig_sector)

# Distribución de Aplicaciones por Tipo de Trabajo
st.header('Distribución de Aplicaciones por Tipo de Trabajo')
type_job_counts = df['Type Job'].value_counts().reset_index()
type_job_counts.columns = ['Type Job', 'Count']
fig_type_job = px.pie(type_job_counts, names='Type Job', values='Count', title='Distribución de Aplicaciones por Tipo de Trabajo')
st.plotly_chart(fig_type_job)

# Estado de las Aplicaciones
st.header('Estado de las Aplicaciones')
status_counts = df['Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']
fig_status = px.bar(status_counts, x='Status', y='Count', title='Estado de las Aplicaciones', 
                    labels={'Status': 'Estado', 'Count': 'Número de Aplicaciones'}, color='Count')
st.plotly_chart(fig_status)

# Aplicaciones a lo Largo del Tiempo
st.header('Aplicaciones a lo Largo del Tiempo')
applications_by_day = df.resample('D', on='Application Date').size().reset_index()
applications_by_day.columns = ['Application Date', 'Count']
fig_applications_by_day = px.line(applications_by_day, x='Application Date', y='Count', title='Aplicaciones a lo Largo del Tiempo', 
                                    labels={'Application Date': 'Fecha', 'Count': 'Número de Aplicaciones'}, markers=True)
st.plotly_chart(fig_applications_by_day)

# Regiones más comunes
st.header('Regiones de las Vacantes')
region_counts = df['Location'].value_counts().reset_index()
region_counts.columns = ['Location', 'Count']
fig_region = px.bar(region_counts, x='Location', y='Count', title= 'Número de Vacantes por Región', 
                    labels={'Location': 'Región', 'Count': 'Número de Vacantes'}, color='Count')
st.plotly_chart(fig_region)
