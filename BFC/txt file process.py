#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

with open('190614_fd+Os+GOx(2)_CA(double-step5s)_simple.txt') as textfile:
    df = pd.read_csv(textfile, dtype=np.float64)
    df.columns = ['time', 'current']
    df['current'] = df['current'] 
    df = df[:len(df)//10]
    print(df)
    # print(df[len(df)//2-4:len(df)//2+4])

fig = plt.figure(figsize=(5,5))
ax1 = fig.add_subplot(1,1,1)
ax1.plot(df['time'], df['current'])

a = 0
for _ in range(30):
    df['loss'] = (a*df['time']**-0.5-df['current'])**2
    df['der_loss'] = 2 * (a*df['time']**-0.5-df['current']) * df['time']**-0.5
    a -= 0.00005 * df['der_loss'].sum()
    print(df['loss'].sum())

ax1.plot(df['time'], a*df['time']**-0.5)