randforest= RandomForestRegressor()
randforest.fit(Xtrain_cancer[~arr_cancer],ytrain_cancer[~arr_cancer])
ypred = randforest.predict(Xtrain_cancer[~arr_cancer])
print('Random Forest R^2 Score on TRAIN DATA: {:.4f}'.format(r2_score(ytrain_cancer[~arr_cancer],ypred)))