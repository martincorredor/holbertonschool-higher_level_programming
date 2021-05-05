#!/usr/bin/node
/*
- Prints the title of a Star Wars movie where the episode number matches a given integer
*/
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
