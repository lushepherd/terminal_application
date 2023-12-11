from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from tinydb import TinyDB, Query

# User needs to be able to create a recipe under a category with name/ ingredients/ method
# Needs to be able to be modified/ deleted/ browsed/ searched/ exported to PDF

db = TinyDB("recipes_db.json")

def add_recipe():
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]

    category = inquirer.rawlist(
            message = "Select a category or 'Exit' to cancel",
            choices = categories
    ).execute()
    
    if category == "Exit":
        print("Selection canceled.")
        return
    
    name = inquirer.text(message="Enter the recipe name:").execute()

    ingredients = inquirer.text(message="Enter the ingredients separated by commas:").execute().split(',')

    method = inquirer.text(message="Enter the method:").execute()

    recipe_data = {
            "recipe_category": category,
            "recipe_name": name,
            "ingredients": ingredients,
            "method": method,
        }
    
    category_db = db.table(category)
    category_db.insert(recipe_data)

    print("Recipe added successfully!")

if __name__ == "__main__":
    add_recipe()    

def modify_recipe():
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    
    category = inquirer.rawlist(
        message="Select a category to modify a recipe:",
        choices=categories
    ).execute() 

    if category == "Exit":
        print("Selection canceled.")
        return

def delete_recipe():
    pass

def current_recipes():
    pass

def search_recipes():
    pass

def export_recipe():
    pass