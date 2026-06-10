import pandas as pd

def hybrid_score():

    taxi_data = pd.DataFrame({

        'Taxi_ID': ['T1','T2','T3','T4','T5'],

        'ML_Score': [15.38,7.50,19.56,5.55,11.29],

        'RL_Score': [0.90,0.60,0.95,0.50,0.80]

    })

    taxi_data['Hybrid_Score'] = (

        taxi_data['ML_Score']

        +

        taxi_data['RL_Score']

    )

    result = taxi_data.sort_values(

        by='Hybrid_Score',

        ascending=False

    )

    return result