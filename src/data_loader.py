import kaggle
import os
import config
import pandas as pd
def download_dataset():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(config.DATASET, 'data/', unzip=True)
    

def load_data():
    if not os.path.exists('./data/chatgpt.csv'):
        print('### Downloading data ###')
        download_dataset()
    
    

if __name__ == '__main__':
    download_dataset()