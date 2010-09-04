$(function() {
  // delete post
  $('#posts li a.delete').click(function() {
      var that = $(this);
      console.log(link = that);
      $.ajax({
          url: this.href,
          type: 'delete',
          success: function(d) { that.parent().fadeOut(); }
      });

      return false;
  });

  //$('#edit-post').submit(function() {
    //$.ajax({
      //url: this.action,
      //type: 'PUT',
      //data: $('#edit-post').serialize(),
      //success: function(d) { $(location).attr('href', '/') },
      //failure: function(d) { alert('fail.'); }
    //});
    //return false;
  //});

  $('#create-new-post').click(function() {
      $('#create-new-post').toggle();
      $('#new-post').slideDown('fast', function() {
        });
    });

  $('#cancel-new-post').click(function() {
      $('#new-post').slideUp('fast', function() {
        $('#create-new-post').toggle();
        });
    });
    
});
