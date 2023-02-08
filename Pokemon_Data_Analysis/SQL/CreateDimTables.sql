CREATE TABLE [DimPokemon] (
    [pokemonSK] [INT] IDENTITY(1,1) NOT NULL,
	[name] varchar(30),
    [first_form] varchar(50),
    [second_form] varchar(50),
    [ability_1] varchar(50),
    [ability_2] varchar(50),
    [ability_3] varchar(50),
);

CREATE TABLE [DimMove] (
    [moveSK] [INT] IDENTITY(1,1) NOT NULL,
    [name] varchar(30),
	[type] varchar(30),
    [category] varchar(30),
);