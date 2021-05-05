#!/usr/bin/node
/*
- Gets the contents of a webpage and stores it in a file
*/
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(fileName, body, 'utf-8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
