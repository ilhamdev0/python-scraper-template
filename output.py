import pandas as pd


def dataframe(data: list):
    return pd.DataFrame.from_records(data)


def save_csv(data, filename: str):
    data.to_csv(f"{filename}.csv", index=False)


def save_csv_incremental(filename: str, num: int, data):
    filename = f"{filename}{num}.csv"

    if num > 1:
        data.to_csv(filename, index=False, header=False)
        return

    data.to_csv(filename, index=False)
