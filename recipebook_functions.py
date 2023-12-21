import os
import sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from tinydb import TinyDB, Query
from fpdf import FPDF

# User needs to be able to create a recipe under a category with name/ ingredients/ method
# Needs to be able to be modified/ deleted/ browsed/ searched/ exported to PDF

db = TinyDB("recipes_db.json")

# Clears the screen after completing a function


def clear_screen():
    os.system("clear")

# Exit message function used to clear screen and print exit message either at the end of a function
# or when a user selects exit


def exit_message(message):
    clear_screen()
    print(message)

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

# Exit handler


def user_exit(category, error_message):
    if category is None:
        exit_message(error_message)
        return True
    return False

# Displays an error if user input is empty
# Catches potential errors during input handling, and input validation is handled by the inquirerpy inquirer.text function


def validate_input(result):
    return len(result) > 0


def input_text(message, validate):
    while True:
        user_input = inquirer.text(
            message=message,
            validate=validate,
            invalid_message="Did you just try to add a recipe of nothing? Spice it up with some text, chef!"
        ).execute()

        if user_input:
            return user_input

# Function that allows you to select a category and returns an error if no recipes
# Used in functions that require recipe retrieval - modify recipe, view recipe, delete recipe, export recipe
# Returns the names of recipes in the category in alphabetical order using the sort function


def select_recipe(category, db):
    category_recipes = db.table(category).all()

    if not category_recipes:
        exit_message(
            f"Oops, the {category} category is as empty as my fridge.")
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

# Creates a new list (all_recipes) containing only recipes from all_recipes that meet the specified conditions
# Used in the search_recipes function and for checking for duplicate names in the add_recipe function


def get_all_recipes():
    all_recipes = []
    for category in db.tables():
        category_recipes = db.table(category).all()
        all_recipes.extend(category_recipes)
    return all_recipes

# Checks for any matching recipe names when a user adds a new recipe


def recipe_name_already_exists(recipe_name):
    all_recipes = get_all_recipes()
    same_recipe_name = recipe_name.lower()

    return any(same_recipe_name == recipe["recipe_name"].lower() for recipe in all_recipes)


def get_recipe_details(error_message="Recipe add canceled. Oh, the culinary world will surely mourn the loss of this masterpiece."):
    """
    Get recipe details before the add function
    Accepts user input of recipe name, ingredients, and method.
    Checks at each stage if the input is 'exit', in which case it returns to the main menu.
    Displays an error if the recipe name already exists in any category.
    """
    while True:
        def input_or_exit(message):
            user_input = input_text(message, validate_input)
            return None if user_input.lower() == 'exit' else user_input

        recipe_name = input_or_exit(
            "Enter the recipe name or 'exit' to cancel:")
        if recipe_name is None:
            exit_message(error_message)
            return None

        if recipe_name_already_exists(recipe_name):
            exit_message(
                f"Nope. '{recipe_name}' already exists. Try again (or not).")
        else:
            break

    ingredients = input_or_exit("Enter the ingredients separated by commas:")
    if ingredients is None:
        exit_message(error_message)
        return None
    ingredients = ingredients.split(',')

    method = input_or_exit("Enter the method:")
    if method is None:
        exit_message(error_message)
        return None

    return {
        "recipe_name": recipe_name,
        "ingredients": ingredients,
        "method": method,
    }


