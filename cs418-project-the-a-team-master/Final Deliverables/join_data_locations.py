data = pd.read_csv('dataframes/cleaned_data.csv',index_col=0).set_index('UniqueID')
locations = pd.read_csv('dataframes/cleaned_locations.csv').set_index('UniqueID')
#Join Location and and data dataframes
data_join = data.join(locations[['GeographicLevel','StateAbbr','CityName']]).copy()
# Keeping only census level data
census_data = data_join[data_join['GeographicLevel'] == 'Census Tract']
# Drop unnecessary and NOT needed columns
census_data_req = census_data.drop(['DataValueTypeID','GeographicLevel','StateAbbr','CityName'],axis=1).reset_index().set_index('UniqueID')