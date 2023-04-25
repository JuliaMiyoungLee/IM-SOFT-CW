var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";
ctx.fillStyle = "red";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circle";
    }
    else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 50, 120);
}

var drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 30, 0, Math.PI * 2, true);
    ctx.fill();
    // ctx.beginPath();
    // ctx.strokeStyle = "black";
    // ctx.lineWidth = 1;
    // ctx.moveTo(mouseX, mouseY);
    // ctx.arcTo(mouseX, mouseY, 30, 40, 30);
    // ctx.stroke();
}
var draw = (e) => {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
    console.log("draw");
}

var wipeCanvas = () => {
    clearRect(0, 0, ctx.height, ctx.width);
}

c.addEventListener("click",draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', ()=>{toggleMode()});
var clearB = document.getElementById("buttonClear");
clearB.addEventListener('click', ()=>{wipeCanvas()});