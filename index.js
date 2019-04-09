// const imagesToPdf = require("images-to-pdf")


const PDFDocument = require('pdfkit');
let fs = require('fs');

console.log("please wait..we are generating pdf");

const doc = new PDFDocument;

doc.pipe(fs.createWriteStream('output.pdf'));

let n = 11

for(let i = 2; i<=n;i++) {
    if (i !== 3) {

        doc.image('test' + i + '.png', {
            fit: [500, 500],
        });
        if(i !== n)
        doc.addPage()
    }
}

doc.end();

// imagesToPdf(["test2.png", "test4.png", "test5.png", "test6.png", "test7.png", "test8.png", "test9.png", "test10.png", "test11.png"], "final2.pdf")

