##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    mauna_df=pd.read_csv('/home/whiteri/hw/hw07/mauna_loa/mauna_loa.csv')
    mauna_df
   

def plot_df(df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    
    (mauna_df['decimal_date'][0])
    mauna_df.plt(x="decimal_date",y='CO2')
