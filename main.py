import json
from urllib.request import urlopen
from termcolor import colored

with urlopen("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json") as responce:
    source = responce.read()

# Data
data = json.loads(source)
stat_list = ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]
name_list = ["Sort by name", 5, "english", "french", "chinese", "japanese"]
# Menu
stats_menu = ["Sort by stats", 7, "HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]
main_menu = ["POKEDEX", 4, "Sort by name", "Sort by ID", "Sort by stats"]


def reverser():
    reverse_choice = input("Crescent order (AnyKey + Enter) or decreasing order (Enter):")
    return True if reverse_choice == "" else False


# Sorting data by id    / reverse=True (Optional)
def sorting_id():
    print("--   Sort by ID   --\n")
    sorted_data = sorted(data, key=lambda d: d["id"], reverse=reverser())
    return sorted_data


# Sorting data by name  / reverse=True (Optional)
def sorting_name():
    choice = navigate(name_list, 2)
    sorted_name = sorted(data, key=lambda d: d["name"][name_list[choice+1]], reverse=reverser())
    return sorted_name


# Sorting data by base stat  / reverse=True (Optional)
def sorting_stat():
    choice = navigate(stats_menu, 4)
    sorted_data = sorted(data, key=lambda d: d["base"][stat_list[choice-1]], reverse=reverser())
    return sorted_data


# Printing function
def print_data(data_display):
    for i in data_display:
        print(colored("ID:", "yellow"), i.get("id"))
        print(colored("Type:", "blue"), *i.get("type"))
        print(colored("Name:", "red"), end="")
        for name in name_list[2:]:
            print(colored("   [" + name + "]:", "red"), i.get("name").get(name), end="")
        print()
        for stat in stat_list:
            print("     " + stat + ": " + colored(i.get("base").get(stat), "green"))
        print()


def navigate(menu_option, menu_name):
    while True:
        option_list = [i for i in menu_option[1:] if type(i) == str]
        if main_menu[menu_name] == main_menu[0]:
            print("--       POKEDEX         --\n")
        else:
            print("--   Sort by " + main_menu[menu_name] + "   --\n")
        for i in range(1, menu_option[1]):
            print(" " + str(i) + "- " + option_list[i-1])
        print(" " + str(menu_option[1]) + "- exit")
        user_choice = input("\n ")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Valid number, please")
            continue
        if user_choice == menu_option[1]:
            exit()
        if main_menu[menu_name] == main_menu[2] or main_menu[menu_name] == main_menu[4]:
            return user_choice

        if 0 < user_choice <= menu_option[1]:
            if user_choice == 1:
                print_data(sorting_name())
            elif user_choice == 2:
                print_data(sorting_id())
            elif user_choice == 3:
                print_data(sorting_stat())
        else:
            print("Valid range, please")


navigate(main_menu, 0)

# Get all raw data
# print(json.dumps(data, indent=2))
# Sorting data by id with use of / import itemgetter  / reverse=True (Optional)
# sorted_by_id = sorted(data, key=itemgetter("id"), reverse=True)

# pokedex_list = [i for i in data]
# Get min/max value from specific base stat
# print(max(pokedex_list, key=lambda d: d["base"]["Attack"]))
