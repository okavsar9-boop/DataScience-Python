import pandas as pd
import re
from sklearn.datasets import fetch_20newsgroups

# Ominakavsar Abduganieva, ID: 74026

all_cats_OA = fetch_20newsgroups(subset='all')
print("Categories:", all_cats_OA.target_names)

cats_OA = ['rec.sport.hockey', 'rec.sport.baseball', 'sci.space', 'sci.electronics']
data_OA = fetch_20newsgroups(subset='train', categories=cats_OA)

df_OA = pd.DataFrame({
    'text': data_OA.data, 
    'category': [data_OA.target_names[i] for i in data_OA.target]
})

print("\n--- Info ---")
print(df_OA.info())

print("\n--- 3 Full Documents ---")
for i in range(3):
    print(f"\nDOCUMENT {i}:\n", df_OA['text'].iloc[i])

def manual_clean_OA(text):
    text = re.sub(r'^(From|Subject|Lines|Organization|Reply-To|Expires|Distribution):.*', '', text, flags=re.MULTILINE)
    return text.strip()

data_auto_OA = fetch_20newsgroups(subset='train', categories=cats_OA, remove=('headers', 'footers'))
df_OA['text_auto'] = data_auto_OA.data

print("\n--- Step 3: Comparison ---")
for i in range(3):
    print(f"\n[Doc {i}] Manual Clean:\n", manual_clean_OA(df_OA['text'].iloc[i])[:150])
    print(f"[Doc {i}] Auto Clean:\n", df_OA['text_auto'].iloc[i][:150])

df_OA['char_count_OA'] = df_OA['text'].apply(len)
df_OA['word_count_OA'] = df_OA['text'].apply(lambda x: len(x.split()))

email_pattern_OA = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern_OA = r'https?://\S+|www\.\S+'

emails_count_OA = df_OA['text'].str.findall(email_pattern_OA).apply(len).sum()
urls_count_OA = df_OA['text'].str.findall(url_pattern_OA).apply(len).sum()
nasa_docs_OA = df_OA['text'].str.contains('NASA', case=False).sum()

print(f"\nEmails: {emails_count_OA}")
print(f"URLs: {urls_count_OA}")
print(f"NASA documents: {nasa_docs_OA}")

# Chosen words (Step 5 logic): 
# Words like NASA, space, orbit, electronics, and hockey were chosen as they are 
# specific to the topics. Visualization is done via summary counts in the console.