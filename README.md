# Midland-Property-Analysis

This is an Analysis of Hong Kong Housing Price, A simple demonstration on web-crawling by Selenium and data visualization, individual project of HKU STAT7008 Course - Programming for data science

![image](https://user-images.githubusercontent.com/29504448/58641354-9babb800-832d-11e9-9134-9c7c70a10e41.png)


### Data Collection
Data of this project was collected from Midland Property Website by utilizing web-crawling method. Midland Property Search page (https://en.midland.com.hk/find-property/#list) listed out all the properties currently in sell while no searching criteria has been input. This page was mainly constructed by JS hence Selenium was used to crawl the data.

chromedriver of Version 73.0.3683.68 was used in this project, drivers for other versions/browsers can be downloaded here (https://www.seleniumhq.org/download/)

### Data Cleansing
geocoders was used to find GPS Coordinates by the property's address, by which scatter plot can be drawn on the map

### Data Visualization
Several plots for the Analysis as below. 

Basemap of HK was base on the shape file gadm36_HKG_1, all shape files can be found here (https://gadm.org/download_country_v3.html)

![image](https://user-images.githubusercontent.com/29504448/58641110-2344f700-832d-11e9-9541-b5f9e2c4e487.png)

![image](https://user-images.githubusercontent.com/29504448/58641208-57b8b300-832d-11e9-9892-65cb0669e126.png)

![image](https://user-images.githubusercontent.com/29504448/58641282-7c148f80-832d-11e9-9da2-90c432feb7cb.png)

