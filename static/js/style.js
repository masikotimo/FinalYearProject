document.getElementById("Name_of_Area").value = localStorage.getItem("currentplace");

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
    $('#sidebarCollapse1').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});
function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      
      reader.onload = function(e) {
        $('#imgInput').attr('src', e.target.result);
      };   
      reader.readAsDataURL(input.files[0]);
    }
  }
  $("#imgUpload").change(function() {
    readURL(this);
    $('#msg').hide();
  });
  function validateImage(){
    var fileName = document.getElementById("imgUpload").value;
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
        //TO DO
    }else{
        $('#imgErrModal').modal('show');
    }   
}
function validateEmail() {
    var email=document.getElementById("inputEmail").value;
    var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    if( !emailReg.test( email ) ) {
        $('#emailErrModal').modal('show');
    } else {
        return true;
    }
}


function generatePass(pLength){

    var keyListAlpha="abcdefghijklmnopqrstuvwxyz",
        keyListInt="123456789",
        keyListSpec="!@#_",
        password='';
    var len = Math.ceil(pLength/2);
    len = len - 1;
    var lenSpec = pLength-2*len;

    for (i=0;i<len;i++) {
        password+=keyListAlpha.charAt(Math.floor(Math.random()*keyListAlpha.length));
        password+=keyListInt.charAt(Math.floor(Math.random()*keyListInt.length));
    }

    for (i=0;i<lenSpec;i++)
        password+=keyListSpec.charAt(Math.floor(Math.random()*keyListSpec.length));

    password=password.split('').sort(function(){return 0.5-Math.random()}).join('');

    return password;
}