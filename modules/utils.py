import pandas as pd
import plotly.graph_objects as go

def report1(df):
    df_total = pd.DataFrame()
    df_total['state'] = df['state'] 
    df_total['date'] = df['date']
    df_total['total_adultos_en_cama_con_covid'] = df['total_adult_patients_hospitalized_confirmed_covid']
    df_total['adultos_en_cama_UCI_con_covid'] = df['staffed_icu_adult_patients_confirmed_covid']
    df_total['total_pediatricos_en_cama_con_covid'] = df['total_pediatric_patients_hospitalized_confirmed_covid']
    df_total['pediatricos_en_cama_UCI_con_covid'] = df['staffed_icu_pediatric_patients_confirmed_covid']

    df_total.fillna(0, inplace=True)
    df_total['date'] = pd.to_datetime(df_total['date'])
    df_total.sort_values('date', inplace=True)
    df_total.reset_index(drop=True, inplace=True) 
    return df_total

def report11(df):
    df_total = report1(df)
    mask = (df_total['date'] >= '2020-01-01') & (df_total['date'] < '2020-07-01')
    df_new = df_total[mask]
    df_new = df_new.groupby('date').sum()
    df_new.reset_index(inplace=True)
    return df_new

def reportplot11(df_new):
    fig= go.Figure()
    fig.add_trace(go.Scatter(
        x=df_new['date'],
        y=df_new['total_adultos_en_cama_con_covid'],
        mode='lines', 
        name='Adultos con Covid',
        line=dict(color='#cee3e1')
        # visible='legendonly'
    ))
    fig.add_trace(go.Scatter(
        x=df_new['date'],
        y=df_new['total_pediatricos_en_cama_con_covid'],
        mode='lines',
        name='Menores de Edad con Covid'
    ))
    fig.update_layout(
        plot_bgcolor='#111111',
        paper_bgcolor= '#111111',
        font_color='#cee3e1',
        legend=dict(
            x=0.05,
            y=1,
            traceorder="reversed",
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
        margin=dict(
                    l=10,
                    r=10,
                    b=10,
                    t=10,
                    pad=1
                ),
    )
    return fig

def report12(df):
    df_total = report1(df)
    mask = (df_total['date'] >= '2020-01-01') & (df_total['date'] < '2020-07-01')
    df_new = df_total[mask].groupby('state').sum()
    df_new['total'] = df_new['total_adultos_en_cama_con_covid'] + df_new['total_pediatricos_en_cama_con_covid']
    df_new.drop(['adultos_en_cama_UCI_con_covid','pediatricos_en_cama_UCI_con_covid'], axis=1, inplace=True)
    df_new.sort_values('total', ascending=False, inplace=True)
    df_new.reset_index(inplace=True)
    df_new.rename(columns={'state':'estado',
            'total_adultos_en_cama_con_covid':'adultos',
            'total_pediatricos_en_cama_con_covid':'pediatricos'}, inplace=True)
    df_new['adultos']=df_new['adultos'].astype(int)
    df_new['pediatricos']=df_new['pediatricos'].astype(int)
    df_new['total']=df_new['total'].astype(int)
    df_new= df_new.head(5)
    return df_new

def reportplot12(df_new):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_new.columns),
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[df_new['estado'],df_new['adultos'],df_new['pediatricos'],df_new['total']],
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
    ])

    fig.update_layout(width=700,
                height=150,
                paper_bgcolor= '#111111',
                font_color='#111111',
                # autosize=False,
                # automargin=True

                margin=dict(
                    l=10,
                    r=10,
                    b=10,
                    t=10,
                    pad=1
                ),
            )
    fig.update_yaxes(automargin=True)
    return fig