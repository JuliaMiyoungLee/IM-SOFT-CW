var c = document.getElementById("slate");

var ctx = c.getContext("2d");

var mode = "rect";

var toggleMode = () => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circle";
    }
    else {
        mode = "rect";
    }
}

// var drawRect = function(e) {
//     var mouseX = 
// }
var draw = () => {
    console.log("draw");
}

c.addEventListener("click",draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', ()=>{toggleMode()});