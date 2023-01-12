#!/usr/bin/env python
# coding: utf-8

# In[93]:


#plot trajectory of hot air balloon 
import numpy as np        
import os 
os.getcwd()
import pandas as pd 
data = pd.read_csv('VelocityData.csv')
Vxm = data['Vx (mph)'].to_numpy()
Vym = data['Vy (mph)'].to_numpy()

def task1():
    import matplotlib.pyplot as plt
    for x in range(0,len(data)): #integrate over 120 minutes
        global rx1 
        global ry1
        rx = (((Vxm[x])/60)*x) + 1  
        ry = (((Vym[x])/60)*x) + 4.9
        #convert velocities into miles per minute and find position of rx at time x by multiplying miles by dt
        rx1 = np.asarray(rx)
        ry1 = np.asarray(ry)
        r = rx, ry
        #placing graph outside of for loop only plots last value of rx1,ry1
        #placing graph inside of for loop creates a seperate graph for each value of r? 
        
    x = range(1,120,1)
    fig,ax = plt.subplots()
    plt1 = ax.plot((((Vxm[x])/60)*x)+1,(((Vym[x])/60)*x)+4.9 , linewidth=3,label = 'Trajectory of Hot Air Balloon')
    img = plt.imread('BristolMap.png')
    ax.imshow(img, extent=[0, 12.5, 0, 14.41])
    ax.set_title("Trajectory of Hot Air Balloon",fontsize=14)  #setting titles and axes
    ax.set_xlabel("x (miles)",fontsize=11)
    ax.set_ylabel("y (miles)",fontsize=11)
    rxf = rx1-1 
    ryf = ry1-4.9 
    dr = np.sqrt((rxf)**2+(ryf)**2)
    print('Change in position is')  
    print(dr)
    


# In[58]:


task1()


# In[42]:


len(data)


# In[137]:


import numpy as np  #calling various libraries and modules       
import os 
os.getcwd() 
import pandas as pd
import matplotlib.pyplot as plt 
data = pd.read_csv('VelocityData.csv') #converting data into a useable form 
Vxm = data['Vx (mph)'].to_numpy()
Vym = data['Vy (mph)'].to_numpy()
r = np.zeros(shape = (len(data),2))
r[0] = (1,4.9)      #creating a zero matrix with the initial values 
      
for x in range(1,len(data),1):   #timestep of 1min over the range len of the data(120)
    r[x,0] = r[x-1,0]+(Vxm[x]/60)*1
    r[x,1]= r[x-1,1]+(Vym[x]/60)*1 
    #position is equal to the previous position + velocity(in miles/min) * dt(dt=1min)
   

fig,ax = plt.subplots()
plt1 = ax.plot(r[:,0],r[:,1],linewidth=3,label = 'Trajectory of Hot Air Balloon')
#indicies corresponding to the x or y column of the r matrix 
img = plt.imread('BristolMap.png')
ax.imshow(img, extent=[0, 12.5, 0, 14.41])
ax.set_title("Trajectory of Hot Air Balloon",fontsize=14)  #setting titles and axes
ax.set_xlabel("x (miles)",fontsize=11)
ax.set_ylabel("y (miles)",fontsize=11)


print('Change in distance is:')
dr = r[119]-r[0]
#the r[120] value returns an error 'not in the index of 120' so I used the closest value
dr1 = np.sqrt(dr[0]**2+dr[1]**2)
print(dr1)


# In[136]:


len(data)


# In[3]:


import numpy as np  
import os 
os.getcwd() 
import pandas as pd
import matplotlib.pyplot as plt 
data = pd.read_csv('VelocityData.csv')
Vxm = data['Vx (mph)'].to_numpy()
Vym = data['Vy (mph)'].to_numpy()
r = np.zeros(shape = (len(data),2))
r[0] = (1,4.9)      
      
for x in range(1,len(data),1): 
    r[x,0] = r[x-1,0]+(Vxm[x]/60)*1
    r[x,1]= r[x-1,1]+(Vym[x]/60)*1 
   
fig,ax = plt.subplots()
plt1 = ax.plot(r[:,0],r[:,1],linewidth=3,label = 'Trajectory of Hot Air Balloon')
img = plt.imread('BristolMap.png')
ax.imshow(img, extent=[0, 12.5, 0, 14.41])
ax.set_title("Trajectory of Hot Air Balloon",fontsize=14)  
ax.set_xlabel("x (miles)",fontsize=11)
ax.set_ylabel("y (miles)",fontsize=11)


print('Change in distance is:')
dr = r[119]-r[0]
dr1 = np.sqrt(dr[0]**2+dr[1]**2)
print(dr1)


# In[4]:


import numpy as np
print(np.asarray(Vxm))


# In[ ]:




