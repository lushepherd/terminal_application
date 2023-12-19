# T1A3 Lucy Shepherd

## My Recipes Terminal Application

Github: https://github.com/lushepherd/your-recipe-book

This is Term 1 Assignment 3 - Terminal Application.

For my assignment, I decided to create a recipe application. 
The code style guide I will be adhering to is Pep 8 - https://peps.python.org/pep-0008/
I am using the VsCode formatter extension autopep8 to ensure code is in line with this requirement. I have provided some of the main points below:

- Prefers use of 4 spaces for indentation over tabs

- Limited line length of 79 characters

- Two blank lines separating main functions/ class definitions

- Imports should go in order of:
    1. Standard library imports
    2. Related third party imports
    3. Local application/ library specific imports

## Features

### Feature 1: Add new recipes with ingredients and instructions

Users are able to add new recipes with ingredients and instructions to 5 different categories:
- Breakfast
- Lunch
- Dinner
- Snacks
- Dessert

They are sorted alphabetically for easy navigation.<br>
Users are also able to amend or delete recipes they have created.<br>
One a recipe has been created, users receive a confirmation message so they know it has been successful.<br>
I have implemented exception handling for invalid inputs from the user.

### Feature 2: Display a list of available recipes. 

With this feature, users are able to print a list of the available recipes in a category, or print all recipes from each category. Recipes are sorted alphabetically within each category for ease of navigation.<br>
I have implemented error handling for empty lists.

### Feature 3: Allow users to search for recipes based on ingredients.

With this feature, users are able to search for recipes based on ingredients. There is an additional function allowing users to filter by category.<br>
I have implemented error handling for invalid inputs or empty results.

### Other

Users will also be able to export recipes to a PDF to save to their local computer in an easy-to-read printable format.<br>

### Implementation Plan

I have used Asana to break this task down into smaller items. Each item is a task to be ticked off. Some tasks have a description and some have sub-tasks to break these down even further.<br>
The project management board was the first thing I completed and each item have a due date. This allowed me to keep track of where I'm up to and how much further I needed to go. If I completed a task early it was checked off and I immediately started on the next item of the list.<br>
I have provided detailed screenshots below.

![Description of my project board](/images/asana1.png)
![Overview of my list of tasks](/images/asana2.png)
![Create main page task and its description](/images/asana6.png)
![Define functions task and its description](/images/asana7.png)
![Feature 1 checklist](/images/asana3.png)
![Feature 2 checklist](/images/asana4.png)
![Feature 3 checklist](/images/asana5.png)
![Write execution script on the list and its description](/images/asana8.png)
![Create help doc task and its description](/images/asana9.png)
![Create Readme task and its checklist](/images/asana10.png)

## System Requirements and Installation

### Required OS
- Linux
- Windows with WSL (Windows Subsystem for Linux)
- MacOS

Requires python3 and pip3 to be installed.
To run the application, please follow the help documentation below.

### Help Documentation

1. Ensure you are currently in the src folder in the terminal.
2. Execute the bash script with the following prompts:
```
chmod +x run.sh
```

```
bash run.sh
```
3. The first command will allow permissions for you to execute it. The script will check if Python is installed and also check the version is Python3.
4. If the above requirement is met, it will create and activate a virtual environment, install requirements from requirements.txt and run the program.
5. Yes, you will be subject to my random loading messages (sorry, not sorry!)

༼つ ◕_◕ ༽つ🍰🍔🍕

## Resources

- inquirerpy.readthedocs.io. (n.d.). rawlist - InquirerPy. [online] Available at: https://inquirerpy.readthedocs.io/en/latest/pages/prompts/rawlist.html [Accessed 11 Dec. 2023].

- www.tutorialspoint.com. (n.d.). TinyDB - Tables. [online] Available at: https://www.tutorialspoint.com/tinydb/tinydb_tables.htm [Accessed 11 Dec. 2023].

- inquirerpy.readthedocs.io. (n.d.). text - InquirerPy. [online] Available at: https://inquirerpy.readthedocs.io/en/latest/pages/prompts/input.html [Accessed 11 Dec. 2023].

- tinydb.readthedocs.io. (n.d.). Getting Started — TinyDB 4.8.0 documentation. [online] Available at: https://tinydb.readthedocs.io/en/latest/getting-started.html#basic-usage [Accessed 11 Dec. 2023].

- inquirerpy.readthedocs.io. (n.d.). inquirer - InquirerPy. [online] Available at: https://inquirerpy.readthedocs.io/en/latest/pages/inquirer.html [Accessed 11 Dec. 2023].

- tinydb.readthedocs.io. (n.d.). Advanced Usage — TinyDB 4.8.0 documentation. [online] Available at: https://tinydb.readthedocs.io/en/latest/usage.html#updating-data [Accessed 11 Dec. 2023].

- pyfpdf.readthedocs.io. (n.d.). Tutorial - PyFPDF. [online] Available at: https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html#tutorial [Accessed 11 Dec. 2023].

- Stack Overflow. (n.d.). Trying to create a function to search for a word in a string. [online] Available at: https://stackoverflow.com/questions/69509917/trying-to-create-a-function-to-search-for-a-word-in-a-string [Accessed 12 Dec. 2023].

- Stack Overflow. (n.d.). How to make a search function case in-sensitive | Python. [online] Available at: https://stackoverflow.com/questions/47251439/how-to-make-a-search-function-case-in-sensitive-python [Accessed 12 Dec. 2023].

- Stack Overflow. (n.d.). Is it possible to ask for keys from TinyDB. [online] Available at: https://stackoverflow.com/questions/27197052/is-it-possible-to-ask-for-keys-from-tinydb [Accessed 12 Dec. 2023].

- python.hotexamples.com. (n.d.). Python TinyDB Examples, tinydb.TinyDB Python Examples - HotExamples. [online] Available at: https://python.hotexamples.com/examples/tinydb/TinyDB/-/python-tinydb-class-examples.html [Accessed 12 Dec. 2023].

- edstem.org. (n.d.). Ed Discussion. [online] Available at: https://edstem.org/au/courses/13988/lessons/43347/slides/297106 [Accessed 17 Dec. 2023].

‌
‌