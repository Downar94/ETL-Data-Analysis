CREATE TABLE [FactStatistics] (
    [pokemonSK] int NOT NULL,
    [HP] int,
    [attack] int,
    [defense] int,
    [special_attack] int,
    [special_defense] int,
    [speed] int,
    [weakness-normal] real,
    [weakness-fire] real,
    [weakness-water] real,
    [weakness-electric] real,
    [weakness-grass] real,
    [weakness-ice] real,
    [weakness-fighting] real,
    [weakness-poison] real,
    [weakness-ground] real,
    [weakness-flying] real,
    [weakness-psychic] real,
    [weakness-bug] real,
    [weakness-rock] real,
    [weakness-ghost] real,
    [weakness-dragon] real,
    [weakness-dark] real,
    [weakness-steel] real,
    [weakness-fairy] real
)

CREATE TABLE [FactMoves] (
    [pokemonSK] int NOT NULL,
    [moveSK] int NOT NULL,
    [power_points] int,
    [base_power] int,
    [accuracy] int,
    [critical_rate] real,
    [speed_priority] real
)