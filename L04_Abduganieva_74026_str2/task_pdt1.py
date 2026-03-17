import pandas as pd
import re
from sklearn.datasets import fetch_20newsgroups

categories_MA = ['sci.electronics', 'sci.space', 'rec.sport.baseball', 'rec.sport.hockey']
data_raw_MA = fetch_20newsgroups(subset='train', categories=categories_MA)

df_MA = pd.DataFrame({
    'text': data_raw_MA.data,
    'category': [data_raw_MA.target_names[i] for i in data_raw_MA.target]
})

df_MA['char_count'] = df_MA['text'].apply(len)
df_MA['word_count'] = df_MA['text'].apply(lambda x: len(x.split()))

email_pattern = r'[a-zA-Z0-9._%+-]+@[\w.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?://\S+'

nasa_count_MA = df_MA['text'].str.contains('NASA', case=False).sum()

print("--- Dataset Summary ---")
print(df_MA.head(3)) 
print(f"\nTotal documents loaded: {len(df_MA)}")
print(f"Total documents mentioning 'NASA': {nasa_count_MA}")

longest_doc_MA = df_MA.loc[df_MA['word_count'].idxmax()]
print(f"\nThe longest document is in category '{longest_doc_MA['category']}' "
      f"with {longest_doc_MA['word_count']} words.")