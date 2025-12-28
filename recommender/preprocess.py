import pandas as pd
import re

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["description"] = df["description"].fillna("").apply(clean_text)

    df["title_clean"] = (
        df["title"]
        .str.lower()
        .str.strip()
    )

    return df
