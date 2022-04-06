from pytrials.client import ClinicalTrials
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#This module pulls in clinical trial data from clinicaltrials.gov API
class Clinical_Trials:
    
    def clinicalTrials_Breast_All ():
#Get active breast cancer trials in 2021
        nfields=["NCTId", "Condition", "BriefTitle","LeadSponsorName","BriefSummary"]
        ct = ClinicalTrials()
        for i in range (1):

            output_fields = ct.get_study_fields(
                search_expr="breast cancer+active+2021",
                fields=nfields,
                max_studies=1000,   
                fmt="csv"
                )
    
        df = pd.DataFrame(output_fields)
        return(df)


    def clinicalTrials_Breast_CustomSearch (CustomSearch):
#Get active breast cancer trials for a specific keyword
        nfields=["NCTId", "Condition", "BriefTitle","LeadSponsorName","BriefSummary"]
        ct = ClinicalTrials()
        
        for i in range (1):

            output_fields = ct.get_study_fields(
                search_expr="breast cancer+active+"+CustomSearch,
                fields=nfields,
                max_studies=1000,   
                fmt="csv"
                )
    
        df = pd.DataFrame(output_fields)
        return(df)
        
        
    def clinicalTrials_Lung_All ():
#Get active breast cancer trials in 2021
        nfields=["NCTId", "Condition", "BriefTitle","LeadSponsorName","BriefSummary"]
        ct = ClinicalTrials()
        for i in range (1):

            output_fields = ct.get_study_fields(
                search_expr="lung cancer+active+2021",
                fields=nfields,
                max_studies=1000,   
                fmt="csv"
                )
    
        df = pd.DataFrame(output_fields)
        return(df)


    def clinicalTrials_Lung_CustomSearch (CustomSearch):
#Get active breast cancer trials for a specific keyword
        nfields=["NCTId", "Condition", "BriefTitle","LeadSponsorName","BriefSummary"]
        ct = ClinicalTrials()
        
        for i in range (1):

            output_fields = ct.get_study_fields(
                search_expr="lung cancer+active+"+CustomSearch,
                fields=nfields,
                max_studies=1000,   
                fmt="csv"
                )
    
        df = pd.DataFrame(output_fields)
        return(df)       

    def clinicalTrials_byNCT (NCTID):
#Get active breast cancer trials for a specific sponsor
        nfields=["NCTId", "Condition", "BriefTitle","LeadSponsorName","BriefSummary"]
        ct = ClinicalTrials()

        for i in range (1):

            output_fields = ct.get_study_fields(
                search_expr=NCTID,
                fields=nfields,
                max_studies=1000,   
                fmt="csv"
                )
    
        df = pd.DataFrame(output_fields)
        return(df) 
        
    def clinicalTrials_Breast_Graphing (no_of_years):
#Build interactive plots based on user input
        ct = ClinicalTrials()
        a = 2022-no_of_years
        x = []
        y = []
        
        for i in range (no_of_years):
            x.append(a)
            y.append(ct.get_study_count(search_expr="breast cancer+"+str(a)))
            a = a+1
 
        # creating the bar plot
        plt.bar(x, y, color ='pink',
                width = 0.5)
         
        plt.xlabel("Year")
        plt.ylabel("No. of breast cancer trials")
        plt.title("Clinical Trials over the Years")
        plt.show()
        
    def clinicalTrials_Lung_Graphing (no_of_years):
#Build interactive plots based on user input
        ct = ClinicalTrials()
        a = 2022-no_of_years
        x = []
        y = []
        
        for i in range (no_of_years):
            x.append(a)
            y.append(ct.get_study_count(search_expr="lung cancer+"+str(a)))
            a = a+1
 
        # creating the bar plot
        plt.bar(x, y, color ='blue',
                width = 0.5)
         
        plt.xlabel("Year")
        plt.ylabel("No. of lung cancer trials")
        plt.title("Clinical Trials over the Years")
        plt.show()
        
    def clinicalTrials_Breast_Graphing_Sponsor (no_of_years):
#Build interactive plots based on user input
        ct = ClinicalTrials()
        a = 2022-no_of_years
        x = []
        pfizer = []
        amgen = []
        merck = []
        
        for i in range (no_of_years):
            x.append(a)
            pfizer.append(ct.get_study_count(search_expr="breast cancer+pfizer+"+str(a)))
            amgen.append(ct.get_study_count(search_expr="breast cancer+amgen+"+str(a)))
            merck.append(ct.get_study_count(search_expr="breast cancer+merck+"+str(a)))
            a = a+1
        
        g = np.arange(no_of_years)
        width = 0.2
  
        # plot data in grouped manner of bar type
        plt.bar(g-0.2, pfizer, width, color='cyan')
        plt.bar(g, amgen, width, color='orange')
        plt.bar(g+0.2, merck, width, color='green')
        plt.xticks(g,x)
        plt.xlabel("Years")
        plt.ylabel("No. of Breast Cancer Trials")
        plt.legend(["Pfizer", "Amgen", "Merck"])
        plt.show()

    def clinicalTrials_Lung_Graphing_Sponsor (no_of_years):
#Build interactive plots based on user input
        ct = ClinicalTrials()
        a = 2022-no_of_years
        x = []
        pfizer = []
        amgen = []
        merck = []
        
        for i in range (no_of_years):
            x.append(a)
            pfizer.append(ct.get_study_count(search_expr="lung cancer+pfizer+"+str(a)))
            amgen.append(ct.get_study_count(search_expr="lung cancer+amgen+"+str(a)))
            merck.append(ct.get_study_count(search_expr="lung cancer+merck+"+str(a)))
            a = a+1
        
        g = np.arange(no_of_years)
        width = 0.2
  
        # plot data in grouped manner of bar type
        plt.bar(g-0.2, pfizer, width, color='cyan')
        plt.bar(g, amgen, width, color='orange')
        plt.bar(g+0.2, merck, width, color='green')
        plt.xticks(g,x)
        plt.xlabel("Years")
        plt.ylabel("No. of lung Cancer Trials")
        plt.legend(["Pfizer", "Amgen", "Merck"])
        plt.show()
      