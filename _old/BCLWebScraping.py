#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:45:01 2021

@author: johanndrayne
"""
# import requests
from bs4 import BeautifulSoup
import time
import csv


baseurl = 'https://www.bcliquorstores.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}






from selenium import webdriver

driver_path = r'/Users/johanndrayne/Downloads/chromedriver'
browser = webdriver.Chrome(driver_path)

productlinks = []

for x in range(1, 135):
    browser.get(f"https://www.bcliquorstores.com/product-catalogue?category=wine&sort=name.raw:asc&page={x}")


    time.sleep(10)  # wait 20 seconds for the site to load.
    html = browser.page_source
    soup = BeautifulSoup(html, features='html.parser')


    for item in soup.findAll('div', attrs={'class': 'product-description-container'}):
            firstparse = item.find_all('a', href=True)[0]
            link = firstparse.attrs['href']
            productlinks.append(baseurl + link)

data = []
dict = {"Name":[],
            "Type":[],
            "Full Price":[],
            "Sale Price":[],
            "Number of Units":[],
            "Litres per unit":[],
            "Alcohol Percentage":[],
            "Alcohol Volume":[],
            "Efficiency":[],
            "Sale Efficiency":[],
            "link":[]}


# name ... price saleprice units volume alcper alcvolume efficiency saleefficiency ...
csv_file = 'wineefficiency.csv'
csv_columns = ["Name", "Type", "Full Price", "Sale Price", "Number of Units", "Litres per unit", "Alcohol Percentage", "Alcohol Volume", "Efficiency", "Sale Efficiency", "link"]


for i in productlinks:
    
    browser.get(f"{i}")
    time.sleep(8)  # wait 5 seconds for the site to load.
    html = browser.page_source
    soup = BeautifulSoup(html, features='html.parser')
    
    nameparse1 = soup.findAll('h1', attrs={'data-bind': "text: _source.name"})[0]
    name = nameparse1.text
    
    
    salepriceparse1 = soup.findAll('div', attrs={'data-bind': "text: '$' + _source.currentPrice"})[0]
    salepriceparse2 = salepriceparse1.text
    saleprice = float(salepriceparse2.split("$")[1])
    
    priceparse1 = soup.findAll('div', attrs={'data-bind': "price: _source.regularPrice"})[0]
    priceparse2 = priceparse1.text
    price = float(priceparse2.split("$")[1])
    
    
    unitparse1 = soup.findAll('span', attrs={'data-bind': 'volume: _source, visible: _source.volume != 0'})[0]
    unitparse2 = unitparse1.text
    
    if 'x' in unitparse2:
        if 'L' in unitparse2:
            units = float(unitparse2.split("x")[0])
            volumenop = unitparse2.split("x")[1]
            volume = float(volumenop.split("L")[0])*1000
        else:
            units = float(unitparse2.split("x")[0])
            volumenop = unitparse2.split("x")[1]
            volume = float(volumenop.split("ml")[0])
    else:
        if 'L' in unitparse2:
            units = 1
            volume = float(unitparse2.split("L")[0])*1000
        else:
            units = 1
            volumenop = unitparse2.split("x")[0]
            volume = float(unitparse2.split("ml")[0])
            
    alcperparse1 = soup.findAll('span', attrs={'data-bind': "text: _source.alcoholPercentage + '%'"})[0]
    alcperparse2 = alcperparse1.text      
    alcper = float(alcperparse2.split("%")[0])
    if alcper == 0:
        alcper = 1
    
    
    alcvolume = ((units * volume) / 1000) * (alcper / 100)
    saleefficiency = saleprice / alcvolume
    efficiency = price / alcvolume
    
    
    # dict["Name"].append(name)
    # dict["Type"].append("N/A")
    # dict["Full Price"].append(price)
    # dict["Sale Price"].append(saleprice)
    # dict["Number of Units"].append(units)
    # dict["Litres per unit"].append(volume)
    # dict["Alcohol Percentage"].append(alcper)
    # dict["Alcohol Volume"].append(alcvolume)
    # dict["Efficiency"].append(efficiency)
    # dict["Sale Efficiency"].append(saleefficiency)
    # dict["link"].append(i)

    dict = {"Name":name,
                "Type":"N/A",
                "Full Price":price,
                "Sale Price":saleprice,
                "Number of Units":units,
                "Litres per unit":volume,
                "Alcohol Percentage":alcper,
                "Alcohol Volume":alcvolume,
                "Efficiency":efficiency,
                "Sale Efficiency":saleefficiency,
                "link":i}

    data.append(dict)

    
    with open(csv_file, 'a') as csvfile:
        
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writerow(dict)
        csvfile.close()

browser.close()


# csv_file = 'drinkefficiency.csv'
# csv_columns = ["Name", "Type", "Full Price", "Sale Price", "Number of Units", "Litres per unit", "Alcohol Percentage", "Alcohol Volume", "Efficiency", "Sale Efficiency", "link"]


# with open(csv_file, 'w') as csvfile:  
#     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)



# print("finished")
    
    
    