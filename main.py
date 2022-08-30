import json
from urllib.request import urlopen
from colorama import init
from termcolor import colored
import unidecode
from operator import itemgetter

with urlopen("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json") as responce:
    source = responce.read()

data = json.loads(source)

# Get all raw data
# print(json.dumps(data, indent=2))
# Sorting data by id with use of / import itemgetter  / reverse=True (Optional)
# sorted_by_id = sorted(data, key=itemgetter("id"), reverse=True)

pokedex_list = [i for i in data]
# Get min/max value from specific base stat
# print(max(pokedex_list, key=lambda d: d["base"]["Attack"]))


# Sorting data by id    / reverse=True (Optional)
def sorting_id(reverse=False):
    sorted_id = sorted(data, key=lambda d: d["id"], reverse=reverse)
    return sorted_id


# Sorting data by name  / reverse=True (Optional)
def sorting_name(choice_name: int, reverse=False):
    add = "crescent"
    if choice_name == 1:
        name = "english"
    elif choice_name == 2:
        name = "french"
    elif choice_name == 3:
        name = "japanese"
    else:
        name = "chinese"
    if reverse:
        add = "decreasing"
    print("Sort by " + name + " name " + add + " order\n")
    sorted_name = sorted(data, key=lambda d: d["name"][name], reverse=reverse)
    return sorted_name


# Sorting data by base stat  / reverse=True (Optional)
def sorting_stat(choice_stat: int, reverse=False):
    if choice_stat == 1:
        stat = "HP"
    elif choice_stat == 2:
        stat = "Attack"
    elif choice_stat == 3:
        stat = "Defense"
    elif choice_stat == 4:
        stat = "Sp. Attack"
    elif choice_stat == 5:
        stat = "Sp. Defense"
    else:
        stat = "Speed"

    sorted_stat = sorted(data, key=lambda d: d["base"][stat], reverse=reverse)
    return sorted_stat


# Sorting data by type  / reverse=True (Optional)
def sorting_type(reverse=False):
    sorted_type = sorted(data, key=lambda d: d["type"], reverse=reverse)
    return sorted_type


# Printing function
def print_data(data_display):
    for i in data_display:
        print(colored("ID:", "red"), i.get("id"),
              colored("\n Name:     [English]:", "red"), i.get("name").get("english"), colored("[French]:", "red"), i.get("name").get("french"),
              colored("[Chinese]:", "red"), i.get("name").get("chinese"), colored("[Japanese]:", "red"), i.get("name").get("japanese"),
              colored("\n Type:", "blue"), *i.get("type"),
              "\n    HP:", colored(i.get("base").get("HP"), "green"),
              "\n    Attack:", colored(i.get("base").get("Attack"), "green"),
              "\n    Defense:", colored(i.get("base").get("Defense"), "green"),
              "\n    Sp. Attack:", colored(i.get("base").get("Sp. Attack"), "green"),
              "\n    Sp. Defense:", colored(i.get("base").get("Sp. Defense"), "green"),
              "\n    Speed:", colored(i.get("base").get("Speed"), "green"))
        print()


def navigate(menu_option):
    while True:
        option_list = [i for i in menu_option[1:] if type(i) == str]
        print("--   Sort by " + menu_option[0] + "   --\n")
        for i in range(1, menu_option[1]):
            print(" " + str(i) + "- " + option_list[i-1])

        user_choice = input("\n ")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Valid number, please")
            continue
        if 0 < user_choice <= menu_option[1]:
            print("ok")
        else:
            print("Valid range, please")


def main():
    while True:     # Start main menu
        print("--   POKEDEX   --\n")
        print(" 1- Sort by name")
        print(" 2- Sort by ID")
        print(" 3- Sort by stats")
        print(" 4- Best or worst stats")
        print(" 5- Exit")
        user_choice = input("\n ")
        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Valid number, please")
            continue
        if 0 < user_choice <= 4:
            while True:
                if user_choice == 1:    # User choose sorting by name
                    print("--   Sort by name   --\n")
                    print(" 1- English")
                    print(" 2- French")
                    print(" 3- Chinese")
                    print(" 4- Japanese")
                    print(" 5- Back to main menu")
                    user_choice_name = input("\n ")
                    try:
                        user_choice_name = int(user_choice_name)
                    except ValueError:
                        print("Valid number, please")
                        continue
                    if 0 <= user_choice_name <= 5:
                        if user_choice_name == 5:
                            break
                        else:
                            reverse_choice = input("Crescent order (AnyKey + Enter) or decreasing order (Enter):")
                            if reverse_choice:
                                x = False
                            else:
                                x = True
                            print_data(sorting_name(user_choice_name, x))
                            input("Press AnyKey")
                    else:
                        print("Valid range, please")
                elif user_choice == 2:  # User choose sorting by ID
                    print("--   Sort by ID   --\n")
                    reverse_choice = input("Crescent order (AnyKey + Enter) or decreasing order (Enter):")
                    if reverse_choice:
                        x = False
                    else:
                        x = True
                    print_data(sorting_id(x))
                    input("Press AnyKey")
                    break
                elif user_choice == 3:  # User choose sorting by stats
                    print("--   Sort by stats   --\n")
                    reverse_choice
                else:
                    break   # End sorting by name menu
        elif user_choice == 5:
            break   # End main menu
        else:
            print("Valid range, please")


# main()
stats_menu = ["Sort by stats", 7, "HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]
main_menu = ["POKEDEX", 5, "Sort by name", "Sort by ID", "Sort by stats", "Best or worst stats"]
navigate(stats_menu)
