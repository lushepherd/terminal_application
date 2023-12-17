from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from tinydb import TinyDB, Query
from fpdf import FPDF
import os

# User needs to be able to create a recipe under a category with name/ ingredients/ method
# Needs to be able to be modified/ deleted/ browsed/ searched/ exported to PDF

db = TinyDB("recipes_db.json")

# Select category function used across most features


def select_category():
    categories = ["Breakfast", "Lunch", "Dinner", "Snacks", "Dessert", "Exit"]
    selected_category = inquirer.rawlist(
        message="Select a category or 'Exit' to cancel",
        choices=categories
    ).execute()

    if selected_category == "Exit":
        clear_screen()
        return None

    return selected_category

# Displays an error if user input is empty
# Catches potential errors during input handling, and input validation is handled by the inquirerpy inquirer.text function


def validate_input(result):
    return len(result) > 0


def input_text(message, validate):
    try:
        return inquirer.text(
            message=message,
            validate=validate,
            invalid_message="Input cannot be empty."
        ).execute()
    except Exception:
        pass

# Function that allows you to select a category and returns an error if no recipes
# Used in functions that require recipe retrieval - modify recipe, view recipe, delete recipe, export recipe
# Returns the names of recipes in the category in alphabetical order using the sort function


def select_recipe(category, db):
    category_recipes = db.table(category).all()

    if not category_recipes:
        print(f"No recipes found in the {category} category.")
        return None

    sorted_recipes = sorted(
        category_recipes, key=lambda x: x["recipe_name"].lower())

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"])
                      for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message="Select a recipe:",
        choices=recipe_choices
    ).execute()

    return sorted_recipes[selected_recipe_index]

def clear_screen():
    os.system('clear')


def get_recipe_details():
    """
    Get recipe details before add function
    Accepts user input of recipe name, ingredients, method and checks at each stage if the input is exit, in which case it returns to the main menu
    """
    def input_or_exit(message):
        user_input = input_text(message, validate_input)
        return None if user_input.lower() == 'exit' else user_input

    recipe_name = input_or_exit("Enter the recipe name or 'exit' to cancel:")
    if recipe_name is None:
        clear_screen()
        print("Recipe add canceled.")
        return None

    ingredients = input_or_exit("Enter the ingredients separated by commas:")
    if ingredients is None or 'exit' in ingredients:
        clear_screen()
        print("Recipe add canceled.")
        return None
    ingredients = ingredients.split(',')

    method = input_or_exit("Enter the method:")
    if method is None:
        clear_screen()
        print("Recipe add canceled.")
        return None

    return {
        "recipe_name": recipe_name,
        "ingredients": ingredients,
        "method": method,
    }

# Add recipe


def add_recipe():
    """
    This function allows the user to add a new recipe to a category of their choosing.

    After selecting a category, they are prompted to enter a recipe name, ingredients and a method.
    This recipe is then added to the database under the chosen category.
    Users can select exit or type as input at each stage to return to the main menu.
    """
    category = select_category()

    if category is None:
        print("Recipe add canceled.")
        return

    recipe_data = get_recipe_details()

    if recipe_data is not None:
        category_db = db.table(category)
        category_db.insert(recipe_data)
        print("Recipe added successfully!")

    if recipe_data is not None:
        clear_screen()
        print("Recipe added successfully!")


if __name__ == "__main__":
    add_recipe()

# Modify a current recipe


