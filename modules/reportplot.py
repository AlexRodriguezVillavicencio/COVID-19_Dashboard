import plotly.graph_objects as go
import plotly.express as px

def linealPlot(df_new):
    fig= go.Figure(data=[
        go.Scatter(
        x=df_new['date'],
        y=df_new['adultos_cama_covid'],
        mode='lines', 
        name='Adultos con Covid',
        line=dict(color='cyan')
        ),
        go.Scatter(
        x=df_new['date'],
        y=df_new['menores_cama_covid'],
        mode='lines',
        name='Menores de Edad con Covid'
        ),
    ])
    fig.update_layout(
        height=300,
        plot_bgcolor='black',
        paper_bgcolor= 'black',
        font_color='#cee3e1',
        legend=dict(
            x=0.05,
            y=1,
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


def lineal2Plot(df_NY,dft_adultos,dft_menores):
    fig= go.Figure(data=[
        go.Scatter(
        x=df_NY['fecha'],
        y=df_NY['adultos_cama_comun'],
        mode='lines', 
        name='Adultos con Covid',
        line=dict(color='cyan')
        ),
        go.Scatter(
        x=df_NY['fecha'],
        y=df_NY['menores_cama_comun'],
        mode='lines',
        name='Menores de Edad con Covid'
        ),
        go.Scatter(
        x=dft_adultos['fecha'],
        y=dft_adultos['top'],
        mode='markers + text',
        name='Adultos Picos',
        marker=dict(color='red',size=12),
        text = dft_adultos['fecha'],
        textposition="top center",
        visible='legendonly'
        ),
        go.Scatter(
        x=dft_menores['fecha'],
        y=dft_menores['top'],
        mode='markers + text',
        name='Menores Picos',
        marker=dict(color='orange',size=12),
        text = dft_menores['fecha'],
        textposition="top center",
        visible='legendonly'
        ),
    ])
    fig.update_layout(
        # title=name_title,
        height=300,
        plot_bgcolor='black',
        paper_bgcolor= 'black',
        font_color='#cee3e1',
        legend=dict(
            x=0.05,
            y=1,
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


def lineal3Plot(df_new):
    fig= go.Figure(data=[
        go.Scatter(
        x=df_new['date'],
        y=df_new['Muertes covid'],
        mode='lines', 
        name='Muertes covid',
        line=dict(color='cyan')
        ),
        go.Scatter(
        x=df_new['date'],
        y=df_new['Personal Ausente'],
        mode='lines',
        name='Personal Ausente'
        ),
    ])
    fig.update_layout(
        # title=name_title,
        height=300,
        plot_bgcolor='black',
        paper_bgcolor= 'black',
        font_color='#cee3e1',
        legend=dict(
            x=0.05,
            y=1,
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


def piePlot(labels,values,ta):
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values, hole=.4))
    fig.update_traces(marker=dict(colors=['rgb(100, 255, 233)', 'cyan']))
    fig.update_layout(
        height=260,
        paper_bgcolor= 'royalblue',
        font_color='#cee3e1',
        margin=dict(l=10,r=10,b=15,t=15),
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
        ))
    fig.add_annotation(x=2, y=0.03,
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
        ))
    return fig

def tablePlot(df_head,df_body):
    fig = go.Figure(data=[go.Table(
        columnwidth = [3,2],
        header=dict(
                    values=df_head,
                    line_color='black',
                    fill_color='black',
                    align='left',
                    font=dict(size=20)),
        cells=dict(values=df_body.T,
                   line_color='black',
                   fill_color='royalblue',
                   align=['left','center'],
                   height=30,
                   font=dict(size=15),))
    ])
    fig.update_layout(
        # width=50,
        height=260,
        # paper_bgcolor= 'royalblue',
        font_color='#cee3e1',
        margin=dict(l=10,r=10,b=10,t=10))
    return fig

def barPlot(df,x,y):
    fig = px.bar(df,x,y,color=y,template='plotly_dark',text=y,
            color_continuous_scale=[
                [0, "rgb(166, 255, 249)"],
                [0.25, "rgb(132, 255, 233)"],
                [0.50, "rgb(100, 255, 233)"],
                [0.75, "rgb(0, 186, 186)"],
                [1, "rgb(0, 124, 124)"],
            ])
    fig.update_layout(
            width=700,
            height=300,
            margin=dict(l=10,r=10,b=10,t=10),
            yaxis_title='',
            xaxis_title='',
            yaxis=dict(
                showticklabels=False)
        )
    return fig


def mapPlot(df_newmap):
    data = dict(type = 'choropleth', 
                locations = df_newmap['ticker'], 
                locationmode = 'USA-states', 
                z = list(df_newmap['Muertes covid']), 
                colorscale=[
                    [0, "rgb(243, 255, 250)"],
                    [0.10, "rgb(166, 255, 249)"],
                    [0.25, "rgb(132, 255, 233)"],
                    [0.50, "rgb(100, 255, 233)"],
                    [0.60, "rgb(0, 248, 248)"],
                    [0.75, "rgb(0, 186, 186)"],
                    [1, "rgb(0, 124, 124)"]],
                text = df_newmap['estado'])
    layout = dict(geo = dict(scope='usa'))

    fig = go.Figure(data=[data], layout=layout)
    fig.update_layout(
        # title='Mapa de fallecidos por covid',
        # width=800,
        margin=dict(l=5,r=5,b=5,t=5),
        paper_bgcolor= 'black',
        font_color='#cee3e1',
    )              
    return fig

def scatterPlot(dfr):
    fig = px.scatter(dfr, x="Personal Ausente", y="Muertes covid", 
            color="Muertes covid", template='plotly_dark',
            color_continuous_scale=[
                    [0.0, "rgb(132, 255, 233)"],
                    [0.50, "rgb(100, 255, 233)"],
                    [1, "rgb(0, 186, 186)"],
                ])
    fig.update_layout(height=300)
    return fig