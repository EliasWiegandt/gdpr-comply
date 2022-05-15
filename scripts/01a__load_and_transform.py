# %% imports
import pandas as pd
from glob import glob
from tqdm import tqdm
import json

# %% Import news
failed_files = 0
news_files = []
for news_file_path in tqdm(glob(os.path.join('..', 'data', '20news-18828', '*', '*'))):
    try:
        with open(news_file_path, 'r') as f:
            news_files.append(f.read())
    except:
        failed_files += 1
print(f"Failed to read {failed_files} files")

news_df = pd.DataFrame()
news_df['text'] = news_files
news_df['source'] = "20news-18828"
news_df['id'] = 'news-' + news_df.index.astype('string')
print("Df with 20news-texts created")


# %% Import enron
failed_files = 0    
enron_file_paths = []
enron_files = []
relevant_folders = ['inbox', 'sent', 'sent_items']
for relevant_folder in relevant_folders:
    enron_file_path_in_folder = glob(os.path.join('..', 'data', 'enron_mail_20150507', 'maildir', '*', relevant_folder, '*.'))
    assert len(enron_file_path_in_folder) > 0
    enron_file_paths += enron_file_path_in_folder

for enron_file_path in tqdm(enron_file_paths):
    try:
        with open(enron_file_path, 'r') as f:
            enron_files.append(f.read())
    except:
        failed_files += 1
print(f"Failed to read {failed_files} files")

enron_df = pd.DataFrame()
enron_df['text'] = enron_files
enron_df['source'] = "enron_mail_20150507"
enron_df['id'] = 'enron-' + enron_df.index.astype('string')
print("Df with enron-email-texts created")

# %% Import reddit
failed_files = 0
reddit_files = []
for reddit_file_path in tqdm(glob(os.path.join('..', 'data', 'reddit', '*.csv'))):
    try:
        reddit_file = pd.read_csv(reddit_file_path)
        reddit_files.append(reddit_file)
    except:
        failed_files += 1
reddit_files = pd.concat(reddit_files)
reddit_files.reset_index(inplace=True)
print(f"Failed to read {failed_files} files")

rename_dict = {
    'title': 'text'
}

reddit_df = reddit_files[list(rename_dict.keys())].rename(rename_dict, axis=1)
reddit_df['source'] = "reddit"
reddit_df['id'] = 'reddit-' + reddit_df.index.astype('string')
print("Df with reddit-texts created")

# %% Import legal cases
failed_files = 0
legal_case_files = []
for legal_case_file_path in tqdm(glob(os.path.join('..', 'data', 'legal-cases', 'corpus', 'fulltext', '*'))):
    try:
        with open(legal_case_file_path, 'r') as f:
            legal_case_files.append(f.read())
    except:
        failed_files += 1
print(f"Failed to read {failed_files} files")

legal_case_df = pd.DataFrame()
legal_case_df['text'] = legal_case_files
legal_case_df['source'] = "legal-cases"
legal_case_df['id'] = 'legal-' + legal_case_df.index.astype('string')
print("Df with legal-case-texts created")


# %%
sample_specs = (
    {'sample_size': 100, 'df': news_df}
    , {'sample_size': 100, 'df': enron_df}
    , {'sample_size': 400, 'df': reddit_df}
    , {'sample_size': 100, 'df': legal_case_df}
)

df_list = [news_df, enron_df, reddit_df, legal_case_df]
df = pd.DataFrame()

for sample_spec in sample_specs:
    df = pd.concat(
        [
            df
            , sample_spec['df'].sample(sample_spec['sample_size'], random_state=1)
        ]
        )
df = df.sample(frac=1.0)
df.reset_index(inplace=True)

# %%
data_list = []
for ix, row in tqdm(df.iterrows(), total=df.shape[0]):
    data_dict = {'header': row['id'], 'text_label' : row['text'], 'id': row['id']}
    data_list.append(data_dict)

json_data = json.dumps(data_list)
with open(f'../data/for_annotation/20220515-test-01.json', 'w', encoding='utf8') as f:
    f.write(json_data)

# %%
len(data_list)
# %%
