# movie-recommendation
Repository for the advanced machine learning course

## Setup
### Python environment
1. Create virtual environment `python -m venv env`
2. Activate venv `env/Scripts/activate`
3. Install python requirements `pip install -r requirements.txt`

### Dataset
1. Go to your kaggle settings, scroll down to API and create a new API Token. This will download a `kaggle.json` file
2. If you are on a Unix system save this token at `~/.kaggle/kaggle.json`, if you are on Windows `C:\Users\<win_username>\.kaggle\kaggle.json`
3. Activate the environment if not already activated `env/Scripts/activate`
4. Go to src folder `cd src`
5. Run `python data_loader.py`

### Make changes to the requirements file
After installing or deleting pip packages make sure you add them to the requirements file by running `pip freeze > requirements.txt` in the project's root folder

## Data

.
