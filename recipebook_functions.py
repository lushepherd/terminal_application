from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from tinydb import TinyDB, Query
from fpdf import FPDF

# User needs to be able to create a recipe under a category with name/ ingredients/ method
# Needs to be able to be modified/ deleted/ browsed/ searched/ exported to PDF

db = TinyDB("recipes_db.json")

def select_category():
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    return inquirer.rawlist(
        message="Select a category or 'Exit' to cancel",
        choices=categories
    ).execute()

def validate_input(result):
    return len(result) > 0

def input_text(message, validate):
    return inquirer.text(
        message=message,
        validate=validate,
        invalid_message="Input cannot be empty."
    ).execute()

def select_recipe(category, db):
    category_recipes = db.table(category).all()

    if not category_recipes:
        print(f"No recipes found in the {category} category.")
        return None

    sorted_recipes = sorted(category_recipes, key=lambda x: x["recipe_name"].lower())

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"]) for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message="Select a recipe:",
        choices=recipe_choices
    ).execute()

    return sorted_recipes[selected_recipe_index] if selected_recipe_index is not None else None

def add_recipe():
    """
    This function allows the user to add a new recipe to a category of their choosing.
    
    After selecting a category, they are prompted to enter a recipe name, ingredients and a method.
    This recipe is then added to the database under the category.
    """

    category = select_category()

    if category == "Exit":
        print("Selection canceled.")
        return

    exit_flag = False

    while not exit_flag:
        recipe_name = input_text("Enter the recipe name or 'exit' to cancel:", lambda result: len(result) > 0)

        if recipe_name.lower() == 'exit':
            print("Recipe add canceled.")
            exit_flag = True
            return

        ingredients = input_text("Enter the ingredients separated by commas:", lambda result: len(result) > 0).split(',')

        if 'exit' in ingredients:
            print("Recipe add canceled.")
            exit_flag = True
            return

        method = input_text("Enter the method:", lambda result: len(result) > 0)

        if method.lower() == 'exit':
            print("Recipe add canceled.")
            exit_flag = True
            return

        recipe_data = {
            "recipe_name": recipe_name,
            "ingredients": ingredients,
            "method": method,
        }

        category_db = db.table(category)
        category_db.insert(recipe_data)

        print("Recipe added successfully!")
        return

if __name__ == "__main__":
    add_recipe()

# Modify a current recipe

def modify_recipe():
    """
    This function allows the user to modify a recipe already in the database.
    
    They are prompted to select a category then select a recipe to modify, then choose which
    part of the recipe to modify (name, ingredients, method.)
    """
    category = select_category()

    if category == "Exit":
        print("Selection canceled.")
        return
    
    selected_recipe = select_recipe(category, db)

    if selected_recipe:
        print(f"\nRecipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

        item_to_modify = inquirer.select(
            message="Select the item to modify:",
            choices=["Name", "Ingredients", "Method"]
        ).execute()

        new_value = inquirer.text(message=f"Enter the new {item_to_modify.lower()}:").execute()

        if item_to_modify == "Name":
            db.table(category).update({"recipe_name": new_value}, Query()["recipe_name"] == selected_recipe["recipe_name"])
        elif item_to_modify == "Ingredients":
            db.table(category).update({"ingredients": new_value}, Query()["ingredients"] == selected_recipe["ingredients"])
        elif item_to_modify == "Method":
            db.table(category).update({"method": new_value}, Query()["method"] == selected_recipe["method"])

        print(f"\nRecipe has been successfully updated.")

if __name__ == "__main__":
    modify_recipe()     

# Delete a recipe

def delete_recipe():
    """
    This function allows a user to delete a recipe already in the database.

    They are prompted to select a category, then a recipe to delete.
    """
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    
    category = inquirer.rawlist(
        message="Select a category to delete a recipe:",
        choices = categories
    ).execute() 

    if category == "Exit":
        print("Selection canceled.")
        return
    
    category_recipes = db.table(category).all()

    if not category_recipes:
        print(f"No recipes found in the {category} category.")
        return

    sorted_recipes = sorted(category_recipes, key=lambda x: x["recipe_name"].lower())

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"]) for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message="Select a recipe to delete:",
        choices=recipe_choices
    ).execute()

    selected_recipe = sorted_recipes[selected_recipe_index]

    db.table(category).remove(Query().recipe_name == selected_recipe["recipe_name"])
    print(f"{selected_recipe['recipe_name']} has been deleted.")

