import pandas as pd
import numpy as np

def get_unhealthy_behaviors_and_outcomes():
    data = pd.read_csv('dataframes/cleaned_data.csv')
    dataDef = pd.read_csv('dataframes/cleaned_data_definition.csv')
    locations = pd.read_csv('dataframes/cleaned_locations.csv')
    
    data2 = data.set_index('UniqueID').join(locations.set_index('UniqueID')['GeographicLevel']).copy()
    data2 = data2[data2['GeographicLevel'] == 'Census Tract']
    data2 = data2.drop(['Unnamed: 0','DataValueTypeID','GeographicLevel'],axis=1).reset_index()
    dataMelt = data2.melt(id_vars=['UniqueID','PopulationCount'],var_name='measureid')
    dataDef2 = dataDef[['MeasureId','Category']].drop_duplicates()
    joined = dataMelt.set_index('measureid').join(dataDef2.set_index('MeasureId'),rsuffix='_def',how='left').reset_index().set_index(['UniqueID','PopulationCount'])
    
    preventative = joined[joined['Category'] == 'Prevention'].copy()
    outcomes = joined[joined['Category'] == 'Health Outcomes'].copy()
    unhealthy = joined[(joined['Category'] == 'Unhealthy Behaviors') | (joined['Category'] == 'Prevention')].copy()
    
    unhealthypiv = unhealthy.reset_index().pivot_table('value','UniqueID','index',aggfunc=np.sum)
    outcomespiv = outcomes.reset_index().pivot_table('value','UniqueID','index',aggfunc=np.sum)
    
    return unhealthypiv,outcomespiv,data2
