const url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  for (const i in data.results) {
    $('UL#list_movies').append(`<li>${data.results[i].title}</li>`);
  }
});
