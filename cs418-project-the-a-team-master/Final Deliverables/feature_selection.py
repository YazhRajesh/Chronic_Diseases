# Contextualy irrelevant features for Obesity
noncontext = np.array(['MAMMOUSE','PAPTEST','BPMED','TEETHLOST','DENTAL']) 
# Already known effects of Obesity
known_effects_of_obesity = np.array(['CHD','BPHIGH','ARTHRITIS','DIABETES','HIGHCHOL','PHLTH','KIDNEY','STROKE'])
# Drop above two from our dataframe
census_data_Obesity = census_data_req.drop(np.concatenate([noncontext,known_effects_of_obesity]),axis=1)
census_data_Obesity.drop(['MHLTH','COREM','COPD','COLON_SCREEN'],axis=1,inplace=True)

# Contextualy irrelevant features for Cancer
noncontext_cancer = np.array(['MAMMOUSE','TEETHLOST','DENTAL']) 
# Drop above two from our dataframe
census_data_Cancer = census_data_req.drop(np.concatenate([noncontext_cancer]),axis=1)