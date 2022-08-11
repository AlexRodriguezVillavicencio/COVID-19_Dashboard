import pandas as pd
from scipy.signal import find_peaks

def data_organize(df):
    df.fillna(0, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def get_peaks(df,feature:str, prominence:int) -> tuple:
    peak_blue, _ = find_peaks(df[feature], prominence=prominence)

    listd = []
    listv = []
    for i in peak_blue:
        d = list(df[df.index == i].fecha)[0]
        v = list(df[df.index == i][feature])[0]
        listd.append(d)
        listv.append(v)

    df_top = pd.DataFrame()
    df_top['fecha'] =listd
    df_top['top'] =listv 
    return df_top

def tableTransform(dfr4, df_map):
    dfr4.rename(columns={'Estado':'ticker'}, inplace=True)
    dfr4.sort_values('ticker',inplace=True)
    dfr4.reset_index(drop=True,inplace=True)
    df_map.sort_values('ticker', inplace=True)
    df_map.reset_index(drop=True,inplace=True)
    df_newmap =df_map.merge(dfr4, on='ticker', how='left')
    df_newmap.drop('ticker', axis=1,inplace=True)
    df_newmap.sort_values('Total', ascending=False, inplace=True)
    df_newmap.reset_index(drop=True,inplace=True)
    return df_newmap.head(5)