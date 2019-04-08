#!/bin/sh

echo "Please wait while we are activating the environment for python"
. venv/bin/activate


echo "Executing the python program to generate images and create html"
python test.py

echo "Deactivating the python environment"
deactivate


echo "creating html to generate flex screenshot"

echo "taking screenshot and converting to pdf"
#node screenshot.js
sleep(100)


echo "running node libary to generate pdf"
node index.js

echo "success !!!"

echo "output : screenshot.png , screenshot.pdf, output.pdf, ...test11.png"
