# Ominakavsar Abduganieva, ID: 74026
import pandas as pd

df1_OA = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'specialization': ['AI', 'Data', 'AI', 'Web', 'Data']
})

df2_OA = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'years_working': [2, 5, 3, 1, 4]
})

df4_OA = pd.DataFrame({
    'specialization': ['AI', 'Data', 'Web'],
    'supervisor': ['Zaremba', 'Kowalski', 'Pietrzak']
})

df5_OA = pd.DataFrame({
    'specialization': ['AI', 'Data', 'Web'],
    'skill': ['Python', 'SQL', 'JS']
})

merged_12_OA = pd.merge(df1_OA, df2_OA, on='name')
merged_all_OA = pd.merge(merged_12_OA, df4_OA, on='specialization')
joined_OA = df1_OA.set_index('name').join(df2_OA.set_index('name'))

print("--- Merged Data (All) ---")
print(merged_all_OA)
print("\n--- Joined Data (df1 + df2) ---")
print(joined_OA)