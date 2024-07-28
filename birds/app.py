import streamlit as st

from birds.data import get_games, get_statistics

# File path to the CSV file
file_path = "scores.csv"

# Load the data and statistics
score_board, overall_stats = get_statistics(file_path)
games = get_games(file_path)

# Streamlit app
st.title("Birds Game Statistics")

st.image("birds/content/main.webp")
st.header("Score Board")
st.dataframe(score_board)

st.header("Overall Statistics")
st.dataframe(overall_stats.T)  # Transpose for better readability

# Game selection
st.header("Select a Game")
game_list = list(games.keys())
selected_game = st.selectbox("Select a game to view details", game_list)

# Display the selected game's details
if selected_game:
    st.subheader(f"Details for {selected_game}")
    st.dataframe(
        games[selected_game].drop(columns=["game_id"])
    )  # Drop game_id for cleaner display
