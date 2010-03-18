$(function() {
  // delete post
  $('#posts li a.delete').each(function() {
    this.addEventListener('click', function(e) {
      link = this;
      $.ajax({
        url: link.href,
        type: 'DELETE',
        success: function(d) { $(link.parentElement).fadeOut(); }
        });
      e.preventDefault();
    }, false);
  });

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
