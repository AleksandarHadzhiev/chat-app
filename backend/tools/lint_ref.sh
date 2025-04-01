#!/bin/bash

# Navigate to the backend folder
cd ..

# Run isort check on code
echo "____________________ISORT_REF____________________"
isort .

# Run black check on code
echo "____________________BLACK_REF____________________"
black .