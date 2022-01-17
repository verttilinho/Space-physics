# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:24:12 2021

@author: Vertti
"""
import pandas as pd
import numpy as np

from astropy.coordinates import SkyCoord
from sunpy.coordinates import frames


#This code transforms from HGI to HEEQ.

#reading the file with the data of spacecraft locations
df = pd.read_csv("where-spacecraft_heliographiccoor1.txt", delim_whitespace = True)

#dates of events in right format
date = np.loadtxt("dates_forsunpy.txt", dtype=np.str)


#Storing the columns
lat_a = df["lat_a_(deg)"]
long_a = df["lon_a_(deg)"]


lat_b = df["lat_b_(deg)"]
long_b = df["lon_b_(deg)"]


lat_e = df["lat_e_(deg)"]
long_e = df["lon_e_(deg)"]


#Defining that they are longitude and lattidude (mby) and telling which coordinates and obstime
sta = SkyCoord(long_a, lat_a, unit = "deg", frame=frames.HeliocentricInertial, obstime = date )

stb = SkyCoord(long_b, lat_b, unit = "deg", frame=frames.HeliocentricInertial,  obstime = date)

earth = SkyCoord(long_e, lat_e, unit = "deg", frame=frames.HeliocentricInertial,  obstime = date)



#transform them to HEEQ
sta_t = sta.transform_to(frames.HeliographicStonyhurst)
stb_t =stb.transform_to(frames.HeliographicStonyhurst)
earth_t = earth.transform_to(frames.HeliographicStonyhurst)



df2 = pd.DataFrame({"year": df.iloc[:, 0], "day": df.iloc[:, 1],
                    "r_a_(AU)": df.iloc[:, 2], "lat_a_(deg)": sta_t.lat.degree, 
                    "lon_a_(deg)": sta_t.lon.degree,"r_b_(AU)": df.iloc[:, 5], 
                    "lat_b_(deg)": stb_t.lat.degree, "lon_b_(deg)": stb_t.lon.degree, 
                    "r_e_(AU)": df.iloc[:,8], "lat_e_(deg)": earth_t.lat.degree,
                    "lon_e_(deg)": earth_t.lon.degree})



df2.to_csv("where-spacecraft_HEEQ2.txt", sep='\t')

