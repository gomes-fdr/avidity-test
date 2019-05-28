document.addEventListener('DOMContentLoaded', function () {
  var timeleft = 10;
  var downloadTimer = setInterval(function () {
    document.getElementById("counter").innerHTML = timeleft;
    timeleft -= 1;
    if(timeleft <= 0) {
      clearInterval(downloadTimer);
      location.reload(); 
    }
  }, 1000);
}, false);