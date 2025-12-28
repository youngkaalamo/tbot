import pandas as pd
from recommender.preprocess import preprocess_dataframe
from config import DATA_PATH

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="utf-8")
    df = preprocess_dataframe(df)
    return df
