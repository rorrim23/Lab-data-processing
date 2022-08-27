#%%
from nptdms import TdmsFile, TdmsWriter, RootObject, GroupObject,ChannelObject
import matplotlib.pyplot as plt
import numpy as np 

voltage_file = TdmsFile("200421_sample/13um_goldbead_10ulmin.tdms")
# print(voltage_file.groups())
# print(voltage_file['Untitled'].channels())
"""
These lines worked in the older version of nptdms but not now
for group in voltage_file.groups(): # TdmsFile object has no "object" attribute
    df = voltage_file.object(group).as_dataframe()
    print(df.head())
"""
df = voltage_file['Untitled'].as_dataframe()
print(df.head())

original_file = TdmsFile("200421_sample/13um_goldbead_10ulmin.tdms")
root_object = RootObject(original_file.properties)
original_groups = original_file.groups()
channel_object_Voltage = ChannelObject("Untitled","Voltage",df["Voltage"].to_numpy())
channel_object_Voltage_0= ChannelObject("Untitled","Voltage_0",df["Voltage_0"].to_numpy())
#original_channels = [chan for group in original_groups for chan in group.channels()]

with TdmsWriter("copied_file.tdms") as copied_file:
    copied_file.write_segment([root_object] + original_groups + [channel_object_Voltage])
    copied_file.write_segment([root_object] + original_groups + [channel_object_Voltage_0])


voltage_file = TdmsFile("copied_file.tdms")
print(voltage_file.groups())
print(voltage_file['Untitled'].channels())
for group in voltage_file.groups():
    df = voltage_file.object(group).as_dataframe()
    print(df.head())
