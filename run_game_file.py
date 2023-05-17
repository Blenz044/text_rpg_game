# The purpose of this file is to be the main file that is used as the only file to run the game
# Functions are stored in other parts of this application and are imported here in order to be utilized

# For now this file will serve as a testing grounds for multiple parts of the application
# As new files are created to be imported they will be added here 

# Built-in Python module imports


# Inter-Application imports
from imports.save_and_load_functions import load_game_file, character_save_data_class, save_game_file, delete_file
from imports.menu_list import main_menu, file_empty




# Loading all file data prior to game initiation
file_1_save_data = load_game_file("file_1_save")
file_2_save_data = load_game_file("file_2_save")
file_3_save_data = load_game_file("file_3_save")



# Games master loading list
master_load_list = (
    "file_1_not_empty",
    "file_1_empty",
    "file_2_not_empty",
    "file_2_empty",
    "file_3_not_empty",
    "file_3_empty",
    "main_menu",
)

# Definition of the main game's router
def game_router():
    next_load = "main_menu"
    while True:
        if next_load == "file_1_empty":
            next_load = file_empty(file_1_save_data)

        elif next_load == "file_1_not_empty":
            pass

        elif next_load == "file_2_empty":
            next_load = file_empty(file_2_save_data)

        elif next_load == "file_2_not_empty":
            pass

        elif next_load == "file_3_empty":
            next_load = file_empty(file_3_save_data)

        elif next_load == "file_3_not_empty":
            pass

        elif next_load == "main_menu":
            next_load = main_menu(file_1_save_data, file_2_save_data, file_3_save_data)
        
        else:
            print("Something went wrong navigating to the proper menu! Terminating the program to prevent an infinite loop!")
            quit()


# Initialization of Games Main Menu
print("\n\n\n\n")
game_router()
