from statsmodels.stats import weightstats as stests
import numpy as np

income = np.genfromtxt("income.csv", delimiter=',')

#ztest, income mean is equals to 188888
ztest,pval = stests.ztest(income[:,1], value=188888)
print("p-values",pval)

if pval<0.05:
    print("Z-test => we are rejecting hypothesis")
else:
    print("Z-test => we are accepting hypothesis")
