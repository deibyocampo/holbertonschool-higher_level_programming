#!/usr/bin/node
// Prints the title of a star wars movies

const request = require('request');
const argv = process.argv;
const url = 'http://swapi.co/api/films/' + argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const films = JSON.parse(body);
  console.log(films.title);
});
