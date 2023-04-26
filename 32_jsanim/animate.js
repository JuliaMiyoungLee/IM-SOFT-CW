var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var stopButton = document.getElementById("dvd");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    e.preventDefault();
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = () =>{
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
    clear();
    if (radius == 250) {
        growing = !growing;
    } else if (radius == 0 && !growing) {
        growing = !growing;
    }
    if (growing == true) {
        radius++;
    } else {
        radius--;
    }
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.stroke();
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 12;
    var rectHeight = 8;

    var rectX = Math.floor(Math.random() * (500-rectWidth));
    var rectY = Math.floor(Math.random() * (500-rectHeight));

    var xVel = 5;
    var yVel = 5;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if () {
            xVel = ;
        } 
        if () {
            yVel = ;
        }
        rectX = rectX + xVel;
        rectY = rectY + yVel;
        requestId = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
}




var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);

