data = pd.read_csv('dataframes/cleaned_data.csv',index_col=0).set_index('UniqueID')
locations = pd.read_csv('dataframes/cleaned_locations.csv')
# join locations data
main = data.join(locations.set_index('UniqueID')[['GeographicLevel','StateAbbr','CityName']]).copy()

# Only keep census level data
main = main[main['GeographicLevel'] == 'Census Tract']
main = main.drop(['GeographicLevel','StateAbbr','CityName', 'DataValueTypeID'],axis=1).reset_index().set_index('UniqueID')
# Contextualy irrelevant features
#dropping data irrelevant
drop_data = np.array(['MAMMOUSE','PAPTEST','BPMED','TEETHLOST','DENTAL']) 


# Drop effects/irrelevant features
mainData = main.drop(np.concatenate([drop_data]),axis=1)
fig,ax = plt.subplots(figsize=(15,5))
sns.heatmap(mainData.drop('CANCER',axis=1).corr(),annot=True, cmap='RdYlGn')
plt.title('Correlation of Features')
plt.show()