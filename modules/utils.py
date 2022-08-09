import pandas as pd
import plotly.graph_objects as go

def data_organize(df):
    df.fillna(0, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def report1_data_adult_pediatric(df):
    df_new = pd.DataFrame()
    df_new['state'] = df['state'] 
    df_new['date'] = df['date']
    df_new['total_adultos_en_cama_con_covid'] = df['total_adult_patients_hospitalized_confirmed_covid']
    df_new['adultos_en_cama_UCI_con_covid'] = df['staffed_icu_adult_patients_confirmed_covid']
    df_new['total_pediatricos_en_cama_con_covid'] = df['total_pediatric_patients_hospitalized_confirmed_covid']
    df_new['pediatricos_en_cama_UCI_con_covid'] = df['staffed_icu_pediatric_patients_confirmed_covid']
    df_new = data_organize(df_new)  
    return df_new


def report1_data_agerange_adult(df):
    df_new = pd.DataFrame()
    df_new['state'] = df['state'] 
    df_new['date'] = df['date']
    df_new['covid_18_19'] = df['previous_day_admission_adult_covid_confirmed_18-19']
    df_new['covid_20_29'] = df['previous_day_admission_adult_covid_confirmed_20-29']
    df_new['covid_30_39'] = df['previous_day_admission_adult_covid_confirmed_30-39']
    df_new['covid_40_49'] = df['previous_day_admission_adult_covid_confirmed_40-49']
    df_new['covid_50_59'] = df['previous_day_admission_adult_covid_confirmed_50-59']
    df_new['covid_60_69'] = df['previous_day_admission_adult_covid_confirmed_60-69']
    df_new['covid_70_79'] = df['previous_day_admission_adult_covid_confirmed_70-79']
    df_new['covid_80+'] = df['previous_day_admission_adult_covid_confirmed_80+']
    df_new['covid_desconocido'] = df['previous_day_admission_adult_covid_confirmed_unknown']
    df_new = data_organize(df_new) 
    return df_new

def report1_data_agerange_pediatric(df):
    df_new = pd.DataFrame()
    df_new['state'] = df['state'] 
    df_new['date'] = df['date']
    df_new['covid_0_4'] = df['previous_day_admission_pediatric_covid_confirmed_0_4']
    df_new['covid_5_11'] = df['previous_day_admission_pediatric_covid_confirmed_5_11']
    df_new['covid_12_17'] = df['previous_day_admission_pediatric_covid_confirmed_12_17']
    df_new['covid_desconocido'] = df['previous_day_admission_pediatric_covid_confirmed_unknown']
    df_new = data_organize(df_new) 
    return df_new

####################################
def report1_lineal(df):
    df_total = report1_data_adult_pediatric(df)
    mask = (df_total['date'] >= '2020-01-01') & (df_total['date'] < '2020-07-01')
    df_new = df_total[mask]
    df_new = df_new.groupby('date').sum()
    df_new.reset_index(inplace=True)
    return df_new

def reportplot1_lineal(df_new):
    fig= go.Figure(data=[
        go.Scatter(
        x=df_new['date'],
        y=df_new['total_adultos_en_cama_con_covid'],
        mode='lines', 
        name='Adultos con Covid',
        line=dict(color='cyan')
        # visible='legendonly'
        ),
        go.Scatter(
        x=df_new['date'],
        y=df_new['total_pediatricos_en_cama_con_covid'],
        mode='lines',
        name='Menores de Edad con Covid'
        ),

    ])
    fig.update_layout(
        plot_bgcolor='#111111',
        paper_bgcolor= '#111111',
        font_color='#cee3e1',
        legend=dict(
            x=0.05,
            y=1,
            # traceorder="reversed",
            title_font_family="Times New Roman",
            font=dict(
                family="Courier",
                size=12,
                color="LightSteelBlue"
            ),
            bgcolor="Black",
            bordercolor="LightSteelBlue",
            borderwidth=1
        ),
        xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
        yaxis=dict(showgrid=False),
        margin=dict(l=10,r=10,b=10,t=10)
    )
    return fig

####################################

def report1_pie(df):
    df_total = report1_data_adult_pediatric(df)
    mask = (df_total['date'] >= '2020-01-01') & (df_total['date'] < '2020-07-01')
    dft = df_total[mask]
    ta = int(dft['total_adultos_en_cama_con_covid'].sum())
    a = int(dft['adultos_en_cama_UCI_con_covid'].sum())
    nt= int(dft['total_pediatricos_en_cama_con_covid'].sum())
    n = int(dft['pediatricos_en_cama_UCI_con_covid'].sum())
    
    p1 = ta-a
    labels1 = ['Adultos en cama normal','Adultos en cama UCI']
    values1 = [p1,a]  
    p2 = nt-n
    labels2 = ['Menores de edad en cama normal','Menores de edad en cama UCI']
    values2 = [p2,n]
    return labels1,values1,ta,labels2,values2,nt

def reportplot1_pie(labels,values,ta):
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values, hole=.4))
    fig.update_traces(marker=dict(colors=['royalblue', 'cyan']))
    fig.update_layout(
        width=600,
        paper_bgcolor= 'darkblue',
        font_color='#cee3e1',
        margin=dict(
            l=10,
            r=10,
            b=10,
            t=10, 
        ),
        legend=dict(
            y=0.9,
            font=dict(
                family="Courier",
                size=12,
                color="LightSteelBlue"
            ),
            bgcolor="Black",
            bordercolor="LightSteelBlue",
            borderwidth=1
        )
    )
    fig.add_annotation(x=1.4, y=0.03,
        text= f'Total: {ta} casos',
        showarrow=False,
        bordercolor="LightSteelBlue",
        borderwidth=1,
        borderpad=8,
        bgcolor="Black",
        align="center",
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="#ffffff"
        )
    )
    return fig

