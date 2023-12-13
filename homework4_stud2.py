import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/TSLA.csv", sep = ",")
df2 = df[(df["Date"] >= "2022-01-03") & (df["Date"] <= "2022-12-30")]

plt.title("TSLA, Inc. (TSLA)")
plt.ylabel("Price in USD")
plt.plot(df2.Date, df2.Close, label="Closing Price")
plt.legend(loc="upper right")
plt.xticks(df2.Date[::55])
plt.show()
