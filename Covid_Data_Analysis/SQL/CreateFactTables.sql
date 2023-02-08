CREATE TABLE [FactVacaccinations] (
    [locationSK] int NOT NULL,
	[dateSK] int NOT NULL,
    [people_fully_vaccinated_per_hundred_converted] real,
    [people_vaccinated_per_hundred_converted] real,
    [total_vaccinations_per_hundred_converted] real,
    [sputnikv_total_vaccinations] bigint,
    [sinovac_total_vaccinations] bigint,
    [sinopharm_total_vaccinations] bigint,
    [pfizer_total_vaccinations] bigint,
    [astrazeneca_total_vaccinations] bigint,
    [novavax_total_vaccinations] bigint,
    [moderna_total_vaccinations] bigint,
    [johnson&johnson_total_vaccinations] bigint,
    [covaxin_total_vaccinations] bigint,
    [cansino_total_vaccinations] bigint
);
CREATE TABLE [FactHospitalization] (
    [locationSK] int NOT NULL,
    [dateSK] int NOT NULL,
    [icu_patients] int,
    [icu_patients_per_million] real,
    [hosp_patients] int,
    [hosp_patients_per_million] real
);

CREATE TABLE [FactTests] (
    [locationSK] int NOT NULL,
    [dateSK] int NOT NULL,
    [new_tests] int,
    [new_tests_per_thousand] real
);

CREATE TABLE [FactCases] (
    [locationSK] int NOT NULL,
    [dateSK] int NOT NULL,
    [new_cases] int,
    [new_cases_per_million] int
);

CREATE TABLE [FactMortality] (
    [locationSK] int NOT NULL,
    [dateSK] int NOT NULL,
    [new_deaths] int,
    [new_deaths_per_million] real,
    [total_deaths] int,
    [total_deaths_per_million] real
);
