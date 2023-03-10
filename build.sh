#!/bin/bash

echo " BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py tailwind install
echo " BUILD END" 

# # Build the project
# echo "Building the project..."
# python3 -m pip install -r requirements.txt

# python3 manage.py tailwind install
# echo "Make Migration..."
# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

# echo "Collect Static..."
# python3 manage.py collectstatic --noinput --clear