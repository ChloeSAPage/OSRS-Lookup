import requests

# player =  input("Enter a Player Name: ")
player = "player"
URL = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={
    player}"
response = requests.get(URL)

data = response.json()
# print(data)

# ask user if they want skills or activities?
# user_choice = input("Do you want to see Skills or Activities: ").lower()
user_choice = "skills"
skills_cleaned = []

# go through find all KCs or skills
if user_choice == "skills":
    skills = data["skills"]
    print(skills)
    for skill in skills:
        print("\n", skill)
        skill_name = skill["name"]
        skill_level = skill["level"]
        skills_cleaned.append((skill_name, str(skill_level)))
        print(f"{skill_name}: {skill_level}")


elif user_choice == "activities":
    activities = data["activities"]
    print(activities)


# order them by KC or rank
skills_cleaned.sort(reverse=True, key=lambda a: int(a[1]))
print(skills_cleaned)

# save to file
with open(user_choice, "w") as file:
    for skill_name, skill_level in skills_cleaned:
        file.write(f"{skill_name}: {skill_level}\n")
