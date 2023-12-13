from InquirerPy import inquirer
from rich.console import Console
from rich.markdown import Markdown
from InquirerPy import prompt
from recipebook_functions import add_recipe, modify_recipe, delete_recipe, current_recipes, search_recipes, export_recipe
# Pep 8 guide states imports should go 1. Standard library imports, 2. Related third party imports, 3. Local application/ library specific imports

"""
Your Recipe Book

A terminal application that allows the user to create and manage a recipe book.
They can add, modify, delete, browse, search, and export recipes to PDF.

"""

MARKDOWN = """
# 🥗 🍔 Welcome to Your Recipe Book! 🍰 🍨
"""
console = Console()
md = Markdown(MARKDOWN)
console.print(md)

def option_menu():
    """
    The main menu that handles user interaction.

    Continually prompts the user for input until they choose to exit.
    Calls the corresponding function based on the user's selection.
    """

    while True:
        choices = [
            "➕ Add a new recipe",
            "✏️  Modify a recipe",
            "❌ Delete a recipe",
            "🧐 View your current recipes",
            "🔍 Search for a recipe",
            "📄 Export to PDF",
            "Exit",
        ]
            
        action = inquirer.rawlist(
            message="Please select an option from the menu:",
            choices = choices
        ).execute()

        if action == "Exit":
            print("\nThank you for using Your Recipe Book!")
            print("\n༼ つ ◕_◕ ༽つ🍰🍔🍕\n")
            break

        if action:
            users_selection = choices.index(action) + 1
            if users_selection == 1:
                add_recipe()
            elif users_selection == 2:
                modify_recipe()
            elif users_selection == 3:
                delete_recipe()
            elif users_selection == 4:
                current_recipes()
            elif users_selection == 5:
                search_recipes()
            elif users_selection == 6:
                export_recipe()
            else:
                print("Invalid Input")

if __name__ == "__main__":
    option_menu()