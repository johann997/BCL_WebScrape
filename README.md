There are two folders:
- `src/BCLWebScrape` (efficient web scrape and ML analysis)
- `_old` (slow webscrape no analysis)

The scripts in `_old` were originally created to answer the age old question of, "which alcohol is most cost effective". i.e. What is the cost per litre ($/l).

However, I ended up coming back to this project with improved web scraping capabilities (thanks to YouTube and the Insomnia service) and found that I could collect much more information. So I turned this into an ML project 

# src/BCL_WebScrape/CollectData.ipynb
This notebook webscrapes https://www.bcliquorstores.com and saves the data to a .csv

You only need to install the packages in the Notebook.
I also attached the scraped .csv `src/BCL_WebScrape/data/web-scraped-result.csv` so you do not need to run the scraping code if it does not work for you.
The Notebook contains some feature engineering, e.g. using geopy to plot add the lattitude and longitude of drink locations.
An example plot `src/BCL_WebScrape/figures/BCL-world-map.html` shows the number of BLC product from each country on a world map. You can view this in your favourie web browser. :)


# src/BCL_WebScrape/Analysis.ipynb
This data loads the saved .csv and does some analysis.
The analysis and thought process is laid out in markdown textblocks through the notebook. 

Overall, the business question was to see which products receive the highest ratings. This would help inform how the inventory should be managed for the next year to improve the overall rating of drinks available. Higher rating -> greater customer satisfaction -> perhaps more footfall in store.

I tried regression with price, alohol content, and drink profile which was determined by using NLP to cluster drink types using a text description of the drink. </br>
I also tried multi-class classification by breaking down the ratings into 3 categories to see if simplifying the problem would obtian useful results. 

Different tools, techniques and evaluation metrics were used. 
- Hierarchical clustering using a dendrogram
- Grid search
- PCA
- Regression models used
  1. linear regression
  2. random forest regression (`ensemble learning : bagging`)
  3. gradient boosting (`ensemble learning : boosting`)
- Classification models used
  1. random forest (`ensemble learning : bagging`)
- Confusion matrix
- Classification report
- ROC curve
- Learning curve

Predicting a drinks rating proved to be difficult. There are many TODO's laid out which I will get back to at some point. :)

---
---

# _old/BCLWebScraping.py

## Running the script

1) Download [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads)
2) Update path to ChromeDriver download on line 27


## Optional changes
1) At the moment you have to manually change whether the scripts scrapes through the beer, wine or cider etc. To update the categroy, change the link on line 33 and update the number of possible pages line 32
2) My internet is slow so you may be able to lower lines 36 & 68. This timing is to allow the page to load so that the code can scrape all the information
3) Change .csv file name/location line 61

At the moment the code will update the .csv as the code runs so that you can track the progress. The commented lines are only there so that if for some reason you want to create the csv after the code has finished running. But I would advise against this...