#######################################


def report1_barstate(df):
    df_total = report1_data_adult_pediatric(df)
    mask = (df_total['date'] >= '2020-01-01') & (df_total['date'] < '2020-07-01')
    df_new = df_total[mask].groupby('state').sum()
    df_new['total'] = df_new['total_adultos_en_cama_con_covid'] + df_new['total_pediatricos_en_cama_con_covid']
    df_new.drop(['adultos_en_cama_UCI_con_covid','pediatricos_en_cama_UCI_con_covid'], axis=1, inplace=True)
    df_new.sort_values('total', ascending=False, inplace=True)
    df_new.reset_index(inplace=True)
    df_new['total_adultos_en_cama_con_covid']=df_new['total_adultos_en_cama_con_covid'].astype(int)
    df_new['total_pediatricos_en_cama_con_covid']=df_new['total_pediatricos_en_cama_con_covid'].astype(int)
    df_new['total']=df_new['total'].astype(int)
    return df_new

def reportplot1_barstate(df):
    X=list(df['state'])
    Ya=list(df['total_adultos_en_cama_con_covid'])
    Ym=list(df['total_pediatricos_en_cama_con_covid'])
    fig = go.Figure(data = [
        go.Bar(x=X, y=Ya, name='Adultos'),
        go.Bar(x=X, y=Ym, name='Menores de Edad')
        ])
    return fig

##############################

def reportplot1_table(df):
    df_new = df.head(5)
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Estado','Adultos','Menores de Edad','Total'],
                    line_color='cyan',
                    fill_color='royalblue',
                    align='left'),
        cells=dict(values=[df_new['state'],df_new['total_adultos_en_cama_con_covid'],
                   df_new['total_pediatricos_en_cama_con_covid'],df_new['total']],
                   line_color='cyan',
                   fill_color='black',
                   align='left'))
    ])

    fig.update_layout(
                width=550,
                height=150,
                paper_bgcolor= '#111111',
                font_color='#cee3e1',

                margin=dict(
                    l=10,
                    r=10,
                    b=10,
                    t=10,
                ),
            )
    return fig

#########################################

def report1_agerange_adult(df):
    df_adult = report1_data_agerange_adult(df)
    mask = (df_adult['date'] >= '2020-01-01') & (df_adult['date'] < '2020-07-01')
    df_new = df_adult[mask]
    c1 = int(df_new['covid_18_19'].sum())
    c2 = int(df_new['covid_20_29'].sum())
    c3 = int(df_new['covid_30_39'].sum())
    c4 = int(df_new['covid_40_49'].sum())
    c5 = int(df_new['covid_50_59'].sum())
    c6 = int(df_new['covid_60_69'].sum())
    c7 = int(df_new['covid_70_79'].sum())
    c8 = int(df_new['covid_80+'].sum())
    c9 = int(df_new['covid_desconocido'].sum())
    x=['18-19','20-29','30-39','40-49','50-59','60-69','70-79','80+','Desconocido']
    y=[c1,c2,c3,c4,c5,c6,c7,c8,c9]
    return x,y

def report1_agerange_pediatric(df):
    df_pediatric = report1_data_agerange_pediatric(df)
    mask = (df_pediatric['date'] >= '2020-01-01') & (df_pediatric['date'] < '2020-07-01')
    df_new = df_pediatric[mask]
    c1 = int(df_new['covid_0_4'].sum())
    c2 = int(df_new['covid_5_11'].sum())
    c3 = int(df_new['covid_12_17'].sum())
    c4 = int(df_new['covid_desconocido'].sum())
    x=['0-4','5-11','12-17','Desconocido']
    y=[c1,c2,c3,c4]
    return x,y


def reportplot1_agerange(x,y):
    fig = go.Figure()
    fig.add_bar(x=x, y=y, text=y, textposition='auto')
    fig.update_traces(
        # marker_color='royalblue'
    )
    fig.update_layout(
            width=550,
            height=300,
            paper_bgcolor= '#111111',
            plot_bgcolor='#111111',
            font_color='#cee3e1',

            margin=dict(
                l=10,
                r=10,
                b=10,
                t=10,
            ),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
    )
    return fig