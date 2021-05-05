#!/usr/bin/node
/*
- Display the status code of a GET request
*/
const url = process.argv[2];
const request = require('request');
request(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
