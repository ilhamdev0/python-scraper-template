import pandas as pd


def dataframe(data: list):
    return pd.DataFrame.from_records(data)


def save_csv(data):
    data.to_csv("out.csv", index=False)


def save_csv_incremental(num: int, data):
    filename = f"out{num}.csv"
    
    if num > 1:
        data.to_csv(filename, index=False, header=False)
        return

    data.to_csv(filename, index=False)
