#!/usr/bin/env bash
#/bin/bash

echo "Do you wish to install npm packages? (note:'yarn is required to run only once')"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) yarn; break;;
        No ) exit;;
    esac
done

echo "Do you wish to install apt packages? (note:'apt is required to run only once')"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo apt-get install xvfb; break;;
        No ) exit;;
    esac
done

echo "Please wait while we are activating the environment for python"
. venv/bin/activate
echo "success !!!"
echo ""
echo "Do you wish to install pippy packages? (note:'pip is required to run only once')"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) pip install -r requirements.txt; break;;
        No ) exit;;
    esac
done
echo "Executing the python program to generate images"
python test.py
echo "success"
echo ""
echo "generating html from images and json"
python writehtml.py
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
node screenshot.js
echo "success !!!"
echo ""
echo ""
echo "output : screenshot.png , screenshot.pdf, output.pdf, ...test11.png"
echo ""

echo "Do you wish to remove generated images?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) rm -r images/; break;;
        No ) exit;;
    esac
done

echo "Do you wish to remove generated html?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) rm -r html/; break;;
        No ) exit;;
    esac
done


echo "Done !!!"