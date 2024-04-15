import csv
import customtkinter as ctk
from unittest.mock import Mock
from ui_test import create_window, load, save


def test_create_window():
    # Call create_window
    window = create_window()

    # See if it returns a ctk.CTk (have no idea how else to test the widgets/windows)
    assert isinstance(window, ctk.CTk)


def test_load():
    from recipe_manager import RecipeManager
    from recipe import Recipe
    from recipe_ui import RecipeUI
    
    # Makes a mock file
    mock_file = "mock_file.csv"
    
    # Adds to the file data that would represent a recipe
    recipe_data = [
        ["Title1", "Ingredients1", "Steps1"],
        ["Title2", "Ingredients2", "Steps2"],
        ["Title3", "Ingredients3", "Steps3"]
    ]
    with open(mock_file, "w") as file:
        writer = csv.writer(file)
        writer.writerows(recipe_data)

    # Replaces the add method in RecipeManager with a mock version
    RecipeManager.add = Mock()

    # Should load the recipes and add them to the recipes list inside RecipeManager
    load(mock_file)

    # Read the number of lines in the CSV file, excluding newline characters
    with open(mock_file) as file:
        num_lines = sum(1 for _ in file)

    # Assert that the add function in RecipeManager was called
    # the same amount of times as there are lines in the mock_file
    assert RecipeManager.add.call_count == num_lines

    # Goes over all the arguments passed to the add function
    for call_args in RecipeManager.add.call_args_list:        
        recipe_args = call_args[0] # Gets the first argument (happens to be a tuple for some reason)     
        recipe = recipe_args[1]  # Gets the second argument in the tuple (should be the Recipe obj or RecipeUI obj)
        try:
            assert isinstance(recipe, Recipe)  # Checks if a Recipe object was passed
        except:
            assert isinstance(recipe, RecipeUI)
    

def test_save():
    from recipe_manager import RecipeManager
    from recipe import Recipe

    # Makes a mock file
    mock_file = "mock_file.csv"
    
    # Data that would make up a recipe
    recipe_data = [
        ["Title1", "Ingredients1", "Steps1"],
        ["Title2", "Ingredients2", "Steps2"]
    ]
    
    # Adds data directly into the RecipeManager list of recipes
    RecipeManager.recipes = [
        Recipe(
            title=title, 
            ingredients=ingredients, 
            steps=steps
            ) 
        for title, ingredients, steps in recipe_data
        ]

    # Should save the recipe data into the mock file
    save(mock_file)
    
    # Opens the file to check if the data was stored there
    with open(mock_file) as file:
        for line in file.readlines(): # for each line in the file
            saved_content = [line.strip().split(",")] # get whats stored in the line
            assert saved_content[0] in recipe_data # check if it is in the original data

