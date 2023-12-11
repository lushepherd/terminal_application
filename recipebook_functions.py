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
    
    recipe_name = inquirer.text(message="Enter the recipe name:").execute()

    ingredients = inquirer.text(message="Enter the ingredients separated by commas:").execute().split(',')

    method = inquirer.text(message="Enter the method:").execute()

    recipe_data = {
            "recipe_category": category,
            "recipe_name": recipe_name,
            "ingredients": ingredients,
            "method": method,
        }
    
    category_db = db.table(category)
    category_db.insert(recipe_data)

    print("Recipe added successfully!")

if __name__ == "__main__":
    add_recipe()  

# Modify a current recipe

def modify_recipe():
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    
    category = inquirer.rawlist(
        message="Select a category to modify a recipe:",
        choices = categories
    ).execute() 

    if category == "Exit":
        print("Selection canceled.")
        return
    
    category_recipes = db.table(category).all()

    if not category_recipes:
        print(f"No recipes found in the {category} category.")
        return

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"]) for index, recipe in enumerate(category_recipes)]

    selected_recipe_index = inquirer.select(
        message="Select a recipe to modify:",
        choices=recipe_choices
    ).execute()

    selected_recipe = category_recipes[selected_recipe_index]

    print(f"\nRecipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

    item_to_modify = inquirer.select(
        message="Select the item to modify:",
        choices=[
            "Name", 
            "Ingredients", 
            "Method"
    ]
    ).execute()

    new_value = inquirer.text(message=f"Enter the new {item_to_modify.lower()}:").execute()

    if item_to_modify == "Name":
        db.table(category).upsert({"recipe_name": new_value}, Query()["recipe_name"] == selected_recipe["recipe_name"])
    elif item_to_modify == "Ingredients":
        db.table(category).upsert({"ingredients": new_value}, Query()["ingredients"] == selected_recipe["ingredients"])
    elif item_to_modify == "Method":
        db.table(category).upsert({"method": new_value}, Query()["method"] == selected_recipe["method"])   

    print(f"\nRecipe has been successfully updated.")

def delete_recipe():
    pass

def current_recipes():
    pass

def search_recipes():
    pass

def export_recipe():
    pass