
$(document).ready(function() {
  $('.tooltiper').tooltipster({
    content: 'loading',
    // 'instance' is basically the tooltip. More details in the "Object-oriented Tooltipster" section.
    functionBefore: function(instance, helper) {

        var $origin = $(helper.origin);
 
        // we set a variable so the data is only loaded once via Ajax, not every time the tooltip opens
        if ($origin.data('loaded') !== true) {

            $.get('/get_data', function(data) {

                // create line chart here from data

                console.log(data);
                // call the 'content' method to update the content of our tooltip with the returned data.
                // note: this content update will trigger an update animation (see the updateAnimation option)
                instance.content('<h1>hello</h1>');

                // to remember that the data has been loaded
                $origin.data('loaded', true);
            });
        }
    },
    contentCloning: true
  });

    //content: $('#tooltip_content'),
    //contentCloning: true

  $('#test').on('click', function(){
    $.get('/get_data')
      .success(function(data){
        console.log(data) 
      })
  });

  // hover over an IP address
  // return the activity data
  // plot on d3 and send back


});
 
