/* this will add data for authors */
$(document).ready(function(){
    var form = document.getElementById('form-wrapper-1')
    if (form!=null) {
      form.addEventListener('submit', function(e){
        /*e.preventDefault()*/
        console.log('Form submitted')
        var url = '/addauthor/'
        var first_name = document.getElementById('first-name').value;
        var last_name = document.getElementById('last-name').value;
        fetch(url, {
            method:'POST',
            headers:{
              'Content-type':'application/json',
              'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'first_name':first_name,'last_name':last_name})
          }
        ).then(function(response){
          /* this will reset the form*/
          document.form1.reset();
          buildtable()
          $("#myModalauthor").modal('hide')
          return false;
        })
      })
    }
  });
  /*./*/