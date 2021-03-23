#!/usr/bin/node
//converts the argument passed to it into a number and print it

const num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log("Not a number");
} else {
  console.log(`My number: ${num}`);
}
