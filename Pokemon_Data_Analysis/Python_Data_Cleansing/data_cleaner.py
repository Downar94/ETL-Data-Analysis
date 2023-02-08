import pandas as pd
import math

pokemon_data = pd.read_csv('DimPokemon.txt')
def pokemon_data_cleaning():
    pokemon_data['Ability_1'] = 'missing'
    pokemon_data['Ability_2'] = 'missing'
    pokemon_data['Ability_3'] = 'missing'
    for i in range(len(pokemon_data)):
        try:
            if pokemon_data['Pokemon'][i] == pokemon_data['Pokemon'][i+1]:
                pokemon_data['Ability_1'][i] = pokemon_data['Ability'][i]
                pokemon_data['Ability_2'][i] = pokemon_data['Ability'][i+1]
                if pokemon_data['Pokemon'][i] == pokemon_data['Pokemon'][i+2]:
                    pokemon_data['Ability_3'][i] = pokemon_data['Ability'][i+2]
                    
            else: 
                pokemon_data['Ability_1'][i] = pokemon_data['Ability'][i]
                
        except:
            ('eof')
    pokemon_data.drop_duplicates(subset=['Pokemon'], inplace = True)
    pokemon_data.reset_index(inplace = True)
    pokemon_data.to_csv('cleaned_data/PokemonDim_data_cleaned.csv', index=False)
        
pokemon_data_cleaning()