$(document).ready(function () {
  $('INPUT#language_code').click(function() {
    const lan = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
