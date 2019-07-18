randforest= RandomForestRegressor()
randforest.fit(Xtrain_obesity[~arr_obesity],ytrain_obesity[~arr_obesity])
ypred = randforest.predict(Xtrain_obesity[~arr_obesity])
print('Random Forest R^2 Score on TRAIN DATA: {:.4f}'.format(r2_score(ytrain_obesity[~arr_obesity],ypred)))