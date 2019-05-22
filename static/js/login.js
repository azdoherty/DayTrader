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
    var data = $('#login').serializeArray()
    var url = window.location.href
    console.log(data);
    $.ajax({
      type: "POST",
      url: url,
      data: data,
      success: function(data, textStatus){
        console.log(data) 
        window.location = data;
      },
    }); 
  

  }
})

/*
$('#login').submit(function(){ //listen for submit event
  $.each(params, function(i,param){
      $('<input />').attr('type', 'hidden')
          .attr('name', param.name)
          .attr('value', param.value)
          .appendTo('#commentForm');
  });
  return true;
}); 
*/