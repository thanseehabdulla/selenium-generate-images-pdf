#!/bin/sh

echo "Please wait while we are activating the environment for python"
. venv/bin/activate


echo "Executing the python program to generate images"
python test.py

echo "Deactivating the python environment"
deactivate

echo "running node libary to generate pdf"
node index.js

echo "success !!!"
