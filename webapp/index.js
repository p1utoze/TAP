const express = require("express");
const fileUpload = require("express-fileupload");
const pdfParse = require("pdf-parse");
const fetch = require('node-fetch')

const app = express();

app.use("/", express.static("public"));
app.use(fileUpload());

app.post("/extract-text", async (req, res) => {
    if (!req.files && !req.files.pdfFile) {
        res.status(400);
        res.end();
    }

    const result = await pdfParse(req.files.pdfFile)
    if (result){
        const url = 'https://qiyvjvwm57flqmhhawjq4t4y3u0djofs.lambda-url.us-east-1.on.aws/p1utoze/tap'
        console.log(result.text)
        const data = {
            text: result.text
        };
        const customHeaders = {
            "Content-Type": "application/json",
            "x-api-key": "SbFhRxmGzTaxaoOrol7rh1LXcxl9R8F66pKueeG4"
        }

        const response = await fetch(url, {
            method: "POST",
            headers: customHeaders,
            body: JSON.stringify(data),
        })

        const rr = await response.json()
        const lol = rr.output
        res.send(lol.prediction[0]);
    }
    });

app.listen(3000);