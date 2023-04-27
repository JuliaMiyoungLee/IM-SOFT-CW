// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //A: Will still stop after just one alert.
  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?
//A: No, it doesn't because the DOM model won't change.

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   It determines which ones will be shown first.

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  //tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  //trs[x].addEventListener('click', clicky, false);
}

