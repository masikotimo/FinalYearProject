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