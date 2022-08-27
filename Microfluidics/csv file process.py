#%%
#import csv, then plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from scipy.fftpack import fft, fftfreq, ifft
%matplotlib inline

with open('200421_sample/Single peak.csv') as csvfile:
    df = pd.read_csv(csvfile)
    df.columns = {'time', 'voltage'}

fig1 = plt.figure(figsize=(50,10))
ax1 = fig1.add_subplot(1,1,1)
ax1.plot(df['time'],df['voltage'])

'''
fft_voltage = fft(df['voltage'].tolist())
fftfreq = fftfreq(len(df),0.0001)
fft_voltage_rev = fft_voltage.copy()
for i in range(len(df)):
    if (np.absolute(fft_voltage[i])>1) & (np.absolute(fftfreq[i])>1000):
        fft_voltage_rev[i] = 0
fft_voltage_rev_ifft = ifft(fft_voltage_rev)
ax1.plot(df['time'],fft_voltage_rev_ifft)
'''