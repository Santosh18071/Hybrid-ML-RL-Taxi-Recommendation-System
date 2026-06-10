import pandas as pd

def create_features(df):

    # Convert datetime columns
    df['tpep_pickup_datetime'] = pd.to_datetime(
        df['tpep_pickup_datetime']
    )

    df['tpep_dropoff_datetime'] = pd.to_datetime(
        df['tpep_dropoff_datetime']
    )

    # Trip duration in minutes
    df['trip_duration'] = (
        df['tpep_dropoff_datetime']
        -
        df['tpep_pickup_datetime']
    ).dt.total_seconds()/60

    # Hour of the day
    df['hour'] = df['tpep_pickup_datetime'].dt.hour

    # Day
    df['day'] = df['tpep_pickup_datetime'].dt.day

    # Month
    df['month'] = df['tpep_pickup_datetime'].dt.month

    return df