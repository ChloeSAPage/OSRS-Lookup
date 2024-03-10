from functions import put_data_in_dic, write_to_file, get_data

data, player = get_data()

# go through find all KCs or skills
cleaned_data, user_choice = put_data_in_dic(data)

# order them by KC or rank
sorted_data = sorted(cleaned_data.items(),
                     reverse=True, key=lambda a: a[1])

write_to_file(user_choice, sorted_data, player)
