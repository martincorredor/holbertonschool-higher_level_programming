#!/usr/bin/node
// Add two integers
const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}

add(first, second);
