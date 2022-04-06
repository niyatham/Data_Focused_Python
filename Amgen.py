import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class amgen:
    def _init_(self,dataset):
        self.dataset = dataset
        
    #Scraping the amgen pipeline website and creating a list of the drugs amgen is working on
    def extract_druglist():
        driver  = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://www.amgenpipeline.com/')
        drug_list=[]
        for i in range(1,40):
            drugs = driver.find_elements_by_xpath('/html/body/div[7]/div/div[2]/div[2]/div['+str(i)+']')
            for j in range(len(drugs)):
                drug_list.append(drugs[j].text)

        drugList = [i.split("\n") for i in drug_list]
        driver.quit()

        return drugList

    #curating the final drug list and getting the data ready for filtering. This method performs osme modifications and formatting the list
    #to create a uniform list to be sent ot the dataframe as the scraped data has some uneven entities 
    def finalDrugList(drug_List):
        finalDrugList = []
        row = []
        for drug in drug_List:
            if(drug[0]=="TEZEPELUMAB"):
                continue

            #performing row modifications to get the data in a linear fashion
            if(len(drug) <6):
                row.append(drug[0])
                row.append(" ")
                row.append(drug[1])
                row.append(drug[2])
                row.append(drug[3])
                row.append(drug[4])
                finalDrugList.append(row)
                row = []

            elif(len(drug)==6):
                finalDrugList.append(drug)
            else:
                finalDrugList.append(drug[0:6])
                a = len(drug) - 6
                n = a/4
                p = 6
                while n>0:
                    row.append(drug[0])
                    if(str(drug[1]).startswith("(")):
                        row.append(drug[1])
                    else:
                        row.append(" ")
                    row.append(drug[p])
                    row.append(drug[p+1])
                    row.append(drug[p+2])
                    row.append(drug[p+3])
                    n = n-1
                    finalDrugList.append(row)
                    row = []
                    p=p+4
                p=7
        return finalDrugList

    #filtering data for oncology for this project
    def oncologyDrugList(final_Drug_List):
        oncologyDrugList =[]
        for item in final_Drug_List:
            if(item[2]==("Hematology / Oncology" or "Oncology")):
                oncologyDrugList.append(item)
        return oncologyDrugList


    #filtering data to get breast cancer related records
    def breastCancerList(oncology_drug_list):
        breastCancerList =[]
        for item in oncology_drug_list:
            if(item[3].find("Breast") > -1):
                breastCancerList.append(item)
        return breastCancerList
    
    
    #filtering data to get lung cancer related records
    def lungCancerList(oncology_drug_list):
        lungCancerList =[]
        for item in oncology_drug_list:
            if(item[3].find("Lung") > -1):
                lungCancerList.append(item)
        return lungCancerList
        
        

    #filtering data to get breast cancer related records and curating a dataframe
    def finalLungCancerList(lungCancerList):
        finalLungCancerList =[]
        rows =[]
         #performing row modifications to get the data in a linear fashion
        for item in lungCancerList:
            rows.append(item[0])
            rows.append(item[1].strip("()"))
            rows.append(item[3])
            rows.append("Phase "+item[5])
            rows.append(item[4])
            finalLungCancerList.append(rows)
            rows=[]
        df = pd.DataFrame(finalLungCancerList, columns=["Product Name", "Compound Name", "Indication", "Phase", "Mechanism of Action"])  
        return df




