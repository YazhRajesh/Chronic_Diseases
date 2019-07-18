abnormal_resids_cancer = m0_cancer.resid[m0_cancer.resid <= -.10]

arr_cancer = np.empty(len(Xtrain_cancer.index.values),dtype=np.bool)
for i,j in enumerate(Xtrain_cancer.index.values):
    arr_cancer[i] = True if j in abnormal_resids_cancer.index.values else False

m1_cancer = sm.OLS(ytrain_cancer[~arr_cancer],Xtrain_cancer[~arr_cancer]).fit()