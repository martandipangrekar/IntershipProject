import pandas as pd
import numpy as np

# Load the price data
df = pd.read_excel("Datafile")
print(df)

# Calculate the moving average and standard deviation
ma = df["key"].rolling(window=7).mean()
std = df["key"].rolling(window=7).std()

# # Calculate the upper and lower bands
upper_band = ma + 3 * std
lower_band = ma - 3 * std

# # Calculate the super trend indicator
trend = np.where(df["price"] > ma, 1, -1)
trend = np.where((df["price"] > upper_band) | (df["price"] < lower_band), -trend, trend)

# # Plot the super trend indicator and the price data
import matplotlib.pyplot as plt

plt.plot(df["price"], label="Price")
plt.plot(trend, label="Super Trend")
plt.legend()
plt.show()

