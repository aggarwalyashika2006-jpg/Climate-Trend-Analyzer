import pandas as pd

def preprocess_data(df):
    # convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # sort by date (important for time series)
    df = df.sort_values('date')

    # reset index
    df = df.reset_index(drop=True)

    return df