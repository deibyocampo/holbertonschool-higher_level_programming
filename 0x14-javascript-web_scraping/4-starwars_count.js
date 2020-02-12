#!/usr/bin/node
// Prints the title of a star wars movies

const request = require('request');
let url;
const argv = process.argv;
if (argv[2] === 'http://swapi.co/api/films') {
  url = 'https://swapi.co/api/people/18';
}

request(url, function (err, response, actor) {
  if (err) {
    console.log(err);
  } else if (response && actor) {
    const films = JSON.parse(actor);
    console.log(films.films.length);
  }
});
