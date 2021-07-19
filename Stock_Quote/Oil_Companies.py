import pandas as pd
from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')

def cleandf(csv):
    csvsplit = csv.split('.')
    csvsplit = csvsplit[0]
    varname = pd.read_csv(csv)
    varname = varname[['Date', 'High']]
    varname.rename(columns={'High': 'High_' + csvsplit}, inplace=True)
    return varname

df_XOM = cleandf('XOM.csv')
df_COP = cleandf('COP.csv')
df_CVX = cleandf('CVX.csv')
df_RDS_B = cleandf('RDS_B.csv')

# df = df_XOM.append([df_COP, df_CVX, df_RDS_B], ignore_index=True, sort=True)
# print(df.head(10))

# df = pd.concat([df_XOM, df_COP, df_CVX, df_RDS_B], axis=1, join="inner")
# print(df.head(10))

df1 = pd.merge(left=df_XOM, right=df_COP, left_on='Date', right_on='Date')
df2 = pd.merge(left=df_CVX, right=df_RDS_B, left_on='Date', right_on='Date')
df = pd.merge(left=df1, right=df2, left_on='Date', right_on='Date')
# print(df.head(10))
# df2 = pd.merge(left = )

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df.set_index('Date', inplace = True)

Highs_XOM = df['High_XOM'].resample('D').max()
Highs_COP = df['High_COP'].resample('D').max()
Highs_CVX = df['High_CVX'].resample('D').max()
Highs_RDS_B = df['High_RDS_B'].resample('D').max()

# plt.plot(Highs_XOM, color = 'b', linestyle = (0, (5, 1)), label='Exxon Mobil (XOM)')
# plt.plot(Highs_COP, color = 'r', linestyle = 'dashed', label='ConocoPhillips (COP)')
# plt.plot(Highs_CVX, color = 'g', linestyle = 'solid', label='Chevron (CVX)')
# plt.plot(Highs_RDS_B, color = 'k', linestyle = 'dashdot', label='Royal Dutch Shell (RDS-B)')

plt.plot(Highs_XOM, linewidth=1.0, label='Exxon Mobil (XOM)')
plt.plot(Highs_COP, linewidth=1.0, label='ConocoPhillips (COP)')
plt.plot(Highs_CVX, linewidth=1.0, label='Chevron (CVX)')
plt.plot(Highs_RDS_B, linewidth=1.0, label='Royal Dutch Shell (RDS-B)')

plt.xlabel('Year')
plt.ylabel('Stock Price (USD)')
plt.title('OIL & GAS COMPANIES')

plt.legend()

plt.tight_layout()

# plt.savefig('Oil_Companies.png')

plt.show()

