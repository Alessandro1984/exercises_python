import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'data/TSLA.csv'

df = pd.read_csv(file, decimal = ',')

df = df[['Date', 'Close']]

print(df.head())

print(df.dtypes)

df['Close'] = pd.to_numeric(df['Close'])
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df_2022 = df.loc[(df['Date'] >= '2022-01-03') & (df['Date'] < '2022-12-30')]

print(df_2022.shape)

y = df_2022["Close"]
x = df_2022["Date"]

plt.plot(x, y, label='Closing Price')
plt.xticks(rotation=45)
plt.title('Tesla, Inc. (TSLA)')
plt.legend()
plt.show()
