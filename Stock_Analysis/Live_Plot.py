import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import numpy as np

time_stamp = datetime.datetime.now()
time_stamp = time_stamp.strftime('%Y-%m-%d %H:%M:%S')

# def animate(i):
#     df = pd.read_csv(str(time_stamp[0:11]) + 'stock data.csv')
#     x = df.iloc[:1]
#     y = df.iloc[:2]
#     plt.cla()
#
#     plt.plot(x, y, label='Price')
#
#     plt.tight_layout()
#
# ani = animation.FuncAnimation(plt.gcf(), animate, interval=1)
#
# plt.tight_layout()
# plt.show()

df = pd.read_csv(str(time_stamp[0:11]) + 'stock data.csv')
print(df.head)
print(df.iloc[:,2])
print(df.iloc[:,1])