import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def to_parquet(df, path: str):
    df.to_parquet(path, index=False)
