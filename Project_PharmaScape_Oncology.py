import pandas as pd
#import merck
#import Pfizer
#import Amgen
import Clinical_Trials
import Tweet_Scrap
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
from tabulate import tabulate


indication = 0
company = 0
company_information = 0
clinicaltrial_information = 0
clinicaltrial_sponsor = 0
NCTID=''
clinicaltrial_plot = 0
no_of_years = 0
#Pfizer.Pfizer.Pfizer_indication_all()
#merck_data=merck.merck.scrap("https://www.merck.com/research-and-products/product-pipeline/")
#merck_data["studyID"] = pd.Series(merck_data["Compound_Name"].apply(merck.merck.medicineToStudyId))
#merck_data.to_csv("merck.csv",index=False)
#drugList = amgen.amgen.extract_druglist()
#finalDrugList= amgen.amgen.finalDrugList(drugList)
#oncologyDrugList = amgen.amgen.oncologyDrugList(finalDrugList)
#breastCancerList= amgen.amgen.breastCancerList(oncologyDrugList)
#lungCancerList=amgen.amgen.lungCancerList(oncologyDrugList)
#final=amgen.amgen.finalLungCancerList(lungCancerList)

print ("Welcome to Pharmscape Oncology News Feed \n\
We provide the latest information on Pharma and clinical trials\n\
What's more: The latest tweets in US healthcare")

value_bad = True

while value_bad:

    try:

        user_input = input("Please select your indication to continue\n\
 1: Breast Cancer\n 2: Lung Cancer\n")

        indication = int(user_input)

    except:

        print("Bad value format")

        indication=0

    if indication<1 or indication >2:

        print("Enter value as 1 or 2")

    else:

        value_bad = False



value_bad2 = True

while value_bad2:

    try:

        user_input2 = input("Please select your company of interest\n\
 1: Pfizer\n 2: Merck\n 3: Amgen\n 4: General Clinical Trials\n")

        company = int(user_input2)

    except:

        print("Bad value format")

        company=0

    if company<1 or company>4:

        print("Enter value between 1 and 4")

    else:

        value_bad2 = False
        


