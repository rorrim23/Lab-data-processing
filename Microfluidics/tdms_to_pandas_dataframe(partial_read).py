#%%
from nptdms import TdmsFile
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

# tdms file은 group이라는 상위 분류 밑에 channel이라는 하위분류가 있는 듯.

df = pd.DataFrame([])
# when i don't know the name of group, channel
with TdmsFile.open("200421_sample/13um_goldbead_10ulmin.tdms") as tdms_file:
    '''
    for name, value in tdms_file.properties.items():
        print("{0}: {1}".format(name, value))
    '''
    for group in tdms_file.groups():
        for channel in tdms_file[str(group)[23:-2]].channels():
            # print(channel[:])
            # print(str(channel)[36:-2])
            df[str(channel)[36:-2]] = channel[:]
            # tdms_file.object(str(tdms_file.groups())[23:-2],channel).read_data(1,3)

'''
# when i know the name of group, channel
with TdmsFile.open("") as tdms_file:
    df['voltage'] = tdms_file.object('Untitled','Voltage').read_data(1,3)
    # tdms_file.object(group, channel).read_data(offset,length)
    # df['voltage'] = tdms_file['Untitled']['Voltage'][1:3]
'''
print(df)