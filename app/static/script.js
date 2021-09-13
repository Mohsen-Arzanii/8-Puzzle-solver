ajaxurl = "http://localhost:5000/ajax";

if (mode == 'server') {
  ajaxurl = "https://eightpuzzle-xxx.fandogh.cloud/ajax";
}

function validate(state) {
  // validate the state string
  // len of the state must be 9
  if (state.length != 9) {
    alert('حالت شروع به فرم اشتباه وارد شده. طول رشته باید 9 باشد.')
    return false;
  }

  // check if the state contains all digits from 1 to 8 and a X
  chrs = '12345678X';
  for (var i = 0; i < chrs.length; i++) {
    var regex = new RegExp(chrs[i], 'g');
    var count_digit = (state.match(regex) || []).length;
    if (count_digit != 1) {
      alert(
          'حالت شروع به فرم اشتباه وارد شده. برای نمونه فرم درست بصورت 12346587X میباشد.')
      return false;
    }
  }

  return true;
}

function onclick_run() {
  _state = $("input[name=state]").val();
  _approach = $("select[name=approach]").val();
  _data = {state : _state, approach : _approach};

  // validation
  if (validate(_state) == false) {
    $("p[name=numofnodes]").val("-");
    $("p[name=level]").val("-");
    return;
  }

  // load the waiting spinner and disble the button
  $("div[name=loading]").attr('class', 'loading');
  $("input[name=run]").attr('disabled', true);

  // remove all cells
  // get data and append new cells
  $.ajax({
     url : ajaxurl,
     type : "POST",
     contentType : 'application/json;charset=UTF-8',
     data : JSON.stringify(_data),
     context : document.body
   }).done(function(res) {
    var li = $('ul li'); // all li elements inside the ul
    var solvable = res.solvable;
    var numofnodes = res.num_of_nodes;
    var level = res.level;
    var states = res.data; // all the states to reach the answer

    // hide the loading spinner
    $("div[name=loading]").attr('class', 'loading hide');

    // some cases are not solvable, so we check that
    if (solvable != true) {
      alert('این حالت قابل حل نمیباشد');
      $("input[name=run]").attr('disabled', false);
      return;
    }

    // set num of nodes and level of the goal state
    $("a[name=numofnodes]").text(numofnodes);
    $("a[name=level]").text(level);

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
        }, indx * 600);
      })(delay);
      // enable button after anitaion completed
      setTimeout(function() { $("input[name=run]").attr('disabled', false); },
                 states.length * 600);
    });
  });
}
