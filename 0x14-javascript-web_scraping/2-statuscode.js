#!/usr/bin/node
// display the status code of a GET request

const request = require('request');
const argv = process.argv;
const url = argv[2];

request.get(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
