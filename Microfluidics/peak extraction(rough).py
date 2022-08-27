#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

with open("200421_sample/Entire data.csv") as f:
    df = pd.read_csv(f, dtype=np.float64)
    df.columns = ['time', 'vol_impedance', 'time2', 'vol_fluorescence']
    print(df.head())

fig = plt.figure(figsize=(30,10))
# ax1 = fig.add_subplot(2,3,1)
# ax1.plot(df['time'][:3000],df['vol_impedance'][:3000])
ax2 = fig.add_subplot(1,1,1)
ax2.plot(df['time'],df['vol_impedance'])
ax2.plot(df['time'],df['vol_fluorescence'])

## peak extraction(fluorescence)
i=0
peak_index_f = []
peak_value_f = []
while i < len(df) - 1:
    if df['vol_fluorescence'][i]>0.5:
        peak_index_f.append(i)
        i += int(0.1 * 10000)
    else:
        i += 5

for i, index in enumerate(peak_index_f):
    peak_value_f.append(max(df['vol_fluorescence'][index:index+int(0.1*10000)]))
    peak_index_f[i] = df['vol_fluorescence'][index:index+int(0.1*10000)].argmax() + index

## peak extraction(impedance)
i=0
peak_index_i = []
peak_value_i = []
while i < len(df) - 1:
    if df['vol_impedance'][i]<-0.5:
        peak_index_i.append(i)
        i += int(0.1 * 10000)
    else:
        i += 5

for i in range(len(peak_index_i)):
    peak_value_i.append(min(df['vol_impedance'][index:index+int(0.1*10000)]))
    peak_index_i[i] = df['vol_impedance'][index:index+int(0.1*10000)].argmin() + index

'''
# obtaining peak info based on fluorescence info
for i, index in enumerate(flu_peak_index):
    imp_peak_value.append(df['impedance'][index-20:index+20].min())
    imp_peak_index.append(df['impedance'][index-20:index+20].argmin() + index - 20)
'''

## peak comparison(fluorescence, impedance)

for i in range(90):
    print(peak_index_f[i], peak_index_i[i], peak_index_f[i]-peak_index_i[i])

print(len(peak_index_f), len(peak_index_i))
for i in range(len(peak_index_f)):
    print(i,':',(peak_index_f[i]-peak_index_i[i])/10,'ms','({} s,{} s)'.format(peak_index_f[i]/10000,peak_index_i[i]/10000))