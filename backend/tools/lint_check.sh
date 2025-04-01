#!/bin/bash

# Navigate to the backend folder
cd ..

ls

pipenv install

# Run isort check on code
echo "____________________ISORT_CHECK____________________"
pipenv run check

# Run black check on code
echo "____________________BLACK_CHECK____________________"
pipenv run b-check


# Run pylint check on code
echo "____________________PYLINT_CHECK____________________"
pipenv run py-check