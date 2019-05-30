# Midland-Property-Analysis

This is an Analysis of Hong Kong Housing Price, A simple demonstration on web-crawling by Selenium and data visualization, individual project of HKU STAT7008 Course - Programming for data science

# Data Collection
Data of this project was collected from Midland Property Website by utilizing web-crawling method. Midland Property Search page (https://en.midland.com.hk/find-property/#list) listed out all the properties currently in sell while no searching criteria has been input. This page was mainly constructed by JS hence Selenium was used to crawl the data.

chromedriver of Version 73.0.3683.68 was used in this project, drivers for other versions/browsers can be downloaded here (https://www.seleniumhq.org/download/)

# Data Cleansing
geocoders was used to find GPS Coordinates by the property's address, by which scatter plot can be drawn on the map

# Data Visualization
Several plots for the Analysis as below. 

Basemap of HK was base on the shape file gadm36_HKG_1, all shape files can be found here (https://gadm.org/download_country_v3.html)


