#!/bin/bash

# Navigate to the backend folder
cd ..

ls

pipenv install

# Bootup docker containers for testing
docker -v
docker compose --profile test up -d

# Run pyteest
echo "____________________PYTEST____________________"
pipenv run test-no-workers