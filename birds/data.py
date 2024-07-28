import pandas as pd


def load_and_process_data(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Lowercase player names and mark new games
    data["score"] = data["score"].str.lower()  # Lowercase player names
    data["new_game"] = data["score"].isna()

    # Forward fill the 'new_game' column to mark each game
    data["game_id"] = data["new_game"].cumsum()

    # Filter out the rows with NaN in 'score' as they are game separators
    cleaned_data = data.dropna(subset=["score"])

    # Calculate wins
    win_idx = cleaned_data.groupby("game_id")["total"].idxmax()
    wins = cleaned_data.loc[win_idx, "score"].value_counts()

    # Calculate games played
    games_played = cleaned_data["score"].value_counts()

    # Create a dataframe for the score board
    score_board = pd.DataFrame({"wins": wins, "games_played": games_played}).fillna(0)

    # Calculate wins/games played ratio
    score_board["wins_per_game"] = score_board["wins"] / score_board["games_played"]

    # Sort by wins/games played ratio
    score_board = score_board.sort_values(by="wins_per_game", ascending=False)

    return score_board, cleaned_data


def calculate_stats(df, columns):
    stats = {}
    for column in columns:
        stats[column] = df[column].agg(["mean", "min", "max"])
    return pd.DataFrame(stats)


def get_statistics(file_path):
    score_board, cleaned_data = load_and_process_data(file_path)

    # Columns to calculate statistics for
    score_columns = [
        "birds",
        "bonus cards",
        "end of round goals",
        "eggs",
        "food on cards",
        "tucked cards",
        "total",
    ]

    # Calculate statistics for each column
    overall_stats = calculate_stats(cleaned_data, score_columns)

    return score_board, overall_stats


def display_stats(file_path):
    score_board, overall_stats = get_statistics(file_path)

    print("Score Board:")
    print(score_board)
    print("\nOverall Statistics:")
    print(overall_stats)


if __name__ == "__main__":
    # Example usage:
    file_path = "scores.csv"
    display_stats(file_path)