if __name__ == "__main__":
    delete_recipe()     

# View current recipes

def view_recipes():
    """
    This function allows the user to browse the current list of recipes in the database.

    They are prompted to select a category, then they can select a recipe to view.
    Displays the recipes name, ingredients and method.
    """
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    
    category = inquirer.rawlist(
        message="Select a category to view:",
        choices = categories
    ).execute() 

    if category == "Exit":
        print("Selection canceled.")
        return
    
    category_recipes = db.table(category).all()

    if not category_recipes:
        print(f"No recipes found in the {category} category.")
        return

    sorted_recipes = sorted(category_recipes, key=lambda x: x["recipe_name"].lower())

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"]) for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message="Select a recipe to view:",
        choices=recipe_choices
    ).execute()

    selected_recipe = sorted_recipes[selected_recipe_index]

    print(f"\nRecipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

if __name__ == "__main__":
    view_recipes() 

def search_recipes():
    """
    This function allows the user to search for recipes in the database by name or ingredient.

    They are prompted to enter their search term and then shown a list of recipes that match
    that they can choose from.
    """
    
    search_term = inquirer.text(
        message="Enter a recipe name or ingredient to search or type 'exit' to cancel:"
    ).execute().lower()

    if search_term == 'exit'.lower():
        print("Search canceled.")
        return

    all_recipes = []
    for category in db.tables():
        category_recipes = db.table(category).all()
        all_recipes.extend(category_recipes)

    matching_recipes = [recipe for recipe in all_recipes if search_term in recipe["recipe_name"].lower() or any(search_term in ingredient.lower() for ingredient in recipe["ingredients"])]    

    sorted_recipes = sorted(matching_recipes, key=lambda x: x["recipe_name"].lower())

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"]) for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message=f"Select a recipe from the search results (search term: {search_term}):",
        choices=recipe_choices + [Choice(value=None, name="Exit")],
    ).execute()

    if selected_recipe_index is None:
        return

    selected_recipe = sorted_recipes[selected_recipe_index]

    print(f"\nSelected Recipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

if __name__ == "__main__":
    search_recipes() 

class PDF(FPDF):
    """
    PDF class for exporting to PDF format.
    
    Inherits from FPDF and provides a template/format for the recipe to display.
    """
    def header(self):
        image_path = "images/logo.png"
        self.image(image_path, 10, 8, 33)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Your Recipe", 0, 1, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)

def export_to_pdf(recipe):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title(recipe["recipe_name"])
    pdf.chapter_body(f"Ingredients: {', '.join(recipe['ingredients'])}")
    pdf.chapter_body(f"Method: {recipe['method']}")
    pdf.output(f"{recipe['recipe_name']}_recipe.pdf")        

def export_recipe():
    """
    Allows user to export a recipe to PDF.

    They are prompted to select a category and then a recipe to export.
    Creates a PDF file with the details of the selected recipe.
    """
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    
    category = inquirer.rawlist(
        message="Select a category to view:",
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
        message="Select a recipe to view:",
        choices=recipe_choices
    ).execute()

    selected_recipe = category_recipes[selected_recipe_index]

    print(f"\nSelected Recipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

    export_to_pdf(selected_recipe)
    print(f"Recipe '{selected_recipe['recipe_name']}' exported to PDF.")

if __name__ == "__main__":
    export_recipe() 