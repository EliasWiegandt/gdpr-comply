# %% imports
import pandas as pd
from glob import glob
from tqdm import tqdm

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

# %% Import enron
failed_files = 0    
enron_file_paths = []
enron_files = []
relevant_folders = ['inbox', 'sent', 'sent_items']
for relevant_folder in relevant_folders:
    enron_file_path_in_folder = glob(os.path.join('..', 'data', 'enron_mail_20150507', 'maildir', '*', relevant_folder, '*.'))
    assert len(enron_files_in_folder) > 0
    enron_file_paths += enron_file_path_in_folder

for enron_file_path in tqdm(enron_file_paths):
    try:
        with open(enron_file_path, 'r') as f:
            enron_files.append(f.read())
    except:
        failed_files += 1
print(f"Failed to read {failed_files} files")

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
print(f"Failed to read {failed_files} files")

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

# %%
glob(os.path.join('..', 'data', 'legal-cases', 'corpus', 'fulltext', '*'))

# %%

