import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/TSLA.csv", sep = ",")

dataframe = data[["Date","Adj Close"]]

plt.plot(dataframe["Date"], dataframe["Adj Close"])
plt.xlabel("Date")
plt.ylabel("Close")
plt.title("TSLA")

plt.show()
