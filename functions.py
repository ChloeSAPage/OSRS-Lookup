import requests

def get_data():
    player = input("Enter a Player Name: ")
    # player = "eolhx"
    URL = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={player}"
    response = requests.get(URL)
    data = response.json()
    
    print("Data Retrieved Successfully")
    return data, player


def put_data_in_dic(data):
    user_choice = input("Activities or Skills? ").lower()
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
    with open(f"{user_choice}.txt", "w") as file:
        file.write(player + "\n")
        for skill_name, skill_level in sorted_data:
            file.write(f"{skill_name}: {skill_level}\n")
    print("Written to file successfully")
