

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:47:22 2020

@author: Rehab
"""

# importing the libraries that related to scraping web data
from bs4 import BeautifulSoup
import requests as req 
# web page url (for updated covid cases in the world)
url="https://www.worldometers.info/coronavirus/"

# requesting toa accsess the url
page = req.get(url)
#parsing html tags
soup = BeautifulSoup(page.content, 'lxml')
#retreiving the data form specific table
tabel=soup.find('table',{'id':'main_table_countries_today'})


for row in tabel.find_all('tr'):
    for col in row.find_all('td'):
        print(col.text)
        
list_of_rows = []
for row in tabel.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

for item in list_of_rows:
    print(' '.join(item))
    
import csv
#opening the csv file in 'w+' mode 
file = open('data_cov.csv', 'w+', newline ='') 
  
# writing the data into the file 
with file:     
    write = csv.writer(file) 
    write.writerows(list_of_rows) 


        
        
