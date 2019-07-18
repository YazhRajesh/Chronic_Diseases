lr.fit(Xtrain_obesity[~arr_obesity],ytrain_obesity[~arr_obesity])
#print results
print('Model Accuracy For Obesity')
print('Linear Regression R2: {:.4f}'.format(lr.score(Xtrain_obesity[~arr_obesity],ytrain_obesity[~arr_obesity])))
print('Cross Fold Validation')
print('Linear Regression Cross Val Score: {}'.format(cross_val_score(lr,Xtrain_obesity[~arr_obesity],ytrain_obesity[~arr_obesity],cv=5,scoring=scorer)))