import pandas as pd
from sklearn.datasets import fetch_20newsgroups

cats = ['sci.space', 'sci.electronics']
data = fetch_20newsgroups(subset='train', categories=cats)

df = pd.DataFrame({'text': data.data, 'target': data.target})
df['category'] = df['target'].apply(lambda x: data.target_names[x])

space_df = df[(df['category'] == 'sci.space') & (df['text'].str.len() > 500)]

file_name = "filtered_space_data.csv"
space_df.to_csv(file_name, index=False)

print(f"Filtered data saved to {file_name}")
print(f"Total rows saved: {len(space_df)}")