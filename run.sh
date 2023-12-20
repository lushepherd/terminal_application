#!/bin/bash

# Create and activate virtual environment, install requirements, execute main (start the program)
# Uses || (OR operator) which executes the second block if the first fails. 
# If the virtual environment command fails, it will instead print the error and exit the program.
# This allows us to see where the error has occurred. 

python3 -m venv .venv || { echo "Error creating virtual environment."; exit 1; }
source .venv/bin/activate || { echo "Error activating virtual environment."; exit 1; }
pip3 install -r requirements.txt || { echo "Error installing requirements."; exit 1; }
python3 main.py || { echo "Error running the main script."; exit 1; }