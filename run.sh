#!/bin/sh

echo "Please wait while we are activating the environment for python"
. venv/bin/activate
echo "success !!!"
echo ""
echo "Executing the python program to generate images and create html"
python test.py
echo "success !!!"
echo ""
echo "Deactivating the python environment"
deactivate
echo "success !!!"
echo ""
echo "creating html to generate flex screenshot"
echo "success !!!"
echo ""
echo "taking screenshot and converting to pdf"
#node screenshot.js
sleep 100
echo "success !!!"
echo ""
echo "running node libary to generate pdf"
node index.js

echo "success !!!"
echo ""
echo "output : screenshot.png , screenshot.pdf, output.pdf, ...test11.png"
echo ""
echo "Done !!!"