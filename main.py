import requests


player = "player"
URL = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={
    player}"
response = requests.get(URL)

data = response.json()
print(data)

# ask user if they want all skills? all kc? or 1 or 2.
# go through find all KCs or skills
# order them by KC or rank
# save to file
