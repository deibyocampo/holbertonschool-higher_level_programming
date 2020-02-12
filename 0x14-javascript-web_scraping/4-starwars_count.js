#!/usr/bin/node
// Prints the title of a star wars movies

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, actor) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(actor).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Invalid');
  }
});
