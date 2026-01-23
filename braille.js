let canvas;
let capture;
let tint_color;

function setup() {
  canvas = createCanvas(windowWidth, windowHeight);
  capture = createCapture(VIDEO);
  capture.hide();
  
  tint_color = color(255, 255, 255);
}

function draw() {
  background(0);
  
  tint(tint_color);
  image(capture, 0, 0, width, width * capture.height / capture.width);
}

function mousePressed() {
  ocr(capture.canvas);
}

function ocr(img) {
 Tesseract.recognize(img).progress(print).then(foundWords);
}

function foundWords(words) {
  print("//");
  print(words.text);
  print("//");
  
  if (words.text) {
    if (words.text.toLowerCase().indexOf("umberto") > -1)
      tint_color = color(0, 255, 255);
    else
      tint_color = color(255, 255, 255);
  }
}