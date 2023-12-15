from InquirerPy import inquirer
from rich.console import Console
from rich import print
from rich.style import Style
from rich.markdown import Markdown
from recipebook_functions import add_recipe, modify_recipe, delete_recipe, view_recipes, search_recipes, export_recipe
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
console.print(md, style="cornsilk1 on dark_sea_green3")


def option_menu():
    """
    The main menu that handles user interaction.

    Continually prompts the user for input until they choose to exit.
    Calls the corresponding function based on the user's selection.
    """
    menu_item_style = Style(bgcolor="cornsilk1", color="dark_orange")
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
            choices=choices
        ).execute()

        if action == "Exit":
            MARKDOWN = """
            Thank you for using Your Recipe Book!

            ༼ つ ◕_◕ ༽つ🍰🍔🍕

            Github: https://github.com/lushepherd
            Linkedin: https://www.linkedin.com/in/lucy-shepherd-44236928a/
            """
            console = Console()
            md = Markdown(MARKDOWN)
            console.print(md)
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
                view_recipes()
            elif users_selection == 5:
                search_recipes()
            elif users_selection == 6:
                export_recipe()
            else:
                print("Invalid Input")


if __name__ == "__main__":
    option_menu()
