import pandas as pd
import numpy as np
def create_dataframes(path):
    
    columns_locations = ['UniqueID','StateAbbr','StateDesc','CityName','GeographicLevel', 'TractFIPS','CityFIPS','GeoLocation']
    columns_data_definition = ['Category', 'CategoryID', 'Measure','MeasureId','Data_Value_Type','Short_Question_Text']
    columns_data = ['Data_Value','DataValueTypeID','Data_Value_Footnote_Symbol', 'Data_Value_Footnote','CategoryID',
                'GeoLocation','Low_Confidence_Limit', 'High_Confidence_Limit','PopulationCount','StateAbbr',
               'UniqueID','MeasureId','Year']
  
    df = pd.read_csv(path)
  
    df_data = df[columns_data].copy()
    df_data_piv = df_data.pivot_table(values='Data_Value',
                              index=['UniqueID','DataValueTypeID','PopulationCount'],
                              columns='MeasureId',aggfunc=np.sum)
    df_data_piv.reset_index(inplace=True)
    # Save data where population count is > 50 (CDC website withholds data for population counts < 50)
    df_data_piv = df_data_piv[df_data_piv['PopulationCount']>50]
    df_data_piv.to_csv('dataframes\data.csv')
    
    df_data_definition = df[columns_data_definition].copy()
    df_data_definition = df_data_definition.drop_duplicates()
    df_data_definition.to_csv('dataframes\data_definition.csv')
    
    df_locations = df[columns_locations].copy()

    # df_locations = df_locations.drop_duplicates().sort_values('UniqueID')
    # df_locations.to_csv('locations.csv')


    lat = []
    long =[]
    for row in df_locations['GeoLocation']:
        # Try to,
        try:
            # Split the row by comma and append
            # everything before the comma to lat
            latitude = row.split(',')[0]
            latitude = latitude[1:]
            lat.append(latitude)
            # Split the row by comma and append
            # everything after the comma to lon
            longitude = row.split(',')[1]
            longitude = longitude[:-1]
            long.append(longitude)

        # But if you get an error
        except:
            # append a missing value to lat
            lat.append(np.NaN)
            # append a missing value to lon
            long.append(np.NaN)

    # Create two new columns from lat and lon
    df_locations['Latitude'] = lat
    df_locations['Longitude'] = long

    # df_locations.tail(5)
    del df_locations['GeoLocation']
    df_locations = df_locations.drop_duplicates().sort_values('UniqueID')
    df_locations.to_csv('dataframes\locations.csv')

    
    return df_data_piv,df_data_definition,df_locations
    
    
def clean_data():
    data = pd.read_csv('dataframes/data.csv',index_col=0)
    locations = pd.read_csv('dataframes/locations.csv',index_col=0)
    definitions = pd.read_csv('dataframes/data_definition.csv',index_col=0)
    
    #Fill CITY OF UNITED STATES FOR AGG FUNCTIONS inplace of NAN, 
    locations.CityName = locations.CityName.fillna('United States') 

    #combining data and locations dataframes
    combined_df = data.set_index('UniqueID').join(locations.set_index('UniqueID'))
    #print(combined_df['GeographicLevel'].value_counts())
    
    #MISSING DATA?    
    data.describe().sort_values('count',axis=1)
    missingData = data[data.isnull().values].join(locations[['UniqueID','CityName','GeographicLevel']].
                                              set_index('UniqueID'),on='UniqueID',how='left')

    #value counts of missing data by geographic level
    print("Count of Missing data by geographic level: \n")
    print(missingData['GeographicLevel'].value_counts(),end='\n\n')

    #value counts of all data by geographic level
    print("Count of All data by geographic level: \n")
    print(data.join(locations[['UniqueID','CityName','GeographicLevel']].
                    set_index('UniqueID'),on='UniqueID',how='left')['GeographicLevel'].value_counts())

    missingDataPopMean = missingData.groupby('CityName')['PopulationCount'].mean()
    missingDataCensusCount = missingData.groupby('CityName')['UniqueID'].count()
    missingDataJoined = pd.concat([missingDataPopMean,missingDataCensusCount],axis=1,keys=['AvgPop','MissingCensusCount'])
    fullDataCensusCount = data.join(locations[['UniqueID','CityName','GeographicLevel']].set_index('UniqueID'),on='UniqueID',how='left').groupby('CityName')['UniqueID'].count()
    missingDataCities = missingDataJoined.join(fullDataCensusCount,how='left')
    missingDataCities.columns = ['Avg Population','Census Tracts Missing','Count']
    missingDataCities['perMissing'] = missingDataCities.iloc[:,1]/missingDataCities.iloc[:,2]
    missingDataCities.sort_values('perMissing',ascending=False,inplace=True)
    print('\n \n TOP AND BOTTOM 5 Cities Missing Percentage Of Censuses')
    print(missingDataCities.head(10))
    
    cleanedData = data.join(locations[['UniqueID','CityName','StateAbbr','GeographicLevel']].
                        set_index('UniqueID'),on='UniqueID',how='left').copy()
    colsToClean = cleanedData.drop(['UniqueID','CityName','StateAbbr','DataValueTypeID','PopulationCount','GeographicLevel'],axis=1).columns
    for col in colsToClean:
        cleanedData[col] = cleanedData.groupby('CityName')[col].transform(lambda x: x.fillna(np.mean(x)))
        

    cleanedData.drop(['GeographicLevel','StateAbbr','CityName'],axis=1).to_csv('dataframes\cleaned_data.csv')
    locations.to_csv('dataframes\cleaned_locations.csv')
    definitions.to_csv('dataframes\cleaned_data_definition.csv')
    
    return cleanedData
    
    