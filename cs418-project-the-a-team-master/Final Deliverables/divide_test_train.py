# 1. For Obesity
y = census_data_Obesity['OBESITY']
X = census_data_Obesity.drop('OBESITY',axis=1)
# Separate data into train and test
Xtrain_obesity, Xtest_obesity, ytrain_obesity, ytest_obesity = train_test_split(X,y,test_size=.25)

#2. For Cancer
y = census_data_Cancer['CANCER']
X = census_data_Cancer.drop('CANCER',axis=1)
# Separate data into train and test
Xtrain_cancer, Xtest_cancer, ytrain_cancer, ytest_cancer = train_test_split(X,y,test_size=.25)