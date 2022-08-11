import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import datetime
import modules.report as rp
import modules.reportplot as rplt
from modules.utils import get_peaks, tableTransform

df = pd.read_csv("report/covid19.csv")
df_map = pd.read_csv('report/mapaeeuu.csv')

st.set_page_config(page_title="Dashboard Covid-19",
                    page_icon=":bar_chart:",
                    layout="wide",
                    )

# --------------- SIDEBAR ----------------------
with st.sidebar:
    choose = option_menu("Menú",["PRINCIPAL","Conclusiones"],
        icons=['kanban','kanban','kanban'],
        menu_icon="app-indicator", default_index=0,
        styles={
            'container': {'padding':'0!important'},
            'icon':{'color':'cyan','font-size':'25px'},
            'nav-link':{'font-size':'16px'},
            'nav-link-selected':{'background':'cyan'}
        }
    )
    col1, col2 = st.columns(2)
    with col1:
        d_in = st.date_input("inicio",datetime.date(2020,1,1))
    with col2:
        d_out = st.date_input("fin",datetime.date(2020,6,30))

    optionTicker = st.selectbox(
     'Selecciona un Estado:',
     list(df_map['ticker']))


######################################################
dfr1 = rp.linealDataframe(df,str(d_in),str(d_out))
fig1 = rplt.linealPlot(dfr1)

dfr2 = rp.pieTuple(df,str(d_in),str(d_out))
fig2 = rplt.piePlot(dfr2[0],dfr2[1],dfr2[2])

dfr3 = rp.pieTuple(df,str(d_in),str(d_out))
fig3 = rplt.piePlot(dfr3[3],dfr3[4],dfr3[5])

dfr4 = rp.barDataframe(df,
        df_var=['adultos_cama_covid','menores_cama_covid'],
        date_in=str(d_in),date_out=str(d_out))
dfr4 = tableTransform(dfr4,df_map)
fig4 = rplt.tablePlot(
        df_head=['TOP 5'],
        df_body=dfr4)

dfr5 = rp.rangeAdult(df,str(d_in),str(d_out))
fig5 = rplt.barPlot(dfr5,'Rango de edad','Casos con covid')

dfr6 = rp.rangePediatric(df,str(d_in),str(d_out))
fig6 = rplt.barPlot(dfr6,'Rango de edad','Casos con covid')


######################################################
df_NY = rp.onlyState_Dataframe(df,ticker= optionTicker,date_in=str(d_in),date_out=str(d_out))
dft_menores = get_peaks(df_NY,'menores_cama_comun',prominence=30)
dft_adultos = get_peaks(df_NY,'adultos_cama_comun',prominence=200)
fig7 = rplt.lineal2Plot(df_NY,dft_adultos,dft_menores)

######################################################
# tabla top 5
dfr8 = rp.barDataframe(df=df,
        df_var=['adultos_camaUci_covid','menores_camaUci_covid'],
        date_in=str(d_in),date_out=str(d_out))
dfr8 = tableTransform(dfr8,df_map)
fig8 = rplt.tablePlot(
        df_head=['TOP 5'],
        df_body=dfr8)


######################################################
# total camas pediatricas covid 2020
dfr9 = rp.report4(df,date_in=str(d_in),date_out=str(d_out))

# gráfico de barras de camas pediatricas por estado
fig9 = rplt.barPlot(dfr9,'estado','Camas pediátrico')


######################################################
# porcentaje de camas uci por estado
dfrN = rp.bar2Dataframe(df=df,
        df_var=['adultos_camaUci','menores_camaUci','adultos_camaUci_covid','menores_camaUci_covid'],
        df_remove=['adultos_cama_covid','menores_cama_covid'],
        date_in=str(d_in),date_out=str(d_out))
figN = rplt.barPlot(dfrN,'state','porcentaje')
######################################################
# muertes por covid por estado en 2021
dfr10 = rp.deathBarDataframe(df,date_in=str(d_in),date_out=str(d_out))
fig10 = rplt.barPlot(dfr10,'Estado','Muertes covid')
dfm = dfr10['Muertes covid'].sum()
######################################################
# muertes por covid vs personal medico lineal
dfr11 = rp.absentStaffDataframe(df,date_in=str(d_in),date_out=str(d_out))
fig11 = rplt.lineal3Plot(dfr11)

