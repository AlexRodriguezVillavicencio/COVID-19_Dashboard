from modules.utils import data_organize
import pandas as pd

def data_adult_pediatric(df):
    df_new = pd.DataFrame()
    df_new['state'] = df['state'] 
    df_new['date'] = df['date']
    df_new['adultos_camaUci'] = df['staffed_adult_icu_bed_occupancy']
    df_new['adultos_camaUci_covid'] = df['staffed_icu_adult_patients_confirmed_covid']
    df_new['adultos_cama_covid'] = df['total_adult_patients_hospitalized_confirmed_covid']
    df_new['menores_camaUci'] = df['staffed_pediatric_icu_bed_occupancy']
    df_new['menores_camaUci_covid'] = df['staffed_icu_pediatric_patients_confirmed_covid']
    df_new['menores_cama_covid'] = df['total_pediatric_patients_hospitalized_confirmed_covid']
    df_new = data_organize(df_new)  
    df_new = df_new.convert_dtypes()
    return df_new

def data_agerange_adult(df):
    df_new = pd.DataFrame()
    df_new['state'] = df['state'] 
    df_new['date'] = df['date']
    df_new['18-19'] = df['previous_day_admission_adult_covid_confirmed_18-19']
    df_new['20-29'] = df['previous_day_admission_adult_covid_confirmed_20-29']
    df_new['30-39'] = df['previous_day_admission_adult_covid_confirmed_30-39']
    df_new['40-49'] = df['previous_day_admission_adult_covid_confirmed_40-49']
    df_new['50-59'] = df['previous_day_admission_adult_covid_confirmed_50-59']
    df_new['60-69'] = df['previous_day_admission_adult_covid_confirmed_60-69']
    df_new['70-79'] = df['previous_day_admission_adult_covid_confirmed_70-79']
    df_new['80+'] = df['previous_day_admission_adult_covid_confirmed_80+']
    df_new['desconocido'] = df['previous_day_admission_adult_covid_confirmed_unknown']
    df_new = data_organize(df_new) 
    df_new = df_new.convert_dtypes()
    return df_new

def data_agerange_pediatric(df):
    df_new = pd.DataFrame()
    df_new['state'] = df['state'] 
    df_new['date'] = df['date']
    df_new['0-4'] = df['previous_day_admission_pediatric_covid_confirmed_0_4']
    df_new['5-11'] = df['previous_day_admission_pediatric_covid_confirmed_5_11']
    df_new['12-17'] = df['previous_day_admission_pediatric_covid_confirmed_12_17']
    df_new['desconocido'] = df['previous_day_admission_pediatric_covid_confirmed_unknown']
    df_new = data_organize(df_new) 
    df_new = df_new.convert_dtypes()
    return df_new
