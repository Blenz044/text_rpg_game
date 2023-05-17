# The purpose of this file is to be a repository for save and load items to be used in the main program

# General Python Data import
import json


# The purpose of this class is to create a character save class to be utilized instead of a dictionary
class character_save_data_class:
    def __init__(self, file_x: dict):
        self.name = file_x["name"]
        self.current_hp = file_x["current_hp"]
        self.current_location = file_x["current_location"]

    def dictionary_converter(self):
        save_data = {}
        save_data["name"] = self.name
        save_data["current_hp"] = self.current_hp
        save_data["current_location"] = self.current_location
        return save_data


# This function serves to load a game file into your current game dictionary from a Json file
def load_game_file(file_x_save: str):
    with open("imports/save_data/" + file_x_save + ".json", "r") as file:
        file_data = json.load(file)
        file_save = character_save_data_class(file_data)
        return file_save


# This is meant to be a function defined to save the game file with proper json arrangement to the json save
def save_game_file(file_x_save_data: classmethod, file_x_save: str):
    save_data = file_x_save_data.dictionary_converter()
    with open(
        "imports/save_data/" + file_x_save + ".json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(save_data, file, ensure_ascii=False, indent=4)


# This Function is designed to erase save data and restore a file to it's default setting
def delete_file(file_x_save_data: classmethod, file_x_save: str):

    save_data = file_x_save_data.dictionary_converter()

    save_data["name"] = "Empty"
    save_data["current_hp"] = 10
    save_data["current_location"] = "Tutorial"


    with open(
        "imports/save_data/" + file_x_save + ".json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(save_data, file, ensure_ascii=False, indent=4)
