#!/usr/bin/node
// Searches the second biggest number in the list of arguments
const number = process.argv;
number.splice(0, 2);
if (number.length < 2) {
  console.log('0');
} else {
  number.sort((a, b) => a - b);
  console.log(number[number.length - 2]);
}