# muertes por covid vs personal medico scatter
dfr12 = rp.absentStaffDataframe(df,date_in=str(d_in),date_out=str(d_out))
fig12 = rplt.scatterPlot(dfr12)

dfr13 = rp.mapDataframe(df,df_map,date_in=str(d_in),date_out=str(d_out))
dfr13 = dfr13.sort_values('Muertes covid', ascending=False)
dfr13 = dfr13.reset_index(drop=True)
dfn = dfr13['estado'][0]
dfp = dfr13['Muertes covid'][0]
fig13 = rplt.mapPlot(dfr13)

# ------------- MAIN ----------------
st.title(":bar_chart: Dashboard Covid-19")
st.markdown("##")

if choose == "PRINCIPAL":
    
    # --------------- KPI's -------------

    col1, col2= st.columns([2,3])
    with col1:
        st.subheader(f"Total Muertoss: {dfm:,}")
    with col2:
        st.subheader(f"Estado más Afectado: {dfn} con {dfp:,} casos")

    st.markdown("----")


    col1,col2 = st.columns([1,4])
    with col1:
        genre = st.radio('',
        ('Ocupación hospitalaria',
        'Ocupación de camas pediátricas',
        ))
        if genre == 'Ocupación hospitalaria':
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.plotly_chart(fig8, use_container_width=True)
    with col2:
        tab1,tab2= st.tabs(['Ausencia de personal vs Muertes',
                                    'Personal vs Muertes',
                                    ])
        tab1.plotly_chart(fig12, use_container_width=True)
        tab2.plotly_chart(fig11, use_container_width=True)

    tab1,tab2,tab3,tab4,tab5= st.tabs(['Contagios','Ocupación camas común',
                        "Muertes por covid","Camas que se utilizaron en pacientes pediátricos",
                        "(camas UCI covid)/(camas UCI total) por estado"])
    tab1.plotly_chart(fig1, use_container_width=True) 
    tab2.plotly_chart(fig7, use_container_width=True)
    tab3.plotly_chart(fig10, use_container_width=True)
    tab4.plotly_chart(fig9, use_container_width=True)
    tab5.plotly_chart(figN, use_container_width=True)

    col1,col2 = st.columns([2,3])        
    with col1:
        tab1, tab2= st.tabs(["Adultos con covid", "Menores de edad con covid"])
        with tab1:
            st.plotly_chart(fig2, use_container_width=True)
        with tab2:
            st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        tab1, tab2= st.tabs(["Rango de edad Adultos", "Rango de edad Menores"])
        with tab1:
            st.plotly_chart(fig5, use_container_width=True)
        with tab2:
            st.plotly_chart(fig6, use_container_width=True)
   
    st.plotly_chart(fig13, use_container_width=True)


if choose == "Conclusiones":
    st.markdown('''
    - El rango de edad si influye, esto lo podimos observar en los gráficos circulares,
    comparando adultos y niños, los adultos tuvieron la mayor tasa de mortalidad cientos de veces más que
    los menores de edad. Este comportamiento también lo observamos en la linea de tiempo de los infectados.
    Al comparar el gráfico de barras dividido por rangos de edad, observamos que las personas mayores
    de 50 años fueron las más afectadas.

    - Para el estado de nueva york, consideramos un rango de todo el 2020 a partir de marzo para fines didacticos, 
    los picos fueron el 29-julio-2020, 30-diciembre-2020, 19 de enero del 2021 donde fue uno de los puntos más altos.

    - Ahora analizaremos en todo el trayecto que la data indique: 01-enero-2020 a 31-julio-2020:
        -Nuevo Mexico (MN): los picos son de 29-diciembre-2020, 14-abril-2021, 9-diciembre-2021, 14-junio-2020
        -Nueva York (YK): lod picod más relevantes son el 19-enero-2021 y 11-enero-2020
        -Arizona (AZ): 16-julio-2020, 8-enero-2021 y 27-enero-2020
        -Texas (TX): 28-julio-2020, 11-enero-2021, 31-agosto-2021, 24-enero-2022 

    -Del análisis anterior podemos pensar que uno de los peores meses para EEUU fue en enero del 2021

    - Al analizar la gráfica de personal ausente vs personas muertas por covid, no vemos un patrón de linealidad tan marcada,
    con lo que podemos decir que la relación entre ambas variables es debil.
    
    ''')