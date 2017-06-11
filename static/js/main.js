
$(document).ready(function() {
  $('.tooltiper').tooltipster({
    content: $('#tooltip_content'),
    contentCloning: true
  });

  $('#test').on('click', function(){
    $.get('/get_data')
      .success(function(data){
        console.log(data) 
      })
  });

});
 
