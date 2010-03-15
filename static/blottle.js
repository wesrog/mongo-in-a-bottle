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
});
