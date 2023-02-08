ALTER TABLE [DimDate]
ADD CONSTRAINT PK_DimDate
PRIMARY KEY(dateSK);

ALTER TABLE [DimLocation]
ADD CONSTRAINT PK_DimLocation
PRIMARY KEY(locationSK);

ALTER TABLE [FactMortality]
ADD CONSTRAINT PK_FactMortality
PRIMARY KEY(locationSK, dateSK);

ALTER TABLE [FactMortality]
ADD CONSTRAINT FK_FactMortalityLocation
FOREIGN KEY(locationSK) REFERENCES [DimLocation](locationSK);

ALTER TABLE [FactMortality]
ADD CONSTRAINT FK_FactMortalityDate
FOREIGN KEY(dateSK) REFERENCES [DimDate](dateSK);

ALTER TABLE [FactVacaccinations]
ADD CONSTRAINT PK_FactVacaccinations
PRIMARY KEY(locationSK, dateSK);

ALTER TABLE [FactVacaccinations]
ADD CONSTRAINT FK_FactVacaccinationsLocation
FOREIGN KEY(locationSK) REFERENCES [DimLocation](locationSK);

ALTER TABLE [FactVacaccinations]
ADD CONSTRAINT FK_FactVacaccinationsDate
FOREIGN KEY(dateSK) REFERENCES [DimDate](dateSK);

ALTER TABLE [FactHospitalization]
ADD CONSTRAINT PK_FactHospitalization
PRIMARY KEY(locationSK, dateSK);

ALTER TABLE [FactHospitalization]
ADD CONSTRAINT FK_FactHospitalizationLocation
FOREIGN KEY(locationSK) REFERENCES [DimLocation](locationSK);

ALTER TABLE [FactHospitalization]
ADD CONSTRAINT FK_FactHospitalizationDate
FOREIGN KEY(dateSK) REFERENCES [DimDate](dateSK);

ALTER TABLE [FactTests]
ADD CONSTRAINT PK_FactTests
PRIMARY KEY(locationSK, dateSK);

ALTER TABLE [FactTests]
ADD CONSTRAINT FK_FactTestsLocation
FOREIGN KEY(locationSK) REFERENCES [DimLocation](locationSK);

ALTER TABLE [FactTests]
ADD CONSTRAINT FK_FactTestsDate
FOREIGN KEY(dateSK) REFERENCES [DimDate](dateSK);

ALTER TABLE [FactCases]
ADD CONSTRAINT PK_FactCases
PRIMARY KEY(locationSK, dateSK);

ALTER TABLE [FactCases]
ADD CONSTRAINT FK_FactCasesLocation
FOREIGN KEY(locationSK) REFERENCES [DimLocation](locationSK);

ALTER TABLE [FactCases]
ADD CONSTRAINT FK_FactCasesDate
FOREIGN KEY(dateSK) REFERENCES [DimDate](dateSK);