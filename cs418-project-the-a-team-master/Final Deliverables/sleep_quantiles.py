## Define whether or not a certain sleep % falls within best 20%, worst 20%, or in the middle
def quant(x,y):
    if x < y[.2]:
        return 0
    elif x > y[.8]:
        return 2
    return 1

data['sleepQuantile'] = data.SLEEP.apply(lambda x: quant(x,data.SLEEP.quantile([.2,.8])))
data['lpaQuantile'] = data.LPA.apply(lambda x: quant(x,data.LPA.quantile([.2,.8])))
data['csmokingQuantile'] = data.CSMOKING.apply(lambda x: quant(x,data.CSMOKING.quantile([.2,.8])))

#Plt the scatter plot of Low physical activity and Obesity separated by sleep quantiles
sns.lmplot('LPA','OBESITY',data=data,col='sleepQuantile')
_ = plt.xlabel('LPA')
_ = plt.ylabel('OBESITY')
plt.show()