# The purpose of this python file is to be a repository for different functions dealing with game menus


# Standard imports from python library
import time

# inter-application imports


# Definition of general menu display function below. Purpose is to be used to call a menu option from any menu in the game
def display_menu_options(options: list, menu_title: str):
    while True:
        print(menu_title + "\n")

        for i in range(len(options)):
            print(str(i + 1) + "-" + options[i])

        print("\n")
        user_choice = input("Selection: ")

        # Checks for input being a digit
        if user_choice.isnumeric() == True:
            pass
        else:
            print("You must use an integer to select a menu option!\n\n")
            time.sleep(1)
            continue

        if 0 < int(user_choice) <= len(options):
            print(options[int(user_choice) - 1] + " selected!\n\n")
            time.sleep(1)
            return user_choice
            break

        else:
            print("You must select a valid menu option!\n\n")
            time.sleep(1)
            continue




