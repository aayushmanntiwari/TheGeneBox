$(window).on('load',function(e){
    e.preventDefault();
    $.ajax({
      type:'GET',
              /* if no error will be found then this url will be run successfully*/
              url:'/ajax/load-authors/',
      data_type:'html',
      success:function (data){
        console.log("success");
        /* this will basically show the data based on the size we selected just below div size-option*/
        $('#auhtor_id').html(data.rendered_table);
      },

    });
});