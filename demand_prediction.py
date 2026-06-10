from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(df):

    # Take a sample of 50,000 rows
    df_sample = df.sample(
        n=50000,
        random_state=42
    )

    # Features
    X = df_sample[
        [
            'PULocationID',
            'hour',
            'trip_duration'
        ]
    ]

    # Target
    y = df_sample['trip_distance']

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Random Forest Model
    model = RandomForestRegressor(
        n_estimators=20,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test