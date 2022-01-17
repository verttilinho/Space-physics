#!/usr/bin/env python
# coding: utf-8

# In[12]:


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 07:37:53 2021

@author: Vertti Linho
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.font_manager import FontProperties
import os

''''
This code plots locations of different spacecraft of specific date.
Also it plots the parker spiral to the spacecraft.
'''

#Makes paths where the images are saved
my_path = os.path.abspath("images")
my_path2 = os.path.abspath("images_without_axis")


#Read the data of locations of the spacecraft
df = pd.read_csv("where-spacecraft_HEEQ2.txt", delim_whitespace = True)
dates = np.loadtxt("dates_format.txt",  dtype = str)
file_name = np.loadtxt("filenames.txt", dtype = str)
file_name2 = np.loadtxt("filenames_noaxis.txt", dtype = str)

#constants
au = 49597870700 # 1 = 49597870700 m
v = 300*10**3 #m/s
omg = 2.7*10**(-6) #rad/s
r_0 = 695340*10**3/au #AU

#formula for source angle (parker spiral)
def phi_0(r, phi):
    return au*(r -r_0)*omg/v+np.radians(phi) #returns radians




for k in range(len(dates)):
    
        
    #STEREO-A
    #take the right values
        
    phi_sta = df.loc[k].at["lon_a_(deg)"] #unit = deg
    r_sta = df.loc[k].at["r_a_(AU)"] #unit = deg
    

        
    #radius goes from sun to spacecraft
    rp_a = np.linspace(r_0, r_sta, 3600)


    #loacation of stereo_b
    
    phi_stb = df.loc[k].at["lon_b_(deg)"] #unit = deg
    r_stb = df.loc[k].at["r_b_(AU)"] #unit = AU
    
    #radius goes from sun to spacecraft
    rp_b = np.linspace(r_0, r_stb, 3600)
    


    #location for earth
    phi_e =df.loc[k].at["lon_e_(deg)"] #unit = deg
    r_e = df.loc[k].at["r_e_(AU)"] # unit = AU
    
    
    #radius goes from sun to spacecraft
    rp_e = np.linspace(r_0, r_e, 3600)
    
    phia_0 = phi_0(r_sta, phi_sta)

    phib_0 = phi_0(r_stb, phi_stb)

    phie_0 = phi_0(r_e, phi_e)
    

    # Formula for the angle, given distance
    def phi_a(r):
        return au*(r_0-r)*omg/v+phia_0

    def phi_b(r):
        return au*(r_0-r)*omg/v+phib_0

    

    def phi_earth(r):
        return au*(r_0-r)*omg/v+phie_0
    
    def x(r, phi):
        return r*np.cos(phi)
    
    def y(r, phi):
        return r*np.sin(phi)
            
  
    #Images
    fig, ax = plt.subplots(figsize=(7, 7), dpi = 800)

    fontP = FontProperties()
    fontP.set_size('large') 
        
    ax.set_xlim((-1.2, 1.2))
    ax.set_ylim((-1.2, 1.2))
        
    #Circle at 1 Au distance from Sun
    circle = plt.Circle((0, 0), 1, color='grey', fill=False)

    ax.add_artist(circle)

    
    ax.plot((0), (0), 'o', color='y')
    

    
    ax.plot(x(rp_a, phi_a(rp_a)), y(rp_a, phi_a(rp_a)),'--', 
            color = '#377eb8')
    ax.plot(x(rp_a[-1], phi_a(rp_a[-1])), y(rp_a[-1], phi_a(rp_a[-1])),
            "d", label = "STA", color = '#377eb8')
    
    ax.plot(x(rp_b, phi_b(rp_b)), y(rp_a, phi_b(rp_b)),
            ':', color = '#ff7f00')
    ax.plot(x(rp_b[-1], phi_b(rp_b[-1])), y(rp_b[-1], phi_b(rp_b[-1])),
            "x", label = "STB", color = '#ff7f00')

    ax.plot(x(rp_e, phi_earth(rp_e)), y(rp_e, phi_earth(rp_e)),
            color = '#4daf4a')
    ax.plot(x(rp_e[-1], phi_earth(rp_e[-1])), y(rp_e[-1], phi_earth(rp_e[-1])), 
            "s", label = "Earth", color = '#4daf4a')
    
    
    
    
    ax.set_xlabel("Au")
    ax.set_ylabel("Au")
    ax.set_title(dates[k])

    ax.legend(loc="lower center",ncol = 3, 
              bbox_to_anchor=(0.5, -0.16),  prop=fontP)
    
    plt.ioff()
    plt.close()
    
    fig2, bx = plt.subplots(figsize=(7, 7), dpi = 500)
    
    bx.set_xlim((-1.2, 1.2))
    bx.set_ylim((-1.2, 1.2))
    
    circle2 = plt.Circle((0, 0), 1, color='grey', fill=False)
    bx.add_artist(circle2)

    
    bx.plot((0), (0), 'o', color='y')
    
    bx.plot(x(rp_a, phi_a(rp_a)), y(rp_a, phi_a(rp_a)),'--', 
            color = '#377eb8')
    bx.plot(x(rp_a[-1], phi_a(rp_a[-1])), y(rp_a[-1], phi_a(rp_a[-1])),
            "d", label = "STA", color = '#377eb8')
    
    bx.plot(x(rp_b, phi_b(rp_b)), y(rp_a, phi_b(rp_b)),
            ':', color = '#ff7f00')
    bx.plot(x(rp_b[-1], phi_b(rp_b[-1])), y(rp_b[-1], phi_b(rp_b[-1])),
            "x", label = "STB", color = '#ff7f00')

    bx.plot(x(rp_e, phi_earth(rp_e)), y(rp_e, phi_earth(rp_e)),
            color = '#4daf4a')
    bx.plot(x(rp_e[-1], phi_earth(rp_e[-1])), y(rp_e[-1], phi_earth(rp_e[-1])), 
            "s", label = "Earth", color = '#4daf4a')
    
    bx.set_title(dates[k])
    bx.legend(loc="lower center",ncol = 3, 
              bbox_to_anchor=(0.5, -0.16),  prop=fontP)
    bx.axis('off')
    
    plt.ioff()
    plt.close()
    
    
    
    if k == 0:
        print("Here it begins!")
    
    if k == 47: 
        print("Over 25% done!")
    if k == 94:
        print("50% done!")
    if k == 142:
        print("Over 75% done!")
    
    
    fig.savefig(os.path.join(my_path, file_name[k]))
    
    fig2.savefig(os.path.join(my_path2, file_name2[k]))
    
print("100% done!")


# In[31]:





# In[ ]:





# In[ ]:




