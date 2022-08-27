from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd 
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
soup=bs(page.text,"html.parser")
startable=soup.find_all("table")
temp_list=[]
tablerows=startable[7].find_all("tr")
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
starname=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(temp_list)):
    starname.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
df=pd.DataFrame(list(zip(starname,distance,mass,radius) ) ,columns=["star_name","distance","mass","radius"]) 
print(df)   
df.to_csv("dwarfstars.csv")