def add_recipe():
    """
    Adds a new recipe to the category selected by the user.
    If exit is typed, an exit message is displayed.
    If a recipe with a name matching the database is entered, an error is displayed.
    The recipe is inserted into the database and prints a confirmation.
    """
    category = select_category()

    error_message = "Recipe add canceled. Oh, the culinary world will surely mourn the loss of this masterpiece."

    # Error message prints if user types "exit" at any input step (name, ingredients, method)

    if user_exit(category, error_message):
        return

    # Checks DB for recipes with the same name - if any are found, user is prompted to enter a different name

    recipe_data = get_recipe_details(error_message)

    # If recipe name, ingredients, and method are entered the details are added to the database

    if recipe_data is not None:
        category_db = db.table(category)
        category_db.insert(recipe_data)
        exit_message("Boom! Recipe added! 🤜🤛")

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

    error_message = "Recipe modify canceled. It's not you; it's the recipe. It just wasn't ready for your brilliance."

    # If user selects exit, error message is printed.

    if user_exit(category, error_message):
        return

    selected_recipe = select_recipe(category, db)

    # Prints the selected recipe then prompts the user to confirm they would like to modify recipe
    # Prompts the user for which details they would like to modify

    if selected_recipe:
        print(
            f"\nRecipe Details:\nName: {selected_recipe['recipe_name']}\nIngredients: {selected_recipe['ingredients']}\nMethod: {selected_recipe['method']}")

        # Confirms if the user would like to modify selected recipe
        # If Y, prompts them to select what item they would like to modify
        # If N, prints exit message

        confirm_modify = inquirer.confirm(
            message="Are you sure you want to modify this recipe?"
        ).execute()

        if not confirm_modify:
            exit_message("Recipe modify canceled. I too fear change.")
            return

        item_to_modify = inquirer.select(
            message="Select the item to modify:",
            choices=["Name", "Ingredients", "Method"]
        ).execute()

        new_value = inquirer.text(
            message=f"Enter the new {item_to_modify.lower()}:").execute()

        # Updates the selected item in DB (name, ingredients, method)

        if item_to_modify == "Name":
            db.table(category).update({"recipe_name": new_value}, Query()[
                "recipe_name"] == selected_recipe["recipe_name"])
        elif item_to_modify == "Ingredients":
            db.table(category).update({"ingredients": new_value}, Query()[
                "ingredients"] == selected_recipe["ingredients"])
        elif item_to_modify == "Method":
            db.table(category).update({"method": new_value}, Query()[
                "method"] == selected_recipe["method"])

        exit_message(f"Boom! Recipe updated. 🤜🤛")


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

    error_message = "Recipe delete canceled. Because recipes have feelings too, right?"

    if user_exit(category, error_message):
        return

    selected_recipe = select_recipe(category, db)

    if selected_recipe:
        confirm_delete = inquirer.confirm(
            message=f"Are you sure you want to delete {selected_recipe['recipe_name']}?"
        ).execute()

        if not confirm_delete:
            exit_message(
                "Recipe delete canceled. Your recipe has been spared (for now)")
            return

        # Delete the selected recipe
        db.table(category).remove(Query().recipe_name ==
                                  selected_recipe["recipe_name"])
        exit_message(
            f"{selected_recipe['recipe_name']} has been deleted. It's now off to the recipe retirement home in the cloud.")


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

    error_message = "Recipe view canceled. Do you trust your memory or are you ordering pizza?"

    if user_exit(category, error_message):
        return

    selected_recipe = select_recipe(category, db)

    # Prints selected recipe details - recipe name, ingredients, method.

    if selected_recipe:
        exit_message(
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
    # Validates user input. 0 = false - if no input, will return error message above.

    while True:
        search_term = inquirer.text(
            message="Enter a recipe name or ingredient to search or type 'exit' to cancel:",
            validate=validate_input,
            invalid_message="Searching for the recipe to make air today, are we?"
        ).execute().lower()

        if search_term == 'exit':
            exit_message("Recipe search canceled. Winging it today, are we?")
            return

        # Gets all recipes in the database

        all_recipes = get_all_recipes()

        # Conditions = if search_term in recipe (recipe_name, ingredient) matches, it will be included in the matching_recipe list

        matching_recipes = [recipe for recipe in all_recipes if search_term in recipe["recipe_name"].lower(
        ) or any(search_term in ingredient.lower() for ingredient in recipe["ingredients"])]

        # Error handler - if no recipes match search term, returns error.

        if not matching_recipes:
            exit_message(
                f"Uhh no recipes with {search_term} here. Have you added any yet? Awkward.")
        else:
            break

    # Sorts search results alphabetically and case insensitive

    sorted_recipes = sorted(
        matching_recipes, key=lambda x: x["recipe_name"].lower())

    # Displays the choices by recipe name

    recipe_choices = [Choice(value=index, name=recipe["recipe_name"])
                      for index, recipe in enumerate(sorted_recipes)]

    selected_recipe_index = inquirer.select(
        message=f"Select a recipe from the search results (search term: {search_term}):",
        choices=recipe_choices,
    ).execute()

    selected_recipe = sorted_recipes[selected_recipe_index]

    # Clears the screen and prints the recipe to view

    exit_message(
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

    ingredients = ', '.join(recipe['ingredients'])
    method = recipe['method']

    try:
        pdf.chapter_body(f"Ingredients: {ingredients}")
        pdf.chapter_body(f"Method: {method}")
        pdf.output(f"{recipe['recipe_name']}_recipe.pdf")
    except UnicodeEncodeError as e:
        error_message = (
            "Error exporting recipe to PDF. Please remove any special characters and try again."
        )
        print(error_message)
        print(f"Error details: {str(e)}")
        raise


def export_recipe():
    """
    Allows user to export a recipe to PDF.

    They are prompted to select a category and then a recipe to export.
    Creates a PDF file with the details of the selected recipe.
    The user can exit using the "exit" option.
    If the category is empty, it will return an error.
    """
    category = select_category()

    error_message = "Recipe export canceled. Not the right time to leave the nest?"

    if user_exit(category, error_message):
        return

    selected_recipe = select_recipe(category, db)

    if selected_recipe is not None:
        try:
            export_to_pdf(selected_recipe)
            exit_message(
                f"Your recipe has achieved its lifelong dream of becoming a PDF. It's all grown up now and ready for the outside world.")
        except UnicodeEncodeError as e:
            # Catch UnicodeEncodeError
            # Prints error message and returns to main menu
            pass

if __name__ == "__main__":
    export_recipe()
