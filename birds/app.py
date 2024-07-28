import pandas as pd
import streamlit as st

from birds.data import get_statistics

# File path to the CSV file
file_path = "scores.csv"

# Load the data and statistics
score_board, overall_stats = get_statistics(file_path)

# Streamlit app
st.title("Birds Statistics")

st.header("Score Board")
st.dataframe(score_board)

st.header("Overall Statistics")
st.dataframe(overall_stats.T)  # Transpose for better readability
