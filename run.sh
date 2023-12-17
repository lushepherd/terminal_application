#!/bin/bash

# Loading message displayed when script is run
messages=("Loading... Please wait while I count to infinity."
          "Loading... Please wait til I've finished eating! ༼つ ◕_◕ ༽つ🍰🍔🍕"       
          "Loading... This may take a while. Or not. I'm not a fortune teller."
          "Loading... Please enjoy this elevator music while you wait."
          "Loading... I'm sorry, I can't do that. Just kidding. Or am I?"
          "Loading... Searching for the meaning of life. This may take a while!"
          "Loading... Attempting to break the space-time continuum. Hold tight!"
          "Loading... Sending carrier pigeons with your data."
          "Loading... Warming up the hamster on the wheel."
          "Loading... Converting coffee to code.")

# Randomly chooses a message from the array above
echo "${messages[RANDOM % ${#messages[@]}]}"

# Pause for 2 seconds so message can be read (lol)
sleep 2

# Check if the correct version of Python is installed
if command -v python3 &> /dev/null; 
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]; 
    then
        # Create and activate virtual environment
        # Install required libraries
        # Run the application
        python3 -m venv .venv
        source .venv/bin/activate
        pip3 install -r requirements.txt
        python3 main.py

    # Error if incorrect version of Python is installed
    else
        echo "Your Python is old"
        echo "Like a dinosaur fossil"
        echo "Time to evolve it (Upgrade to Python 3!)"
        echo "༼つ ◕_◕ ༽つ🍰🍔🍕"
        exit 1
    fi
    
else
    echo "NO RECIPES FOR YOU! Install Python 3 to continue." >&2
    echo "༼つ ◕_◕ ༽つ🍰🍔🍕"
    exit 1
fi