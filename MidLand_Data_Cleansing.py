# Import dataset
import pandas as pd
dataset = pd.read_csv("midland_realty_data.csv", encoding="cp1252")
dataset = dataset.iloc[:,1:]
dataset = dataset.fillna("")
dataset



#######################################
# Define functions for data cleansing #
#######################################

# Clean sell price, keep only number (in Million)
import re
clean_sell_price = lambda x: float(re.search("\d+(\.\d+)?",x).group())

# Clean Rent Price
def clean_rent_price(x):
    if x != "":
        x = x.replace(",","")
        string_return = float(re.search("\d+(\.\d+)?",x).group())
    else:
        string_return = None
    return string_return


# Clean net area / gross area
def clean_area(x):
    if x != "":
        return float(x.replace(",",""))
    else:
        return None


# Clean effi_ratio
def clean_ratio(x):
    if x != "":
        return float(x.replace("%",""))
    else:
        return None


# Clean layout
def clean_layout(x):
    if x != "":
        return int(x.replace("room(s)",""))
    else:
        return None


from datetime import datetime
def clean_date(x):
    return datetime.strptime(x, '%d/%m/%Y')


def clean_total_flats(x):
    if x != "":
        return int(x.replace(",","").replace("Units","").replace("units",""))
    else:
        return None


def clean_prop_val(x):
    return float(x.replace("$","").replace(",",""))


def clean_rpy_prd(x):
    return int(x.split("Years")[0])


def clean_inc_reqr(x):
    return float(x.replace("$","").replace(",","").replace("/Month",""))



# Deploy all the cleansing steps
dataset["sell_price"] = dataset["sell_price"].apply(clean_sell_price)
dataset["rent_price"] = dataset["rent_price"].apply(clean_rent_price)
dataset["net_area"] = dataset["net_area"].apply(clean_area)
dataset["gross_area"] = dataset["gross_area"].apply(clean_area)
dataset["effi_ratio"] = dataset["effi_ratio"].apply(clean_ratio)
dataset["layout"] = dataset["layout"].apply(clean_layout)
dataset["upd_dt"] = dataset["upd_dt"].apply(clean_date)
dataset["ttl_flt"] = dataset["ttl_flt"].apply(clean_total_flats)
dataset["prop_val"] = dataset["prop_val"].apply(clean_prop_val)
dataset["rpy_prd"] = dataset["rpy_prd"].apply(clean_rpy_prd)
dataset["inc_reqr"] = dataset["inc_reqr"].apply(clean_inc_reqr)




# Keep only the needed variables
dataset = dataset.loc[:,["sell_price"
                       ,"rent_price"
                       ,"net_area"
                       ,"gross_area"
                       ,"effi_ratio"
                       ,"layout"
                       ,"orit"
                       ,"upd_dt"
                       ,"ttl_flt"
                       ,"prop_val"
                       ,"rpy_prd"
                       ,"inc_reqr"
                       ,"addr"]]


######################################
# Find Longitude/Latitude by address #
######################################

import warnings
warnings.filterwarnings("ignore")
from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=3)


def find_lat(addr):
    try:
        location = geolocator.geocode("Hong Kong, "+ addr)
        print("latitude is", location.latitude)
        return location.latitude
    except:
        print("timeout, skip")
        return ""
    

def find_long(addr):
    try:
        location = geolocator.geocode("Hong Kong, "+ addr)
        print("longitude is", location.longitude)
        return location.longitude
    except:
        print("timeout, skip")
        return ""
    


dataset["latitude"] = dataset["addr"].apply(find_lat)
dataset["longitude"] = dataset["addr"].apply(find_long)


dataset.to_csv("midland_data_cleansed.csv")

