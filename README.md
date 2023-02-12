# Data-Analysis
## Table of contents
* [Datasets](#datasets)
  * [Covid dataset](#CDS)
  * [Pokemon dataset](#PDS)
* [Business questions](#BQ)
* [ETL](#SSIS)
* [Analysis Services](#SSAS)
* [Data Visualization](#DS)
<a name="datasets"></a>
# Datasets
<a name="CDS"></a>
## Covid dataset
###  1. country_vaccinations.csv: 

country, iso_code, date, total_vaccinations, people_vaccinated, people_fully_vaccinated, daily_vaccinations_raw, daily_vaccinations, total_vaccinations_per_hundred, people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, daily_vaccinations_per_million, vaccines, source_name, source_website
 
###  2. country_vaccinations_by_manufacturer.csv:
location, date, vaccine, total_vaccinations

###  3. covid_19_clean_complete.csv:
Province/State, Country/Region, Lat, Long, Date, Confirmed, Deaths, Recovered, Active, WHO Region

###  4. cowid-covid-data-full.csv:
iso_code, continent, location, date, total_cases, new_cases, new_cases_smoothed, total_deaths, new_deaths, new_deaths_smoothed, total_cases_per_million, new_cases_per_million, new_cases_smoothed_per_million, total_deaths_per_million, new_deaths_per_million, new_deaths_smoothed_per_million, reproduction_rate, icu_patients, icu_patients_per_million, hosp_patients, hosp_patients_per_million, weekly_icu_admissions, weekly_icu_admissions_per_million, weekly_hosp_admissions, weekly_hosp_admissions_per_million, total_tests, new_tests, total_tests_per_thousand, new_tests_per_thousand, new_tests_smoothed, new_tests_smoothed_per_thousand, positive_rate, tests_per_case, tests_units, total_vaccinations, people_vaccinated, people_fully_vaccinated, total_boosters, new_vaccinations, new_vaccinations_smoothed, total_vaccinations_per_hundred, people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, total_boosters_per_hundred, new_vaccinations_smoothed_per_million, new_people_vaccinated_smoothed, new_people_vaccinated_smoothed_per_hundred, stringency_index, population_density, median_age, aged_65_older, aged_70_older, gdp_per_capita, extreme_poverty, cardiovasc_death_rate, diabetes_prevalence, female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy, human_development_index, population, excess_mortality_cumulative_absolute, excess_mortality_cumulative, excess_mortality, excess_mortality_cumulative_per_million

###  4. vaccinations-by-age-group.csv:
location, date, age_group, people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, people_with_booster_per_hundred
<a name="PDS"></a>
## Pokemon dataset
###  1. gen9_pokemon_abilities.csv: 
Ability, Pokemon, Game's Text, In-Depth Effect, Ability URL

###  2. gen9_pokemon_moves.csv: 
Move, Type, Category, Power Points, Base Power, Accuracy, Battle Effect, Secondary Effect, Secondary Rate, Critical Rate, Speed Priority, Attack URL, Pokemon

###  3. gen9_pokemon_stats.csv: 
Pokemon, Type 1, Type 2, HP, Attack, Defense, Special Attack, Special Defense, Speed, Weakness-Normal, Weakness-Fire, Weakness-Water, Weakness-Electric, Weakness-Grass, Weakness-Ice, Weakness-Fighting, Weakness-Poison, Weakness-Ground, Weakness-Flying, Weakness-Psychic, Weakness-Bug, Weakness-Rock, Weakness-Ghost, Weakness-Dragon, Weakness-Dark, Weakness-Steel, Weakness-Fairy

<a name="BQ"></a>
# Business questions
Business questions will help us select the appropriate data from data sets, design the ETL process. We can answer them with appropriate reports and visualizations using tools (Power BI Desktop) for Business Intelligence. 

#### Business questions for the covid dataset:
1. What is the incidence of covid for the 2nd quarter of 2020?
2. What is the incidence per million of covid for the 2nd quarter of 2020, for 5 countries with the highest covid incidence per million in the 2nd quarter of 2020?
3. What is the covid mortality for the 2nd quarter of 2020?
4. What is the covid mortality per million for the 2nd quarter of 2020, for 5 countries with the highest covid mortality per million in the 2nd quarter of 2020?
5. What is the number of covid tests for the 2nd quarter of 2020?
6. What is the number of covid tests per million for the 2nd quarter of 2020, for 5 countries which performed the highest number of covid tests per million in the 2nd quarter of 2020?
7. What is the number of patients hospitalized due to covid per million for the 2nd quarter of 2020, for 5 countries which have the highest number of patients hospitalized due to covid per million in the 2nd quarter of 2020?
8. What is the number of icu patients due to covid per million for the 2nd quarter of 2020, for 5 countries which have the highest number of icu patients due to covid per million in the 2nd quarter of 2020?
9. What is the correlation between covid vaccinations and incidence of covid for Argentina, for the first 9 months of 2021?
10. What is the correlation between incidence of covid and covid tests performed for Argentina, for the first 9 months of 2021?
11. What is the correlation between covid vaccinations and covid mortality for Argentina, for the first 9 months of 2021?
#### Business questions for the pokemon dataset:
1. What is the power points number for the 5 moves with the highest power points number? What are the categories of these moves?
2. What is the accuracy for the 5 moves with the highest accuracy? What are the categories of these moves?
3. What is the critical rate for the 5 moves with the highest critical rate? What are the categories of these moves?
4. What is the speed priority for the 5 moves with the highest speed priority? What are the types of these moves?
5. What is the base power for the 5 moves with the highest base power? What are the types of these moves?
6. What is the correlation between power points, critical rate and accuracy for the moves with the highest power points number, accuracy, critical rate, speed priority and base power?
7. What is the correlation between power points, accuracy and speed priority for the moves with the highest power points number, accuracy, critical rate, speed priority and base power?
8. What is the attack value for the 4 pokemons with the best attack?
9. What is the defense value for the 4 pokemons with the best defense?
10. What is the HP value for the 4 pokemons with the highest HP?
11. What is the speed value for the 5 pokemons fastest pokemons?
12. What is the correlation between attack, defense and speed for the pokemons with the highest attack, defense, HP and speed?
13. What is the correlation between special attack, special defense and hp for the pokemons with the highest attack, defense, HP and speed?
14. What is the correlation between weaknesses of fire, electric, water and ice for the pokemons with the highest attack, defense, HP and speed?
<a name="SSIS"></a>
# ETL
The whole etl process performed for each dataset is described in the pdf files in the SSIS folder.
<a name="SSAS"></a>
# Analysis Services
The whole cube making process performed for each dataset is described in the pdf files in the SSAS folder.
<a name="DS"></a>
# Data Visualization
#### Covid Dataset
* The incidence of covid for the 2nd quarter of 2020 and the incidence per million of covid for the 2nd quarter of 2020, for 5 countries with the highest covid incidence per million in the 2nd quarter of 2020 (1 and 2 business questions): 

![new_cases](https://user-images.githubusercontent.com/44844566/217676401-19ee6301-bdb7-4613-af49-ad57aa0c10bc.PNG)

* The covid mortality for the 2nd quarter of 2020 and the covid mortality per million for the 2nd quarter of 2020, for 5 countries with the highest covid mortality per million in the 2nd quarter of 2020 (3 and 4 business questions):

![mortality](https://user-images.githubusercontent.com/44844566/217676413-a67d8119-82da-41bd-9947-91e825b4fdf0.PNG)

* The number of covid tests for the 2nd quarter of 2020 and the number of covid tests per million for the 2nd quarter of 2020, for 5 countries which performed the highest number of covid tests per million in the 2nd quarter of 2020 (5 and 6 business questions):

![Tests](https://user-images.githubusercontent.com/44844566/217676390-d35a3588-2dd8-4bdf-9ca6-c2b1d79f4ecb.PNG)

* The number of patients hospitalized due to covid and icu patients per million for the 2nd quarter of 2020, for 5 countries which have the highest number of patients hospitalized due to covid and icu patients per million in the 2nd quarter of 2020 (7 and 8 business questions):

![hospitalization](https://user-images.githubusercontent.com/44844566/217676419-1e834142-a998-4ce8-a6b8-043d0d717acc.PNG)

* The correlation between covid vaccinations and incidence of covid, incidence of covid and covid tests, covid vaccinations and mcovid mortality for Argentina, for the first 9 months of 2021 (9, 10, 11 business questions):

![vaccinations](https://user-images.githubusercontent.com/44844566/217676363-83f39c86-26ba-416c-96f9-5107734e94fe.PNG)

#### Pokemon dataset

* The power points number for the 5 moves with the highest power points numberm, the accuracy for the 5 moves with the highest accuracy, the critical rate for the 5 moves with the highest critical rate. The categories of these moves. (1, 2, 3 business questions) The speed priority for the 5 moves with the highest speed priority and the base power for the 5 moves with the highest base power. The types of these moves (4, 5 business questions):

![move_statistics](https://user-images.githubusercontent.com/44844566/217677006-9ee144a3-04cc-43f6-9aaf-566a782a98ce.PNG)

* The correlation between power points, critical rate and accuracy and the correlation between power points, accuracy and speed priority for the moves with the highest power points number, accuracy, critical rate, speed priority and base power (6, 7 business questions):

![Moves_Statistics_Correlation](https://user-images.githubusercontent.com/44844566/217677008-b87affe8-5f07-4a15-843b-f043936338dd.PNG)

* The attack value for the 4 pokemons with the best attack, the defense value for the 4 pokemons with the best defense, the HP value for the 4 pokemons with the highest HP, The speed value for the 5 pokemons fastest pokemons (8, 9, 10, 11 business questions):

![Pokemon_Statistics](https://user-images.githubusercontent.com/44844566/217677009-8ed53b76-28b7-4245-9cca-7e86701c9823.PNG)

* The correlation between attack, defense and speed, the correlation between special attack, special defense and hp and the correlation between weaknesses of fire, electric, water and ice for the pokemons with the highest attack, defense, HP and speed (12, 13, 14 business questions):

![Pokemon_Statistics_correlation](https://user-images.githubusercontent.com/44844566/217677010-53fd21ba-9a3c-43c3-9d1d-aa03bca55f91.PNG)
