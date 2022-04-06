import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class merck:
    def _init_(self,dataset):
        self.dataset = dataset
        
    
    def scrap(page_link):
        """
        This function returns scraps data from Merck website, it scraps product name, compound name, indication,
        phase and mechanism of action

        Input : str, page link
        Returns : dataframe, dataframe with product name, compound name, indication, phase and mechanism pf action

        """
        page = requests.get(page_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        # create dataframe
        dataset = pd.DataFrame()
        # extracting class category color and category name
        dataset["Colors"] = pd.Series([j.attrs["class"][0].split("-")[0] for i in soup.find_all(class_="category-color") for j in i.children])
        dataset["Indication"] = pd.Series([j.get_text() for i in soup.find_all(class_="category-name") for j in i.children if str(type(j))=="<class 'bs4.element.Tag'>" and str(j).split(">")[0]=='<span'])
        medicines = []
        for i in soup.find_all(class_="category-name"):
            for j in i.children:
                if str(type(j))=="<class 'bs4.element.Tag'>" and str(j).split(">")[0]=='<small':
                    try:
                        medicines.append(j.get_text()[re.search("MK-....", j.get_text()).start():re.search("MK-....", j.get_text()).end()])
                    except:
                        medicines.append("Not Found")
        # extracting phases from  page
        dataset["Compound_Name"] = pd.Series(medicines)

        phases = [i.get_text().strip().split()[0]+" "+i.get_text().strip().split()[1] for i in soup.find_all(class_="fadeInUp") if i.attrs["class"][1]=="fadeInUp"]
        counts = [int(i.get_text().strip().split()[2]) for i in soup.find_all(class_="fadeInUp") if i.attrs["class"][1]=="fadeInUp"]

        phase_list = []
        for i in range(len(phases)):
            phase_list += [phases[i],]*counts[i]
        # adding compound name to the dataframe
        dataset["Phase"] = phase_list
        dataset['Product_Name'] = np.where((dataset.Compound_Name == "MK-7902"), "LENVIMA", 
        np.where((dataset.Compound_Name == "MK-7119"), "TUKYSA",
        np.where((dataset.Compound_Name == "MK-6440"), "ladiratuzumab vedotin",
        np.where((dataset.Compound_Name == "MK-7339"), "LYNPARZA",
        np.where((dataset.Compound_Name == "MK-1308A"),"quavonlimab+ pembrolizumab",
        np.where((dataset.Compound_Name == "MK-3475"), "KEYTRUDA",
        np.where((dataset.Compound_Name == "MK-6482"), "RCC",
        "unnamed")))))))
        dataset = dataset[dataset.Colors=='blue']
        dataset
        new_df = dataset.reindex(columns =['Product_Name','Compound_Name','Indication','Phase'])
        new_df = new_df[new_df["Indication"].isin(["Non-small cell lung cancer","small cell lung cancer","Breast cancer"])]

        return new_df
    
    
    def medicineToStudyId(med_name):
        """
        This function returns study ID from merck website, uses selenium to search through the compound name and returns the study ID
        Input : str, med_name
        Returns : series of study IDs


        :return:
        """

        ## opening web driver to scrape study IDs
        driver = webdriver.Chrome(ChromeDriverManager().install())
        if med_name!="Not Found":
       #     driver = webdriver.Chrome()
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get("https://www.merckclinicaltrials.com/")
            input1 = driver.find_element_by_xpath('//*[@id="HeaderContent_ucFindAStudy_txtKeyword"]')
            input1.send_keys(med_name)
            input1.send_keys(Keys.ENTER)
            time.sleep(2)

            #search-results
            ret = [j.split(":")[-1].strip() for i in driver.find_elements_by_class_name("search-results") for j in i.text.split("\n") if "Study ID: " in j]
            driver.close()
            return ret
        else:
            return ["",]
