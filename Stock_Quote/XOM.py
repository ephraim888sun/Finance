import pandas as pd
from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('seaborn-dark-palette')

df_XOM = pd.read_csv('XOM.csv')
print(df_XOM.head())

df_XOM['Date'] = pd.to_datetime(df_XOM['Date'], format='%Y-%m-%d')
#print(df.loc[0, 'Date'].day_name())

df_XOM['DayOfWeek'] = df_XOM['Date'].dt.day_name()
#print(df.head())

# print(df['Date'].min())
# print(df['Date'].max())

df_XOM.set_index('Date', inplace = True)
# print(df.head())
# print(df.loc['2019'])

df_XOM.dropna

Highs_XOM = df_XOM.resample('D').agg({'High': 'max'})
Highs_XOM = df_XOM['High'].resample('D').max()
# print(Highs['2021-05-11'])

Highs_XOM.plot()

plt.xlabel('Year')
plt.ylabel('Stock Price (USD)')
plt.title('Exxon Mobil Corporation (XOM)')

plt.savefig('XOM.png')
plt.show()

