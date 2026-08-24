#!/bin/bash

# Deactivate any number of nested virtual environments
while [ -n "$VIRTUAL_ENV" ]; do
    deactivate
done

# Remove existing venv if it exists
if [ -d "venv" ]; then
    rm -rf venv
fi

# Create and activate a new virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install the required packages
pip install --upgrade pip
