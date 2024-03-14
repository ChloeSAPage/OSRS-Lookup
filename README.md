# OSRS Lookup

A CLI application that allows the user to look up a player from Old School RuneScape and find their stats.

## Using the app

This app requires no API key. Just install the requests module.
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
