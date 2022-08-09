import streamlit as st
import pandas as pd
from modules.utils import report11, reportplot11
from modules.utils import report12, reportplot12

st.title("Dashboard Covid-19")
columna = st.sidebar.radio("Cuestionario: ", [
                                "1 - ¿Cuáles fueron los 5 Estados con mayor ocupación hospitalaria por COVID?",
                                "2 - Ocupación de camas (Común) por COVID en el Estado de Nueva York",
                                "3 - ¿Cuáles fueron los cinco Estados que más camas UCI utilizaron durante el año 2020?",
                                "4 - ¿Qué cantidad de camas se utilizaron, por Estado, para pacientes pediátricos con COVID durante el 2020?",
                                "5 - ¿Qué porcentaje de camas UCI corresponden a casos confirmados de COVID-19?",
                                "6 - ¿Cuántas muertes por covid hubo, por Estado, durante el año 2021?",
                                "7 - ¿Qué relación presenta la falta de camas UCI disponibles con la cantidad de muertes durante el año 2021?",
                                "8 - ¿cuál fue el peor mes de la pandemia para USA en su conjunto?",
                                "9 - ¿Qué recomendaciones haría, ex post, con respecto a los recursos hospitalarios y su uso?"])

df = pd.read_csv("report/covid19.csv")

df_new = report11(df)
fig = reportplot11(df_new)
df_new2 = report12(df)
fig2 = reportplot12(df_new2)
if columna == "1 - ¿Cuáles fueron los 5 Estados con mayor ocupación hospitalaria por COVID?":
    st.subheader("Estados con mayor ocupación hospitalaria")
    st.text(" Criterio de ocupación por cama común.")
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)


if columna == "2 - Ocupación de camas (Común) por COVID en el Estado de Nueva York":
    st.subheader("Ocupación de camas (Común) por COVID en el Estado de Nueva York")
    st.text("Intervalos de crecimiento y decrecimiento")
    st.text("Puntos críticos (mínimos y máximos)")
    