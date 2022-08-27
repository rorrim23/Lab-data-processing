#%%
# %matplotlib auto enables graph scaling
from scipy.fftpack import fft,fftfreq,ifft
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

with open("200421_sample/Entire data.csv") as csv_file:
    df = pd.read_csv(csv_file)
    df.columns = ['time', 'voltage_imp', 'time2', 'voltage_fluorescence']

# Fourier transform & frequency spectrum
# fft(x) returns y(0), y(1), ... , y(n-1)
# y(j) = (x * exp(-2*pi*i*j*np.arange(n)/n)).sum()
# originally F(v) = integral(f(t) * exp(-2*pi*i*v*t))
fft_imp = fft(df['voltage_imp'].tolist())
fftfreq_imp = fftfreq(len(df), 0.0001) # fftfreq(n,delta_t) makes frequency axis
# fftfreq = np.arange(len[df('time')]) / (len(time*(df[time[1]]-df[time[0]]))
i = fftfreq_imp >0
fig = plt.figure(figsize=(30,60))
ax1 = fig.add_subplot(6,1,1)
ax1.plot(fftfreq_imp, fft_imp**2)
print(len(fft_imp))

# removing unwanted noise
asdf = []
fft_imp_rev = fft_imp.copy()
for i in range(len(df)):
    if (np.absolute(fft_imp[i]**2) > 1*10**5) & (np.absolute(fftfreq_imp[i])>2000):
        fft_imp_rev[i] = 0
        asdf.append(i)

# Frequency spectrum after noise removal
ax2 = fig.add_subplot(6,1,2)
i = fftfreq_imp >0
ax2.plot(fftfreq_imp, fft_imp_rev**2)

# original data
ax3 = fig.add_subplot(6,1,3)
ax3.plot(df['time'],df['voltage_imp'])

# Noise removed data through inverse fourier transform
fft_imp_rev_ifft = ifft(fft_imp_rev)
ax4 = fig.add_subplot(6,1,4)
ax4.plot(df['time'],fft_imp_rev_ifft)


'''
1. Remove high frequency peaks(those at low frequency data are
    the ones you need) in frequency spectrum data 
    (This includes peaks at (-) frequencies)
2. Freuquency spectrum has both +,- value. So better use
    np.absolute() function.
'''