const puppeteer = require('puppeteer');
const imagesToPdf = require("images-to-pdf")

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
};

(async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({width: 5960, height: 14209})
    // await page.goto('http://stackoverflow.com', {waitUntil: 'networkidle2'});
    await page.goto("file:///home/sinergia/Desktop/davis/selenium/index.html");

    await page.screenshot({path: 'screenshot.png'});
    // await page.pdf({path: 'example.pdf', format: 'A4'});



    await imagesToPdf(["screenshot.png"], "screenshot.pdf")
    browser.close();

})();