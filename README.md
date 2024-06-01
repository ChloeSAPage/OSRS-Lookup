# OSRS Lookup

A CLI application that utilises the Old School RuneScape API, which enables the user to look up a player and find their in-game statistics.

## Using the app

This app requires no API key. Just clone the repo and install requests, then run `main.py`. 
Example players that can be looked up include: player, Figs, David, Karma, Hunter, woox

### Example

```
Enter a Player Name: player
Data Retrieved Successfully
Would you like to get a single random choice? (y or n) n
Activities or Skills? skills
Written to player_info/player_skills.txt successfully
```

## Additional Modules

This uses the requests module in order to retrieve the JSON from the API endpoint. As well as the random module in order to select a random skill or activity for the selected user.
