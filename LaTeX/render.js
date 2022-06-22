const fs = require("fs");
const xmlserializer = require('xmlserializer');

const source = process.argv[2]
const output = process.argv[3]
const scale = 15

async function latexToSVG(){
  let { render } = require("./renderer.js");
  let latex = fs.readFileSync(source, 'utf8', (_, data) => data);
  console.log("------------------------------------------------------------")
  console.log(latex)

  latex = await render(latex)
  
  const html2xhtml = function (htmlString) {
    var parser = require('parse5'),
        dom = parser.parse(htmlString).childNodes[0].childNodes[1].childNodes[0].childNodes[0];
    let oldWidth = dom.attrs.find(el => el.name == "width").value
    dom.attrs.find(el => el.name == "width").value = parseFloat(oldWidth.slice(0,-2))*scale + "px"
    // console.log(dom.attrs.find(el => el.name == "width"))
    let oldHeight = dom.attrs.find(el => el.name == "height").value
    dom.attrs.find(el => el.name == "height").value = parseFloat(oldHeight.slice(0,-2))*scale + "px"
    // console.log(dom.attrs.find(el => el.name == "height"))

    return xmlserializer.serializeToString(dom);
  };

  latex = html2xhtml(latex);
  latex = latex.replace(/xlink/, 'xmlns:xlink');
  latex = latex.replace(/href/g, 'xlink:href');

  fs.writeFile(output, latex, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

latexToSVG()