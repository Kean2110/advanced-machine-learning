import kaggle
import config
def download_dataset():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(config.DATASET, 'data/', unzip=True)
    
if __name__ == '__main__':
    download_dataset()