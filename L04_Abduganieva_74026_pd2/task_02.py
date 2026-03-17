# Ominakavsar Abduganieva, ID: 74026
import pandas as pd

name_OA = "OMINAKAVSAR"
surname_OA = "ABDUGANIEVA"

cols1_OA = list(dict.fromkeys(surname_OA))
df1_OA = pd.DataFrame([[f"{c}{i}" for c in cols1_OA] for i in range(0, 4)], columns=cols1_OA, index=range(0, 4))

cols2_OA = list(dict.fromkeys(name_OA))
df2_OA = pd.DataFrame([[f"{c}{i}" for c in cols2_OA] for i in range(4, 8)], columns=cols2_OA, index=range(4, 8))

outer_concat_OA = pd.concat([df1_OA, df2_OA], join='outer')
inner_concat_OA = pd.concat([df1_OA, df2_OA], join='inner')

print("--- Outer Concatenation ---")
print(outer_concat_OA)
print("\n--- Inner Concatenation ---")
print(inner_concat_OA)