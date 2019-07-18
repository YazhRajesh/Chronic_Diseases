## Define r2 scoring for cross_val_score scoring
def scorer(model,X,y):
    model.fit(X,y)
    ypred = model.predict(X)
    return r2_score(y,ypred)

#INIT Linear Regression
lr = LinearRegression()