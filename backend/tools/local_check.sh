#!/bin/bash

# Navigate to the backend folder
cd ..

ls

# Run isort check on code
echo "____________________ISORT_CHECK____________________"
isort . -c -v

# Run black check on code
echo "____________________BLACK_CHECK____________________"
black . --check


# Run pylint check on code
echo "____________________PYLINT_CHECK____________________"
pylint .