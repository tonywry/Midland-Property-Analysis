
# Init Selenium test browser
import pandas as pd
import time
from selenium import webdriver
browser = webdriver.Chrome('./chromedriver')
browser.get("https://en.midland.com.hk/find-property/#list")



# Scrap all information of a property given a detail page
def scrap_item_page():
    try:
        sell_price = browser.find_element_by_xpath("//div[@class='sect-sellrent']//p[@class='sell-color']").text
    except:
        sell_price = ""

    try:
        rent_price = browser.find_element_by_xpath("//div[@class='sect-sellrent']//p[@class='rent-color']").text
    except:
        rent_price = ""
    
    item_list = browser.find_elements_by_xpath("//li[@class='label-group']")
    
    for item in item_list:
        item_text = item.text
        # saleable area
        if "Saleable Area" in item_text:
            net_area = item_text.split(":")[1].split("sq")[0].replace(" ","")
        # gross area
        if "Gross Area" in item_text:
            gross_area = item_text.split(":")[1].split("sq")[0].replace(" ","")
        # Efficiency Ratio
        if "Efficiency Ratio" in item_text:
            effi_ratio = item_text.split(":")[1].replace(" ","")
        # Layout
        if "Layout" in item_text:
            layout = item_text.split(":")[1].replace(" ","")
        # Orientation
        if "Orientation" in item_text:
            orit = item_text.split(":")[1].replace(" ","")
        # View
        if "View" in item_text:
            view = item_text.split(":")[1].replace(" ","")
        # Description
        if "Description" in item_text:
            desc = item_text.split(":")[1].replace(" ","")
        # Update date
        if "Update Date" in item_text:
            upd_dt = item_text.split(":")[1].replace(" ","")
        # Address
        if "Address" in item_text:
            addr = item_text.split(":")[1]
        # Number of Blocks
        if "No. of Blocks" in item_text:
            blk_num = item_text.split(":")[1].replace(" ","")
        # Property School Net
        if "Property School Net" in item_text:
            school = item_text.split(":")[1]
        # Total Flats
        if "Total Flats" in item_text:
            ttl_flt = item_text.split(":")[1].replace(" ","")
        # Date of occupation Permit
        if "Date of Occupation Permit" in item_text:
            occu_permit_dt = item_text.split(":")[1].replace(" ","")
        # Facilities
        if "Facilities" in item_text:
            facilities = item_text.split(":")[1].replace(" ","")
        # Property Value
        if "Property Value" in item_text:
            prop_val = item_text.split(":")[1].replace(" ","")
        # Loan Amount
        if "Loan Amount" in item_text:
            ln_amt = item_text.split(":")[1].replace(" ","")
        # Interest Rate
        if "Interest Rate" in item_text:
            int_rt = item_text.split(":")[1].replace(" ","")
        # Repayment Period
        if "Repayment Period" in item_text:
            rpy_prd = item_text.split(":")[1].replace(" ","")
        # Income Requirement
        if "Income Requirement" in item_text:
            inc_reqr = item_text.split(":")[1].replace(" ","")
        
        
    # Check if all variable has been assigned , if not, assign as ""
    if "sell_price" not in locals():
        sell_price = ""
    if "rent_price" not in locals():
        rent_price = ""
    if "net_area" not in locals():
        net_area = ""
    if "gross_area" not in locals():
        gross_area = ""
    if "effi_ratio" not in locals():
        effi_ratio = ""
    if "layout" not in locals():
        layout = ""
    if "orit" not in locals():
        orit = ""
    if "view" not in locals():
        view = ""
    if "desc" not in locals():
        desc = ""
    if "addr" not in locals():
        addr = ""
    if "blk_num" not in locals():
        blk_num = ""
    if "school" not in locals():
        school = ""
    if "ttl_flt" not in locals():
        ttl_flt = ""
    if "occu_permit_dt" not in locals():
        occu_permit_dt = ""
    if "facilities" not in locals():
        facilities = ""
    if "prop_val" not in locals():
        prop_val = ""
    if "ln_amt" not in locals():
        ln_amt = ""
    if "int_rt" not in locals():
        int_rt = ""
    if "rpy_prd" not in locals():
        rpy_prd = ""
    if "inc_reqr" not in locals():
        inc_reqr = ""
    
    
    info_dict = {"sell_price":sell_price
                ,"rent_price":rent_price
                ,"net_area":net_area
                ,"gross_area":gross_area
                ,"effi_ratio":effi_ratio
                ,"layout":layout
                ,"orit":orit
                ,"view":view
                ,"desc":desc
                ,"upd_dt":upd_dt
                ,"addr":addr
                ,"blk_num":blk_num
                ,"school":school
                ,"ttl_flt":ttl_flt
                ,"occu_permit_dt":occu_permit_dt
                ,"facilities":facilities
                ,"prop_val":prop_val
                ,"ln_amt":ln_amt
                ,"int_rt":int_rt
                ,"rpy_prd":rpy_prd
                ,"inc_reqr":inc_reqr
                }
    
    return info_dict



# Loop through the list, for each page of the list, open the item detail, and scrap, then return to the list
def scrap_current_page():
    item_list = browser.find_elements_by_xpath("//*[@class='address-detail']")
    tmp = pd.DataFrame(columns = ["sell_price",
                                    "rent_price",
                                    "net_area",
                                    "gross_area",
                                    "effi_ratio",
                                    "layout",
                                    "orit",
                                    "view",
                                    "desc",
                                    "upd_dt",
                                    "addr",
                                    "blk_num",
                                    "school",
                                    "ttl_flt",
                                    "occu_permit_dt",
                                    "facilities",
                                    "prop_val",
                                    "ln_amt",
                                    "int_rt",
                                    "rpy_prd",
                                    "inc_reqr"])
    
    for item in item_list:
        item.click() # Open the item page
        browser.switch_to.window(browser.window_handles[-1]) # Switch to that item tab
        try:
            info = scrap_item_page() # Scrap the item information
        except: # Some item page are broken, close it and switch back
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            continue
        tmp = tmp.append(pd.DataFrame(info, index=[0]))
        browser.close() # Close the item tab
        browser.switch_to.window(browser.window_handles[0]) # Switch to that item list tab
    return tmp



# Init the dataset format
midland_reality_data = pd.DataFrame(columns = ["sell_price",
                                            "rent_price",
                                            "net_area",
                                            "gross_area",
                                            "effi_ratio",
                                            "layout",
                                            "orit",
                                            "view",
                                            "desc",
                                            "upd_dt",
                                            "addr",
                                            "blk_num",
                                            "school",
                                            "ttl_flt",
                                            "occu_permit_dt",
                                            "facilities",
                                            "prop_val",
                                            "ln_amt",
                                            "int_rt",
                                            "rpy_prd",
                                            "inc_reqr"])




# Loop through all the pages, and collect all information
i=1
while i>0: # Keep looping till break
    print("Scraping page", i, "......")
    cur_pg_df = scrap_current_page()
    midland_reality_data = midland_reality_data.append(cur_pg_df)
    try:
        midland_reality_data.to_csv("midland_realty_data.csv", encoding = "utf-8")
        print("Updated csv file successfully!")
    except:
        print("opps!! Error occured while appending page", i)
    
    i+=1
    try:
        next_page_button = browser.find_element_by_xpath("//*[@id='page-selection']/ul/li[@data-lp='"+str(i)+"']/a")
        next_page_button.click()
        time.sleep(5)
    except:
        print("No next page available, Done Scraping!")
        break

