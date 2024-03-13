import requests
import random


def get_data():
    '''
    Retrieve Data from OSRS API for a given user.
    '''
    player = input("Enter a Player Name: ")
    # player = "player"
    URL = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={player}"
    response = requests.get(URL)
    data = response.json()

    print("Data Retrieved Successfully")
    return data, player


def put_data_in_dic(data, user_choice):
    '''
    Data is then spliced and put into a dictionary.
    '''
    chosen_data = data[user_choice]
    cleaned_data = {}

    for data in chosen_data:
        name = data["name"]

        if user_choice == "skills":
            skill_level = data["level"]
            cleaned_data[name] = skill_level

        elif user_choice == "activities":
            score = data["score"]
            if score > 0:
                cleaned_data[name] = score

    return cleaned_data, user_choice


def write_to_file(user_choice, sorted_data, player):
    '''
    Write data and player name to file. 
    '''
    with open(f"{player}_{user_choice}.txt", "w") as file:
        file.write(player + "\n")
        for name, value in sorted_data:
            file.write(f"{name}: {value}\n")
    print(f"Written to {player}_{user_choice}.txt successfully")


# Get Random KC or Skill
def get_random(data):
    '''
    Get a random skill or activity.
    '''
    choice = random.choice(("skills", "activities"))

    new_data, user_choice = put_data_in_dic(data, choice)

    value = random.choices(list(new_data.items()))

    return value, choice
