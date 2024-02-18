import pandas as pd

clean = pd.read_csv("2.csv")

#cleaning $
clean = clean.replace(to_replace=r'\$', value='', regex=True)

#cleaning months
clean = clean.replace(['Jan'],'1')
clean = clean.replace(['Feb'],'2')
clean = clean.replace(['Mar'],'3')
clean = clean.replace(['Apr'],'4')
clean = clean.replace(['May'],'5')
clean = clean.replace(['Jun'],'6')
clean = clean.replace(['Jul'],'7')
clean = clean.replace(['Aug'],'8')
clean = clean.replace(['Sep'],'9')
clean = clean.replace(['Oct'],'10')
clean = clean.replace(['Nov'],'11')
clean = clean.replace(['Dez'],'12')

#cleaning age-groups
ages_groups = ['19-29','29-39','39-49','59-69','69-79','79-89']
ages_numbers = ['1','2','3','4','5','6']

clean = clean.replace(ages_groups, ages_numbers)

#creating a new and cleaned dataset
clean.to_csv("clean2.csv")
