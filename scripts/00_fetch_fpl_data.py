import requests
import pandas as pd
from time import sleep

all_gws = []

# adjust for current season; max GW is usually 38
for gw in range(1, 10):
    url = f"https://fantasy.premierleague.com/api/event/{gw}/live/"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"❌ GW {gw} not available yet — stopping.")
        break
    data = r.json()

    # Flatten JSON: each element is a player
    gw_df = pd.json_normalize(data["elements"])
    gw_df["gameweek"] = gw  # <-- add GW column
    all_gws.append(gw_df)

    print(f"✅ Fetched GW {gw}, rows: {len(gw_df)}")
    sleep(1)  # be kind to the API

# Combine all gameweeks
df = pd.concat(all_gws, ignore_index=True)

# Flatten nested stats dicts into columns
stats_cols = [c for c in df.columns if c.startswith("stats.")]
df_stats = df[["id", "gameweek"] + stats_cols].copy()
df_stats.columns = [c.replace("stats.", "") for c in df_stats.columns]

print("Shape:", df_stats.shape)
df_stats.head(3)

# Save for next steps
df_stats.to_csv("../data/raw/fpl_player_gameweeks.csv", index=False)
