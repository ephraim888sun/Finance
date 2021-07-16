# Description: This program visualizes your stock portfolio

# Import Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Load data

# Store data
df = pd.read_csv('')

# Show the data
print(df)

# Get total invested amount of money in portfolio
total_amount = sum(df['Amount'] * df['Average Price'])
total_amount = round(total_amount, 2)

# Visually show portfolio & additional information
stock_tickers = df['Column Name for Ticker'].values
sizes = df['Amount'] * df['Average Price']

listOfZeros = [0] * df.shape[0]
n = random.randiant(0, df.shape[0]-1)
listOfZeros[n] = 0.1
explode = listOfZeros

# Create a figure
fig1, ax1 = plt.subplots(figsize=(10, 10))

# Plot pie chart
ax1.pie(sizes, explode=explode, labels=stock_tickers, autopct='%.2f%%', shadow='True', startangle=360)

# Set the title
ax1.set_title('Portfolio Pie Chart', color='Purple', fontsize=22)

# Add text to the visual
x = -1.75
y = 1
ax1.text(x, y, 'Overview:', fontsize=24, color='Purple')

# Input Company Ticker & Price & Total
y_counter = 0.12
ax1.text(x, y - y_counter, 'Total:'+str(total_amount), fontsize=15, color='Blue')
for i in range(0, df.shape[0]):
    ax1.text(x, 0.88 - y_counter, df['Ticker'][i] + ': $' + str(round(df['Amount'][i] * df['Average_Price'][i], 2)),
             fontsize=14, color='Black')
    y_counter = y_counter + 0.12
