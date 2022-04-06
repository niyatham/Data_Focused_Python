
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

class Pfizer:
    def Pfizer_indication_all():

        from bs4 import BeautifulSoup as bs
        import pandas as pd
        import requests
        ##define the URL of the site to be scrapped
        url = 'https://www.pfizer.com/science/oncology-cancer/pipeline'
        ##get the html
        page = requests.get(url)

        soup = bs(page.text,'lxml')
        ##find table in the html body
        table_body = soup.find('table')
        
        row_data =[]
        #get data from each row and append it to row_data list
        for row in table_body.find_all('tr'):
            list_of_td = row.find_all('td') 
            trim_txt = [td.text.strip() for td in list_of_td]
            row_data.append(trim_txt)
        
        #get headers
        header = []
        for i in soup.find_all("th"):
            col_name = i.text.strip().lower().replace(" ","_")
            header.append(col_name)
        #create dataframe    
        df = pd.DataFrame(row_data, columns = header)
        
        #Create a list of links and attach it to the dataframe. If no link is found, append the text 'No Link'
        link_list =[]
        for row in table_body.find_all('tr'):
            found = True
            row_data = []
            for td in row.find_all('td'):
                td_check = td.find('a')
                if td_check is not None:
                    found = False
                    link = td.a['href']
                    link_list.append(link)
                
            if(found):
                link_list.append('No Link') 
        
        # from the list of links, extract the NCT IDs and insert the NCT list into dataframe
        NCT_list = []
        for every_link in link_list:
            try:
                left_cut = every_link.index('NCT')
                right_cut = every_link.index('?')
                NCT_ID = every_link[left_cut:right_cut]
                NCT_list.append(NCT_ID)
            except:
                NCT_ID = ''
                NCT_list.append(NCT_ID)
        df.insert(3,"NCT",NCT_list)
        
        #drop the first row
        df.drop(index=df.index[0],axis=0,inplace=True)
        
        # Extract drug name from column 1 and attach it to the data frame.
        drug_name_list = []
        for i in range(0,len(df)):
            right_cut = df.iloc[i,0].index('Therapeutic')
            drug_name = df.iloc[i,0][:right_cut]
            drug_name_list.append(drug_name)
            
        df.insert(1,"drug_name",drug_name_list)
        
        
        # Extract mechanism of action from column 1 and attach it to the data frame.
            
        moa_name_list = []
        for i in range(0,len(df)):
            left_cut = df.iloc[i,0].index('Mechanism of Action:') + 20
            try:
                right_cut = df.iloc[i,0].index('Go to clinical trial')
            except:
                right_cut = len(df.iloc[i,0])
                
            
            moa_desc = df.iloc[i,0][left_cut:right_cut]
            moa_name_list.append(moa_desc)
            
        df.insert(2,"Mechanism of Action",moa_name_list)
        
        filtered_dataframe_breast = df[df['indication'].str.contains('Breast',na = False)]
        
        filtered_dataframe_lung = df[df['indication'].str.contains('Lung',na = False)]
        
        # extract compound_name and product_name as lists for lungs
        # insert the lists into filtered_dataframe_lung
        compound_name_list = []
        for i in range(0,len(filtered_dataframe_lung)):
            element = filtered_dataframe_lung.iloc[i,1]
            try:
                left_cut_first_part = element.index('(')+1
                right_cut_first_part = element.index(')')
                try:
                    check_plus = element.index('+')
                except:
                    check_plus = 0
                    compound_name_list.append(element[left_cut_first_part:right_cut_first_part])
                if(check_plus>0):
                    left_cut_second_part =  element.index('(',right_cut_first_part) +1
                    right_cut_second_part =  element.index(')',left_cut_second_part)
                    z = element[left_cut_first_part:right_cut_first_part] + " and " + element[left_cut_second_part:right_cut_second_part]
                    compound_name_list.append(z)
                
            except:
                compound_name_list.append("")

        drug_name_list = []
        for i in range(0,len(filtered_dataframe_lung)):
            element = filtered_dataframe_lung.iloc[i,1]
            try:
                left_cut_first_part = 0
                right_cut_first_part = element.index('(')
                try:
                    check_plus = element.index('+')
                except:
                    check_plus = 0
                    drug_name_list.append(element[left_cut_first_part:right_cut_first_part])
                if(check_plus>0):
                    left_cut_second_part =  check_plus+1
                    right_cut_second_part =  element.index('(',left_cut_second_part) 
                    z = element[left_cut_first_part:right_cut_first_part] + " and " + element[left_cut_second_part:right_cut_second_part]
                    drug_name_list.append(z)
                
            except:
                drug_name_list.append("element")
                
        
        filtered_dataframe_lung.insert(2,"Product_Name",drug_name_list)
        filtered_dataframe_lung.insert(3,"Compound_Name",compound_name_list)
        
        
        # extract compound_name and product_name as lists for breast
        # insert the lists into filtered_dataframe_breast
        compound_name_list = []
        for i in range(0,len(filtered_dataframe_breast)):
            element = filtered_dataframe_breast.iloc[i,1]
            try:
                left_cut_first_part = element.index('(')+1
                right_cut_first_part = element.index(')')
                try:
                    check_plus = element.index('+')
                except:
                    check_plus = 0
                    compound_name_list.append(element[left_cut_first_part:right_cut_first_part])
                if(check_plus>0):
                    left_cut_second_part =  element.index('(',right_cut_first_part) +1
                    right_cut_second_part =  element.index(')',left_cut_second_part)
                    z = element[left_cut_first_part:right_cut_first_part] + " and " + element[left_cut_second_part:right_cut_second_part]
                    compound_name_list.append(z)
                
            except:
                compound_name_list.append("")
                
        drug_name_list = []
        for i in range(0,len(filtered_dataframe_breast)):
            element = filtered_dataframe_breast.iloc[i,1]
            try:
                left_cut_first_part = 0
                right_cut_first_part = element.index('(')
                try:
                    check_plus = element.index('+')
                except:
                    check_plus = 0
                    drug_name_list.append(element[left_cut_first_part:right_cut_first_part])
                if(check_plus>0):
                    left_cut_second_part =  check_plus+1
                    right_cut_second_part =  element.index('(',left_cut_second_part) 
                    z = element[left_cut_first_part:right_cut_first_part] + " and " + element[left_cut_second_part:right_cut_second_part]
                    drug_name_list.append(z)
                
            except:
                drug_name_list.append(element)
                
        #insert the product name and coumpound name list into dataframe
        filtered_dataframe_breast.insert(2,"Product_Name",drug_name_list)
        filtered_dataframe_breast.insert(3,"Compound_Name",compound_name_list)
        
        #renaming the columns as per project requirement
        filtered_dataframe_lung = filtered_dataframe_lung.rename(columns={'phase':'Phase','indication':'Indication'})
        filtered_dataframe_breast = filtered_dataframe_breast.rename(columns={'phase':'Phase','indication':'Indication'})
        #make the final dataframe to be written out as csv
        filtered_dataframe_lung_final = filtered_dataframe_lung[['Product_Name','Compound_Name','Indication','Phase','Mechanism of Action','NCT']]
        filtered_dataframe_breast_final = filtered_dataframe_breast[['Product_Name','Compound_Name','Indication','Phase','Mechanism of Action','NCT']]
       # write out dataframes to csv
        filtered_dataframe_breast_final.to_csv("Pfizer_Breast.csv",index = False)
        filtered_dataframe_lung_final.to_csv("Pfizer_Lung.csv",index = False)
