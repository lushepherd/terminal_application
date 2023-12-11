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

if __name__ == "__main__":
    add_recipe()    

def modify_recipe():
    pass 

def delete_recipe():
    pass

def current_recipes():
    pass

def search_recipes():
    pass

def export_recipe():
    pass