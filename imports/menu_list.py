# The purpose of this file is to be a list of all available menus that can be called upon with the main game file

# General python imports


# Inter-application imports
from imports.menu_functions import display_menu_options

# master menu list
# master_menu_list = [
#     "file_1_not_empty",
#     "file_1_empty",
#     "file_2_not_empty",
#     "file_2_empty",
#     "file_3_not_empty",
#     "file_3_empty",
# ]



def main_menu(file_x_save_data: classmethod, file_y_save_data: classmethod, file_z_save_data: classmethod):
    user_selection = display_menu_options(
        [
            "File 1 (" + file_x_save_data.name + ")",
            "File 2 (" + file_y_save_data.name + ")",
            "File 3 (" + file_z_save_data.name + ")",
            "Exit Game"
        ],
        "MAIN MENU",
    )
    
    menu_router = ""
    if user_selection == str(1) and file_x_save_data.name == "Empty":
        menu_router = "file_1_empty"
        return menu_router

    elif user_selection == str(1) and file_x_save_data.name != "Empty":
        menu_router = "file_1_not_empty"
        return menu_router

    elif user_selection == str(2) and file_y_save_data.name == "Empty":
        menu_router = "file_2_empty"
        return menu_router

    elif user_selection == str(2) and file_y_save_data.name != "Empty":
        menu_router = "file_2_not_empty"
        return menu_router

    elif user_selection == str(3) and file_z_save_data.name == "Empty":
        menu_router = "file_3_empty"
        return menu_router

    elif user_selection == str(3) and file_z_save_data.name != "Empty":
        menu_router = "file_3_not_empty"
        return menu_router

    else:
        print("Thanks for playing! Now exiting the game!")
        quit()


# This function serves as a menu for a file that is empty when selected from the main menu
def file_empty(file_x_save_data: classmethod):
    user_selection = display_menu_options(["Start New Game", "Back"], "File: "+file_x_save_data.name)

    menu_router = ""
    if user_selection == str(1):
        print("Beginning a new adventure...")
        menu_router = file_x_save_data.current_location
        return menu_router
    
    else:
        menu_router = "main_menu"
        return menu_router



    