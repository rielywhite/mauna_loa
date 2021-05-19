##This file contains functions that plots mauna_loa carbon dioxide data

import pandas as pd
import matplotlib.pyplot as plt
def get_df(filename):
    '''
    INPUT:filename e.g. mauna_loa.csv
    OUTPUT: Pandas Dataframe
    '''
    mauna_df=pd.read_csv(filename)
    mauna_df['years_since']=mauna_df['year']-mauna_df['year'][0]
    mauna_df=mauna_df[['years_since','C02']]
    return mauna_df
   

def plot_df(mauna_df):
    '''
    INPUT: Pandas DataFrame
    OUTPUT: handle to plot axis
    '''
    plt.plot(mauna_df['years_since','C02'])
    plt.title('C02 recorded levels vs start of C02 observations')
