## Midland-Property-Analysis

This is an Analysis of Hong Kong Housing Price, A simple demonstration on web-crawling by Selenium and data visualization, individual project of HKU STAT7008 Course

![image](https://user-images.githubusercontent.com/29504448/58641354-9babb800-832d-11e9-9134-9c7c70a10e41.png)


### Data Collection
Data of this project was collected from Midland Property Website by utilizing web-crawling method. Midland Property Search page (https://en.midland.com.hk/find-property/#list) listed out all the properties currently in sell while no searching criteria has been input. This page was mainly constructed by JS hence Selenium was used to crawl the data.

chromedriver of Version 73.0.3683.68 was used in this project, drivers for other versions/browsers can be downloaded here (https://www.seleniumhq.org/download/)

Folder "Sample Data" comprises the collected data as of 22-May-2019

Variables collected in this project:
1. sell_price – Selling price of the property, in Million
2. rent_price – Renting price of the property if the property is also open for renting
3. net_area – Net area of the property, in square feet
4. gross_area – Gross area of the property, in square feet
5. effi_ratio – Efficiency Ratio, in percentage, value equal to net_area/gross_area
6. layout – Layout of the property, stated how many rooms does the property have
7. orit – Orientation of the property, possible values include North/West/East/South, etc.
8. view – View of the property, if any
9. desc – Any description of the property that the owner provided, if any
10. upd_dt – Update date of the property on the website
11. addr – Address of the property
12. blk_num – Number of blocks of the property
13. school – Name of school(s) around the property, if any
14. ttl_flt – Total number of flats
15. occu_permit_dt – Date of occupation Permit
16. facilities – Facilities around the property, if any
17. prop_val – Property Value
18. ln_amt – Loan Amount
19. int_rt – Interest Rate of the Mortgage Plan
20. rpy_prd – Repayment Period of the Mortgage Plan
21. inc_reqr – Income requirement of buying this property/applying the mortgage

Other information can also be scraped from this page, but not in scope of this project

### Data Cleansing
geocoders was used to find GPS Coordinates by the property's address, by which scatter plot can be drawn on the map

### Data Visualization
Several plots for the Analysis as below. 

Basemap of HK was base on the shape file gadm36_HKG_1, all shape files can be downloaded here (https://gadm.org/download_country_v3.html)

![image](https://user-images.githubusercontent.com/29504448/58641110-2344f700-832d-11e9-9541-b5f9e2c4e487.png)

![image](https://user-images.githubusercontent.com/29504448/58641208-57b8b300-832d-11e9-9892-65cb0669e126.png)


Size of properties across region
![image](https://user-images.githubusercontent.com/29504448/58641282-7c148f80-832d-11e9-9da2-90c432feb7cb.png)

