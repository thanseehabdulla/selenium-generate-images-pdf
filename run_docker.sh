#!/usr/bin/env bash
#/bin/bash

cd test

ls

git pull origin master

echo "Executing the python program to generate images"
python generate_images.py
echo "success"
echo ""
echo "generating html from images and json"
python writehtml.py
echo "success !!!"
echo ""

echo ""
echo "creating html to generate flex screenshot"
echo "success !!!"
echo ""
echo "taking screenshot and converting to pdf"
node screenshot.js
echo "success !!!"
echo ""
echo ""
echo "output : screenshot.png , screenshot.pdf, output.pdf, ...test11.png"
echo ""

echo "Done !!!"