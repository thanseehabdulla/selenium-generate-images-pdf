const jo = require('./project.json');
const puppeteer = require('puppeteer');
const imagesToPdf = require("images-to-pdf")
var fs = require('fs');

var dir = './output';

if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
}

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
};

(async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({width: 5960, height: 14209});
    // await page.goto('http://stackoverflow.com', {waitUntil: 'networkidle2'});
    await page.goto(jo.file_path);



    await page.screenshot({path: 'output/screenshot.png'});
    // await page.pdf({path: 'example.pdf', format: 'A4'});



    await imagesToPdf(["output/screenshot.png"], "output/screenshot.pdf");
    browser.close();

})();