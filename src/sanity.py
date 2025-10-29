def check_required_columns(df, cols):
    missing = [c for c in cols if c not in df.columns]
    return missing

def check_unique_player_gw(df, player_key="player_name", gw_key="gameweek"):
    if gw_key not in df.columns:
        return "gameweek column missing"
    dupes = df.duplicated([player_key, gw_key]).sum()
    return dupes  # should be 0
