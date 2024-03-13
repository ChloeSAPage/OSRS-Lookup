from functions import put_data_in_dic, write_to_file, get_data, get_random, check_status

# Player examples include player, Figs, David, Karma, Hunter
status, response, player = check_status()

if status == True:
    data = get_data(response)

    # Ask if user wants a random choice
    random_choice = input(
        "Would you like to get a single random choice? y or n ").lower()
    # random_choice = "n"

    if random_choice == "y":
        value, choice = get_random(data)
        write_to_file(choice, value, player)

    elif random_choice == "n":
        # Get data of User's choice
        user_choice = input("Activities or Skills? ").lower()
        # user_choice = "skills"
        cleaned_data, user_choice = put_data_in_dic(data, user_choice)

        # Sort them by skill level or KC
        sorted_data = sorted(cleaned_data.items(),
                             reverse=True, key=lambda a: a[1])

        write_to_file(user_choice, sorted_data, player)

    else:
        print("Invalid choice")

elif status == False:
    print("Could not retrieve data for this Player.")
