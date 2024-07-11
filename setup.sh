#!/bin/bash

# TODO pip3 freeze > requirements.txt
# Add Error Checking
# Add return codes
# Add code to check if python installed version is greater than 3.10

echo "Creating Virtual requirement"
python -m venv venv

echo "Activating Virtual Enviroment ..."
source venv/bin/activate

echo "Installing required packages ..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready."
