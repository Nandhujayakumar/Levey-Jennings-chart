#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import pyautogui
import numpy as np
import tkinter.ttk as ttk
import csv



data = pd.read_csv('C:/Users/nandh/Downloads/lj_chart1.csv')
#print(data)

column_names = list(data.columns)
col = np.array(column_names)
print(col)


#give function for recursion
def testinput():
    x = pyautogui.prompt('Enter Test name ')
    a=0
    for i in col:
        if x == i:
            #print("Found "+ x)
            a = 1
            #print(data[x])
            break
        else:
            continue
    if a == 1:
        print("found")
        pyautogui.alert('Data Found')
        
    else:
        print("Not found")
        pyautogui.alert('Data Not Found !! Try Again')
        
testinput()






test= data['Glucose']
day = np.array(data['Day'])






mean = np.array(test.mean())
m = mean.reshape(1,-1)
print(mean)


#standard deviation
import statistics
sd = statistics.stdev(test)
print("sd is ",sd)


#positive sd

#sd -1
sd_1 = mean+sd
print("sd +1 = ", sd_1)

#sd -2
sd_2 = mean + (sd * 2)
print("sd +2 = ",sd_2)

#sd -3
sd_3 = mean + (sd * 3)
print("sd +3 = ", sd_3)











#negative sd

#sd -1
sd_negative1 = mean-sd
print("sd1 = ", sd_negative1)

#sd -2
sd_negative2 = mean - (sd * 2)
print("sd -2 = ",sd_negative2)

#sd -3
sd_negative3 = mean - (sd * 3)
print("sd -3 = ", sd_negative3)




plt.figure(figsize=(15, 7))
Day = data['Day']

test_data = data[['Glucose']].mean(axis=1)


plt.plot(Day,test_data,'g', label='Data', marker= "o")

plt.ylim(80, 130)
plt.xlim(1, 10)

#mean line
plt.axhline(y= m, color='red',label="Mean" ,linestyle='--', alpha=1.0)


#sd positive plots
#sd +1
plt.axhline(y= sd_1, color='blue',label="SD +1" ,linestyle=':', alpha=0.5)
#sd +2
plt.axhline(y= sd_2, color='yellow',label="SD +2" ,linestyle='-', alpha=0.5)
#sd +3
plt.axhline(y= sd_3, color='green',label="SD +3" ,linestyle='-.', alpha=0.5)


#sd negative plots
#sd -1
plt.axhline(y= sd_negative1, color='pink',label="SD -1" ,linestyle=':', alpha=0.5)
#sd +2
plt.axhline(y= sd_negative2, color='brown',label="SD +2" ,linestyle='-', alpha=0.5)
#sd +3
plt.axhline(y= sd_negative3, color='black',label="SD +3" ,linestyle='-.', alpha=0.5)

plt.xlabel('Day')
plt.ylabel('Quality Value')
plt.title("Qc Grapgh Of glucose")
ax = plt.subplot()
ax.set_xticks(Day)
plt.legend()
plt.show()



# In[ ]:




