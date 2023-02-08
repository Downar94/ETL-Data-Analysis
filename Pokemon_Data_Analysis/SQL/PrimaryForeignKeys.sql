ALTER TABLE [DimPokemon]
ADD CONSTRAINT PK_DimPokemon
PRIMARY KEY(pokemonSK);

ALTER TABLE [DimMove]
ADD CONSTRAINT PK_DimMove
PRIMARY KEY(moveSK);

ALTER TABLE [FactStatistics]
ADD CONSTRAINT PK_FactStatistics
PRIMARY KEY(pokemonSK);

ALTER TABLE [FactStatistics]
ADD CONSTRAINT FK_FactStatisticsPokemon
FOREIGN KEY(pokemonSK) REFERENCES [DimPokemon](pokemonSK);

ALTER TABLE [FactMoves]
ADD CONSTRAINT PK_FactMoves
PRIMARY KEY(pokemonSK,moveSK);

ALTER TABLE [FactMoves]
ADD CONSTRAINT FK_FactMovesPokemon
FOREIGN KEY(pokemonSK) REFERENCES [DimPokemon](pokemonSK);

ALTER TABLE [FactMoves]
ADD CONSTRAINT FK_FactMovesMove
FOREIGN KEY(moveSK) REFERENCES [DimMove](moveSK);