if company==1 or company==2 or company==3:
    value_bad3 = True
        
    while value_bad3:
    
        try:
    
            user_input3 = input("What would you like to know\n\
 1: New products in pipeline\n 2: Existing products in market\n 3: Full product portfolio\n 4: Recent tweets posted\n")
    
            company_information = int(user_input3)
    
        except:
    
            print("Bad value format")
    
            company_information=0
    
        if company_information<1 or company_information>4:
    
            print("Enter value between 1 and 4")
    
        else:
    
            value_bad3 = False

    if indication==1 and company==1 and company_information==1:
        read_dF = pd.read_csv('Pfizer_Breast.csv', index_col=0)

        Pfizer_Breast_new_products = read_dF[read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2')| read_dF['Phase'].str.contains('Registration')]
        if Pfizer_Breast_new_products.empty:
            print("Pfizer has no new products in pipeline")
        else:
            print(tabulate(Pfizer_Breast_new_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==1 and company_information==2:
        read_dF = pd.read_csv('Pfizer_Breast.csv', index_col=0)

        Pfizer_Breast_existing_products = read_dF[read_dF['Phase'].str.contains('3')]
        if Pfizer_Breast_existing_products.empty:
            print("Pfizer has no current products in market")
        else:
            print(tabulate(Pfizer_Breast_existing_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==1 and company_information==3:

        read_dF = pd.read_csv('Pfizer_Breast.csv', index_col=0)
        if read_dF.empty:
            print("Pfizer has no new OR existing products for Breast Cancer.")
        else:
            print(tabulate(read_dF, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==1 and company_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Pfizer Breast Cancer"), headers = 'keys', tablefmt = 'psql'))
    
    elif indication==1 and company==2 and company_information==1:
        read_dF = pd.read_csv('merck.csv', index_col=0)
        merck_Breast_new_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('breast')) ]
        if merck_Breast_new_products.empty:
            print("Merck has no new products in pipeline")
        else:
            print(tabulate(merck_Breast_new_products, headers = 'keys', tablefmt = 'psql'))


    elif indication==1 and company==2 and company_information==2:
        read_dF = pd.read_csv('merck.csv', index_col=0)

        merck_Breast_existing_products = read_dF[(read_dF['Phase'].str.contains('3')) & (read_dF['Indication'].str.contains('breast'))]
        if merck_Breast_existing_products.empty:
            print("merck has no current products in market")
        else:
            print(tabulate(merck_Breast_existing_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==2 and company_information==3:
        read_dF = pd.read_csv('merck.csv', index_col=0)
        merck_breast_all_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                '3') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('breast')) ]
        if merck_breast_all_products.empty:
                print("merck has no current or new products for breast cancer")
        else:
            print(tabulate(merck_breast_all_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==2 and company_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Merck Breast Cancer"), headers = 'keys', tablefmt = 'psql'))
        
    elif indication==1 and company==3 and company_information==1:
        read_dF = pd.read_csv('amgen.csv', index_col=0)
        amgen_Breast_new_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('breast')) ]
        if amgen_Breast_new_products.empty:
                print("amgen has no new products in pipeline")
        else:
            print(tabulate(amgen_Breast_new_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==3 and company_information==2:
        read_dF = pd.read_csv('amgen.csv', index_col=0)

        amgen_Breast_existing_products = read_dF[
            (read_dF['Phase'].str.contains('3')) & (read_dF['Indication'].str.contains('breast'))]
        if amgen_Breast_existing_products.empty:
            print("amgen has no current products in market")
        else:
            print(tabulate(amgen_Breast_existing_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==3 and company_information==3:
        read_dF = pd.read_csv('amgen.csv', index_col=0)
        amgen_breast_all_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                '3') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('breast') )]
        if amgen_breast_all_products.empty:
            print("amgen has no current or new products for breast cancer")
        else:
            print(tabulate(amgen_breast_all_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==1 and company==3 and company_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Amgen Breast Cancer"), headers = 'keys', tablefmt = 'psql'))
    
    elif indication==2 and company==1 and company_information==1:

        read_dF = pd.read_csv('Pfizer_Lung.csv', index_col=0)
        Pfizer_lung_new_products = read_dF[read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2')| read_dF['Phase'].str.contains('Registration')]

        if Pfizer_lung_new_products.empty:
            print("Pfizer has no new products in pipeline")
        else:
            print(tabulate(Pfizer_lung_new_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==1 and company_information==2:
        read_dF = pd.read_csv('Pfizer_Lung.csv', index_col=0)
        Pfizer_lung_existing_products = read_dF[read_dF['Phase'].str.contains('3')]

        if Pfizer_lung_existing_products.empty:
            print("Pfizer has no current products in market")
        else:
            print(tabulate(Pfizer_lung_existing_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==1 and company_information==3:
        read_dF = pd.read_csv('Pfizer_Lung.csv', index_col=0)
        if read_dF.empty:
            print("Pfizer has no new OR existing products for Lung Cancer.")
        else:
            print(tabulate(read_dF, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==1 and company_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Pfizer Lung Cancer"), headers = 'keys', tablefmt = 'psql'))
    
    elif indication==2 and company==2 and company_information==1:
        ## merck new prod
        read_dF = pd.read_csv('merck.csv', index_col=0)
        merck_lung_new_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('lung')) ]
        if merck_lung_new_products.empty:
            print("Merck has no new products in pipeline")
        else:
            print(tabulate(merck_lung_new_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==2 and company_information==2:
        read_dF = pd.read_csv('merck.csv', index_col=0)
        merck_lung_existing_products = read_dF[
            (read_dF['Phase'].str.contains('3')) & (read_dF['Indication'].str.contains('lung'))]
        if merck_lung_existing_products.empty:
            print("merck has no current products in market")
        else:
            print(tabulate(merck_lung_existing_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==2 and company_information==3:
        read_dF = pd.read_csv('merck.csv', index_col=0)
        merck_lung_all_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains('3') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('lung')) ]
        if merck_lung_all_products.empty:
            print("merck has no current or new products for lung cancer")
        else:
            print(tabulate(merck_lung_all_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==2 and company_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Merck Lung Cancer"), headers = 'keys', tablefmt = 'psql'))
        
    elif indication==2 and company==3 and company_information==1:
        read_dF = pd.read_csv('amgen.csv', index_col=0)
        amgen_lung_new_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('lung')) ]
        if amgen_lung_new_products.empty:
            print("Amgen has no new products in pipeline")
        else:
            print(tabulate(merck_lung_new_products, headers = 'keys', tablefmt = 'psql'))


    elif indication==2 and company==3 and company_information==2:
        read_dF = pd.read_csv('amgen.csv', index_col=0)
        amgen_lung_existing_products = read_dF[
            (read_dF['Phase'].str.contains('3')) & (read_dF['Indication'].str.contains('lung'))]
        if amgen_lung_existing_products.empty:
            print("amgen has no current products in market")
        else:
            print(tabulate(amgen_lung_existing_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==3 and company_information==3:
        read_dF = pd.read_csv('amgen.csv', index_col=0)
        amgen_lung_all_products = read_dF[
            (read_dF['Phase'].str.contains('1') | read_dF['Phase'].str.contains('2') | read_dF['Phase'].str.contains(
                '3') | read_dF['Phase'].str.contains(
                'Registration')) & (read_dF['Indication'].str.contains('lung')) ]
        if amgen_lung_all_products.empty:
            print("amgen has no current or new products for lung cancer")
        else:
            print(tabulate(amgen_lung_all_products, headers = 'keys', tablefmt = 'psql'))

    elif indication==2 and company==3 and company_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Amgen Lung Cancer"), headers = 'keys', tablefmt = 'psql'))

elif company==4:
    value_bad4 = True
        
    while value_bad4:
    
        try:
    
            user_input4 = input("What would you like to know\n\
 1: show active trials in 2021\n 2: show active trials for specific sponsor\n 3: Search trial by NCT ID\n 4: Recent tweets posted\n 5: Trials over the years (interactive plots)\n")
    
            clinicaltrial_information = int(user_input4)
    
        except:
    
            print("Bad value format")
    
            clinicaltrial_information=0
    
        if clinicaltrial_information<1 or clinicaltrial_information>5:
    
            print("Enter value between 1 and 5")
    
        else:
    
            value_bad4 = False
    
    if indication==1 and clinicaltrial_information==1:
        print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Breast_All(), headers = 'keys', tablefmt = 'psql'))
    elif indication==1 and clinicaltrial_information==2:
        value_bad5 = True
        
        while value_bad5:
        
            try:
        
                user_input5 = input("Please select sponsor\n\
 1: Pfizer\n 2: Merck\n 3: Amgen\n")
        
                clinicaltrial_sponsor = int(user_input5)
        
            except:
        
                print("Bad value format")
        
                clinicaltrial_sponsor=0
        
            if clinicaltrial_sponsor<1 or clinicaltrial_information>3:
        
                print("Enter value between 1 and 3")
        
            else:
        
                value_bad5 = False
        
        if clinicaltrial_sponsor==1:
            print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Breast_CustomSearch("Pfizer"), headers = 'keys', tablefmt = 'psql'))
        elif clinicaltrial_sponsor==2:
            print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Breast_CustomSearch("Merck"), headers = 'keys', tablefmt = 'psql'))
        elif clinicaltrial_sponsor==3:
            print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Breast_CustomSearch("Amgen"), headers = 'keys', tablefmt = 'psql'))
            
    elif indication==1 and clinicaltrial_information==3:
        NCTID = input("Please enter NCT ID\n")
        print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_byNCT(NCTID), headers = 'keys', tablefmt = 'psql'))
    elif indication==1 and clinicaltrial_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Clinical Trials Breast Cancer"), headers = 'keys', tablefmt = 'psql'))
    elif indication==1 and clinicaltrial_information==5:
        value_bad6 = True
        
        while value_bad6:
        
            try:
        
                user_input6 = input("Please select preferred plot\n\
 1: Indication Trials over Past X years\n 2: Trials for indication by Sponsor over Past X Years\n")
        
                clinicaltrial_plot = int(user_input6)
        
            except:
        
                print("Bad value format")
        
                clinicaltrial_plot=0
        
            if clinicaltrial_plot<1 or clinicaltrial_plot>2:
        
                print("Enter value 1 or 2")
        
            else:
        
                value_bad6 = False
        
        value_bad7 = True
        
        while value_bad7:
        
            try:
        
                user_input7 = input("Please select no. of years (Max of 10 years) (example: 5 years indicates 2017 - 2021)\n")
        
                no_of_years = int(user_input7)
        
            except:
        
                print("Bad value format")
        
                no_of_years=0
        
            if no_of_years<1 or no_of_years>10:
        
                print("Enter value between 1 and 10")
        
            else:
        
                value_bad7 = False
        if clinicaltrial_plot==1:
            Clinical_Trials.Clinical_Trials.clinicalTrials_Breast_Graphing(no_of_years)
        elif clinicaltrial_plot==2:
            Clinical_Trials.Clinical_Trials.clinicalTrials_Breast_Graphing_Sponsor(no_of_years)

    if indication==2 and clinicaltrial_information==1:
        print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Lung_All(), headers = 'keys', tablefmt = 'psql'))
    elif indication==2 and clinicaltrial_information==2:
        value_bad8 = True
        
        while value_bad8:
        
            try:
        
                user_input8 = input("Please select sponsor\n\
 1: Pfizer\n 2: Merck\n 3: Amgen\n")
        
                clinicaltrial_sponsor = int(user_input8)
        
            except:
        
                print("Bad value format")
        
                clinicaltrial_sponsor=0
        
            if clinicaltrial_sponsor<1 or clinicaltrial_information>3:
        
                print("Enter value between 1 and 3")
        
            else:
        
                value_bad8 = False
        
        if clinicaltrial_sponsor==1:
            print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Lung_CustomSearch("Pfizer"), headers = 'keys', tablefmt = 'psql'))
        elif clinicaltrial_sponsor==2:
            print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Lung_CustomSearch("Merck"), headers = 'keys', tablefmt = 'psql'))
        elif clinicaltrial_sponsor==3:
            print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_Lung_CustomSearch("Amgen"), headers = 'keys', tablefmt = 'psql'))
            
    elif indication==2 and clinicaltrial_information==3:
        NCTID = input("Please enter NCT ID")
        print(tabulate(Clinical_Trials.Clinical_Trials.clinicalTrials_byNCT(NCTID), headers = 'keys', tablefmt = 'psql'))
    elif indication==2 and clinicaltrial_information==4:
        print(tabulate(Tweet_Scrap.pharma_tweets.get_tweets_cancer("Clinical Trials Lung Cancer"), headers = 'keys', tablefmt = 'psql'))
    elif indication==2 and clinicaltrial_information==5:
        value_bad9 = True
        
        while value_bad9:
        
            try:
        
                user_input9 = input("Please select preferred plot\n\
 1: Indication Trials over Past X years\n 2: Trials for indication by Sponsor over Past X Years\n")
        
                clinicaltrial_plot = int(user_input9)
        
            except:
        
                print("Bad value format")
        
                clinicaltrial_plot=0
        
            if clinicaltrial_plot<1 or clinicaltrial_plot>2:
        
                print("Enter value 1 or 2")
        
            else:
        
                value_bad9 = False
        
        value_bad10 = True
        
        while value_bad10:
        
            try:
        
                user_input10 = input("Please select no. of years (Max of 10 years) (example: 5 years indicates 2017 - 2021)\n")
        
                no_of_years = int(user_input10)
        
            except:
        
                print("Bad value format")
        
                no_of_years=0
        
            if no_of_years<1 or no_of_years>10:
        
                print("Enter value between 1 and 10")
        
            else:
        
                value_bad10 = False
        if clinicaltrial_plot==1:
            Clinical_Trials.Clinical_Trials.clinicalTrials_Lung_Graphing(no_of_years)
        elif clinicaltrial_plot==2:
            Clinical_Trials.Clinical_Trials.clinicalTrials_Lung_Graphing_Sponsor(no_of_years)
        
        






