import streamlit as st
from recommendation import recommend_taxis
from hybrid_model import hybrid_score
from eta_calculation import calculate_eta

st.title("🚕 Hybrid ML-RL Taxi Recommendation System")

st.header("User Input")

distance = st.number_input(
    "Enter Distance (km)",
    min_value=0.1,
    value=2.5
)

eta = calculate_eta(distance)

st.success(f"Estimated ETA: {eta:.2f} minutes")

st.header("Machine Learning Recommendations")

st.dataframe(recommend_taxis())

st.header("Hybrid ML + RL Recommendations")

st.dataframe(hybrid_score())

top_taxi = hybrid_score().iloc[0]

st.header("🏆 Best Taxi Recommendation")

st.write("Taxi ID:", top_taxi['Taxi_ID'])

st.write("Hybrid Score:", top_taxi['Hybrid_Score'])