#Docker image
FROM ubuntu

MAINTAINER Abdulla Thanseeh <thanseehabdulla@gmail.com>

RUN apt-get update && apt-get install -y git nodejs firefox chromium-browser npm python3 python3-pip apt-utils xvfb

RUN git clone https://github.com/thanseehabdulla/selenium-puppeteer-generate-images-pdf-html.git test

RUN  npm install -g yarn puppeteer && cd test && yarn && pip3 install -r requirements.txt

CMD ./test/run_docker.sh
