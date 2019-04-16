#!/usr/bin/env bash
#/bin/bash

cd test
echo "current working directory"
pwd

git pull origin master

echo "Enter html path to take screenshot"
echo "sample path is file:///test/new.html"

read html_path
sed -i "/file_path/ s/:\"[^\"]*\"/:\"$html_path\"/" project.json
echo "Enter css class name to take screenshot of div"

echo "sample class is .react-grid-item.react-draggable.react-resizable"
read css_name
sed -i "/selector/ s/:\"[^\"]*\"/:\"$css_name\"/" project.json


echo "Executing the python program to generate images"
python3 generate_images.py
echo "success"
echo ""
echo "generating html from images and json"
python3 writehtml.py
echo "success !!!"
echo ""

echo ""
echo "creating html to generate flex screenshot"
echo "success !!!"
echo ""
yarn
echo "taking screenshot and converting to pdf"
node screenshot.js
echo "success !!!"
echo ""
echo ""
echo "output : screenshot.png , screenshot.pdf, output.pdf, ...test11.png"
echo ""

echo "Done !!!"

echo " please run sudo docker cp <container-id>:/test/output/screenshot.pdf /tmp/outputs"

#sleep 100