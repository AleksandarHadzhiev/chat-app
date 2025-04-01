#!/bin/bash

# Navigate to the backend folder
cd ..

# Run isort check on code
echo "____________________ISORT_CHECK____________________"
isort . -c -v

# Run black check on code
echo "____________________BLACK_CHECK____________________"
black . --check