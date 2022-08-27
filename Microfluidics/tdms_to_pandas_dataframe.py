#%%
from nptdms import TdmsFile
import matplotlib.pyplot as plt
import numpy as np 

voltage_file = TdmsFile("200421_sample/13um_goldbead_10ulmin.tdms")
# print(voltage_file.groups())
# print(voltage_file['Untitled'].channels())
for group in voltage_file.groups():
    df = voltage_file.object(group).as_dataframe()
    print(df.head())

# df = df.rename(columns={'Voltage':'voltage'})
# df.columns = {'voltage'}

fig1 = plt.figure(figsize=(50,10))
ax1 = fig1.add_subplot(1,1,1)
ax1.plot(df['Voltage'],linewidth=1)