def modify_recipe():
    """
    This function allows the user to modify a recipe already in the database.

    They are prompted to select a category then select a recipe to modify, then choose which
    part of the recipe to modify (name, ingredients, method.)
    Users can cancel out with the exit option. 
    If the selected category is empty it will return an error.
    """
    category = select_category()

    if category is None:
        clear_screen()
        print("Recipe modify canceled.")
        return

    selected_recipe = select_recipe(category, db)

    # Prints the selected recipe then prompts the user for which details they would like to modify

    if selected_recipe:
        print(
            f"\nRecipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

        item_to_modify = inquirer.select(
            message="Select the item to modify:",
            choices=["Name", "Ingredients", "Method"]
        ).execute()

        new_value = inquirer.text(
            message=f"Enter the new {item_to_modify.lower()}:").execute()

        if item_to_modify == "Name":
            db.table(category).update({"recipe_name": new_value}, Query()[
                "recipe_name"] == selected_recipe["recipe_name"])
        elif item_to_modify == "Ingredients":
            db.table(category).update({"ingredients": new_value}, Query()[
                "ingredients"] == selected_recipe["ingredients"])
        elif item_to_modify == "Method":
            db.table(category).update({"method": new_value}, Query()[
                "method"] == selected_recipe["method"])

        # Prints confirmation message once completed
        clear_screen()
        print(f"\nRecipe has been successfully updated.")


if __name__ == "__main__":
    modify_recipe()

# Delete a recipe


def delete_recipe():
    """
    This function allows a user to delete a recipe already in the database.
    They are prompted to select a category, then a recipe to delete.
    The user can exit using the "exit" option.
    If the chosen category is empty, it will return an error.
    """
    category = select_category()

    if category is None:
        clear_screen()
        print("Recipe delete canceled.")
        return

    selected_recipe = select_recipe(category, db)

    # Selected recipe is deleted and confirmation provided to the user.

    if selected_recipe:
        db.table(category).remove(Query().recipe_name == selected_recipe["recipe_name"])
        clear_screen()
        print(f"{selected_recipe['recipe_name']} has been deleted.")


if __name__ == "__main__":
    delete_recipe()

# View current recipes


def view_recipes():
    """
    This function allows the user to browse the current list of recipes in the database.

    They are prompted to select a category, then they can select a recipe to view.
    Displays the recipes name, ingredients and method.
    The user can exit using the "exit" option.
    If the category is empty, it will return an error.

    """
    category = select_category()

    if category is None:
        clear_screen()
        print("Recipe view canceled.")
        return

    selected_recipe = select_recipe(category, db)

    # Prints selected recipe details - recipe name, ingredients, method.

    if selected_recipe:
        clear_screen()
        print(
            f"\nRecipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")


if __name__ == "__main__":
    view_recipes()


def search_recipes():
    """
    This function allows the user to search for recipes in the database by name or ingredient.

    They are prompted to enter their search term and then shown a list of recipes that match
    that they can choose from that are sorted alphabetically.
    The search input isn't case sensitive to provide a more user-friendly experience.

    If the user types "exit" it will return to the main menu.
    """
    search_term = inquirer.text(
        message="Enter a recipe name or ingredient to search or type 'exit' to cancel:"
    ).execute().lower()

    if search_term == 'exit'.lower():
        clear_screen()
        print("Recipe search canceled.")
        return

    # Gets all recipes in the database

    all_recipes = []
    for category in db.tables():
        category_recipes = db.table(category).all()
        all_recipes.extend(category_recipes)

    # Creates a new list (matching_recipes) containing only recipes from all_recipes that meet the specified conditions
    # Conditions = if search_term in recipe (recipe_name, ingredient) matches, it will be included in the matching_recipe list
    matching_recipes = [recipe for recipe in all_recipes if search_term in recipe["recipe_name"].lower(
    ) or any(search_term in ingredient.lower() for ingredient in recipe["ingredients"])]

    sorted_recipes = sorted(
        matching_recipes, key=lambda x: x["recipe_name"].lower())

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"])
                      for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message=f"Select a recipe from the search results (search term: {search_term}):",
        choices=recipe_choices + [Choice(value=None, name="Exit")],
    ).execute()

    if selected_recipe_index is None:
        return

    selected_recipe = sorted_recipes[selected_recipe_index]

    clear_screen()

    print(
        f"\nSelected Recipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")


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
    The user can exit using the "exit" option.
    If the category is empty, it will return an error.
    """
    category = select_category()

    if category is None:
        clear_screen()
        print("Recipe export canceled.")
        return

    selected_recipe = select_recipe(category, db)

    # Exports selected_recipe to PDF and prints a confirmation statement to the user.

    if selected_recipe is not None:
        clear_screen()
        export_to_pdf(selected_recipe)
        print(
            f"Recipe '{selected_recipe['recipe_name']}' successfully exported to PDF.")


if __name__ == "__main__":
    export_recipe()
