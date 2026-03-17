# Ominakavsar Abduganieva, ID: 74026
import pandas as pd
import re
from sklearn.datasets import fetch_20newsgroups
all_data_MA = fetch_20newsgroups(subset='all')
print("All categories in 20newsgroups:", all_data_MA.target_names)

cats_MA = ['rec.sport.hockey', 'rec.sport.baseball', 'sci.space', 'sci.electronics']
data_train_MA = fetch_20newsgroups(subset='train', categories=cats_MA)

df_MA = pd.DataFrame({
    'text': data_train_MA.data,
    'category': [data_train_MA.target_names[i] for i in data_train_MA.target]
})

print("\n--- Dataset Info ---")
print(df_MA.info()) 

print("\n--- 3 Example Documents (Full) ---")
for i in range(3):
    print(f"\nDocument {i+1}:\n", df_MA['text'].iloc[i]) 

def manual_clean_MA(text):
    text = re.sub(r'^(From|Subject|Lines|Organization|Expires|Reply-To):.*', '', text, flags=re.MULTILINE)
    return text.strip()

data_removed_MA = fetch_20newsgroups(subset='train', categories=cats_MA, remove=('headers', 'footers'))
df_MA['text_auto_clean'] = data_removed_MA.data

print("\n--- Step 3: Comparison (First 3 Documents) ---")
for i in range(3):
    print(f"\n[Doc {i}] Manual Clean (Sample):\n", manual_clean_MA(df_MA['text'].iloc[i])[:100], "...")
    print(f"[Doc {i}] Auto Clean (Sample):\n", df_MA['text_auto_clean'].iloc[i][:100], "...") # [cite: 155]

df_MA['char_count_MA'] = df_MA['text'].apply(len) 
df_MA['word_count_MA'] = df_MA['text'].apply(lambda x: len(x.split())) 

email_pattern_MA = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern_MA = r'https?://\S+|www\.\S+' 

emails_found_MA = df_MA['text'].str.findall(email_pattern_MA).apply(len).sum()
urls_found_MA = df_MA['text'].str.findall(url_pattern_MA).apply(len).sum()
nasa_docs_MA = df_MA['text'].str.contains(r'NASA', flags=re.IGNORECASE).sum() 

print(f"\n--- Analysis Results ---")
print(f"Total Email addresses found: {emails_found_MA}")
print(f"Total URLs found: {urls_found_MA}")
print(f"Documents mentioning 'NASA': {nasa_docs_MA}")