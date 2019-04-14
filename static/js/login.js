function validateLogin() {
  var f, fields = ["email", "password"];
  for(f of fields){
    if( document.forms["login"][f].value == ""){
      alert("Please enter " + f);
      return false;
    }
    return true;
  }
}

$('#submit-btn').click(function(e){
  e.preventDefault()
  var validated = validateLogin();
  if(validated){
    var data = $('#login').serialize()
    var url = window.location.href
    console.log(data)
    $.post(url, function(data, status){
      console.log(status)     
  });

  }
  
})