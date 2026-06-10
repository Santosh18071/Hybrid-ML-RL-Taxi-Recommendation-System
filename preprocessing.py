import pandas as pd

def load_data(path):

    df = pd.read_parquet(path)

    # Remove missing values
    df.dropna(inplace=True)

    # Keep only valid trip distances
    df = df[df['trip_distance'] > 0]

    return df