tst = cleanedData[cleanedData['GeographicLevel']=='Census Tract'].set_index('UniqueID').drop(['CityName','StateAbbr','GeographicLevel','DataValueTypeID','PopulationCount'],axis=1)
tst1 = tst.multiply(cleanedData[cleanedData['GeographicLevel']=='Census Tract'].set_index('UniqueID')['PopulationCount'],axis=0)
tst2 = tst1.join(cleanedData[cleanedData['GeographicLevel']=='Census Tract'].set_index('UniqueID')[['StateAbbr','CityName']]).groupby(['StateAbbr','CityName']).agg(np.sum)
tst3 = tst2.divide(cleanedData[cleanedData['GeographicLevel']=='Census Tract'].groupby(['StateAbbr','CityName'])['PopulationCount'].sum(),axis=0)

fig, ax = plt.subplots(1,1,figsize=(20,12))
_  = sns.boxplot(data=tst3,orient='horizontal')
plt.show()