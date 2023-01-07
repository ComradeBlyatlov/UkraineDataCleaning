from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv ('refugees1.csv', index_col=False)

df['date'] = pd.to_datetime(df['date'])

#Sorting data to weekly format
countries = []
weekno = 0

for x in range(len(df['date'])):


    date = df['date'][x]
    week = datetime.date(date).isocalendar()[1]

    if (df['country'][x] in countries and week == weekno):
        df = df.drop(x)
        continue

    if week != weekno:
        countries = []
        weekno = week
        
    if (df['country'][x] not in countries):
        countries.append(df['country'][x])
        weekno = week
        print ('weekno:', weekno)


print(countries)
print(df)

df['date'] = pd.to_datetime(df['date']) - pd.to_timedelta(7, unit='d')

df.reset_index(drop=True, inplace=True)

#Adding population to countries
array = []
for x,y in enumerate(df['country']):
    if df['country'][x] == 'Belarus':
        print(df['country'][x])
        array.append(9340000)
    if df['country'][x] == 'Hungary':
        array.append(9710000)
        print(df['country'][x])
    if df['country'][x] == 'Poland':
        array.append(37780000)
        print(df['country'][x])
    if df['country'][x] == 'Romania':
        array.append(19120000)
        print(df['country'][x])
    if df['country'][x] == 'Russian Federation':
        array.append(143400000)
        print(df['country'][x])
    if df['country'][x] == 'Slovakia':
        array.append(5477000)
        print(df['country'][x])
    if df['country'][x] == 'Republic of Moldova':
        array.append(2574000)
        print(df['country'][x])
    if df['country'][x] == 'Ukraine':
        array.append(43810000)
        print(df['country'][x])
    if df['country'][x] == 'Other European countries':
        array.append(0)
        print(df['country'][x])

df['pop'] = array


df.to_csv('refugeesprocessed.csv', encoding='utf-8', index=False)
