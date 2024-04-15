import csv
from recipe_manager import RecipeManager


def save_recipes(file_name):
    with open(file_name, "w", newline="") as file:
        file.truncate(0) 
        writer = csv.writer(file)
        for recipe in RecipeManager.recipes:            
            writer.writerow([
                recipe.title, 
                recipe.ingredients, 
                recipe.steps
                ])


def load_recipes(file_name):
    with open(file_name) as file:
        reader = csv.reader(file)
        for recipe in reader:
            try:
                title, ingredients, steps = recipe
                RecipeManager.close_editor(
                    title=title, 
                    ingredients=ingredients, 
                    steps=steps
                    )
            except:
                pass
            