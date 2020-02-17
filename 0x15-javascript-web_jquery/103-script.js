$(document).ready(function () {
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
