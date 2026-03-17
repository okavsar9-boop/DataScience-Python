import pandas as pd
import numpy as np

# Ominakavsar Abduganieva, ID: 74026

np.random.seed(74026)

towns_OA = ['Warsaw', 'Krakow', 'Gdansk', 'Wroclaw']
groups_OA = ['Group1', 'Group2', 'Group3']
ages_OA = ['Adult', 'Child']

years_OA = [2021, 2022, 2023, 2024, 2025]
seasons_OA = ['S1', 'S2', 'S3']
parts_OA = ['P1', 'P2']

row_index_OA = pd.MultiIndex.from_product([towns_OA, groups_OA, ages_OA], names=['Town', 'Group', 'Age'])
col_index_OA = pd.MultiIndex.from_product([years_OA, seasons_OA, parts_OA], names=['Year', 'Season', 'Part'])

data_OA = np.random.randint(1000, 74026, size=(len(row_index_OA), len(col_index_OA)))
df_OA = pd.DataFrame(data_OA, index=row_index_OA, columns=col_index_OA)

print(df_OA.head())

print("\n--- Mean values for second town ---")
print(df_OA.loc['Krakow'].mean())

print("\n--- Mean values for each season ---")
print(df_OA.groupby(level='Season', axis=1).mean())

print("\n--- Mean values for each age group ---")
print(df_OA.groupby(level='Age').mean())