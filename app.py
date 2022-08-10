import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

import modules.report as rp
import modules.reportplot as rplt
from modules.utils import get_peaks

df = pd.read_csv("report/covid19.csv")
df_map = pd.read_csv('report/mapaeeuu.csv')

######################################################
# gráfico de lineas
dfr1 = rp.linealDataframe(df)
fig1 = rplt.linealPlot(dfr1)

# gráfico circular adultos
dfr2 = rp.pieTuple(df)
labels = dfr2[0]
values = dfr2[1]
ta = dfr2[2]
fig2 = rplt.piePlot(labels,values,ta)

#gráfico circular pediatricos
dfr3 = rp.pieTuple(df)
labels = dfr3[3]
values = dfr3[4]
ta = dfr3[5]
fig3 = rplt.piePlot(labels,values,ta)

# tabla top 5
dfr4 = rp.barDataframe(df,
        df_var=['total_adultos_en_cama_con_covid','total_pediatricos_en_cama_con_covid'],
        df_remove=['adultos_en_cama_UCI_con_covid','pediatricos_en_cama_UCI_con_covid'],
        date_in='2020-01-01',date_out='2020-07-01')
df_new = dfr4.head(5)
fig4 = rplt.tablePlot(
        df_head=['Estado','Adultos','Menores de edad', 'Total'],
        df_body=df_new)

# grafico de barras de adultos
dfr5 = rp.rangeAdult(df)
fig5 = rplt.barPlot(dfr5,'Rango de edad','Casos con covid')

# grafico de barras de pediatricos
dfr6 = rp.rangePediatric(df)
fig6 = rplt.barPlot(dfr6,'Rango de edad','Casos con covid')


######################################################
df_NY = rp.lineal2Dataframe(df)
dft_menores = get_peaks(df_NY,'menores_cama_comun',prominence=30)
dft_adultos = get_peaks(df_NY,'adultos_cama_comun',prominence=200)
fig7 = rplt.lineal2Plot(df_NY,dft_adultos,dft_menores)



######################################################
# tabla top 5
dfr8 = rp.barDataframe(df=df,
        df_var=['adultos_en_cama_UCI_con_covid','pediatricos_en_cama_UCI_con_covid'],
        df_remove=['total_adultos_en_cama_con_covid','total_pediatricos_en_cama_con_covid'],
        date_in='2020-01-01',date_out='2020-07-01')
df_new = dfr8.head(5)
fig8 = rplt.tablePlot(
        df_head=['Estado','Adultos UCI','Menores de edad UCI', 'Total'],
        df_body=df_new)


######################################################
# total camas pediatricas covid 2020
dfr9 = rp.report4(df)
dfr9['Camas pediátrico'].sum()

# gráfico de barras de camas pediatricas por estado
fig8 = rplt.barPlot(dfr8,'estado','Camas pediátrico')


######################################################
# porcentaje de camas uci por estado
dfr9 = rp.bar2Dataframe(df=df,
        df_var=['adultos_camaUci','menores_camaUci','adultos_camaUci_covid','menores_camaUci_covid'],
        df_remove=['adultos_cama_covid','menores_cama_covid'],
        date_in='2020-01-01',date_out='2022-03-01')

######################################################
# muertes por covid por estado en 2021
dfr10 = rp.deathBarDataframe(df,'2021-01-01','2021-12-31')
fig10 = rplt.barPlot(dfr10,'Estado','Muertes covid')






st.title("Dashboard Covid-19")
with st.sidebar:
    choose = option_menu("Menú Principal",["Página 1","Página 2","Página 3"],
        icons=['house','camera fill','kanban'],
        menu_icon="app-indicator", default_index=0,
        styles={
            'container': {'padding':'0!important'},
            'icon':{'color':'orange','font-size':'25px'},
            'nav-link':{'font-size':'16px'},
            'nav-link-selected':{'background':'cyan'}
        }
    )

if choose == "Página 1":
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.plotly_chart(fig3, use_container_width=True)
    st.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)
    st.plotly_chart(fig6, use_container_width=True)