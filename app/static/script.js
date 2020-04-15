ajaxurl = "http://localhost:5000/ajax";

if (mode == 'server') {
  ajaxurl = "https://eightpuzzle-amirpalang.fandogh.cloud/ajax";
}

function onclick_run() {
  // remove all cells
  // get data and append new cells
  $.ajax({url : ajaxurl, context : document.body}).done(function(res) {
    var li = $('ul li');   // all li elements inside the ul
    var states = res.data; // all the states to reach the answer

    var delay = 0;
    // apply states
    states.forEach(function(state) {
      delay++;
      (function(indx) {
        // delay to animate
        setTimeout(function() {
          // just replace old values with new one
          for (var i = 0; i < li.length; i++) {
            $(li[i]).html(state[i].val);
            $(li[i]).attr('class', state[i].attrib);
          }
        }, indx * 1000);
      })(delay);
    });
  });
}
