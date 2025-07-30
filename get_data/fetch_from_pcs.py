

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.procyclingstats.com/race/tour-de-france/2025/startlist"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

data = []

# Each team block
team_blocks = soup.select("ul.startlist_v4 > li")

print(f"Found {len(team_blocks)} teams")


for team_block in team_blocks:
    # Get team link
    team_a = team_block.find("a", class_="team")
    if not team_a:
        continue

    team_name = team_a.get_text(strip=True)
    team_href = "https://www.procyclingstats.com/" + team_a.get("href", "").strip()

    # Get rider list items
    rider_lis = team_block.select("ul > li")

    for rider_li in rider_lis:
        bib_span = rider_li.find("span", class_="bib")
        rider_link = rider_li.find("a")

        if not bib_span or not rider_link:
            continue

        bib = bib_span.get_text(strip=True)
        rider_name = rider_link.get_text(strip=True)
        rider_href = "https://www.procyclingstats.com/" + rider_link.get("href", "").strip()

        data.append({
            "bib": bib,
            "rider_name": rider_name,
            "team": team_name,
            "team_link": team_href,
            "rider_link": rider_href
        })

# Convert to DataFrame
df = pd.DataFrame(data)

df.to_csv("tdf2025_startlist.csv", index=False)

# Convert to DataFrame
df = pd.DataFrame(data)