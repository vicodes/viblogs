function openNav() {
    document.getElementById("mySidenav").style.width = "50px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function toggle_edit() {
    var x = document.getElementById("bio");
    var y = document.getElementById("bioedit");
    if (x.style.display === "block" || y.style.display === "none") {
      x.style.display = "none";
      y.style.display = "block";

  } else {
      y.style.display = "none";
      x.style.display = "block";

  }
}

$(document).ready(function(){
   $('.materialboxed').materialbox();
   $('.collapsible').collapsible();
   $('.modal').modal();
   $('textarea').froalaEditor();
   $('.tooltipped').tooltip();
   $('#id_dob').datepicker();

   $(".pushme").click(function () {
           $(this).text(function(i, v){
              return v === '😶' ? '😲' : '😶'
           })
       });
});
document.getElementById("id_first_name").onkeyup = function() {uname()};
document.getElementById("id_first_name").oninput = function() {activateuname()};
document.getElementById("id_password2").onkeyup = function() { checkPassImg()};

function activateuname() {
  var x = document.getElementById("id_usernamelbl");
  var y = document.getElementById("id_usernameicn");

  x.className += " active";
  y.className += " active";

}

function uname() {
    var x = document.getElementById("id_first_name");
    var y = document.getElementById("id_username");

    y.value = x.value.replace(/ /g,'_');
}

function checkPassImg(){
  var pass1 = document.getElementById('id_password1');
  var pass2 = document.getElementById('id_password2');
  var check = document.getElementById('act2');
  var verified = document.getElementById('act1');

  var goodColor = "#66cc66";
  var badColor = "#ff6666";

  if(pass1.value == pass2.value){
    check.style.color = goodColor;
    verified.style.color = goodColor;

  }else{
    verified.style.color = badColor;
    check.style.color = badColor;
  }
}
