/* this will add books */
$(document).ready(function(){
    var form = document.getElementById('form-wrapper-2')
    if (form!=null) {
      form.addEventListener('submit', function(e){
        console.log('Form submitted')
        var url = '/addbook/'
        var book_name = document.getElementById('book_name').value;
        var book_genre = document.getElementById('book_genre').value;
        var auhtor_id = document.getElementById('auhtor_id').value;
        fetch(url, {
            method:'POST',
            headers:{
              'Content-type':'application/json',
              'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'book_name':book_name,'book_genre':book_genre,'author':auhtor_id})
          }
        ).then(function(response){
          /* this will reset the form*/
          document.form2.reset();
          buildtable()
          $("#myModalbooks").modal('hide')
          return false;
        })
      })
    }
  });