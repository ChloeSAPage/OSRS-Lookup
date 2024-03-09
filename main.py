import requests

#player =  input("Enter a Player Name: ")
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
if user_choice == "skills":
    skills = data["skills"]
    print(skills)
    for skill in skills:
        print("\n", skill)
        skill_name = skill["name"]
        skill_level = skill["level"]
        skills_cleaned.append((skill_name, skill_level))
        print(f"{skill_name}: {skill_level}")
        

elif user_choice == "activities":
    activities = data["activities"]
    print(activities)

skills_cleaned.sort(reverse=True, key=lambda a: a[1])
print(skills_cleaned)
# go through find all KCs or skills
# order them by KC or rank
# save to file
