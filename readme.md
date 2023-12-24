# T1A3 Lucy Shepherd

## My Recipes Terminal Application

[Github](https://github.com/lushepherd/terminal_application/)<br>
[Presentation](https://www.youtube.com/watch?v=pQ8zHWcNSZA)<br>

## Menu
- [Intro](#intro)
- [Features](#features)
    - [Add new recipe](#feature1) 
    - [Modify, delete, view recipes](#feature2) 
    - [Search recipes](#feature3) 
    - [Other features](#feature4) 
- [Implementation plan - Asana](#asana)
    - [Completed Asana and final thoughts](#completedasana)
- [System requirements and installation](#requirements)
- [Help Documentation](#help)
- [Installation troubleshooting](#install-troubleshoot)
    - [Python needs updating](#updatepython)
    - [Python needs to be installed](#installpython)
- [How to...](#howto)
    - [Add a recipe](#addrecipe)
    - [Modify a recipe](#modifyrecipe)
    - [Delete a recipe](#deleterecipe)
    - [View recipes](#viewrecipes)
    - [Search recipes](#searchrecipes)
    - [Export a recipe to PDF](#exportrecipe)   
- [Resources](#resources)

### This is Term 1 Assignment 3 - Terminal Application.<a id="intro"></a>
For my assignment, I decided to create a recipe application. Users will be able add recipes, and retrieve them to modify/ delete/ view/ search/ export to PDF.<br><br>
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

### Feature 1: Add new recipes with ingredients and instructions <a id="feature1"></a>

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

### Feature 2: Modify, Delete and View current recipes <a id="feature2"></a>

These features all have very similar code so I am rolling them into one. 
With this feature, users are able to retrieve recipes from the database to edit name/ method/ ingredient, delete a current recipe or view a recipe.<br>
I have implemented error handling for empty lists.

### Feature 3: Allow users to search for recipes based on ingredients.<a id="feature3"></a>

With this feature, users are able to search the database for recipes by name or by ingredient. Any matches are displayed alphabetically for them to click to view.<br>
I have implemented error handling for invalid inputs and no matching search results.

### Other <a id="feature4"></a>

Users will also be able to export recipes to a PDF to save to their local computer in an easy-to-read printable format.<br>

### Implementation Plan <a id="asana"></a>

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
#### Completed Asana and final thoughts <a id="completedasana"></a>

![Completed Asana board](/images/Completedasana.png)

I have successfully completed my assignment board within the timeframe. I do have a few thoughts on the way I arranged my tasks and how to improve for future use.
- When I started this assignment I wasn't really sure how to structure my tasks or how to implement my features. I started off with each of my features broken down into smaller tasks assuming I would work on one feature at a time until each were completed.
- Instead, I created each feature and got them all working before I went down my checklist for each. I completed the "create function" item for each within the first day or two, then spent time working down the list. I also added extra subtasks as I went along - <br><br>
![New add recipe checklist](/images/asanalist.png)<br><br>
- I do understand this would very much be due to my lack of experience, however I still found tracking in this way to be very helpful when I was wondering what I should do next/ how to proceed. It also ensured I had less chance of missing things that were important.

## System Requirements and Installation <a id="requirements"></a>

### Required OS
- Linux
- Windows with WSL (Windows Subsystem for Linux)
- MacOS

Requires python3 and pip3 to be installed.
To run the application, please follow the help documentation below.

### Help Documentation <a id="help"></a>

1. Ensure you are currently in the src folder in the terminal.
2. Execute the bash script with the following prompts:
```
chmod +x setup.sh run.sh
```

```
bash setup.sh
```
3. The first command will allow permissions for you to execute it. The script will check if Python is installed and also check the version is Python3.
4. If the above requirement is met, it will create and activate a virtual environment, install requirements from requirements.txt and run the program.
5. Yes, you will be subject to my random loading messages (sorry, not sorry!)

༼つ ◕_◕ ༽つ🍰🍔🍕

##### Troubleshooting <a id="install-troubleshoot"></a>
##### <u>Python version out of date</u><a id="updatepython"></a>
If you receive the following message when running the application, you will need to update your version of Python.
      
        Your Python is old
        Like a dinosaur fossil
        Time to evolve it (Upgrade to Python 3!)
        ༼つ ◕_◕ ༽つ🍰🍔🍕
    
[Here](https://ioflood.com/blog/update-python-step-by-step-guide/) are some step-by-step guides on how to update your version of Python depending on which OS you are using.

##### <u>Python not installed</u><a id="installpython"></a>

If you receive this message, you will need to install Python3.
```
"NO RECIPES FOR YOU! Install Python 3 to continue.
༼つ ◕_◕ ༽つ🍰🍔🍕
```
[Here](https://ioflood.com/blog/?s=install+python) are some guides to installing Python3 depending on your OS.


### How to...<a id="howto"></a>

#### Add a recipe <a id="addrecipe"></a>
1. Select Add a new recipe from the menu.
2. Choose the category you would like to add your recipe to.<br><br>
![Add recipe](/images/addrecipe1.png)<br><br>
3. Enter the name of the recipe you would like to add and press enter. If you would like to cancel at this stage, type exit to return to the main menu.
4. Enter the ingredients separated by a comma then press enter. If you would like to cancel at this stage, type exit to return to the main menu.
5. Enter the method and press enter. If you would like to cancel at this stage, type exit to return to the main menu.<br><br>
![Add recipe instructions](/images/addrecipe2.png)<br><br>
6. You should now see your confirmation that your recipe has been successfully added.<br><br>
![Add recipe success!](/images/addrecipe3.png)

##### Troubleshooting
- If you are getting the following error, you have hit enter without inputting any text. Enter some text, or if you prefer to exit type "exit" to return to the main menu.<br><br>
![Empty input error add recipe](/images/addrecipeemptyinput.png)

- If you are getting the following error, there is a recipe in the database that already has that name. Please enter a unique name, or type exit to return to the main menu.<br><br>
![Same name error add recipe](/images/addrecipesamenameerror.png)

 
 #### Modify a recipe <a id="modifyrecipe"></a>
1. Select Modify a recipe from the menu.
2. Choose the category that contains the recipe you would like to modify.<br><br>
![Modify a recipe](/images/modifyrecipe1.png)<br><br>
3. Select the recipe you would like to modify, then confirm your selection with Y/N. If you cancel at this stage you will be returned to the main menu.<br><br>
![Confirm modify](/images/modifyrecipe2.png)<br><br>
4. Select the item you would like to modify - recipe name, ingredients or method.
5. Enter the new value to be modified and press enter to save.<br><br>
![Modify item](/images/modifyrecipe3.png)<br><br>
6. You should now see confirmation that your recipe has been successfully modified.<br><br>
![Modify successful](/images/modifysuccess.png)

##### Troubleshooting
- If you have selected a category and received this message, there are no recipes in your chosen category. Select another category (or add a recipe!)<br><br>
![Empty category error](/images/emptycategoryerror.png)

#### Delete a recipe <a id="deleterecipe"></a>
1. Select Delete a recipe from the menu.
2. Choose the category that contains the recipe you would like to delete and then select the recipe.<br><br>
![Delete a recipe](/images/deleterecipe1.png)<br><br>
3. Confirm whether you would like to delete the selected recipe with Y/N. If you select N at this stage, you will be returned to the main menu.
4. You should now see confirmation that your recipe has been successfully modified.<br><br>
![Delete successful](/images/deleterecipe2.png)

##### Troubleshooting
- If you have selected a category and received this message, there are no recipes in your chosen category. Select another category (or add a recipe! Maybe not to just delete it again though...)<br><br>
![Empty category error](/images/emptycategoryerror.png)

#### View a recipe <a id="viewrecipes"></a>
1. Choose View your current recipes from the menu.
2. Choose the category that contains the recipe you would like to view, then select your recipe.<br><br>
![View recipe](/images/viewrecipe.png)<br><br>
3. You should now see your selected recipe displayed on the screen.
![View successful](/images/viewsuccess.png)

##### Troubleshooting 
- If you have selected a category and received this message, there are no recipes in your chosen category. Select another category (or add a recipe!)<br><br>
![Empty category error](/images/emptycategoryerror.png)

#### Search for a recipe <a id="searchrecipes"></a>
1. Choose Search for a recipe from the menu.
2. Enter the name or ingredient you would like to search for in your recipe database.<br><br>
![Search recipe](/images/searchrecipe.png)<br><br>
3. This will return a list of recipes in the database that contain the search term. Select the recipe you would like to view and press enter.<br><br>
![Select recipe](/images/searchrecipe2.png)<br><br>
4. Your chosen recipe will now be displayed on your screen.<br><br>
![Search successful](/images/viewsuccess.png)

##### Troubleshooting
- If you can see the following error, you haven't input any text. Input a search term, or type exit to return to the main menu.<br><br>
![Empty search error](/images/emptysearcherror.png)

- If you can see the following error, no recipes match your search term. Check your spelling, try a new search term, add a new recipe, or type "exit" to return to the main menu.<br><br>
![No items match search term](/images/searchtermerror.png)


#### Export to PDF <a id="exportrecipe"></a>
1. Choose Export to PDF from the menu.
2. Choose the category that contains the recipe you would like to view, then select your recipe.<br><br>
![Export recipe](/images/exportrecipe1.png)
3. You should now see confirmation your recipe has been successfully exported. This will be located in the src folder for you to use.<br><br>
![Export successful](/images/exportsuccess.png)

##### Troubleshooting
- If you have selected a category and received this message, there are no recipes in your chosen category. Select another category (or add a recipe!)<br><br>
![Empty category error](/images/emptycategoryerror.png)<br><br>
- If you have received the following error, there is a character in your selected recipe not allowing the export function to proceed. Please remove any special characters. <br><br>
![Unicode Error](/images/exportunicodeerror.png)<br><br>
    - If you are unsure what may be causing this issue, please follow these steps:
    1. Go to [regex](https://regexr.com/)
    2. At the top in the "Expression" field, copy and paste the following:
    ```
    [^\u0000-\u007F]+
    ```
    3. Copy and paste the text you would like to check. Remove any items that are highlighted, then copy and paste the new text into your recipe via the modify function. Now try to export your recipe again.

![Regex unicode](/images/regexunicode.png)    

## Resources <a id="resources"></a>

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

- Anon, (2022). Bash Error Detection and Handling: Tips and Tricks – TecAdmin. [online] Available at: https://tecadmin.net/bash-error-detection-and-handling-tips-and-tricks/ [Accessed 20 Dec. 2023].

‌
‌
‌