#For Cancer
#Fit Linear Regression to the training data with outliers withheld
lr.fit(Xtrain_cancer[~arr_cancer],ytrain_cancer[~arr_cancer])

#print results
print('Model Accuracy For Cancer')
print('Linear Regression R2: {:.4f}'.format(lr.score(Xtrain_cancer[~arr_cancer],ytrain_cancer[~arr_cancer])))
print('Cross Fold Validation')
print('Linear Regression Cross Val Score: {}'.format(cross_val_score(lr,Xtrain_cancer[~arr_cancer],ytrain_cancer[~arr_cancer],cv=5,scoring=scorer)))