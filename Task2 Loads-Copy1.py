#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import os 
os.getcwd()
import pandas as pd 
orders = pd.read_csv('Orders.csv')

def task2(orders):
    ID = orders["Order No."].to_numpy()
    From = orders['From'].to_numpy()  
    To = orders['To'].to_numpy()
    day = orders['When'].to_numpy()
    #importing data from .csv
    Location1 = 'Swansea'
    Location2 = 'London'
    m1 = [] #monday load location 1... monday load swansea
    m2 = []
    t1 = []
    t2 = []
    w1 = []
    w2 = []
    th1 = []
    th2 = []
    f1 = []
    f2 = []
    
    for x in range(0,1787):
        if From[x] == Location1 :#if order is coming from swansea add it to the Swansea_Load array
            if day[x] == 'Monday':
                m1.append(ID[x])
                m2.append(0)#add a 0 to the London_Load array to keep them the same length 
            
            if day[x] == 'Tuesday':
                t1.append(ID[x])
                t2.append(0)
                
            if day[x] == 'Wednesday':
                w1.append(ID[x])
                w2.append(0)
           
            if day[x] == 'Thursday':
                th1.append(ID[x])
                th2.append(0)
            
            if day[x] == 'Friday':
                f1.append(ID[x])
                f2.append(0)
            
       
        if From[x] == Location2:
            if day[x] == 'Monday':
                m2.append(ID[x])
                m1.append(0)
                
            if day[x] == 'Tuesday':
                t2.append(ID[x])
                t1.append(0)
                
            if day[x] == 'Wednesday':
                w2.append(ID[x])
                w1.append(0)
           
            if day[x] == 'Thursday':
                th2.append(ID[x])
                th1.append(0)
            
            if day[x] == 'Friday':
                f2.append(ID[x])
                f1.append(0)
            

            
    my_header = [Location2 +'Load',Location1+'Load',Location1 + 'Unload', Location2 + 'Unload'] #organising the .csv file
    udata = np.stack([m1,m2,m1,m2],axis=1)
    data = pd.DataFrame(udata,columns = my_header)
    data.to_csv("Monday.csv",index=False)
       
    my_header = [Location2 +'Load',Location1+'Load',Location1 + 'Unload', Location2 + 'Unload'] #organising the .csv file
    udata = np.stack([t1,t2,t1,t2],axis=1)
    data = pd.DataFrame(udata,columns = my_header)
    data.to_csv("Tuesday.csv",index=False)
    
    my_header = [Location2 +'Load',Location1+'Load',Location1 + 'Unload', Location2 + 'Unload'] #organising the .csv file
    udata = np.stack([w1,w2,w1,w2],axis=1)
    data = pd.DataFrame(udata,columns = my_header)
    data.to_csv("Wednesday.csv",index=False)
    
    my_header = [Location2 +'Load',Location1+'Load',Location1 + 'Unload', Location2 + 'Unload'] #organising the .csv file
    udata = np.stack([th1,th2,th1,th2],axis=1)
    data = pd.DataFrame(udata,columns = my_header)
    data.to_csv("Thursday.csv",index=False)
    
    my_header = [Location2 +'Load',Location1+'Load',Location1 + 'Unload', Location2 + 'Unload'] #organising the .csv file
    udata = np.stack([f1,f2,f1,f2],axis=1)
    data = pd.DataFrame(udata,columns = my_header)
    data.to_csv("Friday.csv",index=False)
       
    
        
task2(orders)


# In[ ]:




