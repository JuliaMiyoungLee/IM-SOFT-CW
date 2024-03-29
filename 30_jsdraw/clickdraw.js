var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";
ctx.fillStyle = "red";

var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circle";
        buttonToggle.innerHTML = "circle";
    }
    else {
        mode = "rect";
        buttonToggle.innerHTML = "rectangle";
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
    ctx.stroke();
}
var draw = (e) => {
    if (mode == "rect") {
        drawRect(e);
    }
    else {
        drawCircle(e);
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
}

c.addEventListener("click",draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener('click', wipeCanvas);