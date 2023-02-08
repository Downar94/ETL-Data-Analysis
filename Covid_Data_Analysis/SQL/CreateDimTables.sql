CREATE TABLE [DimDate] (
    [dateSK] [INT] IDENTITY(1,1) NOT NULL,
    [date] date,
	[day] int,
	[month] int,
	[month_name] nvarchar(9),
	[quarter] int,
    [year] int,
);
CREATE TABLE [DimLocation] (
    [locationSK] [INT] IDENTITY(1,1) NOT NULL,
    [location] varchar(50),
    [continent] varchar(30),
    [iso_code] varchar(10)
)
