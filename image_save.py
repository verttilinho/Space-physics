


import pyautogui as pg #clicker
import os #folder / file sutff
import pandas as pd #pandas are cute


#image stuff
import glob
from PIL import Image

"""
This code is made to automatize some of the work done with Jhelioviewer.
This code saves the image to right folder and helps making the description to the excel file.
"""


#Loading SEP event data
df = pd.read_excel("SEP_event_data_updated.xlsx")

dates = df["date_f"]

event_desc = df["Desc"]



#click "record" on Jhelioviewer
pg.click(169,193)

#move mouse to the close button and click
pg.moveTo(1191, 591, 0.5)
pg.click(1191,591)
#click terminal
pg.click(38, 337)




#this will help us to locate the place where to type description of the event
w_event = input("Which event are you looking at? ")


 

#this helps to write the description to the excel
what = input("Was it a flare/eruption/something else? ")

where = input("Where was it observed? ")

sp = input("STA/STB/SDO ")

path = "/home/vlinho/Desktop/SEP/Solar_images/" + w_event


#Check if we already have folder for images of current event
if os.path.isdir(path) == False:    
    my_path = os.path.abspath(w_event)
    
    #this should make new folder
    new_folder =  os.makedirs(path)

    a = input("Give time of the event: ") 
    
    file_name = a + "_" + sp + ".png"
    #Loading the image
    image_list = []

    for filename in glob.glob('/home/vlinho/JHelioviewer-SWHV/Exports/*.png'):
        im=Image.open(filename)
        image_list.append(im)

    

    image_list[0].save(os.path.join(path, file_name))
    
else:
    a = input("Give time of the event_2: ") 
    file_name = a +  "_" + sp + ".png"
    #Loading the image
    image_list = []

    for filename in glob.glob('/home/vlinho/JHelioviewer-SWHV/Exports/*.png'):
        im=Image.open(filename)
        image_list.append(im)

    
    image_list[0].save(os.path.join(path, file_name))

#Writes description to the excel

l = input("What color: ")

if what == "f":
    
    if sp == "SDO":
        desc = a + " flare was observed at " + where + " in the point of view of " + sp + " (" + l + " å) ||| "

    else:
        desc = a + " flare was observed at " + where + " in the point of view of " + sp + " (" + l + " å) ||| "
        
elif what == "e":
    
    if sp == "SDO":
        desc = a + " flare was observed at " + where + " in the point of view of " + sp + " (" + l + " å) ||| "

    else:
        desc = a + " flare was observed at " + where + " in the point of view of " + sp + " (" + l + " å) ||| "
else:
    
    if sp == "SDO":
        desc = a + " flare was observed at " + where + " in the point of view of " + sp + " (" + l + " å) ||| "

    else:
        desc = a + " flare was observed at " + where + " in the point of view of " + sp + " (" + l + " å) ||| "

#go through all events and check which event we are looking at
#Then check if there are no other descriptions and add the desc
       
for i in range(len(dates)):
    if w_event == dates[i]:
        if event_desc[i] == "Na":
            event_desc[i] = desc
            
        
        else:
            event_desc[i] = event_desc[i] + desc
            

        
df["Desc"] = event_desc




#Saving the changes to excel

df.to_excel("SEP_event_data_updated.xlsx", index = False)


#Deleting the just taken image from the Jhelioviewer file
dir = '/home/vlinho/JHelioviewer-SWHV/Exports'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))




