from scipy.stats import ttest_ind
import pandas

data = pandas.read_csv('data.csv')

data1 = data.value[data.names == 'sample1']
data2 = data.value[data.names == 'sample2']

stat, p = ttest_ind(data1, data2)

print('P-value = ', p)

confidence = round((1-p)*100)

if p>0.05:
    print('Similar, confidence of ', confidence, '%')
else:
    print('Different, confidence of ', confidence, '%')
