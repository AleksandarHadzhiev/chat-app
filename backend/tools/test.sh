#!/bin/bash

# Navigate to the backend folder
cd ..

ls

pipenv install

# Run pyteest
echo "____________________PYTEST____________________"
pipenv run test-4