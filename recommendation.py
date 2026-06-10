import pandas as pd

def recommend_taxis():

    taxi_data = pd.DataFrame({

        'Taxi_ID': ['T1','T2','T3','T4','T5'],

        'Distance': [2.1,3.5,1.8,4.0,2.6]

    })

    speed = 30

    taxi_data['ETA'] = taxi_data['Distance']/speed*60

    taxi_data['Predicted_Demand'] = [80,60,90,50,70]

    taxi_data['ML_Score'] = (
        taxi_data['Predicted_Demand']
        /(taxi_data['ETA']+1)
    )

    result = taxi_data.sort_values(
        by='ML_Score',
        ascending=False
    )

    return result