RAW_PATH = "data/raw/fpl_player_statistics.csv"
PROC_PATH = "data/processed/labels.parquet"
FEAT_PATH = "data/processed/features.parquet"

TOP_THRESHOLD = 8

# expected essential columns (sanity step)
REQUIRED_COLS = [
    "player_name","position_name","club_name","event_points","minutes"
]
# strongly recommended for temporal modeling
RECOMMENDED_COLS = ["gameweek"]
