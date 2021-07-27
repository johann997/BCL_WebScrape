# BCL_WebScrape

This script aims to answers the age old question of, "which alcohol is most cost effective". i.e. What is the cost per litre ($/l).

## Running the script

1) Download [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads)
2) Update path to ChromeDriver download on line 27


## Optional changes
1) At the moment you have to manually change whether the scripts scrapes through the beer, wine or cider etc. To update the categroy, change the link on line 33 and update the number of possible pages line 32
2) My internet is slow so you may be able to lower lines 36 & 68. This timing is to allow the page to load so that the code can scrape all the information
3) Change .csv file name/location line 61

At the moment the code will update the .csv as the code runs so that you can track the progress. The commented lines are only there so that if for some reason you want to create the csv after the code has finished running. But I would advise against this...
