abnormal_resids_obesity = m0_obesity.resid[m0_obesity.resid <= -.10]

arr_obesity = np.empty(len(Xtrain_obesity.index.values),dtype=np.bool)
for i,j in enumerate(Xtrain_obesity.index.values):
    arr_obesity[i] = True if j in abnormal_resids_obesity.index.values else False

m1_obesity = sm.OLS(ytrain_obesity[~arr_obesity],Xtrain_obesity[~arr_obesity]).fit()