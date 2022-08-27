
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
%matplotlib inline

with open('190611_fd+Os+GOx_1_CC(1).txt') as textfile:
    columns = ['time', 'current']
    df = pd.read_csv(textfile, dtype=np.float64,names=columns)
    #df = pd.read_csv(textfile,skiprows=[x for x in (list(range(28)) + [30,2032])],names=columns,dtype=np.float64)
    #df.head()
    # print(df[len(df)//2-4:len(df)//2+4])
#%%
time_interval = df['time'][1]-df['time'][0]

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax1.plot(df['time'], df['current'])

# current = a * t**-0.5
a = 0
df = df[:len(df)//2]
for _ in range(30):
    df['loss'] = (a*df['time']**-0.5-df['current'])**2
    df['der_loss'] = 2 * (a*df['time']**-0.5-df['current']) * df['time']**-0.5
    a -= 0.00005 * df['der_loss'].sum()
    print(df['loss'].sum())
ax2 = fig.add_subplot(2,1,2)
ax2.plot(df['time'][:len(df)-5], df['current'][:len(df)-5], linewidth=1)
ax2.plot(df['time'], a*df['time']**-0.5)

'''
df = df[len(df)//2:]
print(df)
for _ in range(30):
    df['loss'] = (a*(df['time']-2)**-0.5-df['current'])**2
    df['der_loss'] = 2 * (a*(df['time']-2)**-0.5 - df['current']) * (df['time']-2)**-0.5
    a -= 0.00005 * df['der_loss'].sum()
    print(df['loss'].sum(), a)
ax2 = fig.add_subplot(2,1,2)
ax2.plot((df['time']), df['current'], linewidth=1)
ax2.plot(df['time'], a*(df['time']-2)**-0.5)
'''


'''
charge_fft = fft(df['charge'].tolist()) # make Series into list
charge_psd = charge_fft
fftfreq = fftfreq(len(charge_psd), time_interval) # fftfreq(n,delta_t) makes frequency axis
# fftfreq = np.arange(len(time)) / (len(time*(time[1]-time[0]))
i = fftfreq > 0
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax1.plot(fftfreq[i][:10], charge_psd[i][:10])
# ax3.plot(fftfreq[i], 10 * charge_fft[i])
'''

#%%
from os import walk

mypath = "after shaking"
(_, _, filenames) = next(os.walk(mypath))
a = [f[:-4] for f in filenames if f[-3:]=='txt']
for f in a:
    print(f)