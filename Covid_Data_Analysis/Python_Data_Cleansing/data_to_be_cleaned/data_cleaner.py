# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:10:32 2022

@author: Lukasz
"""

import pandas as pd
import math

vaccinations_data = pd.read_csv('vaccination_data.txt')
print(vaccinations_data)
print(vaccinations_data.count())

cases_data = pd.read_csv('cases_data.txt')
print(cases_data)
print(cases_data.count())

mortality_data = pd.read_csv('mortality_data.txt')
print(mortality_data)
print(mortality_data.count())

tests_performed_data = pd.read_csv('tests_performed_data.txt')
print(tests_performed_data)
print(tests_performed_data.count())

hospitalization_data = pd.read_csv('hospitalization_data.txt')
print(hospitalization_data)
print(hospitalization_data.count())

def cases_data_cleaning():
    old_country = ''
    
    cases_data.dropna(subset=['continent'], inplace=True)
    cases_data.reset_index(drop=True, inplace=True)
   
    for i in range(len(cases_data)):   
        country = cases_data['location'][i]
        
        if country != old_country:
            old_country = cases_data['location'][i]
            indexNum = i
            
            while math.isnan(cases_data['new_cases'][indexNum]) and math.isnan(cases_data['new_cases_per_million'][indexNum]):
                cases_data['new_cases'].iloc[indexNum] = 0
                cases_data['new_cases_per_million'].iloc[indexNum] = 0
                indexNum += 1
                
    cases_data.dropna(subset=['new_cases', 'new_cases_per_million'], how='all', inplace = True)
    
    cases_data.drop(cases_data.loc[cases_data['iso_code'].str.startswith('OWID')].index, inplace=True)
    
    cases_data.to_csv('cleaned_data/cases_data_cleaned.csv', index=False)
          

def mortality_data_cleaning():
    old_country = ''
    mortality_data.dropna(subset=['continent'], inplace=True)
    mortality_data.reset_index(drop=True, inplace=True)
      
    for i in range(len(mortality_data)):      
        country = mortality_data['location'][i]
        
        if country != old_country:
            old_country = mortality_data['location'][i]
            indexNum = i
            while math.isnan(mortality_data['total_deaths'][indexNum]) and math.isnan(mortality_data['total_deaths_per_million'][indexNum]) and math.isnan(mortality_data['new_deaths'][indexNum]) and math.isnan(mortality_data['new_deaths_per_million'][indexNum]):
                mortality_data['total_deaths'].iloc[indexNum] = 0
                mortality_data['total_deaths_per_million'].iloc[indexNum] = 0
                mortality_data['new_deaths'].iloc[indexNum] = 0
                mortality_data['new_deaths_per_million'].iloc[indexNum] = 0
                indexNum += 1
                
            while math.isnan(mortality_data['total_deaths'][indexNum]) and not math.isnan(mortality_data['total_deaths_per_million'][indexNum]):
                mortality_data['total_deaths'][indexNum] = mortality_data['total_deaths_per_million'][indexNum]
                
            while math.isnan(mortality_data['total_deaths_per_million'][indexNum]) and not math.isnan(mortality_data['total_deaths'][indexNum]):
                mortality_data['total_deaths_per_million'][indexNum] = mortality_data['total_deaths'][indexNum]

            while math.isnan(mortality_data['new_deaths'][indexNum]) and not math.isnan(mortality_data['new_deaths_per_million'][indexNum]):
                mortality_data['new_deaths'][indexNum] = mortality_data['new_deaths_per_million'][indexNum]
                
            while math.isnan(mortality_data['new_deaths_per_million'][indexNum]) and not math.isnan(mortality_data['new_deaths'][indexNum]):
                mortality_data['new_deaths_per_million'][indexNum] = mortality_data['new_deaths'][indexNum]                          
                
    mortality_data.dropna(subset=['total_deaths', 'total_deaths_per_million','new_deaths','new_deaths_per_million'], how='any', inplace = True)
    
    mortality_data.drop(mortality_data.loc[mortality_data['iso_code'].str.startswith('OWID')].index, inplace=True)
    
    mortality_data.to_csv('cleaned_data/mortality_data_cleaned.csv', index=False)
    

def tests_performed_data_cleaning():
    old_country = ''
    tests_performed_data.dropna(subset=['continent'], inplace=True)
    tests_performed_data.reset_index(drop=True, inplace=True)
      
    for i in range(len(tests_performed_data)):      
        country = tests_performed_data['location'][i]
        
        if country != old_country:
            old_country = tests_performed_data['location'][i]
            indexNum = i
            while math.isnan(tests_performed_data['new_tests'][indexNum]) and math.isnan(tests_performed_data['new_tests_per_thousand'][indexNum]):
                tests_performed_data['new_tests'].iloc[indexNum] = 0
                tests_performed_data['new_tests_per_thousand'].iloc[indexNum] = 0
                indexNum += 1
                
    tests_performed_data.dropna(subset=['new_tests', 'new_tests_per_thousand'], how='all', inplace = True)
    
    tests_performed_data.drop(tests_performed_data.loc[tests_performed_data['iso_code'].str.startswith('OWID')].index, inplace=True)
    
    tests_performed_data.to_csv('cleaned_data/tests_performed_data_cleaned.csv', index=False)
    
def hospitalization_data_cleaning():   
    hospitalization_data.dropna(subset=['continent'], inplace=True)
    hospitalization_data.reset_index(drop=True, inplace=True)
    hospitalization_data.drop(hospitalization_data.loc[hospitalization_data['iso_code'].str.startswith('OWID')].index, inplace=True)
    hospitalization_data.dropna(subset=['icu_patients','icu_patients_per_million','hosp_patients','hosp_patients_per_million'], 
                                how='any', inplace = True)
    hospitalization_data.to_csv('cleaned_data/hospitalization_data_cleaned.csv', index=False)


def vaccinations_data_cleaning():
    old_country = ''
      
    for i in range(len(vaccinations_data)):      
        country = vaccinations_data['country'][i]
        
        if country != old_country:
            old_country = vaccinations_data['country'][i]
            
            indexNum = i          
            first_rows_filling('people_fully_vaccinated_per_hundred', indexNum)
            
            indexNum = i          
            first_rows_filling('total_vaccinations_per_hundred', indexNum)
            
            indexNum = i         
            first_rows_filling('people_vaccinated_per_hundred', indexNum)
            
            indexNum = i  
            first_rows_filling('sputnikv_total_vaccinations', indexNum)
            
            indexNum = i       
            first_rows_filling('sinovac_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('sinopharm_total_vaccinations', indexNum)
            
            indexNum = i   
            first_rows_filling('pfizer_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('astrazeneca_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('novavax_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('moderna_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('johnson&johnson_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('covaxin_total_vaccinations', indexNum)
            
            indexNum = i
            first_rows_filling('cansino_total_vaccinations', indexNum)
        
    '''
    people_fully_vaccinated_per_hundred = vaccinations_data['people_fully_vaccinated_per_hundred'][0]
    total_vaccinations_per_hundred = vaccinations_data['total_vaccinations_per_hundred'][0]
    people_vaccinated_per_hundred = vaccinations_data['people_vaccinated_per_hundred'][0]
    sputnikv_total_vaccinations = vaccinations_data['sputnikv_total_vaccinations'][0]
    sinovac_total_vaccinations = vaccinations_data['sinovac_total_vaccinations'][0]
    sinopharm_total_vaccinations = vaccinations_data['sinopharm_total_vaccinations'][0]
    pfizer_total_vaccinations = vaccinations_data['pfizer_total_vaccinations'][0]
    astrazeneca_total_vaccinations = vaccinations_data['astrazeneca_total_vaccinations'][0]
    novavax_total_vaccinations = vaccinations_data['novavax_total_vaccinations'][0]
    moderna_total_vaccinations = vaccinations_data['moderna_total_vaccinations'][0]
    johnsonjohnson_total_vaccinations = vaccinations_data['johnson&johnson_total_vaccinations'][0]
    covaxin_total_vaccinations = vaccinations_data['covaxin_total_vaccinations'][0]
    cansino_total_vaccinations = vaccinations_data['cansino_total_vaccinations'][0]'''
    
    for i in range(len(vaccinations_data)):     
        '''
        people_fully_vaccinated_per_hundred = remaining_empty_rows_filling('people_fully_vaccinated_per_hundred', i, people_fully_vaccinated_per_hundred)
        total_vaccinations_per_hundred = remaining_empty_rows_filling('total_vaccinations_per_hundred', i, total_vaccinations_per_hundred)
        people_vaccinated_per_hundred = remaining_empty_rows_filling('people_vaccinated_per_hundred', i, people_vaccinated_per_hundred) 
        sputnikv_total_vaccinations = remaining_empty_rows_filling('sputnikv_total_vaccinations', i, sputnikv_total_vaccinations)
        sinovac_total_vaccinations = remaining_empty_rows_filling('sinovac_total_vaccinations', i, sinovac_total_vaccinations)
        sinopharm_total_vaccinations = remaining_empty_rows_filling('sinopharm_total_vaccinations', i, sinopharm_total_vaccinations)
        pfizer_total_vaccinations = remaining_empty_rows_filling('pfizer_total_vaccinations', i, pfizer_total_vaccinations)
        astrazeneca_total_vaccinations = remaining_empty_rows_filling('astrazeneca_total_vaccinations', i, astrazeneca_total_vaccinations)
        novavax_total_vaccinations = remaining_empty_rows_filling('novavax_total_vaccinations', i, novavax_total_vaccinations)
        moderna_total_vaccinations = remaining_empty_rows_filling('moderna_total_vaccinations', i, moderna_total_vaccinations)
        johnsonjohnson_total_vaccinations = remaining_empty_rows_filling('johnson&johnson_total_vaccinations', i, johnsonjohnson_total_vaccinations)
        covaxin_total_vaccinations = remaining_empty_rows_filling('covaxin_total_vaccinations', i, covaxin_total_vaccinations)
        cansino_total_vaccinations = remaining_empty_rows_filling('cansino_total_vaccinations', i, cansino_total_vaccinations)'''
        
        remaining_empty_rows_filling('people_fully_vaccinated_per_hundred', i)
        remaining_empty_rows_filling('total_vaccinations_per_hundred', i)
        remaining_empty_rows_filling('people_vaccinated_per_hundred', i) 
        remaining_empty_rows_filling('sputnikv_total_vaccinations', i)
        remaining_empty_rows_filling('sinovac_total_vaccinations', i)
        remaining_empty_rows_filling('sinopharm_total_vaccinations', i)
        remaining_empty_rows_filling('pfizer_total_vaccinations', i)
        remaining_empty_rows_filling('astrazeneca_total_vaccinations', i)
        remaining_empty_rows_filling('novavax_total_vaccinations', i)
        remaining_empty_rows_filling('moderna_total_vaccinations', i)
        remaining_empty_rows_filling('johnson&johnson_total_vaccinations', i)
        remaining_empty_rows_filling('covaxin_total_vaccinations', i)
        remaining_empty_rows_filling('cansino_total_vaccinations', i)
        
    vaccinations_data.to_csv('cleaned_data/vaccinations_data_cleaned.csv', index=False)
    
        
def first_rows_filling(column_name, indexNum):
    while math.isnan(vaccinations_data[column_name][indexNum]):
        vaccinations_data[column_name].iloc[indexNum] = 0
        indexNum += 1
        if indexNum >= len(vaccinations_data):
            return


def remaining_empty_rows_filling(column_name, indexNum):       
    if math.isnan(vaccinations_data[column_name][indexNum]):
        vaccinations_data[column_name].iloc[indexNum] = vaccinations_data[column_name][indexNum - 1]
    else:
        return

    
cases_data_cleaning()  
mortality_data_cleaning()
tests_performed_data_cleaning()
hospitalization_data_cleaning()
vaccinations_data_cleaning()

print(cases_data.count())  
print(mortality_data.count())  
print(tests_performed_data.count()) 
print(hospitalization_data.count())
print(vaccinations_data.count())


        
