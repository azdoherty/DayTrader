function validateLogin() {
  var f, fields = ["email", "password"];
  for(f of fields){
    if( document.forms["login"][f].value == ""){
      alert("Please enter " + f);
      return false;
    }
  }
}

var validated = false;

$('#submit-btn').click(function(e){
  if(!validated){
    e.preventDefault()
    validated = validateLogin();
  }
  //$(this).trigger('click');
  
})