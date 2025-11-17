#! /usr/bin/env python

# Dates and times
import datetime as dt

# Yahoo finance data - yFinance (https://github.com/ranaroussi/yfinance)
import yfinance as yf

# Import pandas
import pandas as pd

# Matplotlib for creating plots
import matplotlib.pyplot as plt

# Listing file in a folder
import os

# Pull previous 5 days of data
get_data = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG'], period= '5d', interval= '1h')

# Generate time stamp of when data was pulled
time_stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')

# Save into 'data' folder, titling file with time stamp
get_data.to_csv('data/' + time_stamp + '.csv')

# Specify data folder as location to find the file.
datadir = './data/'

# Data files
data_files = os.listdir('./data/')

# Sort the list of files.
data_files.sort(reverse=True)

# Specify first file in data_files group
latest = data_files[0]

# Read in the CSV file
df= pd.read_csv(datadir + latest, index_col=0, header=[0,1])

# Create plot of data
plot_data = df['Close'].plot(title = 'Closing over Previous 5 Days', xlabel='Date', ylabel='Value (USD)')

# Rotate x-axis lables 45°
plt.xticks(rotation=45)

# Move legend off chart area
# Source: https://stackoverflow.com/questions/25068384/bbox-to-anchor-and-loc-in-matplotlib
plot_data.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Current date & time for plot save file
now = dt.datetime.now()

# File name.
filename = "./plots/" + now.strftime("%Y%m%d-%H%M%S") + ".png"

# Save figure.
plt.savefig(filename, dpi=500)
