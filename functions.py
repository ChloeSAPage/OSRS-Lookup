import requests
import random


def check_status():
    '''
    Check API status for given user.
    '''
    player = input("Enter a Player Name: ")
    # player = "player"
    URL = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={player}"
    response = requests.get(URL)
    status = response.status_code
    
    # Check if the API call worked
    if status == 200:
        return True, response, player

    else:
        return False, response, player


def get_data(response):
    '''
    Retrieve Data from OSRS API for a given user.
    '''
    data = response.json()
    print("Data Retrieved Successfully")
    return data


def put_data_in_dic(data, user_choice):
    '''
    Data is spliced and put into a dictionary.
    '''
    chosen_data = data[user_choice]
    cleaned_data = {}

    # Go through list of dicts
    for data in chosen_data:
        # Take the name of the skill or activity
        name = data["name"]

        if user_choice == "skills":
            skill_level = data["level"]
            xp = data["xp"]

            # Format XP in readable way
            if xp >= 1000000:
                xp = str(xp)
                xp = f"{xp[-9:-6]},{xp[-6:-3]},{xp[-3:]}"

            elif xp >= 1000:
                xp = str(xp)
                xp = f"{xp[-6:-3]},{xp[-3:]}"

            else:
                xp = str(xp)

            # Put the Skill, Level and XP in new dictionary.
            cleaned_data[name] = [skill_level, xp]

        elif user_choice == "activities":
            score = data["score"]
            # Don't include KC less than 1
            if score > 0:
                # Put the Activity and the Score into new dictionary
                cleaned_data[name] = score

    return cleaned_data


def write_to_file(user_choice, sorted_data, player):
    '''
    Write data and player name to file in the player_info directory. 
    '''
    if user_choice == "skills":

        with open(f"player_info/{player}_{user_choice}.txt", "w") as file:
            file.write(f"Username: {player}\n")

            for name, value in sorted_data:
                file.write(f"{name}: {value[0]} - {value[1]} XP\n")

    else:
        with open(f"player_info/{player}_{user_choice}.txt", "w") as file:
            file.write(f"Username: {player}\n")

            for name, value in sorted_data:
                file.write(f"{name}: {value}\n")

    print(f"Written to player_info/{player}_{user_choice}.txt successfully")


def get_random(data):
    '''
    Get a random skill or activity.
    '''
    choice = random.choice(("skills", "activities"))
    
    # Get dictionary of either skills or activities
    new_data = put_data_in_dic(data, choice)

    # Get random choice from new_data keys
    value = random.choices(list(new_data.items()))

    return value, choice
