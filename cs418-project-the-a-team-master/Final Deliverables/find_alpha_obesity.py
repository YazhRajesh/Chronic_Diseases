alphas = np.linspace(0,1,20)
params = {'alpha':alphas}

ridge = Ridge()
grid = GridSearchCV(ridge,params,cv=5)
grid.fit(Xtrain_obesity[~arr_obesity],ytrain_obesity[~arr_obesity])
best_alpha = grid.best_params_['alpha']
best_score = grid.best_score_
print('Best Alpha: {:.4f}'.format(best_alpha))
print('Best Score: {:.4f}'.format(best_score))