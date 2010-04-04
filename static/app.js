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

  $('#edit-post').submit(function() {
    $.ajax({
      url: this.action,
      type: 'PUT',
      data: $('#edit-post').serialize(),
      success: function(d) { $(location).attr('href', '/') },
      failure: function(d) { alert('fail.'); }
    });
    return false;
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
