import pandas as pd
from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')

df = pd.read_csv('RDS_B.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
#print(df.loc[0, 'Date'].day_name())

df['DayOfWeek'] = df['Date'].dt.day_name()
#print(df.head())

# print(df['Date'].min())
# print(df['Date'].max())

df.set_index('Date', inplace = True)
# print(df.head())
# print(df.loc['2019'])

df.dropna

#Highs_RDS_B = df.resample('D').agg({'High': 'max'})
Highs_RDS_B = df['High'].resample('D').max()
# print(Highs['2021-05-11'])

Highs_RDS_B.plot()

plt.xlabel('Year')
plt.ylabel('Stock Price (USD)')
plt.title('Royal Dutch Shell (RDS-B)')

plt.savefig('RDS.png')
plt.show()

