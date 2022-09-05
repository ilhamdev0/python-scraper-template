import pandas as pd


def dataframe(data: list):
    return pd.DataFrame.from_records(data)


def save_parquet(dataframe, filename: str):
    dataframe.to_parquet(f"{filename}.parquet", index=False)


def save_parquet_incremental(filename: str, num: int, divider: int, dataframe):
    leading_zero = len(str(divider))
    num = str(num).zfill(leading_zero)
    
    filename = f"{filename}{num}"
    save_parquet(dataframe, filename)
