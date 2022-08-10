from modules.dataframe import data_adult_pediatric
from modules.dataframe import data_agerange_adult
from modules.dataframe import data_agerange_pediatric
from modules.utils import data_organize
import pandas as pd


def linealDataframe(df, date_in:str='2020-01-01', date_out:str='2020-06-30'):
    df_total = data_adult_pediatric(df)
    mask = (df_total['date'] >= date_in) & (df_total['date'] <= date_out)
    df_new = df_total[mask]
    df_new = df_new.groupby('date').sum()
    df_new.reset_index(inplace=True)
    return df_new


def onlyState_Dataframe(df, date_in:str='2020-03-01', date_out:str='2021-04-01', state:str='NY'):    
    dft = data_adult_pediatric(df)
    mask = (dft['date'] >= date_in) & (dft['date'] < date_out)
    df_new = dft[mask]
    dfm = pd.DataFrame()
    dfm['fecha'] = df_new['date'].astype(str)
    dfm['estado'] = df_new['state']
    dfm['adultos_cama_comun'] = df_new['adultos_cama_covid'] - df_new['adultos_camaUci_covid']
    dfm['menores_cama_comun'] = df_new['menores_cama_covid'] - df_new['menores_camaUci_covid']
    df_NY = dfm[dfm['estado'] == state]
    df_NY.reset_index(drop=True,inplace=True)
    return df_NY


def pieTuple(df, date_in:str='2020-01-01', date_out:str='2020-06-30'):
    df_total = data_adult_pediatric(df)
    mask = (df_total['date'] >= date_in) & (df_total['date'] <= date_out)
    dft = df_total[mask]
    n1 = int(dft['adultos_cama_covid'].sum())
    a = int(dft['adultos_camaUci_covid'].sum())
    n2= int(dft['menores_cama_covid'].sum())
    n = int(dft['menores_camaUci_covid'].sum())  
    p1 = n1-a
    labels1 = ['Adultos en cama normal','Adultos en cama UCI']
    values1 = [p1,a]  
    p2 = n2-n
    labels2 = ['Menores de edad en cama normal','Menores de edad en cama UCI']
    values2 = [p2,n]
    return labels1,values1,n1,labels2,values2,n2


def barDataframe(df,date_in:str,date_out:str, df_var, df_remove:list):
    df_total = data_adult_pediatric(df)
    mask = (df_total['date'] >= date_in) & (df_total['date'] <= date_out)
    df_new = df_total[mask].groupby('state').sum()
    df_new['total'] = df_new[df_var[0]] + df_new[df_var[1]]
    df_new.drop(df_remove, axis=1, inplace=True)
    df_new.sort_values('total', ascending=False, inplace=True)
    df_new.reset_index(inplace=True)
    return df_new


def rangeAdult(df, date_in:str='2020-01-01', date_out:str='2020-06-30'):
    df_adult = data_agerange_adult(df)
    mask = (df_adult['date'] >= date_in) & (df_adult['date'] <= date_out)
    df_new = df_adult[mask]
    c1 = int(df_new['18-19'].sum())
    c2 = int(df_new['20-29'].sum())
    c3 = int(df_new['30-39'].sum())
    c4 = int(df_new['40-49'].sum())
    c5 = int(df_new['50-59'].sum())
    c6 = int(df_new['60-69'].sum())
    c7 = int(df_new['70-79'].sum())
    c8 = int(df_new['80+'].sum())
    c9 = int(df_new['desconocido'].sum())
    dft = pd.DataFrame()
    dft['Rango de edad'] = list(df_new.columns)
    dft['Casos con covid'] = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
    return dft


def rangePediatric(df, date_in:str='2020-01-01', date_out:str='2020-06-30'):
    df_pediatric = data_agerange_pediatric(df)
    mask = (df_pediatric['date'] >= date_in) & (df_pediatric['date'] <= date_out)
    df_new = df_pediatric[mask]
    c1 = int(df_new['0-4'].sum())
    c2 = int(df_new['5-11'].sum())
    c3 = int(df_new['12-17'].sum())
    c4 = int(df_new['desconocido'].sum())

    dft = pd.DataFrame()
    dft['Rango de edad'] = list(df_new.columns)
    dft['Casos con covid'] = [c1,c2,c3,c4]
    return dft

def mapDataframe(df,df_map, date_in:str='2020-01-01', date_out:str='2020-06-30'):
    df_total = data_adult_pediatric(df)
    mask = (df_total['date'] >= date_in) & (df_total['date'] <= date_out)
    df_new = df_total[mask].groupby('state').sum()

    dfc = pd.DataFrame()
    dfc['estado'] = df_new.index
    dfc['camas_pediatrico'] = list(df_new['total_pediatricos_en_cama_con_covid'])
    dfc.rename(columns={'estado':'ticker'}, inplace=True)
    dfc.sort_values('ticker',inplace=True)
    dfc.reset_index(drop=True,inplace=True)

    df_map.sort_values('ticker', inplace=True)
    df_map.reset_index(drop=True,inplace=True)
    df_newmap =df_map.merge(dfc, on='ticker', how='left')
    return df_newmap

def report4(df, date_in:str='2020-01-01', date_out:str='2021-01-01'):
    df_total = data_adult_pediatric(df)
    mask = (df_total['date'] >= date_in) & (df_total['date'] <= date_out)
    df_new = df_total[mask].groupby('state').sum()

    dfc = pd.DataFrame()
    dfc['estado'] = df_new.index
    dfc['Camas pediátrico'] = list(df_new['total_pediatricos_en_cama_con_covid'])
    return dfc

def bar2Dataframe(df,date_in:str,date_out:str, df_var, df_remove:list):
    df_total = data_adult_pediatric(df)
    mask = (df_total['date'] >= date_in) & (df_total['date'] <= date_out)
    df_new = df_total[mask].groupby('state').sum()
    df_new['total_camaUci'] = df_new[df_var[0]] + df_new[df_var[1]]
    df_new['total_camaUci_covid'] = df_new[df_var[2]] + df_new[df_var[3]]
    df_new['porcentaje'] = round(df_new['total_camaUci_covid']/df_new['total_camaUci'],2)
    df_new.drop(df_remove, axis=1, inplace=True)
    df_new.sort_values('porcentaje', ascending=False, inplace=True)
    df_new.reset_index(inplace=True)
    return df_new


def deathBarDataframe(df,date_in:str,date_out:str):
    dfn = pd.DataFrame()
    dfn['Estado'] = df['state'] 
    dfn['date'] = df['date']
    dfn['Muertes covid'] = df['deaths_covid']
    dfn = data_organize(dfn)
    dfn = dfn.convert_dtypes()
    mask = (dfn['date'] >= date_in) & (dfn['date'] <= date_out)
    df_new = dfn[mask].groupby('Estado').sum()
    df_new.sort_values('Muertes covid', ascending=False, inplace=True)
    df_new.reset_index(inplace=True)
    return df_new